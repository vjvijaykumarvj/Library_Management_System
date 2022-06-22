from django.urls import path
from.import views
app_name = 'Library_app'

urlpatterns=[
    path('dashboard/',views.Library_dashboard),
    path('createBooks/',views.CreateBook),
    path('book_id/<pk>',views.book_id,name='book_id'),
    path('book_update/<pk>',views.book_update,name = 'book_update'),
    path('book_delete/<pk>',views.book_delete,name = 'book_delete'),
]