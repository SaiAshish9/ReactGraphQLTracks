from django.db import models

from django.contrib.auth import get_user_model




class Track(models.Model):

    def  __str__(self):
        return self.title

    title= models.CharField(max_length=200)
    description= models.TextField(blank=True)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    posted_by=models.ForeignKey(get_user_model(),null=True,on_delete=models.CASCADE)


class Like(models.Model):

    # def __str__(self):
    #     return self.count

    user=models.ForeignKey(get_user_model(),null=True,on_delete=models.CASCADE)
    track= models.ForeignKey('tracks.track',related_name='likes',on_delete=models.CASCADE)