from rest_framework.filters import BaseFilterBackend


class HabitInstanceFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        queryset = queryset.filter(habit__account=request.user)
        completed_at = request.query_params.get("completed_at", None)
        if completed_at:
            queryset = queryset.filter(completed_at=completed_at)
        return queryset
