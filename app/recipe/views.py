from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Tag
from recipe import serializers


class TagViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    authentication_classes = (TokenAuthentication, )
    permissions_classes = (IsAuthenticated, )
    queryset = Tag.objects.all()
    serializers_classes = (serializers.TagSerializer, )

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('-name')
