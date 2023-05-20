from django.db import models

class Coffee(models.Model):
    image = models.ImageField(upload_to='coffee/')
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    is_about = models.BooleanField(default=False)
    is_blog = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Coffee'
        verbose_name_plural = "Coffee lar"
        
    

class Feedback(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    message = models.TextField()
    is_approved = models.BooleanField(default=False)
    
    def __str__(self):
        return self.phone_number
    
    class Meta:
        verbose_name = 'Feedback'
        verbose_name_plural = "Feedbacks"

