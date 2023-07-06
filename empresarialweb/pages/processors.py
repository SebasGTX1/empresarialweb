from .models import Page


def ctx_dict(request):
    ctx = {}
    pages = Page.objects.all()
    for page in pages:
        ctx[page.key] = page.id
    return ctx
