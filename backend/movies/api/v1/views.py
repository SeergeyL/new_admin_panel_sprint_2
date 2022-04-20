from django.contrib.postgres.aggregates import ArrayAgg
from django.http import JsonResponse
from django.views.generic.list import BaseListView
from django.db.models import Q

from movies.models import Filmwork


class MoviesListApi(BaseListView):
    model = Filmwork
    http_method_names = ['get']
    paginate_by = 50

    def get_queryset(self):
        qs = Filmwork.objects.prefetch_related('genres', 'persons')
        qs = qs.annotate(
            genre=ArrayAgg('genres__name', distinct=True),
            actors=ArrayAgg('persons__full_name', distinct=True,
                filter=Q(personfilmwork__role='actor')),
            writers=ArrayAgg('persons__full_name', distinct=True,
                filter=Q(personfilmwork__role='writer')),
            directors=ArrayAgg('persons__full_name', distinct=True,
                filter=Q(personfilmwork__role='director'))
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

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = self.get_queryset()
        paginator, page, queryset, _ = self.paginate_queryset(queryset, self.paginate_by)
        context = {
            'count': paginator.count,
            'total_pages': paginator.num_pages,
            'prev': page.number,
            'next': page.next_page_number() if page.has_next() else None,
            'results': list(queryset)
        }
        return context

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)
