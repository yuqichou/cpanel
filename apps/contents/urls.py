from django.conf.urls import patterns,  url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

contents_urlpatterns = patterns('',
    url(r'^main.html', 'apps.contents.views.main_page'),
    url(r'^topNav.html', 'apps.contents.views.top_page'),
    url(r'^mainFrame.html','django.views.generic.simple.direct_to_template',{'template': 'mainFrame.html'}),
    url(r'^leftMenu.html', 'apps.contents.views.left_catalogues'),
    
    url(r'^view/(?P<app_id>\w+)/(?P<model_name>\w+)/$','apps.contents.views.view_page'),
    
)




