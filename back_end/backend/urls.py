from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('admin/', admin.site.urls),
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True)))
]
