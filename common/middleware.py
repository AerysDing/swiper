
'''
import logging

from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

from libs.http import render_json
from common import stat

err_log = logging.getLogger('err')

class AuthMiddleware(MiddlewareMixin):
    '''登陆检查中间件'''
    white_list = (
        '/api/user/get_vcode',
        '/api/user/submit_vcode',
    )

    def process_request(self, request):
        # 检查当前请求的路径是否在 白名单 中
        if request.path in self.white_list:
            return

        uid = request.session.get('uid')
        if not uid:
            return render_json(data='LoginRequired', code=stat.LoginRequired.code)
        else:
            request.uid = uid


class LogicErrMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        if isinstance(exception, stat.LogicErr):
            err_log.error(f'Code: {exception.code}  Data: {exception.data}')
            return render_json(exception.data, exception.code)
