from django.http import HttpResponse, JsonResponse
from .models import Feed
# Create your views here.

def getFeed(request):
    result = []
    feeds = Feed.objects.values()
    for feed in feeds:
        result.append(feed)

    return JsonResponse(result, safe=False)


def postFeed(request):
    name = request.GET.get('name')
    title = request.GET.get('title')
    message = request.GET.get('message')
    feed = Feed(name=name, title=title, message=message)
    feed.save()
    return JsonResponse({}, safe=False)