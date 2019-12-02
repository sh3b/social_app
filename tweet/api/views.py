from django.db.models import Q
from rest_framework import generics
from rest_framework import permissions
from rest_framework.exceptions import ParseError
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from tweet.models import Tweet

from .pagination import StandardResultsPagination
from .serializers import TweetModelSerializer


class TweetLikeAPIView(APIView):
    def post(self, request, *args, **kwargs):
        is_liked = Tweet.objects.like_toggle(request.user,
                                             Tweet.objects.get(pk=self.kwargs.get('tweet_pk')))
        return Response({'liked': is_liked})


# class RetweetAPIView(APIView):
#     permission_classes = [permissions.IsAuthenticated]
#
#     def get(self, request, pk, format=None):
#         tweet_qs = Tweet.objects.filter(pk=pk)
#         message = "Not allowed"
#         if tweet_qs.exists() & tweet_qs.count() == 1:
#             # if request.user.is_authenticated():
#             new_tweet = Tweet.objects.retweet(request.user, tweet_qs.first())
#             if new_tweet is not None:
#                 data = TweetModelSerializer(new_tweet).data
#                 return Response(data)
#             message = "Cannot retweet the same in one day"
#         return Response({"message": message}, status=400)


# class TweetCreateAPIView(generics.CreateAPIView):
#     serializer_class = TweetModelSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)


# class TweetDetailAPIView(generics.RetrieveAPIView):
#     queryset = Tweet.objects.all()
#     serializer_class = TweetModelSerializer
#     pagination_class = StandardResultsPagination
#     permission_classes = [permissions.IsAuthenticated]
#
#     def get_queryset(self, *args, **kwargs):
#         tweet_id = self.kwargs.get("pk")
#         qs = Tweet.objects.filter(pk=tweet_id)
#         if qs.exists() and qs.count() == 1:
#             parent_obj = qs.first()
#             qs1 = parent_obj.get_children()
#             qs = (qs | qs1).distinct().extra(select={"parent_id_null": 'parent_id IS NULL'})
#         return qs.order_by("-parent_id_null", '-timestamp')


# class SearchTweetAPIView(generics.ListAPIView):
#     queryset = Tweet.objects.all().order_by("-timestamp")
#     serializer_class = TweetModelSerializer
#     pagination_class = StandardResultsPagination
#
#     def get_serializer_context(self, *args, **kwargs):
#         context = super(SearchTweetAPIView, self).get_serializer_context(*args, **kwargs)
#         context['request'] = self.request
#         return context
#
#     def get_queryset(self, *args, **kwargs):
#         qs = self.queryset
#         query = self.request.GET.get("q", None)
#         if query is not None:
#             qs = qs.filter(
#                 Q(content__icontains=query) |
#                 Q(user__username__icontains=query))
#         return qs


class TweetListAPIView(generics.ListAPIView):
    serializer_class = TweetModelSerializer
    pagination_class = StandardResultsPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        requested_user = self.kwargs.get("user_pk")
        if requested_user:
            return Tweet.objects.filter(user_id=requested_user)
        raise ParseError
