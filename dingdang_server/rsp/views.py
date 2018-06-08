from django.http.response import HttpResponse
import json
from .models import Messages, Users
import logging
# Create your views here.
logger = logging.getLogger('rsp')


def login(request):
    pass


def upload(request):
    logger.info('server get message from rsp success')
    data = json.loads(str(request.body, encoding="utf-8"))
    response = HttpResponse(content_type='application/json')
    if data['email'] is None or data['email'] == '':
        logger.info('data lacks email', data)
        response.status_code = 406
        response.content = json.dumps({
            'msg': '',
            'date': ''
        })
    if data['type'] is None or data['type'] == '':
        # must select one type
        logger.info('data lacks type', data)
        response.status_code = 406
        response.content = json.dumps({
            'msg': 'please confirm your message type',
            'date': ''
        })
        return response
    if data['type'] == 'clock' or data['type'] == 'todo':
        if data['time'] is None or data['time'] == '':
            logger.info('data lacks time', data)
            response.status_code = 406
            response.content = json.dumps({
                'msg': 'this message must have time',
                'date': ''
            })
            return response
    try:
        Users.objects.get(email=data['email'])
    except Users.DoesNotExist:
        response.status_code = 401
        response.content = json.dumps({
            'msg': 'you have not registered yet',
            'date': ''
        })
        return response
    message_save = Messages.create(data)
    message_save.save()
    logger.info('message is saved')
    response.status_code = 200
    response.content = json.dumps({
        'msg': 'upload successfully',
        'date': ''
    })
    return response
