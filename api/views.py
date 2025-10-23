import requests
from datetime import datetime
import pytz  # ✅ you need this import
from django.http import JsonResponse


def profile(request):
    # Fetch random cat fact from API
    try:
        response = requests.get("https://catfact.ninja/fact", timeout=5)
        cat_fact = response.json().get("fact", "Cats are fascinating animals.")
    except Exception:
        # fallback if API fails
        cat_fact = "Cats are curious and playful creatures."

    # Set timezone to West Africa Time (UTC+1)
    wat_timezone = pytz.timezone('Africa/Lagos')

    # response data
    
    data = {
        "full_name": "Paul Ebonka",
        "email": "paulebonka4sure@gmail.com",
        "github_url": "https://github.com/Clever2Sure/hng-stage-zero-backend",
        "current_datetime": "2025-10-23T19:45:12.123456+01:00",
        "cat_fact": "Cats sleep 70% of their lives."
    }

    return JsonResponse(data)
