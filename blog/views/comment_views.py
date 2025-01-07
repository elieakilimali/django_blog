from django.views.generic import CreateView
from ..models.models import Comment
# from ..forms import CommentForm 

class CommentCreateView(CreateView):
    model = Comment
    # form_class = CommentForm 
    template_name = "blog_comment_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user 
        form.save()
        return super().form_valid(form)
    