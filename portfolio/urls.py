from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name="logout"),

    path('aboutme/', views.aboutMe_view, name="aboutMe"),
    path('', views.portfolio_view, name="portfolio"),

    #path('subject/<int:subjectId>/', views.subject_view, name="subjectView"), #href="{% url 'subjectView' cadeira.id %}"


]
