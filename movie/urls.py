from django.urls import path
from movie.views import createReview, deleteReview, detail, home, updateReview

urlpatterns = [
    path('<int:movie_id>', detail, name='details'),
    path('<int:movie_id>/create', createReview, name='create_review'),
    path('review/<int:review_id>', updateReview, name='update_review'),
    path('review/<int:review_id>/delete/', deleteReview, name='delete_review'),

    # Category Wise
    path('<str:category_name>', home, name='category_movie'),
    path('<str:category_name>/<str:subcategory_name>',
         home, name='subcategory_movie')
]
