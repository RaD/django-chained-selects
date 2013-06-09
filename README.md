Introduction
------------

This application adds a new widget into your forms. This widget changes
a behaviour of a Select widget linking it to other select field.

For instance, let you have two select fields on a form: 'categories' and
'items'. Usually, visitors want to choose a category and then take an item
of this category. This widget helps you implement this functionality.

Installation
------------

Hint: Use a virtual environment!

To install this package run:

    pip install -e git+git://github.com/RaD/django-chained-selects#egg=django-chunks

Add the following line into ``INSTALLED_APPS`` in ``settings.py``:

    'chained_selects',

Add the following line into main ``urls.py``:

    url(r'^chained/', include('chained_selects.urls')),

Usage
-----

We have following models:

    class Category(models.Model):
        title = models.CharField(max_length=64)

    class Item(models.Model):
        category = models.ForeignKey(Category)
        title = models.CharField(max_length=64)
        is_present = models.BooleanField(default=False)

You have to implement a model method that will return a queryset. Use this
method to filter a resulting queryset. You may use any name for this
method. For instance:

    class Category(models.Model):
        ...
        def chained_relation(self):
            return self.item_set.filter(is_present=True)

Create a form:

    from chained_selects.widgets import ChainedSelectWidget

    class TestForm(forms.Form):

        category = forms.ModelChoiceField(queryset=Category.objects.all())
        item = forms.ModelChoiceField(queryset=Item.objects.all())

        def __init__(self, *args, **kwargs):
            super(TestForm, self).__init__(*args, **kwargs)

            if 0 == len(self.data):
                # clear queryset if we just show a form
                self.fields['item'].queryset = Item.objects.none()

            # assign a widget to second select field
            self.fields['item'].widget = ChainedSelectWidget(
                parent_name='category',         # the name of parent field
                app_name='app_name',            # the name of model's application
                model_name='category',          # the name of a model with the method
                method_name='chained_relation', # the name of queryset method
                )

Then use this form as usual.
