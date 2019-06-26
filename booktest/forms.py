from django import forms

class BookInfoForm(forms.Form):
    btitle = forms.CharField(label='图书名称',required=True,max_length=20)
    bpub_date = forms.DateField(label='发型日期',required=True)
