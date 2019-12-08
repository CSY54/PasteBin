from django.shortcuts import render
from django.http import HttpResponse
from django.db.utils import IntegrityError
from json import dumps

from pastebin.models import Post

# Create your views here.
def home(request): 
    if request.method == 'POST':
        filename = request.POST.get('filename')
        content = request.POST.get('content')

        res = {}

        if not (0 < len(filename) < 64):
            res['success'] = False
            res['message'] = 'Filename too long'
        elif not (0 < len(content) < 1024):
            res['success'] = False
            res['message'] = 'Content too long'

        try:
            if 'success' not in res:
                Post.objects.create(filename=filename, content=content)
                res['success'] = True
                res['filename'] = filename 
        except IntegrityError:
            res['success'] = False
            res['message'] = 'Filename duplicated'
        except:
            res['success'] = False
            res['message'] = 'Unknown error, please contact admin'

        return HttpResponse(dumps(res), content_type='application/json')
    else:
        filename = request.GET.get('filename')

        if filename is not None:
            try:
                res = Post.objects.get(filename=filename)
                return render(request, 'index.html', {
                    'is_post': True,
                    'filename': res.filename,
                    'content': res.content,
                    'timestamp': res.timestamp,
                })
            except:
                return render(request, 'index.html', {
                    'is_post': True,
                    'error': True
                })
        else:
            return render(request, 'index.html', {
                'is_post': False,
            })
