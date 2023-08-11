from django.shortcuts import render
from django.views import generic
from django.views.generic import FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from perfiles.models import Usuario
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView, DeleteView
from perfiles.models import Usuario
from blog.urls import * 
from blog.models import Post
from perfiles.forms import RegisterForm

class LoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'perfiles/login.html'

class UsuarioDetailView(generic.DetailView):
    model = Usuario
    template_name = 'perfiles/usuario_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usuario'] = self.object 
        return context
    
class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = Usuario
    fields = ['first_name', 'last_name', 'email'] 
    template_name = 'perfiles/usuario_form.html' 

    def get_success_url(self):
        return reverse('perfiles:perfil', kwargs={'pk': self.object.pk})

class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = Usuario
    success_url = reverse_lazy('blog:home')

@login_required
def user_posts(request):
    user = request.user
    posts = Post.objects.filter(autor=user)
    context = {'posts': posts}
    return render(request, 'perfiles/user_posts.html', context)

class UsuarioRegistro(FormView):
    template_name = 'perfiles/registro.html'
    form_class = RegisterForm
    success_url =reverse_lazy('perfiles:success')

    def form_valid(self, form):
        form.save()
        return super(UsuarioRegistro, self).form_valid(form)
