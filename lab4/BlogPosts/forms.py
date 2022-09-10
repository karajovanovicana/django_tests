from django import forms

from BlogPosts.models import Post, CustomUser


class PostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            print(field)
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Post
        exclude = ("user",)


class CustomUserForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CustomUserForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            print(field)
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = CustomUser
        exclude = ("user", "name", "surname", "photo", "interests", "skills", "profession")
