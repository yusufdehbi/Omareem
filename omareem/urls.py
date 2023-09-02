from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('404', views.err404_view, name="404"),
    path('about', views.about_view, name="about"),
    path('blog', views.blog_view, name="blog"),
    path('careers', views.careers_view, name="careers"),
    path('coming-soon', views.coming_soon_view, name="coming-soon"),
    path('contact', views.contact_view, name="contact"),
    path('event', views.event_view, name="event"),
    path('faq', views.faq_view, name="faq"),
    path('home2', views.home2_view, name="home2"),
    path('index', views.index_view, name="index"),
    path('portfolio', views.portfolio_view, name="portfolio"),
    path('prices', views.prices_view, name="prices"),
    path('project', views.project_view, name="project"),
    path('publication', views.publication_view, name="publication"),
    path('service1', views.service1_view, name="service1"),
    path('service2', views.service2_view, name="service2"),
    path('service3', views.service3_view, name="service3"),
    path('service4', views.service4_view, name="service4"),
    path('solution1', views.solution1_view, name="solution1"),
    path('solution2', views.solution2_view, name="solution2"),
    path('solution3', views.solution3_view, name="solution3"),
    path('team', views.team_view, name="team"),
    path('team-single', views.team_single_view, name="team-single"),
]
