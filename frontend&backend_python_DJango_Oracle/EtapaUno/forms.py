from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import Comuna, Publicacion

class PublicacionForm(forms.ModelForm):

    id = forms.CharField(label='Id',max_length=6, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    lapublicacion = forms.CharField(label='Descripción', max_length=1000, widget=forms.Textarea(
        attrs={
            'class':'form-control'
        }
    ))
    fecha = forms.DateField(label='Fecha',widget=forms.DateInput(
        attrs={
            'class':'form-control'
        }
    ))
    comuna = forms.ModelChoiceField(queryset=Comuna.objects.all(), label='Comuna',widget=forms.Select(
        attrs={
            'class':'form-control' 
        }
    ))
    class Meta:
        model = Publicacion
        fields = ('id', 'lapublicacion', 'fecha','comuna')
