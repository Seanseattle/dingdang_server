from django.test import TestCase
import time
from dingdang_server.rsp import views
# Create your tests here.


@TestCase
def test_upload():
    data = {
        'email': '1234@qq.com',
        'type': 'todo',
        'message': 'buy some apples',
        'time': time.time()
    }
    response = views.upload(data)
    assert response.status_code is 200
