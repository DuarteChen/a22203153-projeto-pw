from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path('', views.portfolio_view, name="portfolio"),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name="logout"),
    path('registo/', views.registo_view, name="registo"),

    path('aboutme/', views.aboutMe_view, name="aboutMe"),
    path('user/', views.user_view, name="userView"),

    #path('subject/<int:subjectId>/', views.subject_view, name="subjectView"), #href="{% url 'subjectView' cadeira.id %}"


]
