from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path('', views.portfolio_view, name="portfolio"),

    path('contacto/', views.contacto_view, name="contacto"),

    path('pw/', views.programacaoWeb, name="pwView"),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name="logout"),
    path('registo/', views.registo_view, name="registo"),

    path('user/', views.user_view, name="userView"),
    path('autenticacao/login/', views.user_view),

    path('subject/<int:subjectId>/', views.subject_view, name="subjectView"), #href="{% url 'subjectView' cadeira.id %}"


]
