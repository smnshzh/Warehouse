from django.urls import path

from . import views

urlpatterns = [
    path ('new-account', views.new_account, name='new_account'),
    path ('edit-account-<int:id>', views.new_account, name="edit_account"),
    path ("accountsides-show", views.accountside_show, name='accountside_show'),
    path ('random', views.random_maker),
    path ('auto-Journal', views.making_all_journal, name="auto_journal"),
    path ('show-Journal', views.show_journals, name="show_journals"),
    path ('making-Journal', views.making_journal, name="making_journal"),
    path ('bank-pose', views.define_bank_pose, name="define_bank_pose"),
    path ('settle-invoice', views.settle_invoice, name="settle_invoice"),
    path ('confirm-settel', views.confirm_settelmenet, name="confirm_settelmenet"),
    path ('confirm-pay-order', views.confirm_pay_order, name="confirm_pay_order"),
    path ("map", views.my_map, name='map'),
    path ('detailed-account-<int:id>-report', views.detailed_account_report, name="detailed_account_report")
]
