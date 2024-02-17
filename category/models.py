from django.db import models

from account.models import User



class Category(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # messages = models.ForeignKey(ChatHistory, on_delete=models.CASCADE, blank=True, null=True)
    table = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class ChatHistory(models.Model):
    prompt = models.TextField()
    response = models.TextField()
    image = models.FileField(upload_to='image_responses/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.prompt

    class Meta:
        ordering = ['-created_at']  # Order messages by their creation time in descending order


# class Category(models.Model):
#     name = models.CharField(max_length=255)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     # messages = models.ForeignKey(ChatHistory, on_delete=models.CASCADE, blank=True, null=True)
#     table = models.TextField(blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     modified_at = models.DateTimeField(auto_now=True)
