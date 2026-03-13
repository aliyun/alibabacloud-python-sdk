# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class VatInvoiceScanQueryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.VatInvoiceScanQueryResponseBodyModule = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.message = message
        self.module = module
        # requestId
        self.request_id = request_id
        self.success = success
        # traceId
        self.trace_id = trace_id

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        if self.module is not None:
            result['module'] = self.module.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        if self.trace_id is not None:
            result['traceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('module') is not None:
            temp_model = main_models.VatInvoiceScanQueryResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class VatInvoiceScanQueryResponseBodyModule(DaraModel):
    def __init__(
        self,
        items: List[main_models.VatInvoiceScanQueryResponseBodyModuleItems] = None,
        page_no: int = None,
        page_size: int = None,
        total_page: int = None,
        total_size: int = None,
    ):
        self.items = items
        self.page_no = page_no
        self.page_size = page_size
        self.total_page = total_page
        self.total_size = total_size

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.page_no is not None:
            result['page_no'] = self.page_no

        if self.page_size is not None:
            result['page_size'] = self.page_size

        if self.total_page is not None:
            result['total_page'] = self.total_page

        if self.total_size is not None:
            result['total_size'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.VatInvoiceScanQueryResponseBodyModuleItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('page_no') is not None:
            self.page_no = m.get('page_no')

        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')

        if m.get('total_page') is not None:
            self.total_page = m.get('total_page')

        if m.get('total_size') is not None:
            self.total_size = m.get('total_size')

        return self

class VatInvoiceScanQueryResponseBodyModuleItems(DaraModel):
    def __init__(
        self,
        amount_with_tax: str = None,
        amount_without_tax: str = None,
        bill_date: str = None,
        check_code: str = None,
        drawer: str = None,
        id: str = None,
        invoice_code: str = None,
        invoice_day: str = None,
        invoice_detail: str = None,
        invoice_details: List[main_models.VatInvoiceScanQueryResponseBodyModuleItemsInvoiceDetails] = None,
        invoice_location: str = None,
        invoice_no: str = None,
        invoice_sub_task_id: int = None,
        invoice_type: int = None,
        invoice_type_desc: str = None,
        machine_code: str = None,
        ofd_oss_url: str = None,
        oss_url: str = None,
        password_area: str = None,
        pdf_oss_url: str = None,
        purchaser_bank_account_info: str = None,
        purchaser_contact_info: str = None,
        purchaser_name: str = None,
        purchaser_tax_no: str = None,
        recipient: str = None,
        remarks: str = None,
        reviewer: str = None,
        seller_bank_account_info: str = None,
        seller_contact_info: str = None,
        seller_name: str = None,
        seller_tax_no: str = None,
        smart_check_code: str = None,
        tax_amount: str = None,
        tax_rate: str = None,
        total_amount_in_words: str = None,
        xml_oss_url: str = None,
    ):
        self.amount_with_tax = amount_with_tax
        self.amount_without_tax = amount_without_tax
        self.bill_date = bill_date
        self.check_code = check_code
        self.drawer = drawer
        self.id = id
        self.invoice_code = invoice_code
        self.invoice_day = invoice_day
        self.invoice_detail = invoice_detail
        self.invoice_details = invoice_details
        self.invoice_location = invoice_location
        self.invoice_no = invoice_no
        self.invoice_sub_task_id = invoice_sub_task_id
        self.invoice_type = invoice_type
        self.invoice_type_desc = invoice_type_desc
        # 机器码
        self.machine_code = machine_code
        self.ofd_oss_url = ofd_oss_url
        self.oss_url = oss_url
        self.password_area = password_area
        self.pdf_oss_url = pdf_oss_url
        self.purchaser_bank_account_info = purchaser_bank_account_info
        self.purchaser_contact_info = purchaser_contact_info
        self.purchaser_name = purchaser_name
        self.purchaser_tax_no = purchaser_tax_no
        self.recipient = recipient
        self.remarks = remarks
        self.reviewer = reviewer
        self.seller_bank_account_info = seller_bank_account_info
        self.seller_contact_info = seller_contact_info
        self.seller_name = seller_name
        self.seller_tax_no = seller_tax_no
        self.smart_check_code = smart_check_code
        self.tax_amount = tax_amount
        self.tax_rate = tax_rate
        self.total_amount_in_words = total_amount_in_words
        self.xml_oss_url = xml_oss_url

    def validate(self):
        if self.invoice_details:
            for v1 in self.invoice_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount_with_tax is not None:
            result['amount_with_tax'] = self.amount_with_tax

        if self.amount_without_tax is not None:
            result['amount_without_tax'] = self.amount_without_tax

        if self.bill_date is not None:
            result['bill_date'] = self.bill_date

        if self.check_code is not None:
            result['check_code'] = self.check_code

        if self.drawer is not None:
            result['drawer'] = self.drawer

        if self.id is not None:
            result['id'] = self.id

        if self.invoice_code is not None:
            result['invoice_code'] = self.invoice_code

        if self.invoice_day is not None:
            result['invoice_day'] = self.invoice_day

        if self.invoice_detail is not None:
            result['invoice_detail'] = self.invoice_detail

        result['invoice_details'] = []
        if self.invoice_details is not None:
            for k1 in self.invoice_details:
                result['invoice_details'].append(k1.to_map() if k1 else None)

        if self.invoice_location is not None:
            result['invoice_location'] = self.invoice_location

        if self.invoice_no is not None:
            result['invoice_no'] = self.invoice_no

        if self.invoice_sub_task_id is not None:
            result['invoice_sub_task_id'] = self.invoice_sub_task_id

        if self.invoice_type is not None:
            result['invoice_type'] = self.invoice_type

        if self.invoice_type_desc is not None:
            result['invoice_type_desc'] = self.invoice_type_desc

        if self.machine_code is not None:
            result['machine_code'] = self.machine_code

        if self.ofd_oss_url is not None:
            result['ofd_oss_url'] = self.ofd_oss_url

        if self.oss_url is not None:
            result['oss_url'] = self.oss_url

        if self.password_area is not None:
            result['password_area'] = self.password_area

        if self.pdf_oss_url is not None:
            result['pdf_oss_url'] = self.pdf_oss_url

        if self.purchaser_bank_account_info is not None:
            result['purchaser_bank_account_info'] = self.purchaser_bank_account_info

        if self.purchaser_contact_info is not None:
            result['purchaser_contact_info'] = self.purchaser_contact_info

        if self.purchaser_name is not None:
            result['purchaser_name'] = self.purchaser_name

        if self.purchaser_tax_no is not None:
            result['purchaser_tax_no'] = self.purchaser_tax_no

        if self.recipient is not None:
            result['recipient'] = self.recipient

        if self.remarks is not None:
            result['remarks'] = self.remarks

        if self.reviewer is not None:
            result['reviewer'] = self.reviewer

        if self.seller_bank_account_info is not None:
            result['seller_bank_account_info'] = self.seller_bank_account_info

        if self.seller_contact_info is not None:
            result['seller_contact_info'] = self.seller_contact_info

        if self.seller_name is not None:
            result['seller_name'] = self.seller_name

        if self.seller_tax_no is not None:
            result['seller_tax_no'] = self.seller_tax_no

        if self.smart_check_code is not None:
            result['smart_check_code'] = self.smart_check_code

        if self.tax_amount is not None:
            result['tax_amount'] = self.tax_amount

        if self.tax_rate is not None:
            result['tax_rate'] = self.tax_rate

        if self.total_amount_in_words is not None:
            result['total_amount_in_words'] = self.total_amount_in_words

        if self.xml_oss_url is not None:
            result['xml_oss_url'] = self.xml_oss_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amount_with_tax') is not None:
            self.amount_with_tax = m.get('amount_with_tax')

        if m.get('amount_without_tax') is not None:
            self.amount_without_tax = m.get('amount_without_tax')

        if m.get('bill_date') is not None:
            self.bill_date = m.get('bill_date')

        if m.get('check_code') is not None:
            self.check_code = m.get('check_code')

        if m.get('drawer') is not None:
            self.drawer = m.get('drawer')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('invoice_code') is not None:
            self.invoice_code = m.get('invoice_code')

        if m.get('invoice_day') is not None:
            self.invoice_day = m.get('invoice_day')

        if m.get('invoice_detail') is not None:
            self.invoice_detail = m.get('invoice_detail')

        self.invoice_details = []
        if m.get('invoice_details') is not None:
            for k1 in m.get('invoice_details'):
                temp_model = main_models.VatInvoiceScanQueryResponseBodyModuleItemsInvoiceDetails()
                self.invoice_details.append(temp_model.from_map(k1))

        if m.get('invoice_location') is not None:
            self.invoice_location = m.get('invoice_location')

        if m.get('invoice_no') is not None:
            self.invoice_no = m.get('invoice_no')

        if m.get('invoice_sub_task_id') is not None:
            self.invoice_sub_task_id = m.get('invoice_sub_task_id')

        if m.get('invoice_type') is not None:
            self.invoice_type = m.get('invoice_type')

        if m.get('invoice_type_desc') is not None:
            self.invoice_type_desc = m.get('invoice_type_desc')

        if m.get('machine_code') is not None:
            self.machine_code = m.get('machine_code')

        if m.get('ofd_oss_url') is not None:
            self.ofd_oss_url = m.get('ofd_oss_url')

        if m.get('oss_url') is not None:
            self.oss_url = m.get('oss_url')

        if m.get('password_area') is not None:
            self.password_area = m.get('password_area')

        if m.get('pdf_oss_url') is not None:
            self.pdf_oss_url = m.get('pdf_oss_url')

        if m.get('purchaser_bank_account_info') is not None:
            self.purchaser_bank_account_info = m.get('purchaser_bank_account_info')

        if m.get('purchaser_contact_info') is not None:
            self.purchaser_contact_info = m.get('purchaser_contact_info')

        if m.get('purchaser_name') is not None:
            self.purchaser_name = m.get('purchaser_name')

        if m.get('purchaser_tax_no') is not None:
            self.purchaser_tax_no = m.get('purchaser_tax_no')

        if m.get('recipient') is not None:
            self.recipient = m.get('recipient')

        if m.get('remarks') is not None:
            self.remarks = m.get('remarks')

        if m.get('reviewer') is not None:
            self.reviewer = m.get('reviewer')

        if m.get('seller_bank_account_info') is not None:
            self.seller_bank_account_info = m.get('seller_bank_account_info')

        if m.get('seller_contact_info') is not None:
            self.seller_contact_info = m.get('seller_contact_info')

        if m.get('seller_name') is not None:
            self.seller_name = m.get('seller_name')

        if m.get('seller_tax_no') is not None:
            self.seller_tax_no = m.get('seller_tax_no')

        if m.get('smart_check_code') is not None:
            self.smart_check_code = m.get('smart_check_code')

        if m.get('tax_amount') is not None:
            self.tax_amount = m.get('tax_amount')

        if m.get('tax_rate') is not None:
            self.tax_rate = m.get('tax_rate')

        if m.get('total_amount_in_words') is not None:
            self.total_amount_in_words = m.get('total_amount_in_words')

        if m.get('xml_oss_url') is not None:
            self.xml_oss_url = m.get('xml_oss_url')

        return self

class VatInvoiceScanQueryResponseBodyModuleItemsInvoiceDetails(DaraModel):
    def __init__(
        self,
        amount: str = None,
        index: str = None,
        item_name: str = None,
        quantity: str = None,
        specification: str = None,
        tax: str = None,
        tax_rate: str = None,
        unit: str = None,
        unit_price: str = None,
    ):
        self.amount = amount
        # 行号
        self.index = index
        self.item_name = item_name
        self.quantity = quantity
        self.specification = specification
        self.tax = tax
        self.tax_rate = tax_rate
        self.unit = unit
        self.unit_price = unit_price

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['amount'] = self.amount

        if self.index is not None:
            result['index'] = self.index

        if self.item_name is not None:
            result['item_name'] = self.item_name

        if self.quantity is not None:
            result['quantity'] = self.quantity

        if self.specification is not None:
            result['specification'] = self.specification

        if self.tax is not None:
            result['tax'] = self.tax

        if self.tax_rate is not None:
            result['tax_rate'] = self.tax_rate

        if self.unit is not None:
            result['unit'] = self.unit

        if self.unit_price is not None:
            result['unit_price'] = self.unit_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')

        if m.get('index') is not None:
            self.index = m.get('index')

        if m.get('item_name') is not None:
            self.item_name = m.get('item_name')

        if m.get('quantity') is not None:
            self.quantity = m.get('quantity')

        if m.get('specification') is not None:
            self.specification = m.get('specification')

        if m.get('tax') is not None:
            self.tax = m.get('tax')

        if m.get('tax_rate') is not None:
            self.tax_rate = m.get('tax_rate')

        if m.get('unit') is not None:
            self.unit = m.get('unit')

        if m.get('unit_price') is not None:
            self.unit_price = m.get('unit_price')

        return self

