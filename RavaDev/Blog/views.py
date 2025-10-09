from django.shortcuts import render
from .models import Post, Category, Review

# Create your views here.
def blog(request):
    categories = Category.objects.all()
    posts = Post.objects.all().order_by('-published_date')
    return render(request, 'Blog/blog.html', {'categories': categories, 'posts': posts})

def category(request, category_id):
    category = Category.objects.get(id=category_id)
    posts = Post.objects.filter(category=category).order_by('-published_date')
    return render(request, 'Blog/category.html', {'category': category, 'posts': posts})

def post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.views += 1
    post.save()
    if request.method == 'POST':
        reviewer_name = request.POST.get('reviewer_name')
        rating = int(request.POST.get('rating'))
        comment = request.POST.get('comment')
        Review.objects.create(post=post, reviewer_name=reviewer_name, rating=rating, comment=comment)
    reviews = Review.objects.filter(post=post).order_by('-review_date')
    return render(request, 'Blog/post.html', {'post': post, 'reviews':reviews})