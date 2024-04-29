from models import link

def ctx_dict(request):
    ctx = {}
    links = link.objects.all()
    for link in links:
        ctx[link.key] = link.url
    return ctx   