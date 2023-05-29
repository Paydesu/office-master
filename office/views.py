from typing import Any, Dict
from django.shortcuts import resolve_url, redirect, render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from django.utils import timezone
from .models import Post, Customer, Material
from .forms import OfficeForm, OfficeUpdateForm
import requests
import os
from pathlib import Path
import time
import datetime
import locale
import calendar
import random

# import win32com.client
# import pythoncom
# import pyautogui

BASE_DIR = Path(__file__).resolve().parent.parent


# class Excel():
#     def __init__(self, visible=False):
#         """ Excel機能を提供するクラス """
#         pythoncom.CoInitialize()  # Excelを起動する前にこれを呼び出す
#         self._app = win32com.client.DispatchEx("Excel.Application")
#         self._app.Visible = visible

#     def app(self):
#         return self._app

#     def quit(self):
#         """ Excelを終了させる """
#         self.app.Quit()
#         pythoncom.CoUninitialize()  # Excelを終了した後はこれを呼び出す


class PostListView(ListView):
    model = Post
    template_name = 'office/index.html'
    context_object_name = 'posts'
    # ordering = ['customer_deadline']


# class PostDoneListView(ListView):
#     model = Post
#     template_name = 'office/companyDone.html'
#     context_object_name = 'posts'
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         queryset = queryset.filter(my_company_done=True)
#         return queryset

# class PostUndoneListView(ListView):
#     model = Post
#     template_name = 'office/companyUndone.html'
#     context_object_name = 'posts'
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         queryset = queryset.filter(my_company_done=False)
#         return queryset
    
# class PostDoneListView(ListView):
#     model = Post
#     template_name = 'office/customerDone.html'
#     context_object_name = 'posts'
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         queryset = queryset.filter(customer_done=True)
#         return queryset

# class PostUndoneListView(ListView):
#     model = Post
#     template_name = 'office/customerUndone.html'
#     context_object_name = 'posts'
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         queryset = queryset.filter(customer_done=False)
#         return queryset

