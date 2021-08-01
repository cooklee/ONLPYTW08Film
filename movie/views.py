

from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView, ListView, DeleteView

from movie.forms import MovieForm
from movie.models import Movie, Actor


class AddMovieView(View):

    def get(self, request):
        form = MovieForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_movie')
        return render(request, 'form.html', {'form': form})


class ListMovieView(View):
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, 'list.html', {'object_list': movies})


class AddActorView(CreateView):
    model = Actor
    fields = '__all__'
    template_name = 'form.html'

    def get_success_url(self):
        actor = self.object
        url = reverse('detail_actor', args=(actor.id,))
        return url




class DetailActorView(DetailView):
    model = Actor
    template_name = 'detailActor.html'


class UpdateActorView(UpdateView):
    model = Actor
    fields = '__all__'
    template_name = 'form.html'

    def get_success_url(self):
        actor = self.object
        url = reverse('detail_actor', args=(actor.id,))
        return url

class DeleteActorView(DeleteView):
    model = Actor
    template_name = 'delete_form.html'
    success_url = reverse_lazy('list_actor')


class ListActorView(ListView):
    model = Actor
    template_name = 'list.html'