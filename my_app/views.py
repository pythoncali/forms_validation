from django.http import HttpResponse
from django.template import RequestContext, loader
from .forms import ContactForm

# Create your views here.
def my_view(request):
    template = loader.get_template('my_faulty_template.html')
    if request.GET.get('name'):
        context = {
            'name': request.GET.get('name'),
            'email': request.GET.get('email'),
            'message': request.GET.get('message'),
        }
    else:
        context={}
    return HttpResponse(template.render(context))

def my_better_view(request):
    template = loader.get_template('my_slightly_better_template.html')
    context = {}
    if request.method == 'GET':
        form = ContactForm(request.GET)
        if form.is_valid():
            context = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'message': form.cleaned_data['message'],
            }
        context['form'] = form

        return HttpResponse(template.render(context))

def my_csv_display(request):
    template = loader.get_template('my_csv_data_display.html')
    context = {}
    my_valid_contacts = []
    import csv
    with open('my_app/csv_file.csv', 'rb') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        for row in reader:
            data={
                'name': row[0],
                'email': row[1],
                'message': row[2],
            }
            form = ContactForm(data=data)
            if form.is_valid():
                my_valid_contacts.append(
                        [form.cleaned_data.get('name'),\
                        form.cleaned_data.get('email'),\
                        form.cleaned_data.get('message')]
                    )
    context['contact_list'] = my_valid_contacts
    return HttpResponse(template.render(context))

