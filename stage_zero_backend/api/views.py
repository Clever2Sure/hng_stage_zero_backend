import requests
from datetime import datetime
from django.http import JsonResponse

def profile(request):
    # Fetch dynamic cat fact
    cat_fact_response = requests.get("https://catfact.ninja/fact")
    cat_fact = cat_fact_response.json().get("fact")

    # Prepare response data
    data = {
        "full_name": "Your Full Name",
        "email": "your-email@example.com",
        "github_url": "https://github.com/your-username/hng-stage-zero-backend",
        "current_datetime": datetime.utcnow().isoformat() + "Z",
        "cat_fact": cat_fact
    }

    return JsonResponse(data)
