from django.http import JsonResponse, HttpResponseNotAllowed
import datetime


def index(request):
    daysOfTheWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    print(request.method)


    if request.method == 'GET':
        print(request.method)
   
        return JsonResponse({
            "slack_name" : request.GET.get('slack_name'),
            "current_day": daysOfTheWeek[datetime.datetime.today().weekday()],
            "utc_time": datetime.datetime.now(),
            'track' :request.GET.get('track'),
            'github_file_url' : "https://github.com/psk-98/stage_one/blob/trunk/stage_one_app/views.py",
            'github_repo_url' : "https://github.com/psk-98/stage_one",
            'status_code' : 200
            },
            safe=False
        )
    
    return HttpResponseNotAllowed()

