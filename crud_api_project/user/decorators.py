from django.utils.decorators import method_decorator

def filter_class(filter_class):
    def decorator(func):
        func.filter_class = filter_class
        return func
    return decorator

method_decorator(filter_class)





