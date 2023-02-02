from rest_framework.filters import BaseFilterBackend

class HabitInstanceDateFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        completed_at = request.query_params.get('completed_at')
        if completed_at:
            queryset = queryset.filter(date__exact=completed_at)
        return