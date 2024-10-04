# urls.py
from django.urls import path
from .views import (HomepageView,
                    BookDetailView,
                    BookCreateView,
                    BookUpdateView,
                    BookDeleteView,
                    CategoryView,
                    LoginView,
                    RegisterView,
                    LogoutView,
                    DetailCategoryView)


urlpatterns = [
    path('', HomepageView.as_view(), name='home'),
    path('detail-category/', DetailCategoryView.as_view(), name='detail_category'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('book/add/', BookCreateView.as_view(), name='add_book'),
    path('book/<int:pk>/edit/', BookUpdateView.as_view(), name='edit_book'),
    path('book/<int:pk>/delete/', BookDeleteView.as_view(), name='delete_book'),
    path('category/<int:category_id>/', CategoryView.as_view(), name='category_books'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
