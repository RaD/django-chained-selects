Introduction
------------

This application add a new widget to your forms. This widget change a behaviour
of a Select widget linking it to other select field.

For instance, let you have two select fields on the form: 'categories' and
'items'. Usually, visitors want to choose a category and then take an item
of this category. This widget helps you implement this functionality.

Installation
------------

Hint: Use a virtual environment!

To install this package run::

    pip install -e git+git://github.com/RaD/django-chained-selects#egg=django-chunks

Add the following line into ``INSTALLED_APPS`` in ``settings.py``::

    'chained_selects',

Add the following line into main ``urls.py``::

    url(r'^chained/', include('chained_selects.urls')),

Usage
-----

We have following models::

    class Category(models.Model):
        title = models.CharField(max_length=64)

    class Item(models.Model):
        title = models.CharField(max_length=64)

You have to implement a model method that will return a queryset. Use this
method to make filtering a resulting queryset. You may use any name for this
method. For instance::

    def chained_relation(self):
        return self.relation_set.filter(duration_a__gt=0)

Create a form::

    from chained_selects.widgets import ChainedSelectWidget

    class CatItemForm(forms.ModelForm):
        category = ModelChoiceField(
            label=_('Category'),
            queryset=Category.objects.all()

        class Meta:
            model = Item

        def __init__(self, *args, **kwargs):
            super(CatItemForm, self).__init__(*args, **kwargs)

            if 0 == len(self.data):
                # clear queryset if we just show a form
                self.fields['task'].queryset = Relation.objects.none()

            # assign a widget to second select field
            self.fields['item'].widget = ChainedSelectWidget(
                parent_name='category',         # the name of parent field
                app_name='app_name',            # the name of model's application
                model_name='item',              # the name of related model
                method_name='chained_relation', # the name of queryset method
                )

Then use this form as usual.
