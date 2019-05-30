from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from editorweb import views as editorweb
from joinweb import views as joinweb

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', editorweb.home, name="home"),
    path('new/<int:person_id>', editorweb.new, name="new"),
    #path('board/<int:person_id>/', editorweb.board, name="board"),
    path('summary/<int:person_id>/', editorweb.summary, name="summary"),
    path('read/<int:post_id>/' , editorweb.read,name="read"),
    path('renew/<int:post_id>/' , editorweb.renew , name="renew"),
    path('create/<int:person_id>/',editorweb.create, name="create"),
    path('update/<int:post_id>/' , editorweb.update, name="update"),
    path('delete/<int:post_id>/' , editorweb.delete, name="delete"),
    path('signup/', joinweb.signup, name='signup'),
    path('login/', joinweb.login, name='login'),
    path('logout/', joinweb.logout, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
