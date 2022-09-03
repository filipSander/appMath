from libgravatar import Gravatar

from articles.models import Comment


def get_some_last_comments(count):
    comments = Comment.objects.all()[:count]

    for c in comments:
        g = Gravatar(c.user.email)
        c.user.email = g.get_image()

    return comments
