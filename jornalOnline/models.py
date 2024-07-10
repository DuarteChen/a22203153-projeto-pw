from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth import get_user_model

User = get_user_model()

class Article(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    POLITICS = 1
    SCIENCE = 2
    CULTURE = 3
    ENTERTAINMENT = 4
    SPORTS = 5
    TECHNOLOGY = 6
    HEALTH = 7
    BUSINESS = 8
    ENVIRONMENT = 9
    WORLD = 10

    TIPO_CHOICES = [
        (POLITICS, "Politics"),
        (SCIENCE, "Science"),
        (CULTURE, "Culture"),
        (ENTERTAINMENT, "Entertainment"),
        (SPORTS, "Sports"),
        (TECHNOLOGY, "Technology"),
        (HEALTH, "Health"),
        (BUSINESS, "Business"),
        (ENVIRONMENT, "Environment"),
        (WORLD, "World"),
    ]

    category = models.IntegerField(choices=TIPO_CHOICES, default=POLITICS)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publication_date']

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment on {self.article.title}"

    class Meta:
        ordering = ['-timestamp']

class Rating(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='ratings')
    score = models.PositiveIntegerField(validators=[MaxValueValidator(5)])
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Rating for {self.article.title}"
