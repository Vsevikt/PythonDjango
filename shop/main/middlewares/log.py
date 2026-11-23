import time
from http import cookies


# class LogMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#         print('LogMiddleware')
#         request.my_data = 'Hello'
#         response = self.get_response(request)
#         return response


class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.perf_counter()
        try:
            response = self.get_response(request)
            return response
        finally:
            execution_time = time.perf_counter() - start_time