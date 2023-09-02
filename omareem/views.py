from django.shortcuts import render


# Create your views here.
def base_view(request):
    return render(request, 'base.html')


def home_view(request):
    return render(request, 'home-1.html')


def err404_view(request):
    return render(request, '404.html')


def coming_soon_view(request):
    return render(request, 'coming-soon.html')


def careers_view(request):
    return render(request, 'careers.html')


def blog_view(request):
    return render(request, 'blog.html')


def contact_view(request):
    return render(request, 'contact.html')


def about_view(request):
    return render(request, 'about.html')


def event_view(request):
    return render(request, 'event.html')


def faq_view(request):
    return render(request, 'faq.html')


def home2_view(request):
    return render(request, 'home-2.html')


def index_view(request):
    return render(request, 'index.html')


def portfolio_view(request):
    return render(request,'portfolio.html')


def prices_view(request):
    return render(request, 'prices.html')


def project_view(request):
    return render(request, 'project.html')


def publication_view(request):
    return render(request, 'publication.html')


def service1_view(request):
    return render(request, 'service-1.html')


def service2_view(request):
    return render(request, 'service-2.html')


def service3_view(request):
    return render(request, 'service-3.html')


def service4_view(request):
    return render(request, 'service-4.html')


def solution1_view(request):
    return render(request, 'solution-1.html')


def solution2_view(request):
    return render(request, 'solution-2.html')


def solution3_view(request):
    return render(request, 'solution-3.html')


def team_view(request):
    return render(request, 'team.html')


def team_single_view(request):
    return render(request, 'team-single.html')