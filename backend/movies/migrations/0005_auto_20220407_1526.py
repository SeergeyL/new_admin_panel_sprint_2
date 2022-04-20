from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_alter_filmwork_certificate'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='genrefilmwork',
            unique_together={('film_work', 'genre')},
        ),
        migrations.AlterUniqueTogether(
            name='personfilmwork',
            unique_together={('film_work', 'person', 'role')},
        ),
    ]
