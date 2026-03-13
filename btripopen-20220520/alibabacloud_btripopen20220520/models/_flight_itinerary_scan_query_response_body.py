# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class FlightItineraryScanQueryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.FlightItineraryScanQueryResponseBodyModule = None,
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
            temp_model = main_models.FlightItineraryScanQueryResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class FlightItineraryScanQueryResponseBodyModule(DaraModel):
    def __init__(
        self,
        items: List[main_models.FlightItineraryScanQueryResponseBodyModuleItems] = None,
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
                temp_model = main_models.FlightItineraryScanQueryResponseBodyModuleItems()
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

class FlightItineraryScanQueryResponseBodyModuleItems(DaraModel):
    def __init__(
        self,
        agent_code: str = None,
        apply_id: str = None,
        bill_date: str = None,
        blue_or_red: int = None,
        build: str = None,
        cost_center: str = None,
        department: str = None,
        flights: List[main_models.FlightItineraryScanQueryResponseBodyModuleItemsFlights] = None,
        fuel_surcharge: str = None,
        id: str = None,
        insurance: str = None,
        invoice_title: str = None,
        invoice_type: int = None,
        issue_company: str = None,
        issue_date: str = None,
        itinerary_num: str = None,
        ofd_oss_url: str = None,
        order_id: int = None,
        oss_url: str = None,
        other_taxes: str = None,
        passenger_name: str = None,
        pdf_oss_url: str = None,
        project: str = None,
        prompt_message: str = None,
        purchaser_name: str = None,
        purchaser_tax_no: str = None,
        purchaser_type: int = None,
        tax_amount: str = None,
        tax_rate: str = None,
        ticket_no: str = None,
        ticket_price: str = None,
        total_price: str = None,
        validation_code: str = None,
        xml_oss_url: str = None,
    ):
        # 销售单位代号
        self.agent_code = agent_code
        self.apply_id = apply_id
        self.bill_date = bill_date
        self.blue_or_red = blue_or_red
        self.build = build
        self.cost_center = cost_center
        self.department = department
        # 机票行程明细
        self.flights = flights
        self.fuel_surcharge = fuel_surcharge
        # UK
        self.id = id
        self.insurance = insurance
        self.invoice_title = invoice_title
        self.invoice_type = invoice_type
        # 填开单位
        self.issue_company = issue_company
        # 填开日期
        self.issue_date = issue_date
        self.itinerary_num = itinerary_num
        self.ofd_oss_url = ofd_oss_url
        self.order_id = order_id
        self.oss_url = oss_url
        self.other_taxes = other_taxes
        self.passenger_name = passenger_name
        self.pdf_oss_url = pdf_oss_url
        self.project = project
        # 提示信息
        self.prompt_message = prompt_message
        self.purchaser_name = purchaser_name
        self.purchaser_tax_no = purchaser_tax_no
        self.purchaser_type = purchaser_type
        self.tax_amount = tax_amount
        self.tax_rate = tax_rate
        self.ticket_no = ticket_no
        self.ticket_price = ticket_price
        self.total_price = total_price
        # 验证码
        self.validation_code = validation_code
        self.xml_oss_url = xml_oss_url

    def validate(self):
        if self.flights:
            for v1 in self.flights:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_code is not None:
            result['agent_code'] = self.agent_code

        if self.apply_id is not None:
            result['apply_id'] = self.apply_id

        if self.bill_date is not None:
            result['bill_date'] = self.bill_date

        if self.blue_or_red is not None:
            result['blue_or_red'] = self.blue_or_red

        if self.build is not None:
            result['build'] = self.build

        if self.cost_center is not None:
            result['cost_center'] = self.cost_center

        if self.department is not None:
            result['department'] = self.department

        result['flights'] = []
        if self.flights is not None:
            for k1 in self.flights:
                result['flights'].append(k1.to_map() if k1 else None)

        if self.fuel_surcharge is not None:
            result['fuel_surcharge'] = self.fuel_surcharge

        if self.id is not None:
            result['id'] = self.id

        if self.insurance is not None:
            result['insurance'] = self.insurance

        if self.invoice_title is not None:
            result['invoice_title'] = self.invoice_title

        if self.invoice_type is not None:
            result['invoice_type'] = self.invoice_type

        if self.issue_company is not None:
            result['issue_company'] = self.issue_company

        if self.issue_date is not None:
            result['issue_date'] = self.issue_date

        if self.itinerary_num is not None:
            result['itinerary_num'] = self.itinerary_num

        if self.ofd_oss_url is not None:
            result['ofd_oss_url'] = self.ofd_oss_url

        if self.order_id is not None:
            result['order_id'] = self.order_id

        if self.oss_url is not None:
            result['oss_url'] = self.oss_url

        if self.other_taxes is not None:
            result['other_taxes'] = self.other_taxes

        if self.passenger_name is not None:
            result['passenger_name'] = self.passenger_name

        if self.pdf_oss_url is not None:
            result['pdf_oss_url'] = self.pdf_oss_url

        if self.project is not None:
            result['project'] = self.project

        if self.prompt_message is not None:
            result['prompt_message'] = self.prompt_message

        if self.purchaser_name is not None:
            result['purchaser_name'] = self.purchaser_name

        if self.purchaser_tax_no is not None:
            result['purchaser_tax_no'] = self.purchaser_tax_no

        if self.purchaser_type is not None:
            result['purchaser_type'] = self.purchaser_type

        if self.tax_amount is not None:
            result['tax_amount'] = self.tax_amount

        if self.tax_rate is not None:
            result['tax_rate'] = self.tax_rate

        if self.ticket_no is not None:
            result['ticket_no'] = self.ticket_no

        if self.ticket_price is not None:
            result['ticket_price'] = self.ticket_price

        if self.total_price is not None:
            result['total_price'] = self.total_price

        if self.validation_code is not None:
            result['validation_code'] = self.validation_code

        if self.xml_oss_url is not None:
            result['xml_oss_url'] = self.xml_oss_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agent_code') is not None:
            self.agent_code = m.get('agent_code')

        if m.get('apply_id') is not None:
            self.apply_id = m.get('apply_id')

        if m.get('bill_date') is not None:
            self.bill_date = m.get('bill_date')

        if m.get('blue_or_red') is not None:
            self.blue_or_red = m.get('blue_or_red')

        if m.get('build') is not None:
            self.build = m.get('build')

        if m.get('cost_center') is not None:
            self.cost_center = m.get('cost_center')

        if m.get('department') is not None:
            self.department = m.get('department')

        self.flights = []
        if m.get('flights') is not None:
            for k1 in m.get('flights'):
                temp_model = main_models.FlightItineraryScanQueryResponseBodyModuleItemsFlights()
                self.flights.append(temp_model.from_map(k1))

        if m.get('fuel_surcharge') is not None:
            self.fuel_surcharge = m.get('fuel_surcharge')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('insurance') is not None:
            self.insurance = m.get('insurance')

        if m.get('invoice_title') is not None:
            self.invoice_title = m.get('invoice_title')

        if m.get('invoice_type') is not None:
            self.invoice_type = m.get('invoice_type')

        if m.get('issue_company') is not None:
            self.issue_company = m.get('issue_company')

        if m.get('issue_date') is not None:
            self.issue_date = m.get('issue_date')

        if m.get('itinerary_num') is not None:
            self.itinerary_num = m.get('itinerary_num')

        if m.get('ofd_oss_url') is not None:
            self.ofd_oss_url = m.get('ofd_oss_url')

        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')

        if m.get('oss_url') is not None:
            self.oss_url = m.get('oss_url')

        if m.get('other_taxes') is not None:
            self.other_taxes = m.get('other_taxes')

        if m.get('passenger_name') is not None:
            self.passenger_name = m.get('passenger_name')

        if m.get('pdf_oss_url') is not None:
            self.pdf_oss_url = m.get('pdf_oss_url')

        if m.get('project') is not None:
            self.project = m.get('project')

        if m.get('prompt_message') is not None:
            self.prompt_message = m.get('prompt_message')

        if m.get('purchaser_name') is not None:
            self.purchaser_name = m.get('purchaser_name')

        if m.get('purchaser_tax_no') is not None:
            self.purchaser_tax_no = m.get('purchaser_tax_no')

        if m.get('purchaser_type') is not None:
            self.purchaser_type = m.get('purchaser_type')

        if m.get('tax_amount') is not None:
            self.tax_amount = m.get('tax_amount')

        if m.get('tax_rate') is not None:
            self.tax_rate = m.get('tax_rate')

        if m.get('ticket_no') is not None:
            self.ticket_no = m.get('ticket_no')

        if m.get('ticket_price') is not None:
            self.ticket_price = m.get('ticket_price')

        if m.get('total_price') is not None:
            self.total_price = m.get('total_price')

        if m.get('validation_code') is not None:
            self.validation_code = m.get('validation_code')

        if m.get('xml_oss_url') is not None:
            self.xml_oss_url = m.get('xml_oss_url')

        return self

class FlightItineraryScanQueryResponseBodyModuleItemsFlights(DaraModel):
    def __init__(
        self,
        arrival_station: str = None,
        cabin_class: str = None,
        carrier: str = None,
        departure_station: str = None,
        flight_date: str = None,
        flight_number: str = None,
        flight_time: str = None,
        free_baggage_allowance: str = None,
        index: str = None,
        seat_class: str = None,
        valid_from_date: str = None,
        valid_to_date: str = None,
    ):
        # 航班至
        self.arrival_station = arrival_station
        # 座位等级
        self.cabin_class = cabin_class
        # 承运人
        self.carrier = carrier
        # 航班从
        self.departure_station = departure_station
        # 日期
        self.flight_date = flight_date
        # 航班号
        self.flight_number = flight_number
        # 时间
        self.flight_time = flight_time
        # 免费行李
        self.free_baggage_allowance = free_baggage_allowance
        # 行号
        self.index = index
        # 客票级别
        self.seat_class = seat_class
        # 客票生效日期
        self.valid_from_date = valid_from_date
        # 有效截止日期
        self.valid_to_date = valid_to_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arrival_station is not None:
            result['arrival_station'] = self.arrival_station

        if self.cabin_class is not None:
            result['cabin_class'] = self.cabin_class

        if self.carrier is not None:
            result['carrier'] = self.carrier

        if self.departure_station is not None:
            result['departure_station'] = self.departure_station

        if self.flight_date is not None:
            result['flight_date'] = self.flight_date

        if self.flight_number is not None:
            result['flight_number'] = self.flight_number

        if self.flight_time is not None:
            result['flight_time'] = self.flight_time

        if self.free_baggage_allowance is not None:
            result['free_baggage_allowance'] = self.free_baggage_allowance

        if self.index is not None:
            result['index'] = self.index

        if self.seat_class is not None:
            result['seat_class'] = self.seat_class

        if self.valid_from_date is not None:
            result['valid_from_date'] = self.valid_from_date

        if self.valid_to_date is not None:
            result['valid_to_date'] = self.valid_to_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arrival_station') is not None:
            self.arrival_station = m.get('arrival_station')

        if m.get('cabin_class') is not None:
            self.cabin_class = m.get('cabin_class')

        if m.get('carrier') is not None:
            self.carrier = m.get('carrier')

        if m.get('departure_station') is not None:
            self.departure_station = m.get('departure_station')

        if m.get('flight_date') is not None:
            self.flight_date = m.get('flight_date')

        if m.get('flight_number') is not None:
            self.flight_number = m.get('flight_number')

        if m.get('flight_time') is not None:
            self.flight_time = m.get('flight_time')

        if m.get('free_baggage_allowance') is not None:
            self.free_baggage_allowance = m.get('free_baggage_allowance')

        if m.get('index') is not None:
            self.index = m.get('index')

        if m.get('seat_class') is not None:
            self.seat_class = m.get('seat_class')

        if m.get('valid_from_date') is not None:
            self.valid_from_date = m.get('valid_from_date')

        if m.get('valid_to_date') is not None:
            self.valid_to_date = m.get('valid_to_date')

        return self

