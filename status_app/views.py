from django.http.response import HttpResponse
# Create your views here.


def home(request, *args, **kwargs):
    """
    Default Home view
    :param request: (HttpRequest) Http Request
    :param args: argument list
    :param kwargs: keyword arguments
    """

    return HttpResponse(content="Welcome to Homepage")
