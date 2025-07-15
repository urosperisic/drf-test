from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Note
from .serializers import NoteSerializer
from .permissions import IsAdminOrReadOnlyForUser

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnlyForUser]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        return Note.objects.all()
