from .models import Category, Movie
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from movie.forms import ReviewForm
from django.contrib.auth.decorators import login_required

from movie.models import Movie, Review, Category

# Create your views here.

# Movie show korano porjonto

# def home(request):
#     searchTerm = request.GET.get('SearchMovie')
#     movies = Movie.objects.all()
#     return render(request, 'home.html', {'searchTerm': searchTerm, 'movies': movies})


def home(request):
    searchTerm = request.GET.get('SearchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()
    return render(request, 'home.html', {'searchTerm': searchTerm, 'movies': movies})


# To get Category wise data


# def home(request, category_name=None, subcategory_name=None):
#     searchTerm = request.GET.get('SearchMovie')
#     movies = Movie.objects.all()

#     if category_name:
#         category = Category.objects.get(name=category_name)
#         if subcategory_name:
#             subcategory = Category.objects.filter(
#                 name=subcategory_name, parent_categories=category)
#             if subcategory.exists():
#                 movies = movies.filter(categories__in=subcategory)
#             else:
#                 movies = Movie.objects.none()
#         else:
#             movies = movies.filter(categories=category)

#     if searchTerm:
#         movies = movies.filter(title__icontains=searchTerm)

#     return render(request, 'home.html', {'searchTerm': searchTerm, 'movies': movies})


def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    reviews = Review.objects.filter(movie=movie)
    return render(request, 'detail.html', {'movie': movie, 'reviews': reviews})


@login_required
def createReview(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'GET':
        return render(request, 'create_review.html', {'title': 'Add Review For', 'form': ReviewForm(), 'movie': movie})
    else:
        try:
            form = ReviewForm(request.POST)
            newReview = form.save(commit=False)
            newReview.user = request.user
            newReview.movie = movie
            newReview.save()
            return redirect('details', newReview.movie.id)
        except ValueError:
            return render(request, 'create_review.html',
                          {'form': ReviewForm(), 'error': 'Bad data passed in', 'title': 'Add Review For'})


@login_required
def updateReview(request, review_id):
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    if request.method == 'GET':
        form = ReviewForm(instance=review)
        return render(request, 'create_review.html', {'title': 'Update Review For', 'movie': review.movie.title, 'form': form})
    else:
        try:
            form = ReviewForm(request.POST, instance=review)
            form.save()
            return redirect('details', review.movie.id)
        except ValueError:
            return render(request, 'create_review.html', {'title': 'Update Review For', 'movie': review.movie.title, 'form': form, 'error': 'Bad data in form'})


@login_required
def deleteReview(request, review_id):
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    review.delete()
    return redirect('details', review.movie.id)
