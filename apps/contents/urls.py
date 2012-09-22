from django.conf.urls import patterns,  url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

contents_urlpatterns = patterns('',
    url(r'^main.html', 'apps.contents.views.main_page'),
    url(r'^topNav.html', 'apps.contents.views.top_page'),
    url(r'^mainFrame.html','django.views.generic.simple.direct_to_template',{'template': 'mainFrame.html'}),
    url(r'^leftMenu.html', 'apps.contents.views.left_catalogues'),
    
    url(r'^(?P<app_id>\w+)/(?P<model_name>\w+)/view/$','apps.contents.views.view_page'),
    url(r'^(?P<app_id>\w+)/(?P<model_name>\w+)/add/$','apps.contents.views.add_page'),
    url(r'^(?P<app_id>\w+)/(?P<model_name>\w+)/save/$','apps.contents.views.save_model_data'),
    url(r'^(?P<app_id>\w+)/(?P<model_name>\w+)/(?P<id>\w+)/del/$','apps.contents.views.del_model_data'),
)




