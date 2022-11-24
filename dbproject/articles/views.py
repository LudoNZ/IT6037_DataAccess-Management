from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.decorators.csrf import csrf_exempt
from .models import Articles, Category
from .forms import ArticlesForm

# Create your views here.

@csrf_exempt
def create_article(request):
    new_form = ArticlesForm(instance=Articles())

    if request.method == 'POST':

        filled_form = ArticlesForm(request.POST)

        if filled_form.is_valid():
            article = filled_form.save()
            
            note = 'Article Created: %s' %(article.name)

            context = {'note': note,
                        'article': article,
                        }
            return render(request, 'articles/article.html', context)

        else:
            note = 'Article creation Failed, please try again'
            new_form = filled_form

        context = {'article_form': new_form,
                    'note': note,
                    }
    else:
        note = 'Create new Article'

        context = {'article_form': new_form,
                    'note': note,
                    }
    return render(request, 'articles/forms/create_article.html', context)

@csrf_exempt
def update_article(request, pk):
    article = Articles.objects.get(pk=pk)
    form = ArticlesForm(instance=article)

    if request.method == 'POST':
        filled_form = ArticlesForm(request.POST, instance=article)

        if filled_form.is_valid():
            filled_form.save()
            form = filled_form
            note = 'Article updated: %s' %(filled_form.cleaned_data['name'])

            context = {'note': note,
                        'article': article,
                        }
            return render(request, 'articles/article.html', context)
        else:
            note = 'ERROR, please try again'
    else:
        note = 'updating %s' %(article.name)

    context = {'article_form': form,
                        'article': article,
                        'note': note,
                        }
    return render(request, 'articles/forms/create_article.html', context)
    

@csrf_exempt
def delete_article(request, pk):
    article = Articles.objects.get(pk=pk)
    article.delete()
    return render(request, 'articles/home.html')



@csrf_exempt
def create_category(request):
    name = request.POST['name']

    category = Category(name=name)
    category.save()

    response = "Category created: " + name

    return HttpResponse(response)

def search_result(request):
    articles = Articles.objects.all()
    search_value = request.GET['search'].lower()
    search_results = []

    for a in articles:
        if search_value in a.name.lower():
            a.about = a.about[:100] + "...."
            search_results.append(a)

    context = {'search_value': search_value,
                'articles':search_results,
                'title': 'Search result',
                }

    return render(request, "articles\search_result.html", context)

class HomePageView(TemplateView):

    def get(self, request):

        return render(request, "articles\home.html")

class ArticleView(TemplateView):

    def get(self, request, pk):

        article = Articles.objects.get(id=pk)

        context = {'article':article}

        return render(request, "articles/article.html", context)

class CategoryView(TemplateView):

    def get(self, request, pk):
        category = Category.objects.get(id=pk)
        articles = Articles.objects.filter(category=category.name)

        for a in articles:
            a.about = a.about[:150] + "...."

        context = {'category':category,
                    'articles':articles,
                    'title': category.name,
                    }

        return render(request, "articles/search_result.html", context)