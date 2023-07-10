from .models import Page


def ctx_dict(request):
    return {'pages': Page.objects.all()}
