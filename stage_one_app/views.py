from django.shortcuts import render
from django.http import JsonResponse
import datetime

daysOfTheWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
# Create your views here.
def index(request):
    
    
    slack_name = "Paul K"
    current_day = daysOfTheWeek[datetime.datetime.today().weekday()]
    track = "backend"
    github_file_url = "https://github.com/username/repo/blob/main/file_name.ext",
    github_repo_url = "https://github.com/username/repo",

    return JsonResponse({
        "slack_name" : "Paul K",
        "current_day": daysOfTheWeek[datetime.datetime.today().weekday()],
         "utc_time": datetime.datetime.now(),
        'track' :"backend",
        'github_file_url' : "https://github.com/username/repo/blob/main/file_name.ext",
        'github_repo_url' : "https://github.com/username/repo",
        'status_code' : 200
    },safe=False)

