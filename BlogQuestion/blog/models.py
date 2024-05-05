from django.db import models
from django.utils import timezone
from django.utils.timezone import datetime


# TODO write all of your code here...

class Author(models.Model):
    name = models.CharField(max_length=50)


class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    # Create a Function for Copy Object
    def copy(self):
        # Create New Object
        new_post = BlogPost.objects.create(title=self.title, body=self.body, author=self.author)
        # Change DateTimeField And Save Every thing modified
        new_post.date_created = datetime.now(timezone.utc)
        new_post.save()

        # Copy Comments
        for comment in self.comment_set.all():
            Comment.objects.create(blog_post=new_post, text=comment.text)

        # return id new post
        return new_post.id


class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
