from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Problem


def index(request: HttpRequest) -> HttpResponse:
    problems = Problem.objects.all()
    context = {"problems": problems}
    return render(request, "./index.html", context)


def detail(request: HttpRequest, problem_id: int) -> HttpResponse:
    if not (problem := Problem.objects.filter(id=problem_id).first()):
        raise Http404("Problem does not exist")
    return render(request, "./detail.html", {"problem": problem})
