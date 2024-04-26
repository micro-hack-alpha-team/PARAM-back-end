from django import forms


class ArticleUploadForm(forms.ModelForm):
    title = forms.CharField(max_length=50)
    file = forms.FileField()