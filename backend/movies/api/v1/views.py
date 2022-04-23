from django.contrib.postgres.aggregates import ArrayAgg
from django.http import JsonResponse
from django.views.generic.list import BaseListView
from django.views.generic.detail import BaseDetailView
from django.db.models import Q

from movies.models import Filmwork, RoleType


class MoviesMixinApi:
    model = Filmwork
    http_method_names = ['get']

    def _aggregate_person(self, role):
        return ArrayAgg('persons__full_name', distinct=True,
            filter=Q(personfilmwork__role=role))

    def get_queryset(self):
        qs = Filmwork.objects.prefetch_related('genres', 'persons')
        qs = qs.annotate(
            genre=ArrayAgg('genres__name', distinct=True),
            actors=self._aggregate_person(RoleType.ACTOR),
            writers=self._aggregate_person(RoleType.WRITER),
            directors=self._aggregate_person(RoleType.DIRECTOR)
        )
        return qs.values(
            'id',
            'title',
            'description',
            'creation_date',
            'rating',
            'type',
            'genre',
            'actors',
            'writers',
            'directors'
        )

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)


class MoviesListApi(MoviesMixinApi, BaseListView):
    paginate_by = 50

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = self.get_queryset()
        paginator, page, queryset, _ = self.paginate_queryset(queryset, self.paginate_by)
        context = {
            'count': paginator.count,
            'total_pages': paginator.num_pages,
            'prev': page.previous_page_number() if page.has_previous() else None,
            'next': page.next_page_number() if page.has_next() else None,
            'results': list(queryset)
        }
        return context


class MoviesDetailApi(MoviesMixinApi, BaseDetailView):
    def get_context_data(self, *, object_list=None, **kwargs):
        return kwargs['object']
