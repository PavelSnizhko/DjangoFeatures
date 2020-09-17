import json

from django.http import JsonResponse
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from django.shortcuts import render
from django.views import View
from .forms import CourseraForm
from .schemas import REVIEW_SCHEMA
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from .models import FeedBack
# decorators for deactive crf_token only for education goals
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


class FeedbackCreateView(LoginRequiredMixin, CreateView):
    model = FeedBack
    fields = ['text', 'grade', 'subject']
    success_url = '/feedback/add'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)





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
