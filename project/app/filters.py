import django_filters
from rest_framework import filters
from django.db.models import Q
from app.models import Teacher


class TeacherFilterBackend(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name')
    surname = django_filters.CharFilter(field_name='surname')
    surname2 = django_filters.CharFilter(field_name='surname2')
    department = django_filters.CharFilter(field_name='department')
    birth = django_filters.NumberFilter(field_name='birth')
    full_name = django_filters.CharFilter(method='filter_params')

    def filter_params(self, queryset, name, value):
        return queryset.filter(Q(name__icontains=value) | Q(surname__icontains=value) | Q(surname2__icontains=value))

    class Meta:
        model = Teacher
        fields = ('name', 'surname', 'surname2', 'department', 'birth')
