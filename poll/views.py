from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm, SignUpForm, LoginForm

from django.views.generic import DeleteView, FormView
from .models import Post
from django.conf import settings
from django.shortcuts import redirect

from django.http import HttpResponseRedirect



def home(request):
    return render(request, 'poll/home.html', {})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'poll/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'poll/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'poll/post_substance.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            result = form.login()

            if not result:
                return render (request, 'poll/login.html', {'form': form, 'error': 'Login Failed'})

            else:
                request.session['user_id'] = result[0].id
                print(request.session['user_id'])
                return HttpResponseRedirect('/post/list')

    else:
        print('hello~~~~\\n')
        form = LoginForm()
    return render(request, 'poll/login.html', {'form': form})

def logout(request):
    del request.session['user_id']

    return render(request, 'poll/logout.html', {})

class PostDeleteView(DeleteView):
    model = Post
    template_name = "post_update.html"
    success_url = "/post/list/"

class SignUpView(FormView):
    form_class = SignUpForm
    succes_url = settings.LOGIN_REDIRECT_URL
    template_name = 'sign_up.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect(self.success_url)

        return super(SignUpView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.sign_up(request=self.request)

        return super(SignUpView, self).form_valid(form)

def signup (request):

	if request.method == 'POST':
		form = SignUpForm(request.POST)

		if form.is_valid():
			user_created = form.sign_up()

			if not user_created:
				return render (request, 'poll/sign_up.html', {'form': form, 'error': 'Confirm Password Failed!!!'})

			else:
				return HttpResponseRedirect('/login')

	else:
		form = SignUpForm()


	return render (request, 'poll/sign_up.html', {'form': form})
