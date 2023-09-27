from django import forms


class GoodAddForm(forms.Form):
    product_name = forms.CharField(max_length=100, required=True, label='Название товара:', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Введите название товара.'}))
    product_description = forms.CharField(label='Описание товара',
                                          widget=forms.Textarea(attrs={'placeholder': 'Введите описание товара.'}))
    product_price = forms.DecimalField(max_digits=10, decimal_places=2, label='Цена товара:')
    product_quantity = forms.IntegerField(label='Количество товара:',
                                          widget=forms.NumberInput(attrs={'class': 'form-control'}))
    product_image = forms.ImageField(label='Изображение товара:')
