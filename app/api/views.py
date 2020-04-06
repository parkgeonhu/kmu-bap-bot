from django.http import JsonResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from .parser import *



@csrf_exempt
def reply(request):
    response=json.loads(request.body)

    
    content=response['userRequest']['utterance'].rstrip('\n')
    
    allow_keywords=['학생식당(복지관 1층)', '교직원식당(복지관 1층)', '한울식당(법학관 지하1층)', '청향(법학관 5층)', '생활관식당 일반식(생활관 A동 1층)', '생활관식당 정기식(생활관 A동 1층)']
    
    if content not in allow_keywords:
        result = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": "원상연 그만해!"
                        }
                    }
                ]
            }
        }
        return JsonResponse(result, status=200)
        
    # keyboard={
    #                 "type": "buttons",
    #                 "buttons": ['학생식당(복지관 1층)', '교직원식당(복지관 1층)', '한울식당(법학관 지하1층)', '청향(법학관 5층)', '생활관식당 일반식(생활관 A동 1층)', '생활관식당 정기식(생활관 A동 1층)']
    #             }
    print(request.body.decode('utf-8'))
    
    # response=json.loads(request.body)    
    
    event={'content':content}
    
    temp=get_bap(event)
    
    result = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": temp['message']['text']
                    }
                }
            ]
        }
    }

    return JsonResponse(result, status=200)