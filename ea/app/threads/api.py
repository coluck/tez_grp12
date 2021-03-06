import datetime as dt
import json

from django.db.models import Count, Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.utils.translation import get_language as lang

from app.threads.models import Tag, Thread


def api(queries):
    results = {}
    lis = []

    for query in queries:
        results['title'] = query.title
        results['slug'] = query.slug
        results['cnt'] = query.cnt
        lis.append(results.copy())

    res = json.dumps(lis)
    mimetype = 'application/json'

    return HttpResponse(res, mimetype)


def api_tag(slug, *args, **kwargs):
    # print(args)       ((), {'slug': 'music'}) # slug parameter is useless
    # print(kwargs)     {}
    tag = get_object_or_404(Tag, slug=slug)
    cnt = Count("entries",
                filter=Q(entries__deleted_at=None),
                distinct=True)
    # queries = tag.threads.annotate(cnt=Count('entries')).only("title", "slug") \
    queries = tag.threads.annotate(cnt=cnt).only("title", "slug") \
        .order_by("-last_entry")
    return api(queries)


def api_thread(request, *args, **kwargs):
    if request.GET.get("week", None):
        cnt = Count("entries",
                    filter=Q(entries__created_at__gt=timezone.now()-timezone.timedelta(days=30))&
                           Q(entries__deleted_at=None)
                    , distinct=True)
        queries = Thread.objects.filter(lang=lang()) \
                      .annotate(cnt=cnt).filter(cnt__gt=0) \
                      .order_by("-last_entry").only('title', 'slug')[:20]
    else:
        cnt = Count("entries",
                    filter=Q(entries__deleted_at=None),
                    distinct=True)
        queries = Thread.objects.filter(lang=lang()) \
                      .annotate(cnt=cnt).filter(cnt__gt=0)  \
                      .order_by("-cnt").only('title', 'slug')[:20]
    return api(queries)

# def api(request, now_all):
#     if request.is_ajax():
#         # # tec = Count('entries', filter=Q(entries__created_at__startswith=
#         # #                                 dt.date.today()))
#         # # threads = Thread.objects.only('title', 'slug').filter(lang=lang())\
#         # #     .annotate(tecnt=tec)[:30]
#         # threads = Thread.objects.only('title', 'slug').filter(lang=lang())\
#         #     .annotate(ecnt=Count("entries",
#         #         filter=Q(entries__created_at__startswith=dt.date.today()),
#         #         distinct=True)).order_by("-ecnt")
#
#         results = {}
#         lis = []
#         if now_all == "all":
#             queries = Thread.objects.filter(lang=lang()) \
#                 .annotate(cnt=Count("entries"))\
#                 .order_by("-cnt").only('title', 'slug')[:20]
#
#         elif now_all == "now":
#             # By now is implemented 7 days duration change it to 1 day when site gets popular
#             print("YYY")
#             queries = Thread.objects.filter(lang=lang()) \
#                 .annotate(cnt=Count("entries",
#                     # filter=Q(entries__created_at__startswith=dt.date.today()),
#                     filter=Q(entries__created_at__gt=dt.date.today()-dt.timedelta(days=7)),
#                     distinct=True)).filter(cnt__gt=0).order_by("-last_entry").only('title', 'slug')[:20]
#         else:
#             return Http404()
#
#         for query in queries:
#             results['title'] = query.title
#             results['slug'] = query.slug
#             results['cnt'] = query.cnt
#             lis.append(results.copy())
#
#         res = json.dumps(lis)
#         mimetype = 'application/json'
#
#         return HttpResponse(res, mimetype)
