from django.http import JsonResponse
from django.shortcuts import render

from ajax_app.models import WebSeries

from .forms import WebSeriesForm


def main_view(request):
    return render(request, "index.html")


def photo_add_view(request):
    form = WebSeriesForm(request.POST or None, request.FILES or None)
    data = {}
    if request.is_ajax():
        print(form)
        if form.is_valid():
            form.save()
            data["name"] = form.cleaned_data.get("name")
            data["status"] = "ok"
            return JsonResponse(data)
    context = {"form": form}
    return render(request, "photo_upload.html", context)


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
                    "image": pos.image.url,
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
