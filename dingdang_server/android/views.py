from dingdang_server.rsp.models import Messages
from dingdang_server.rsp.models import Users
from django.contrib.auth.hashers import check_password
from django.http.response import HttpResponse
from django.core import serializers
import json
import logging

# Create your views here.

logger = logging.getLogger('android')


def register(request):
    logger.info('enter register page')
    user_data = json.loads(str(request.body, encoding="utf-8"))
    response = HttpResponse(content_type='application/json')
    if len(user_data['password']) < 6:
        response.status_code = 406
        response.content = json.dump({
            'msg': 'your password is too short',
            'data': ''
        })
        logger.info('password is too short')
        return response
    user = Users.create(user_data)
    check_email = Users.objects.filter(email=user_data['email'])
    if check_email:
        response.status_code = 406
        response.content = json.dumps({
            'msg': 'please use another email',
            'data': ''
        })
        logger.info('this email is used')
        return response
    try:
        user.save()
        response.status_code = 200
        response.content = json.dumps({
            'msg': 'register successfully',
            'data': ''
        })
    except Exception:
        response.status_code = 500
        response.content = json.dumps({
            'msg': 'there are some error in database',
            'data': ''
        })
        logger.error('register error!')
    return response


def login(request):
    logger.info('enter login page')
    login_data = json.loads(str(request.body, encoding="utf-8"))
    response = HttpResponse(content_type='application/json')
    try:
        check_user = Users.objects.get(email=login_data['email'])
    except Users.DoesNotExist:
        response.status_code = 401
        response.content = json.dumps({
            'msg': 'you have not registered yet',
            'data': ''
        })
        return response
    if check_password(login_data['password'], check_user.password) is False:
        response.status_code = 401
        response.content = json.dumps({
            'msg': 'your password is wrong',
            'data': ''
        })
    else:
        request.session['user_email'] = check_user.email
        response.content = json.dumps({
            'msg': 'login successfully'
        })
        HttpResponse.status_code = 200
    return response


def logout(request):
    logger.info('enter logout page')
    logout_data = json.loads(str(request.body, encoding="utf-8"))
    response = HttpResponse(content_type='application/json')
    try:
        del request.session['user_email']
        logger.info('logout fail')
        response.status_code = 406
        response.content = json.dumps({
            'msg': 'logout fail',
            'data': ''
        })
        return response
    except:
        response.status_code = 200
        response.content = json.dumps({
            'msg': 'logout successfully',
            'data': ''
        })
    return response


def get_messages(request, email):
    user_data = {'email': email}
    logger.info('to get messages page')
    response = HttpResponse(content_type='application/json')
    try:
        Users.objects.get(email=user_data['email'])
    except Users.DoesNotExist:
        response.status_code = 401
        response.content = json.dumps({
            'msg': 'you have not registered yet',
            'data': ''
        })
        return response
    if user_data['email'] == request.session.get('user_email'):
        messages = Messages.objects.filter(email=user_data['email'], active=True)
        if messages:
            for message in messages:
                message.active = False
                # message.save()
            response.status_code = 200
            messages_data = serializers.serialize('json', messages)
            response.content = json.dumps({
                'msg': 'get new messages successfully',
                'data': messages_data
            })
        else:
            response.status_code = 200
            response.content = json.dumps({
                'msg': 'no new message',
                'data': ''
            })
        return response
    else:
        response.status_code = 401
        response.content = json.dumps({
            'msg': 'you have not login yet',
            'data': ''
        })
    return response
