from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.db.models.functions import Coalesce

news = "NE"
articles = "AR"

POST = [
    (news, "Новость"),
    (articles, "Статья")
]


class Author(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    rating_author = models.IntegerField(default=0)

    def update_rating(self):
        sum_rating_of_post_multiply = Post.objects.filter(author_id=self.pk).aggregate(rating=Sum('rating_post'))['rating'] * 3
        rating_comments_author = Comment.objects.filter(comment_user=self.author).aggregate(comment_rating=Coalesce(Sum('rating_comment'),0))['comment_rating']
        rating_comments_post = Comment.objects.filter(comment_post__author__author=self.author).aggregate(post_rating=Sum('rating_comment'))['post_rating']
        # print(sum_rating_of_post_multiply)
        # print('..........................')
        # print(rating_comments_author)
        # print('..........................')
        # print(rating_comments_
 post)
        self.rating_author = sum_rating_of_post_multiply + rating_comments_author + rating_comments_post
        self.save()

class Category(models.Model):
    name = models.CharField(max_length=25, unique=True)


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_type = models.CharField(max_length=2, choices=POST, default=news)
    date_in = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through="PostCategory")
    title = models.CharField(max_length=200)
    text = models.TextField()
    rating_post = models.IntegerField(default=0)

    def like(self):
        self.rating_post += 1
        self.save()

    def dislike(self):
        self.rating_post -= 1
        self.save()

    def preview(self):
        return self.text[:124] + '...'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_in = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    rating_comment = models.IntegerField(default=0)

    def like(self):
        self.rating_comment += 1
        self.save()

    def dislike(self):
        self.rating_comment -= 1
        self.save()
