from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import viewsets
from .models import Note
from .serializers import NoteSerializer
from .permissions import IsAdminOrReadOnlyForUser
from rest_framework.permissions import IsAuthenticated
from django.db.models.functions import Length
from rest_framework.decorators import action
from rest_framework.response import Response

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnlyForUser]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name='min_title_len',
                description='Minimalna dužina naslova (title)',
                required=False,
                type=int,
                location=OpenApiParameter.QUERY
            )
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Note.objects.all()
        min_len = self.request.query_params.get('min_title_len')
        if min_len and min_len.isdigit():
            queryset = queryset.annotate(title_length=Length('title')).filter(title_length__gt=int(min_len))
        return queryset

    @action(detail=False, methods=['get'])
    def long(self, request):
        notes = Note.objects.annotate(title_length=Length('title')).filter(title_length__gt=20)
        serializer = self.get_serializer(notes, many=True)
        return Response(serializer.data)
