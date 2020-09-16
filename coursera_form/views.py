import json

from django.http import JsonResponse
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from django.shortcuts import render
from django.views import View
from .forms import CourseraForm
from .schemas import REVIEW_SCHEMA
from django.contrib.auth.mixins import LoginRequiredMixin

# decorators for deactive crf_token only for education goals
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


class FormView(LoginRequiredMixin, View):

    def get(self, request):
        # from pdb import set_trace; set_trace()
        form = CourseraForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = CourseraForm(request.POST)
        if form.is_valid():
            context = form.cleaned_data
            return render(request, 'form.html', context)
        else:
            return render(request, 'error.html', {'error': form.errors})


@method_decorator(csrf_exempt, name='dispatch')
class SchemaView(View):
    """Going to use json schema for validating data
        Will be looking like point into users API
    """

    def post(self, request):
        try:
            document = json.loads(request.body)
            validate(document, REVIEW_SCHEMA)
            return JsonResponse(document, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'There is Invalid Json'}, status=400)
        except ValidationError as exc:
            return JsonResponse({'error': exc.message}, status=400)
