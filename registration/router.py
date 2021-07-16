
from django.conf.urls import url, include
from rest_framework import routers

from registration import views

router = routers.DefaultRouter()
# router.register(r'persons', views.person.PersonViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api/person$', views.person),
    url(r'^api/documentTypes$', views.document_type),
    url(r'^api/registration/preregistration$', views.pre_registration),
    url(r'^api/registration/registration$', views.registration),
    url(r'^api/registration/events$', views.events),
    url(r'^api/registration/tempRegistration$', views.tempRegistration),
    url(r'^api/text$', views.get_text),
    url(r'^api/questions$', views.get_questions),
    url(r'^api/registration/handwash$', views.hand_wash_registration)

]