class WinPostCreateView(CreateView):
    model = Post
    # fields = '__all__'
    form_class = OfficeForm
    template_name = 'office/create.html'
    def form_valid(self, form):
        # 整理番号のランダム生成
        def randstr(length):
            return ''.join([chr(random.randint(65, 90)) for _ in range(length)])
        w_list = ['月', '火', '水', '木', '金', '土', '日']
        # Excelテンプレートを読み込む
        # excel = Excel().app()
        # excel.DisplayAlerts = False
        # workbook = excel.Workbooks.Open(
        #     os.path.abspath('data/excel/コピーtemplating.xlsx'))
        # worksheet = excel.Workbooks[0].Worksheets(1)
        # # 入力内容をExcelファイルに書き込む
        # res = self.request.POST
        # print('fuck', res)
        # now = datetime.datetime.now()
        # locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')
        # print(locale.getlocale(locale.LC_TIME))
        # supply = '(持)'
        # try:
        #     if res['supply'] == 'on':
        #         supply = '(支)'
        # except:
        #     supply = '(持)'

        # my_company_deadline_date = datetime.datetime(
        #     int(res["my_company_deadline_year"]), int(res["my_company_deadline_month"]), int(res["my_company_deadline_day"]))
        # customer_deadline_date = datetime.datetime(
        #     int(res["customer_deadline_year"]), int(res["customer_deadline_month"]), int(res["customer_deadline_day"]))
        # print(customer_deadline_date.strftime("%m/%d ") +
        #       w_list[customer_deadline_date.weekday()])
        # random_id = randstr(2)
        # worksheet.Range("B2").Value = Customer.objects.get(
        #     id=(res['customer'])).name
        # worksheet.Range("B2").Font.Size = 22
        # worksheet.Range("F2").Value = now.strftime(
        #     "%m/%d ") + f'({w_list[now.weekday()]})'
        # worksheet.Range("F2").Font.Size = 16
        # worksheet.Range("I2").Value = my_company_deadline_date.strftime(
        #     "%m/%d ") + '(' + w_list[my_company_deadline_date.weekday()] + ')'
        # worksheet.Range("I2").Font.Size = 22
        # worksheet.Range("M2").Value = customer_deadline_date.strftime(
        #     "%m/%d ") + '(' + w_list[customer_deadline_date.weekday()] + ')'
        # worksheet.Range("M2").Font.Size = 22
        # worksheet.Range("C3").Value = res['memo']
        # worksheet.Range("C3").Font.Size = 28
        # worksheet.Range("T4").Value = res['memo']
        # worksheet.Range("T4").Font.Size = 28
        # worksheet.Range("U2").Value = random_id
        # worksheet.Range("U2").Font.Size = 28
        # worksheet.Range("S2").Value = Customer.objects.get(
        #     id=(res['customer'])).name
        # worksheet.Range("S2").Font.Size = 16
        # worksheet.Range("AE2").Value = res['quantity']
        # worksheet.Range("AE2").Font.Size = 24
        # worksheet.Range("S3").Value = Material.objects.get(
        #     id=(res['material'])).name + supply
        # worksheet.Range("S3").Font.Size = 28
        # worksheet.Range("AC38").Value = Customer.objects.get(
        #     id=(res['customer'])).name
        
        # worksheet.Range("AC38").Font.Size = 18
        # for i in range(int(res['quantity'])):
        #     print(f"A{str(i+6)}", f"{random_id}{str(i+1)}")
        #     worksheet.Range(f"A{str(i+6)}").Value = f"{random_id}{str(i+1)}"
        #     worksheet.Range(f"A{str(i+6)}").Font.Size = 24
        # # PDFファイルを作成する
        # file_name = now.strftime("%Y%m%d")+random_id+'.pdf'
        # output_path = os.path.abspath(file_name)
        # worksheet.ExportAsFixedFormat(0, output_path)

        # # Excelを終了する
        # workbook.Close()
        # excel.quit()
        # # PDFファイルをダウンロードさせる
        # with open(output_path, 'rb') as f:
        #     response = HttpResponse(f.read(), content_type='application/pdf')
        #     response['Content-Disposition'] = f'attachment; filename={file_name}'
        # # os.remove(output_path)
        # def open_outputfile_directory(request):
        #     os.startfile(output_path)
        #     return HttpResponse("Directory opened successfully.")
        # time.sleep(3)

        # # redirect("file:///C:/Users/habir/Downloads/"+file_name)
        # print(output_path)
        # # redirect("file:///C:/Users/habir/OneDrive/%E3%83%87%E3%82%B9%E3%82%AF%E3%83%88%E3%83%83%E3%83%97/%E9%80%A3%E5%A4%AA%E9%83%8E/printer/new/"+file_name)
        # open_outputfile_directory(self.request)
        # # for i in range(35):
        # #     pyautogui.press('tab')
        # time.sleep(1)
        # pyautogui.hotkey('ctrlright','a')
        # pyautogui.hotkey('ctrlright','p')
        # time.sleep(4)
        # pyautogui.press('tab')
        # pyautogui.press('tab')
        # pyautogui.press('tab')
        # pyautogui.press('tab')
        # pyautogui.press('tab')
        # pyautogui.press('tab')
        # pyautogui.press('tab')
        # pyautogui.press('tab')
        # pyautogui.press('enter')
        # pyautogui.press('tab')
        # pyautogui.press('tab')
        # pyautogui.press('down')
        # time.sleep(1)
        # pyautogui.press('tab')
        # pyautogui.press('tab')
        # pyautogui.press('tab')
        # pyautogui.press('enter')

        # time.sleep(1)
        # redirect("http://127.0.0.1:8000/")
        # return response

    def get_success_url(self):
        return reverse('office-index')


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
    form_class = OfficeUpdateForm
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


""" Customer """


class CustomerListView(ListView):
    model = Customer
    template_name = 'customer/index.html'
    context_object_name = 'customers'
    ordering = ['name']

# 取引先でソートした案件を表示する。
class CustomerProjectListView(ListView):
    model = Post
    template_name = 'customer/projects.html'
    context_object_name = 'projects'
    ordering = ['my_company_deadline']

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['pk'] = self.kwargs.get('pk')
    #     print(context['pk'])
    #     return context
    
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     pk = self.request.GET.get('pk')
    #     if pk:
    #         queryset = queryset.filter(customer=pk)
    #     return queryset
    def get_queryset(self):
        queryset = super().get_queryset()
        pk = self.kwargs.get('pk')
        if pk:
            queryset = queryset.filter(customer=pk)
        return queryset

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



# 検索（Sort）機能
class SortView(ListView):
    model = Post
    template_name = 'office/sort.html'
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        return super().get_context_data(**kwargs)
    



