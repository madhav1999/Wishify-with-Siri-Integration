from django.shortcuts import render
from django.urls import reverse_lazy

from forYou.forms import forYouForm
from django.http.response import HttpResponseRedirect


# Create your views here.

#this is to display the data from the data tables on web pages
from .models import forYou
 #this is from another app but to display on one page with details

#class based views libraries from here
from django.views.generic import CreateView,ListView,UpdateView,DetailView
from django.views.generic.edit import DeleteView #for delete
#createview is for entering data into tables, listview is for listing the data from the table
#update view is for updating the data in tables
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import forYouForm #this for model forms- which is used to validate the data and then to reflect data into table

# def list(request):
#     all_data1 = forYou.objects.all()
#     all_data2 = forTwi.objects.all()
#     return render(request, 'forYou/forYou_list.html', {'dataY':all_data1,'dataT':all_data2})
############################################################################
class forYouList(LoginRequiredMixin, ListView):
    model = forYou
    context_object_name = "dataY"
    Template_name = 'forYou/forYou_list.html'
    login_url = "/login"

#this is to display the queries only to the logged in user
    def get_queryset(self):
        return self.request.user.fory.all()

class forYouDetailView(DetailView):
    model = forYou
    context_object_name = "dataD"


class forYouCreateView(CreateView):
    model = forYou
    form_class = forYouForm
    success_url = '/dataofY/allTabs'

    #this definition is for in our model there is one column for user inorder to fill it automatically
    def form_valid(self, form): #this is to tell the logged user details has to be automatically filled when we create a new rack of data in data table
        self.object = form.save(commit=False) # not to save automatically as it throws error as we are not giving user details in the form
        self.object.user = self.request.user #we are requesting for user details 
        self.object.save()
        return HttpResponseRedirect(self.success_url)


class forYouUpdateView(UpdateView):
    model = forYou
    form_class = forYouForm
    success_url = '/dataofY/allTabs'

class forYouDeleteView(DeleteView):
    model = forYou
    success_url = '/dataofY/allTabs'
    template_name='forYou/forYou_delete.html'
    context_object_name = "dataD"