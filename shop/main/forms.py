from django import forms
from .models import Tag


class FormCreateCard(forms.Form):
    title = forms.CharField(
        min_length=3,
        max_length=200,
        error_messages={
            'required': 'Введіть заголовок.',
            'min_length': 'Заголовок має містити щонайменше 3 символи.',
            'max_length': 'Заголовок не може містити більше 200 символів.',
        },
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введіть заголовок',
        }),
    )
    description = forms.CharField(
        required=False,
        max_length=200,
        error_messages={
            'max_length': 'Опис не може містити більше 200 символів.',
        },
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Введіть опис',
        }),
    )
    image = forms.ImageField(
        required=False,
        error_messages={'invalid_image': 'Завантажте коректне зображення.'},
        widget=forms.FileInput(attrs={
            'class': 'form-control',
            'accept': 'image/*',
        }),
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        error_messages={
            'invalid_choice': 'Виберіть коректний тег.',
            'invalid_list': 'Надішліть коректний список тегів.',
        },
        widget=forms.CheckboxSelectMultiple,
    )

    def clean_title(self):
        title = self.cleaned_data['title'].strip()
        if title.isdigit():
            raise forms.ValidationError('Заголовок не може складатися лише з цифр.')
        return title

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image and image.size > 5 * 1024 * 1024:
            raise forms.ValidationError('Розмір зображення не може перевищувати 5 МБ.')
        return image
