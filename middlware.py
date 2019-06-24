# 全局中间件设置
def my_middleware(get_response):
    #因为debug这个模式会被调用两次
    print('init 被调用')
    def middleware(request):
        print('before request 被调用')
        response = get_response(request)
        print('after response 被调用')
        return response
    return middleware

# 测试中间件执行顺序
def my_middleware2(get_response):
    #因为debug这个模式会被调用两次
    print('init2 被调用')
    def middleware(request):
        print('before request2 被调用')
        response = get_response(request)
        print('after response2 被调用')
        return response
    return middleware