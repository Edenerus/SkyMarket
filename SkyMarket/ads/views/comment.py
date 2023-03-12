from django.shortcuts import get_object_or_404
from rest_framework import pagination, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from ads.models import Ad, Comment
from ads.serializers import CommentSerializer
from ads.permissions import IsOwnerOrStaff


class CommentPagination(pagination.PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 4


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().select_related('ad')
    serializer_class = CommentSerializer

    default_permission = [AllowAny(), ]
    permission_classes = {
        'retrieve': [IsAuthenticated(), ],
        'create': [IsAuthenticated(), ],
        'update': [IsAuthenticated(), IsOwnerOrStaff(), ],
        'partial_update': [IsAuthenticated(), IsOwnerOrStaff(), ],
        'destroy': [IsAuthenticated(), IsOwnerOrStaff(), ],

    }

    def get_queryset(self, *args, **kwargs):
        ad_id = self.kwargs.get('ad_pk')
        ad = get_object_or_404(Ad, pk=ad_id)

        return self.queryset.filter(ad=ad)

    def get_permissions(self):
        return self.permission_classes.get(self.action, self.default_permission)

    def perform_create(self, serializer, *args, **kwargs):
        serializer.save(author=self.request.user, ad_id=self.kwargs.get('ad_pk'))
