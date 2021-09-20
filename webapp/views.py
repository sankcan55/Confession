from django.http import HttpResponse, JsonResponse
from .models import Feed
# Create your views here.

def getFeed(request):
    result = []
    feeds = Feed.objects.values()
    for feed in feeds:
        result.append(feed)

    return JsonResponse({'result': result}, safe=False)


def postFeed(request):
    name = request.GET.get('name')
    content = request.GET.get('content')
    feed = Feed(name=name, content=content)
    feed.save()
    return JsonResponse({}, safe=False)