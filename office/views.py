from django.shortcuts import resolve_url, redirect, render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from openpyxl import load_workbook
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from django.utils import timezone
from .models import Post, KidPost, Customer, Material
from .forms import OfficeForm, OfficeKidForm
import requests
import os
from pathlib import Path
import win32com.client
import pythoncom

import datetime

now = datetime.datetime.now()

BASE_DIR = Path(__file__).resolve().parent.parent

class Excel():

    def __init__(self, visible=False):
        """ Excel機能を提供するクラス """
        pythoncom.CoInitialize()  # Excelを起動する前にこれを呼び出す
        self._app = win32com.client.DispatchEx("Excel.Application")
        self._app.Visible = visible

    def app(self):
        return self._app

    def quit(self):
        """ Excelを終了させる """
        self.app.Quit()
        pythoncom.CoUninitialize()  # Excelを終了した後はこれを呼び出す

class PostListView(ListView):
    model = Post
    template_name = 'office/index.html'
    context_object_name = 'posts'
    ordering = ['customer_deadline']


class WinPostCreateView(CreateView):
    model = Post
    # fields = '__all__'
    form_class = OfficeForm
    template_name = 'office/create.html'
    success_url = reverse_lazy('office-index')

    def form_valid(self, form):
        # Excelテンプレートを読み込む
        excel = Excel().app()
        excel.DisplayAlerts = False
        workbook = excel.Workbooks.Open(os.path.abspath('data/excel/temp_prot.xlsx'))
        worksheet = excel.Workbooks[0].Worksheets(1)
        # 入力内容をExcelファイルに書き込む
        res = self.request.POST
        worksheet.Range("B2").Value = Post.object.get(customer=(res['customer']))
        worksheet.Range("F2").Value = now.strftime("%m/%d (%A)")
        worksheet.Range("I2").Value = res['my_company_deadline_month'] + '/' + res['my_company_deadline_day']
        worksheet.Range("N2").Value = res['customer_deadline_month']+'/'+res['customer_deadline_day']
        worksheet.Range("D3").Value = res['memo']
        worksheet.Range("S2").Value = res['customer']
        worksheet.Range("AF2").Value = res['quantity']
        worksheet.Range("T3").Value = res['material']
        worksheet.Range("U6").Value = res['memo']
        worksheet.Range("AC38").Value = res['customer']

        # PDFファイルを作成する
        output_path = os.path.abspath('output.pdf')
        worksheet.ExportAsFixedFormat(0, output_path)

        # Excelを終了する
        workbook.Close()
        excel.quit()

        # PDFファイルをダウンロードさせる
        with open(output_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename=output.pdf'
        os.remove(output_path)
        return response

        excel = win32com.client.DispatchEx(
            "Excel.Application")  # Excelを操作するための設定
        file = excel.Workbooks.Open('Excelファイルの絶対パス')
        excel = win32com.client.Dsipatch("Excel.Application")
        file = excel.Workbooks.Open("エクセルファイルの絶対パス(拡張子は.xlsx)")
        file.WorkSheets(BASE_DIR.joinpath(
            'data/excel/temp_prot.xlsx')).Select()
        file.ActiveSheet.ExportAsFixedFormat(0, "output.pdf")


class PostCreateView(CreateView):
    model = Post
    # fields = '__all__'
    form_class = OfficeForm
    template_name = 'office/create.html'
    success_url = reverse_lazy('office-index')

    def get_success_url(self):
        # rb = xlrd.open_workbook((BASE_DIR.joinpath(
        #     'data/excel'), 'temp_prot.xlsx'), formatting_info=True, on_demand=True)
        return resolve_url('office-index')





class PostUpdateView(UpdateView):
    model = Post
    form_class = OfficeForm
    template_name = 'office/update.html'

    def get_success_url(self):
        return reverse('office-index')

    def get_form(self):
        form = super(PostUpdateView, self).get_form()
        form.fields['customer'].label = '取引先'

        return form


class PostDetailView(DetailView):
    model = Post
    template_name = 'office/detail.html'


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'office/delete.html'

    def get_success_url(self):
        return reverse('office-index')


""" Office-Kid """
""" PostKidとKidPostの順番を間違えた """


class PostKidListView(ListView):
    model = KidPost
    template_name = 'office-kid/index.html'
    context_object_name = 'post_kids'
    ordering = ['customer_deadline']

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['posts'] = Post.objects.all
        return context


class PostKidCreateView(CreateView):
    model = KidPost
    form_class = OfficeKidForm
    template_name = 'office-kid/create.html'

    def get_success_url(self):
        return resolve_url('office-kid-index')


class PostKidUpdateView(UpdateView):
    model = KidPost
    form_class = OfficeKidForm
    template_name = 'office-kid/update.html'

    def get_success_url(self):
        return reverse('office-kid-index')

    def get_form(self):
        form = super(PostKidUpdateView, self).get_form()
        form.fields['customer'].label = '取引先'
        return form


class PostKidDeleteView(DeleteView):
    model = KidPost
    template_name = 'office-kid/delete.html'

    def get_success_url(self):
        return reverse('office-kid-index')


""" Customer """


class CustomerListView(ListView):
    model = Customer
    template_name = 'customer/index.html'
    context_object_name = 'customers'
    ordering = ['name']


class CustomerCreateView(CreateView):
    model = Customer
    template_name = 'customer/create.html'
    fields = ("name", "email", 'fax', "tel_number_1", "tel_number_2")

    def get_success_url(self):
        return reverse('customer-index')


class CustomerUpdateView(UpdateView):
    model = Customer
    fields = ("name", "email", 'fax', "tel_number_1", "tel_number_2")
    template_name = 'customer/update.html'

    def get_success_url(self):
        return reverse('customer-index')

    def get_form(self):
        form = super(CustomerUpdateView, self).get_form()
        form.fields['name'].label = '取引先'
        return form


class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customer/delete.html'

    def get_success_url(self):
        return reverse('customer-index')


class MaterialListView(ListView):
    model = Material
    template_name = 'material/index.html'
    context_object_name = 'materials'
    ordering = ['name']


class MaterialCreateView(CreateView):
    model = Material
    template_name = 'material/create.html'
    fields = ("name")

    def get_success_url(self):
        return reverse('material-index')


class MaterialUpdateView(UpdateView):
    model = Material
    fields = ("name")
    template_name = 'material/update.html'

    def get_success_url(self):
        return reverse('material-index')

    def get_form(self):
        form = super(MaterialUpdateView, self).get_form()
        form.fields['name'].label = '取引先'
        return form


class MaterialDeleteView(DeleteView):
    model = Material
    template_name = 'material/delete.html'

    def get_success_url(self):
        return reverse('material-index')
