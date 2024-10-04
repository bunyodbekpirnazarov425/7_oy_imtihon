# views.py
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .admin import BookAdmin
from .models import Book, Category, Comment
from .forms import BookForm, CommentForm, RegisterForm


# Homepage View
class HomepageView(View):
    def get(self, request):
        book_created = Book.objects.all().order_by('-created_at')
        book_price = Book.objects.all().order_by('-price')
        categories = Category.objects.all()
        return render(request, 'index.html', {'books': book_created, 'categories': categories, 'book_price': book_price})

class CategoryView(View):
    def get(self, request, category_id):
        category = Category.objects.get(id=category_id)
        books = Book.objects.filter(category=category)
        categories = Category.objects.all()

        return render(request, 'category_books.html', {
            'category': category,
            'books': books,
            'categories': categories,
        })

# Book Detail View with Comments
class BookDetailView(View):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        comments = book.comments.all()
        form = CommentForm()
        categories = Category.objects.all()
        return render(request, 'detail.html', {'book': book, 'comments': comments, 'form': form, 'category': categories})

    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment.objects.create(
                text=form.cleaned_data.get('text'),
                book=book,
                user=request.user
            )
            return redirect('book_detail', pk=book.pk)
        comments = book.comments.all()
        return render(request, 'detail.html', {'book': book, 'comments': comments, 'form': form})

# Create Book View
class BookCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = BookForm()
        return render(request, 'create.html', {'form': form})

    def post(self, request):
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            print("Forma valid!")
            form.save()
            return redirect('home')
        else:
            return render(request, 'create.html', {'form': form})
# Update Book View
class BookUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        form = BookForm(instance=book)
        context = {'form': form, 'book': book}
        return render(request, 'update.html', context)

    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', pk=book.pk)
        context = {'form': form, 'book': book}
        return render(request, 'update.html', context)

# Delete Book View
class BookDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        return render(request, 'delete_book.html', {'book': book})

    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return redirect('home')

class LoginView(View):
    template_name = 'login.html'
    success_url = reverse_lazy('home')

    def get(self, request):
        form = AuthenticationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect(self.success_url)


        return render(request, self.template_name, {'form': form})


class RegisterView(View):
    template_name = 'register.html'

    def get(self, request):
        form = RegisterForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()  #
            return redirect(reverse_lazy('login'))

        return render(request, self.template_name, {'form': form})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

class DetailCategoryView(View):
    def get(self, request):
        category_id = request.GET.get('category_id')
        if category_id:
            category = Category.objects.get(id=category_id)
            books = Book.objects.filter(category=category)
        else:
            books = Book.objects.all()
        categories = Category.objects.all()

        context = {
            'books': books,
            'categories': categories
        }
        return render(request, 'categorys.html', context)