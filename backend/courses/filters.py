import django_filters
from .models import Course

class CourseFilter(django_filters.FilterSet):
    course_type = django_filters.CharFilter(field_name='course_type', lookup_expr='iexact')
    skill_level = django_filters.CharFilter(field_name='skill_level', lookup_expr='iexact')
    topics = django_filters.CharFilter(field_name='topics__name', lookup_expr='iexact')
    partnerships = django_filters.CharFilter(field_name='partnerships__title', lookup_expr='iexact')

    class Meta:
        model = Course
        fields = ['course_type', 'skill_level', 'topics', 'partnerships']
