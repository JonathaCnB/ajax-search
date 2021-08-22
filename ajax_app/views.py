from django.http import JsonResponse
from django.shortcuts import render

from ajax_app.models import WebSeries


def main_view(request):
    return render(request, "index.html")


def search_result(request):
    if request.is_ajax():
        res = None
        series = request.POST.get("series")
        qs = WebSeries.objects.filter(name__icontains=series)

        if len(qs) > 0 and len(series) > 0:
            data = []
            for pos in qs:
                item = {
                    "pk": pos.pk,
                    "name": pos.name,
                    "image": pos.image,
                }

                data.append(item)
            res = data
        else:
            res = "No Webseries found with that name"

        return JsonResponse({"data": res})

    return JsonResponse({})


def detail_series(request, pk):
    series_obj = WebSeries.objects.get(id=pk)

    return render(request, "detail.html", context={"series": series_obj})
