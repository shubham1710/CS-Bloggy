from django import forms
from .models import PostDetails

class NewCommentForm(forms.ModelForm):

	class Meta:
		model = PostDetails
		fields = ['comment']