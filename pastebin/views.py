from django.shortcuts import render
from django.http import HttpResponse
from django.db.utils import IntegrityError
from json import dumps
from hashlib import sha256

from pastebin.models import Post

# Create your views here.
def home(request):
    if request.method == 'POST':
        filename = request.POST.get('filename')
        content = request.POST.get('content')

        res = {}

        if not (0 < len(filename) < 32):
            res['success'] = False
            res['message'] = 'Filename too long'
        elif not (0 < len(content) < 1024):
            res['success'] = False
            res['message'] = 'Content too long'

        try:
            if 'success' not in res:
                hash = sha256(content.encode('utf-8')).hexdigest()
                Post.objects.create(id=hash, filename=filename, content=content)
                res['success'] = True
                res['id'] = hash
        except IntegrityError:
            res['success'] = False
            res['message'] = 'Post duplicated'
        except:
            res['success'] = False
            res['message'] = 'Unknown error, please contact admin'

        return HttpResponse(dumps(res), content_type='application/json')
    else:
        hash = request.GET.get('id')

        if hash is not None:
            try:
                res = Post.objects.get(id=hash)
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
