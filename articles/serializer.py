from rest_framework.serializers import \
    ModelSerializer

from articles.models import \
    Article, \
    Comment


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'