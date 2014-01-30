# coding: utf8

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Project


class ProjectsList(ListView):
	queryset = Project.objects.public()
	template_name = "portfolio-simple/project_list.html"
	paginate_by = 3
	context_object_name = "project_list"


class ProjectDetail(DetailView):
	model = Project
	slug_field = 'slug'
	template_name = "portfolio-simple/project_detail.html"
