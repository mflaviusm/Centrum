from django.shortcuts import render
from django.http import HttpResponse

projectsList = [
    {
        'id': '1',
        'title': 'Econ',
        'description': 'Project about e-business ideas.'
    },
    {
        'id': '2',
        'title': 'MarketMe',
        'description': 'Website for professionals to showcast their work'
    },
    {
        'id': '3',
        'title': 'Munchy',
        'description': 'A blog for gourmets to discuss everything food related.'
    }
]


def projects(request):
    item = 'projects'
    number = 10
    context = {'item': item, 'number': number, 'projects': projectsList}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectNumber = None
    for i in projectsList:
        if i['id'] == pk:
            projectNumber = i
    return render(request, 'projects/individual-project.html', {'project': projectNumber})
