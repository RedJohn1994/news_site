from django import forms

class NewsForms(forms.Form):
    title = forms.CharField()
    content = forms.CharField()


class CommentsForm(forms.Form):
    comment = forms.CharField()

