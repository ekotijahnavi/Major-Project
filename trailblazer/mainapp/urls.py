from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^signup/',views.signupaction,name='signupaction'),
    url(r'^projectideas',views.projectideas,name='projectideas'),
    url(r'^preview',views.prerequisitesview,name='preview'),
    url(r'^preweb',views.preweb,name='preweb'),
    url(r'^madview',views.madview,name='madview'),
    url(r'^premlview',views.premlview,name='premlview'),
    url(r'^cseview',views.cseview,name='cseview'),
    url(r'^eceview',views.eceview,name='eceview'),
    url(r'^prevlsi',views.prevlsiview,name='prevlsi'), 
    url(r'^embedded',views.embeddedview,name='embedded'), 
    url(r'^preiot',views.iotview,name='preiot'),
    url(r'^autocad',views.autocadview,name='autocad'),
    url(r'^revit',views.revitview,name='revit'),
    url(r'^sketchup',views.sketchupview,name='sketchup'),
    url(r'^contact',views.contact,name='contact'),
    url(r'^feed',views.feedbackview,name='feed'),
    url(r'^cseab/',views.cseabstract,name='cseab'),
    url(r'^civilab/',views.civilabstract,name='civilab'),
    url(r'^mechab/',views.mechabstract,name='mechab'),
    url(r'^csepro/',views.cseproject,name='csepro'),
    url(r'^ecepro/',views.eceproject,name='ecepro'),
    url(r'^civilpro/',views.civilproject,name='civilpro'),
    url(r'^mechpro/',views.mechproject,name='mechpro'),
    url(r'^about/',views.aboutview,name='about'),
]