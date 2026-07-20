# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class TrainTicketScanQueryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.TrainTicketScanQueryResponseBodyModule = None,
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
            temp_model = main_models.TrainTicketScanQueryResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class TrainTicketScanQueryResponseBodyModule(DaraModel):
    def __init__(
        self,
        items: List[main_models.TrainTicketScanQueryResponseBodyModuleItems] = None,
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
                temp_model = main_models.TrainTicketScanQueryResponseBodyModuleItems()
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

class TrainTicketScanQueryResponseBodyModuleItems(DaraModel):
    def __init__(
        self,
        apply_id: str = None,
        arr_station: str = None,
        bill_date: str = None,
        coach_name: str = None,
        cost_center: str = None,
        dep_station: str = None,
        dep_time: str = None,
        department: str = None,
        electronic_ticket_no: str = None,
        fee_type_show_code: int = None,
        has_changed: bool = None,
        id: str = None,
        invoice_date: str = None,
        invoice_material: int = None,
        invoice_title: str = None,
        ofd_url: str = None,
        order_id: int = None,
        origin_ticket_no: str = None,
        oss_url: str = None,
        passenger: str = None,
        pdf_url: str = None,
        price: str = None,
        project: str = None,
        purchaser_name: str = None,
        purchaser_tax_no: str = None,
        seat: str = None,
        seat_no: str = None,
        serial_number: str = None,
        tax_amount: str = None,
        tax_rate: str = None,
        ticket_no: str = None,
        train_no: str = None,
        xml_url: str = None,
    ):
        self.apply_id = apply_id
        self.arr_station = arr_station
        self.bill_date = bill_date
        self.coach_name = coach_name
        self.cost_center = cost_center
        self.dep_station = dep_station
        self.dep_time = dep_time
        self.department = department
        self.electronic_ticket_no = electronic_ticket_no
        self.fee_type_show_code = fee_type_show_code
        self.has_changed = has_changed
        self.id = id
        self.invoice_date = invoice_date
        self.invoice_material = invoice_material
        self.invoice_title = invoice_title
        self.ofd_url = ofd_url
        self.order_id = order_id
        self.origin_ticket_no = origin_ticket_no
        self.oss_url = oss_url
        self.passenger = passenger
        self.pdf_url = pdf_url
        self.price = price
        self.project = project
        self.purchaser_name = purchaser_name
        self.purchaser_tax_no = purchaser_tax_no
        self.seat = seat
        self.seat_no = seat_no
        self.serial_number = serial_number
        self.tax_amount = tax_amount
        self.tax_rate = tax_rate
        # 取票号
        self.ticket_no = ticket_no
        # 车次
        self.train_no = train_no
        self.xml_url = xml_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_id is not None:
            result['apply_id'] = self.apply_id

        if self.arr_station is not None:
            result['arr_station'] = self.arr_station

        if self.bill_date is not None:
            result['bill_date'] = self.bill_date

        if self.coach_name is not None:
            result['coach_name'] = self.coach_name

        if self.cost_center is not None:
            result['cost_center'] = self.cost_center

        if self.dep_station is not None:
            result['dep_station'] = self.dep_station

        if self.dep_time is not None:
            result['dep_time'] = self.dep_time

        if self.department is not None:
            result['department'] = self.department

        if self.electronic_ticket_no is not None:
            result['electronic_ticket_no'] = self.electronic_ticket_no

        if self.fee_type_show_code is not None:
            result['fee_type_show_code'] = self.fee_type_show_code

        if self.has_changed is not None:
            result['has_changed'] = self.has_changed

        if self.id is not None:
            result['id'] = self.id

        if self.invoice_date is not None:
            result['invoice_date'] = self.invoice_date

        if self.invoice_material is not None:
            result['invoice_material'] = self.invoice_material

        if self.invoice_title is not None:
            result['invoice_title'] = self.invoice_title

        if self.ofd_url is not None:
            result['ofd_url'] = self.ofd_url

        if self.order_id is not None:
            result['order_id'] = self.order_id

        if self.origin_ticket_no is not None:
            result['origin_ticket_no'] = self.origin_ticket_no

        if self.oss_url is not None:
            result['oss_url'] = self.oss_url

        if self.passenger is not None:
            result['passenger'] = self.passenger

        if self.pdf_url is not None:
            result['pdf_url'] = self.pdf_url

        if self.price is not None:
            result['price'] = self.price

        if self.project is not None:
            result['project'] = self.project

        if self.purchaser_name is not None:
            result['purchaser_name'] = self.purchaser_name

        if self.purchaser_tax_no is not None:
            result['purchaser_tax_no'] = self.purchaser_tax_no

        if self.seat is not None:
            result['seat'] = self.seat

        if self.seat_no is not None:
            result['seat_no'] = self.seat_no

        if self.serial_number is not None:
            result['serial_number'] = self.serial_number

        if self.tax_amount is not None:
            result['tax_amount'] = self.tax_amount

        if self.tax_rate is not None:
            result['tax_rate'] = self.tax_rate

        if self.ticket_no is not None:
            result['ticket_no'] = self.ticket_no

        if self.train_no is not None:
            result['train_no'] = self.train_no

        if self.xml_url is not None:
            result['xml_url'] = self.xml_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apply_id') is not None:
            self.apply_id = m.get('apply_id')

        if m.get('arr_station') is not None:
            self.arr_station = m.get('arr_station')

        if m.get('bill_date') is not None:
            self.bill_date = m.get('bill_date')

        if m.get('coach_name') is not None:
            self.coach_name = m.get('coach_name')

        if m.get('cost_center') is not None:
            self.cost_center = m.get('cost_center')

        if m.get('dep_station') is not None:
            self.dep_station = m.get('dep_station')

        if m.get('dep_time') is not None:
            self.dep_time = m.get('dep_time')

        if m.get('department') is not None:
            self.department = m.get('department')

        if m.get('electronic_ticket_no') is not None:
            self.electronic_ticket_no = m.get('electronic_ticket_no')

        if m.get('fee_type_show_code') is not None:
            self.fee_type_show_code = m.get('fee_type_show_code')

        if m.get('has_changed') is not None:
            self.has_changed = m.get('has_changed')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('invoice_date') is not None:
            self.invoice_date = m.get('invoice_date')

        if m.get('invoice_material') is not None:
            self.invoice_material = m.get('invoice_material')

        if m.get('invoice_title') is not None:
            self.invoice_title = m.get('invoice_title')

        if m.get('ofd_url') is not None:
            self.ofd_url = m.get('ofd_url')

        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')

        if m.get('origin_ticket_no') is not None:
            self.origin_ticket_no = m.get('origin_ticket_no')

        if m.get('oss_url') is not None:
            self.oss_url = m.get('oss_url')

        if m.get('passenger') is not None:
            self.passenger = m.get('passenger')

        if m.get('pdf_url') is not None:
            self.pdf_url = m.get('pdf_url')

        if m.get('price') is not None:
            self.price = m.get('price')

        if m.get('project') is not None:
            self.project = m.get('project')

        if m.get('purchaser_name') is not None:
            self.purchaser_name = m.get('purchaser_name')

        if m.get('purchaser_tax_no') is not None:
            self.purchaser_tax_no = m.get('purchaser_tax_no')

        if m.get('seat') is not None:
            self.seat = m.get('seat')

        if m.get('seat_no') is not None:
            self.seat_no = m.get('seat_no')

        if m.get('serial_number') is not None:
            self.serial_number = m.get('serial_number')

        if m.get('tax_amount') is not None:
            self.tax_amount = m.get('tax_amount')

        if m.get('tax_rate') is not None:
            self.tax_rate = m.get('tax_rate')

        if m.get('ticket_no') is not None:
            self.ticket_no = m.get('ticket_no')

        if m.get('train_no') is not None:
            self.train_no = m.get('train_no')

        if m.get('xml_url') is not None:
            self.xml_url = m.get('xml_url')

        return self

