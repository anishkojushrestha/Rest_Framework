from rest_framework import serializers
from .models import Artical

class articalSerializers(serializers.ModelSerializer):
    class Meta:
        model = Artical
        fields = ['title', 'auther','email','date']

         