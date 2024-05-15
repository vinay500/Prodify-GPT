from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@csrf_exempt
def handle_prompt(request):
    print("in handle_prompt")
    if request.method == 'POST':
        print("in post")
        # Get the raw request body
        request_body = json.loads(request.body)
        print('request_body: ',request_body)
        user_prompt = request_body['prompt']
        print('user_prompt: ',user_prompt)
        return JsonResponse({"status":"Success","message":f"Your Prompt: {user_prompt}"})
    return JsonResponse({"status":"Error","message":"Only POST request is Accepted"})