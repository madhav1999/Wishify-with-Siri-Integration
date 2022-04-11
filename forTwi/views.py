from http.client import HTTPResponse
from django.shortcuts import render
from django.http.response import HttpResponseRedirect

from .models import forTwi
# Create your views here.
from django.views.generic import CreateView,ListView,DetailView,UpdateView
from django.views.generic.edit import DeleteView #for delete
from django.contrib.auth.mixins import LoginRequiredMixin



from .forms import forTwiForm

class forTwiList(LoginRequiredMixin,ListView):
    model = forTwi
    context_object_name = "dataT"
    Template_name = 'forTwi/forTwi_list.html'
    login_url = "/login"

    def get_queryset(self):
        return self.request.user.fort.all()


class forTwiDetailView(DetailView):
    model = forTwi
    context_object_name = "dataD"

class forTwiCreateView(CreateView):
    model = forTwi
    success_url = '/dataofT/allTabs'
    form_class = forTwiForm
    #this definition is for in our model there is one column for user inorder to fill it automatically
    def form_valid(self, form): #this is to tell the logged user details has to be automatically filled when we create a new rack of data in data table
        self.object = form.save(commit=False) # not to save automatically as it throws error as we are not giving user details in the form
        self.object.user = self.request.user #we are requesting for user details 
        self.object.save()
        return HttpResponseRedirect('/dataofT/allTabs')
    

class forTwiUpdateView(UpdateView):
    model = forTwi
    success_url = '/dataofY/allTabs'
    form_class = forTwiForm

class forTwiDeleteView(DeleteView):
    model = forTwi
    success_url = '/dataofT/allTabs'
    template_name='forTwi/forTwi_delete.html'
    context_object_name = "dataD"