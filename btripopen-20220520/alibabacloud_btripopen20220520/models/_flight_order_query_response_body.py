# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class FlightOrderQueryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.FlightOrderQueryResponseBodyModule = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.message = message
        self.module = module
        self.request_id = request_id
        self.success = success
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
            temp_model = main_models.FlightOrderQueryResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class FlightOrderQueryResponseBodyModule(DaraModel):
    def __init__(
        self,
        flight_change_ticket_info_list: List[main_models.FlightOrderQueryResponseBodyModuleFlightChangeTicketInfoList] = None,
        flight_info_list: List[main_models.FlightOrderQueryResponseBodyModuleFlightInfoList] = None,
        flight_refund_ticket_info_list: List[main_models.FlightOrderQueryResponseBodyModuleFlightRefundTicketInfoList] = None,
        flight_ticket_info_list: List[main_models.FlightOrderQueryResponseBodyModuleFlightTicketInfoList] = None,
        insurance_info_list: List[main_models.FlightOrderQueryResponseBodyModuleInsuranceInfoList] = None,
        invoice_info: main_models.FlightOrderQueryResponseBodyModuleInvoiceInfo = None,
        order_base_info: main_models.FlightOrderQueryResponseBodyModuleOrderBaseInfo = None,
        passenger_info_list: List[main_models.FlightOrderQueryResponseBodyModulePassengerInfoList] = None,
        price_info_list: List[main_models.FlightOrderQueryResponseBodyModulePriceInfoList] = None,
    ):
        self.flight_change_ticket_info_list = flight_change_ticket_info_list
        self.flight_info_list = flight_info_list
        self.flight_refund_ticket_info_list = flight_refund_ticket_info_list
        self.flight_ticket_info_list = flight_ticket_info_list
        self.insurance_info_list = insurance_info_list
        self.invoice_info = invoice_info
        self.order_base_info = order_base_info
        self.passenger_info_list = passenger_info_list
        self.price_info_list = price_info_list

    def validate(self):
        if self.flight_change_ticket_info_list:
            for v1 in self.flight_change_ticket_info_list:
                 if v1:
                    v1.validate()
        if self.flight_info_list:
            for v1 in self.flight_info_list:
                 if v1:
                    v1.validate()
        if self.flight_refund_ticket_info_list:
            for v1 in self.flight_refund_ticket_info_list:
                 if v1:
                    v1.validate()
        if self.flight_ticket_info_list:
            for v1 in self.flight_ticket_info_list:
                 if v1:
                    v1.validate()
        if self.insurance_info_list:
            for v1 in self.insurance_info_list:
                 if v1:
                    v1.validate()
        if self.invoice_info:
            self.invoice_info.validate()
        if self.order_base_info:
            self.order_base_info.validate()
        if self.passenger_info_list:
            for v1 in self.passenger_info_list:
                 if v1:
                    v1.validate()
        if self.price_info_list:
            for v1 in self.price_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['flight_change_ticket_info_list'] = []
        if self.flight_change_ticket_info_list is not None:
            for k1 in self.flight_change_ticket_info_list:
                result['flight_change_ticket_info_list'].append(k1.to_map() if k1 else None)

        result['flight_info_list'] = []
        if self.flight_info_list is not None:
            for k1 in self.flight_info_list:
                result['flight_info_list'].append(k1.to_map() if k1 else None)

        result['flight_refund_ticket_info_list'] = []
        if self.flight_refund_ticket_info_list is not None:
            for k1 in self.flight_refund_ticket_info_list:
                result['flight_refund_ticket_info_list'].append(k1.to_map() if k1 else None)

        result['flight_ticket_info_list'] = []
        if self.flight_ticket_info_list is not None:
            for k1 in self.flight_ticket_info_list:
                result['flight_ticket_info_list'].append(k1.to_map() if k1 else None)

        result['insurance_info_list'] = []
        if self.insurance_info_list is not None:
            for k1 in self.insurance_info_list:
                result['insurance_info_list'].append(k1.to_map() if k1 else None)

        if self.invoice_info is not None:
            result['invoice_info'] = self.invoice_info.to_map()

        if self.order_base_info is not None:
            result['order_base_info'] = self.order_base_info.to_map()

        result['passenger_info_list'] = []
        if self.passenger_info_list is not None:
            for k1 in self.passenger_info_list:
                result['passenger_info_list'].append(k1.to_map() if k1 else None)

        result['price_info_list'] = []
        if self.price_info_list is not None:
            for k1 in self.price_info_list:
                result['price_info_list'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.flight_change_ticket_info_list = []
        if m.get('flight_change_ticket_info_list') is not None:
            for k1 in m.get('flight_change_ticket_info_list'):
                temp_model = main_models.FlightOrderQueryResponseBodyModuleFlightChangeTicketInfoList()
                self.flight_change_ticket_info_list.append(temp_model.from_map(k1))

        self.flight_info_list = []
        if m.get('flight_info_list') is not None:
            for k1 in m.get('flight_info_list'):
                temp_model = main_models.FlightOrderQueryResponseBodyModuleFlightInfoList()
                self.flight_info_list.append(temp_model.from_map(k1))

        self.flight_refund_ticket_info_list = []
        if m.get('flight_refund_ticket_info_list') is not None:
            for k1 in m.get('flight_refund_ticket_info_list'):
                temp_model = main_models.FlightOrderQueryResponseBodyModuleFlightRefundTicketInfoList()
                self.flight_refund_ticket_info_list.append(temp_model.from_map(k1))

        self.flight_ticket_info_list = []
        if m.get('flight_ticket_info_list') is not None:
            for k1 in m.get('flight_ticket_info_list'):
                temp_model = main_models.FlightOrderQueryResponseBodyModuleFlightTicketInfoList()
                self.flight_ticket_info_list.append(temp_model.from_map(k1))

        self.insurance_info_list = []
        if m.get('insurance_info_list') is not None:
            for k1 in m.get('insurance_info_list'):
                temp_model = main_models.FlightOrderQueryResponseBodyModuleInsuranceInfoList()
                self.insurance_info_list.append(temp_model.from_map(k1))

        if m.get('invoice_info') is not None:
            temp_model = main_models.FlightOrderQueryResponseBodyModuleInvoiceInfo()
            self.invoice_info = temp_model.from_map(m.get('invoice_info'))

        if m.get('order_base_info') is not None:
            temp_model = main_models.FlightOrderQueryResponseBodyModuleOrderBaseInfo()
            self.order_base_info = temp_model.from_map(m.get('order_base_info'))

        self.passenger_info_list = []
        if m.get('passenger_info_list') is not None:
            for k1 in m.get('passenger_info_list'):
                temp_model = main_models.FlightOrderQueryResponseBodyModulePassengerInfoList()
                self.passenger_info_list.append(temp_model.from_map(k1))

        self.price_info_list = []
        if m.get('price_info_list') is not None:
            for k1 in m.get('price_info_list'):
                temp_model = main_models.FlightOrderQueryResponseBodyModulePriceInfoList()
                self.price_info_list.append(temp_model.from_map(k1))

        return self

class FlightOrderQueryResponseBodyModulePriceInfoList(DaraModel):
    def __init__(
        self,
        category_code: int = None,
        gmt_create: str = None,
        passenger_name: str = None,
        pay_type: int = None,
        price: float = None,
        trade_id: str = None,
        type: int = None,
    ):
        self.category_code = category_code
        self.gmt_create = gmt_create
        self.passenger_name = passenger_name
        self.pay_type = pay_type
        self.price = price
        self.trade_id = trade_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_code is not None:
            result['category_code'] = self.category_code

        if self.gmt_create is not None:
            result['gmt_create'] = self.gmt_create

        if self.passenger_name is not None:
            result['passenger_name'] = self.passenger_name

        if self.pay_type is not None:
            result['pay_type'] = self.pay_type

        if self.price is not None:
            result['price'] = self.price

        if self.trade_id is not None:
            result['trade_id'] = self.trade_id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category_code') is not None:
            self.category_code = m.get('category_code')

        if m.get('gmt_create') is not None:
            self.gmt_create = m.get('gmt_create')

        if m.get('passenger_name') is not None:
            self.passenger_name = m.get('passenger_name')

        if m.get('pay_type') is not None:
            self.pay_type = m.get('pay_type')

        if m.get('price') is not None:
            self.price = m.get('price')

        if m.get('trade_id') is not None:
            self.trade_id = m.get('trade_id')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class FlightOrderQueryResponseBodyModulePassengerInfoList(DaraModel):
    def __init__(
        self,
        cost_center_id: int = None,
        cost_center_name: str = None,
        cost_center_number: str = None,
        project_code: str = None,
        project_id: int = None,
        project_title: str = None,
        thirdpart_project_id: str = None,
        user_id: str = None,
        user_name: str = None,
        user_type: int = None,
    ):
        self.cost_center_id = cost_center_id
        self.cost_center_name = cost_center_name
        self.cost_center_number = cost_center_number
        self.project_code = project_code
        self.project_id = project_id
        self.project_title = project_title
        self.thirdpart_project_id = thirdpart_project_id
        self.user_id = user_id
        self.user_name = user_name
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cost_center_id is not None:
            result['cost_center_id'] = self.cost_center_id

        if self.cost_center_name is not None:
            result['cost_center_name'] = self.cost_center_name

        if self.cost_center_number is not None:
            result['cost_center_number'] = self.cost_center_number

        if self.project_code is not None:
            result['project_code'] = self.project_code

        if self.project_id is not None:
            result['project_id'] = self.project_id

        if self.project_title is not None:
            result['project_title'] = self.project_title

        if self.thirdpart_project_id is not None:
            result['thirdpart_project_id'] = self.thirdpart_project_id

        if self.user_id is not None:
            result['user_id'] = self.user_id

        if self.user_name is not None:
            result['user_name'] = self.user_name

        if self.user_type is not None:
            result['user_type'] = self.user_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost_center_id') is not None:
            self.cost_center_id = m.get('cost_center_id')

        if m.get('cost_center_name') is not None:
            self.cost_center_name = m.get('cost_center_name')

        if m.get('cost_center_number') is not None:
            self.cost_center_number = m.get('cost_center_number')

        if m.get('project_code') is not None:
            self.project_code = m.get('project_code')

        if m.get('project_id') is not None:
            self.project_id = m.get('project_id')

        if m.get('project_title') is not None:
            self.project_title = m.get('project_title')

        if m.get('thirdpart_project_id') is not None:
            self.thirdpart_project_id = m.get('thirdpart_project_id')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')

        if m.get('user_type') is not None:
            self.user_type = m.get('user_type')

        return self

class FlightOrderQueryResponseBodyModuleOrderBaseInfo(DaraModel):
    def __init__(
        self,
        apply_id: str = None,
        btrip_title: str = None,
        contact_name: str = None,
        corp_id: str = None,
        corp_name: str = None,
        depart_id: str = None,
        depart_name: str = None,
        exceed_apply_id: str = None,
        exceed_third_part_apply_id: str = None,
        gmt_create: str = None,
        gmt_modify: str = None,
        itinerary_id: str = None,
        order_id: int = None,
        order_status: int = None,
        supplier: str = None,
        thirdpart_apply_id: str = None,
        thirdpart_business_id: str = None,
        thirdpart_corp_id: str = None,
        thirdpart_itinerary_id: str = None,
        trip_type: int = None,
        user_id: str = None,
    ):
        self.apply_id = apply_id
        self.btrip_title = btrip_title
        self.contact_name = contact_name
        self.corp_id = corp_id
        self.corp_name = corp_name
        self.depart_id = depart_id
        self.depart_name = depart_name
        self.exceed_apply_id = exceed_apply_id
        self.exceed_third_part_apply_id = exceed_third_part_apply_id
        self.gmt_create = gmt_create
        self.gmt_modify = gmt_modify
        self.itinerary_id = itinerary_id
        self.order_id = order_id
        self.order_status = order_status
        self.supplier = supplier
        self.thirdpart_apply_id = thirdpart_apply_id
        self.thirdpart_business_id = thirdpart_business_id
        self.thirdpart_corp_id = thirdpart_corp_id
        self.thirdpart_itinerary_id = thirdpart_itinerary_id
        self.trip_type = trip_type
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_id is not None:
            result['apply_id'] = self.apply_id

        if self.btrip_title is not None:
            result['btrip_title'] = self.btrip_title

        if self.contact_name is not None:
            result['contact_name'] = self.contact_name

        if self.corp_id is not None:
            result['corp_id'] = self.corp_id

        if self.corp_name is not None:
            result['corp_name'] = self.corp_name

        if self.depart_id is not None:
            result['depart_id'] = self.depart_id

        if self.depart_name is not None:
            result['depart_name'] = self.depart_name

        if self.exceed_apply_id is not None:
            result['exceed_apply_id'] = self.exceed_apply_id

        if self.exceed_third_part_apply_id is not None:
            result['exceed_third_part_apply_id'] = self.exceed_third_part_apply_id

        if self.gmt_create is not None:
            result['gmt_create'] = self.gmt_create

        if self.gmt_modify is not None:
            result['gmt_modify'] = self.gmt_modify

        if self.itinerary_id is not None:
            result['itinerary_id'] = self.itinerary_id

        if self.order_id is not None:
            result['order_id'] = self.order_id

        if self.order_status is not None:
            result['order_status'] = self.order_status

        if self.supplier is not None:
            result['supplier'] = self.supplier

        if self.thirdpart_apply_id is not None:
            result['thirdpart_apply_id'] = self.thirdpart_apply_id

        if self.thirdpart_business_id is not None:
            result['thirdpart_business_id'] = self.thirdpart_business_id

        if self.thirdpart_corp_id is not None:
            result['thirdpart_corp_id'] = self.thirdpart_corp_id

        if self.thirdpart_itinerary_id is not None:
            result['thirdpart_itinerary_id'] = self.thirdpart_itinerary_id

        if self.trip_type is not None:
            result['trip_type'] = self.trip_type

        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apply_id') is not None:
            self.apply_id = m.get('apply_id')

        if m.get('btrip_title') is not None:
            self.btrip_title = m.get('btrip_title')

        if m.get('contact_name') is not None:
            self.contact_name = m.get('contact_name')

        if m.get('corp_id') is not None:
            self.corp_id = m.get('corp_id')

        if m.get('corp_name') is not None:
            self.corp_name = m.get('corp_name')

        if m.get('depart_id') is not None:
            self.depart_id = m.get('depart_id')

        if m.get('depart_name') is not None:
            self.depart_name = m.get('depart_name')

        if m.get('exceed_apply_id') is not None:
            self.exceed_apply_id = m.get('exceed_apply_id')

        if m.get('exceed_third_part_apply_id') is not None:
            self.exceed_third_part_apply_id = m.get('exceed_third_part_apply_id')

        if m.get('gmt_create') is not None:
            self.gmt_create = m.get('gmt_create')

        if m.get('gmt_modify') is not None:
            self.gmt_modify = m.get('gmt_modify')

        if m.get('itinerary_id') is not None:
            self.itinerary_id = m.get('itinerary_id')

        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')

        if m.get('order_status') is not None:
            self.order_status = m.get('order_status')

        if m.get('supplier') is not None:
            self.supplier = m.get('supplier')

        if m.get('thirdpart_apply_id') is not None:
            self.thirdpart_apply_id = m.get('thirdpart_apply_id')

        if m.get('thirdpart_business_id') is not None:
            self.thirdpart_business_id = m.get('thirdpart_business_id')

        if m.get('thirdpart_corp_id') is not None:
            self.thirdpart_corp_id = m.get('thirdpart_corp_id')

        if m.get('thirdpart_itinerary_id') is not None:
            self.thirdpart_itinerary_id = m.get('thirdpart_itinerary_id')

        if m.get('trip_type') is not None:
            self.trip_type = m.get('trip_type')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

class FlightOrderQueryResponseBodyModuleInvoiceInfo(DaraModel):
    def __init__(
        self,
        id: int = None,
        title: str = None,
    ):
        self.id = id
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['id'] = self.id

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class FlightOrderQueryResponseBodyModuleInsuranceInfoList(DaraModel):
    def __init__(
        self,
        amount: float = None,
        insurance_no: str = None,
        name: str = None,
        status: int = None,
        type: str = None,
    ):
        self.amount = amount
        self.insurance_no = insurance_no
        self.name = name
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['amount'] = self.amount

        if self.insurance_no is not None:
            result['insurance_no'] = self.insurance_no

        if self.name is not None:
            result['name'] = self.name

        if self.status is not None:
            result['status'] = self.status

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')

        if m.get('insurance_no') is not None:
            self.insurance_no = m.get('insurance_no')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class FlightOrderQueryResponseBodyModuleFlightTicketInfoList(DaraModel):
    def __init__(
        self,
        arr_airport: str = None,
        arr_airport_code: str = None,
        arr_city: str = None,
        arr_city_code: str = None,
        build_price: float = None,
        changed: bool = None,
        dep_airport: str = None,
        dep_airport_code: str = None,
        dep_city: str = None,
        dep_city_code: str = None,
        discount: int = None,
        flight_no: str = None,
        gmt_create: str = None,
        gmt_modify: str = None,
        journey_index: int = None,
        oil_price: float = None,
        pay_type: int = None,
        personal_price: float = None,
        segment_index: int = None,
        settle_price: float = None,
        ticket_no: str = None,
        ticket_price: float = None,
        ticket_status: str = None,
        ticket_status_code: int = None,
        user_id: str = None,
    ):
        self.arr_airport = arr_airport
        self.arr_airport_code = arr_airport_code
        self.arr_city = arr_city
        self.arr_city_code = arr_city_code
        self.build_price = build_price
        self.changed = changed
        self.dep_airport = dep_airport
        self.dep_airport_code = dep_airport_code
        self.dep_city = dep_city
        self.dep_city_code = dep_city_code
        self.discount = discount
        self.flight_no = flight_no
        self.gmt_create = gmt_create
        self.gmt_modify = gmt_modify
        self.journey_index = journey_index
        self.oil_price = oil_price
        self.pay_type = pay_type
        self.personal_price = personal_price
        self.segment_index = segment_index
        self.settle_price = settle_price
        self.ticket_no = ticket_no
        self.ticket_price = ticket_price
        self.ticket_status = ticket_status
        self.ticket_status_code = ticket_status_code
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arr_airport is not None:
            result['arr_airport'] = self.arr_airport

        if self.arr_airport_code is not None:
            result['arr_airport_code'] = self.arr_airport_code

        if self.arr_city is not None:
            result['arr_city'] = self.arr_city

        if self.arr_city_code is not None:
            result['arr_city_code'] = self.arr_city_code

        if self.build_price is not None:
            result['build_price'] = self.build_price

        if self.changed is not None:
            result['changed'] = self.changed

        if self.dep_airport is not None:
            result['dep_airport'] = self.dep_airport

        if self.dep_airport_code is not None:
            result['dep_airport_code'] = self.dep_airport_code

        if self.dep_city is not None:
            result['dep_city'] = self.dep_city

        if self.dep_city_code is not None:
            result['dep_city_code'] = self.dep_city_code

        if self.discount is not None:
            result['discount'] = self.discount

        if self.flight_no is not None:
            result['flight_no'] = self.flight_no

        if self.gmt_create is not None:
            result['gmt_create'] = self.gmt_create

        if self.gmt_modify is not None:
            result['gmt_modify'] = self.gmt_modify

        if self.journey_index is not None:
            result['journey_index'] = self.journey_index

        if self.oil_price is not None:
            result['oil_price'] = self.oil_price

        if self.pay_type is not None:
            result['pay_type'] = self.pay_type

        if self.personal_price is not None:
            result['personal_price'] = self.personal_price

        if self.segment_index is not None:
            result['segment_index'] = self.segment_index

        if self.settle_price is not None:
            result['settle_price'] = self.settle_price

        if self.ticket_no is not None:
            result['ticket_no'] = self.ticket_no

        if self.ticket_price is not None:
            result['ticket_price'] = self.ticket_price

        if self.ticket_status is not None:
            result['ticket_status'] = self.ticket_status

        if self.ticket_status_code is not None:
            result['ticket_status_code'] = self.ticket_status_code

        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arr_airport') is not None:
            self.arr_airport = m.get('arr_airport')

        if m.get('arr_airport_code') is not None:
            self.arr_airport_code = m.get('arr_airport_code')

        if m.get('arr_city') is not None:
            self.arr_city = m.get('arr_city')

        if m.get('arr_city_code') is not None:
            self.arr_city_code = m.get('arr_city_code')

        if m.get('build_price') is not None:
            self.build_price = m.get('build_price')

        if m.get('changed') is not None:
            self.changed = m.get('changed')

        if m.get('dep_airport') is not None:
            self.dep_airport = m.get('dep_airport')

        if m.get('dep_airport_code') is not None:
            self.dep_airport_code = m.get('dep_airport_code')

        if m.get('dep_city') is not None:
            self.dep_city = m.get('dep_city')

        if m.get('dep_city_code') is not None:
            self.dep_city_code = m.get('dep_city_code')

        if m.get('discount') is not None:
            self.discount = m.get('discount')

        if m.get('flight_no') is not None:
            self.flight_no = m.get('flight_no')

        if m.get('gmt_create') is not None:
            self.gmt_create = m.get('gmt_create')

        if m.get('gmt_modify') is not None:
            self.gmt_modify = m.get('gmt_modify')

        if m.get('journey_index') is not None:
            self.journey_index = m.get('journey_index')

        if m.get('oil_price') is not None:
            self.oil_price = m.get('oil_price')

        if m.get('pay_type') is not None:
            self.pay_type = m.get('pay_type')

        if m.get('personal_price') is not None:
            self.personal_price = m.get('personal_price')

        if m.get('segment_index') is not None:
            self.segment_index = m.get('segment_index')

        if m.get('settle_price') is not None:
            self.settle_price = m.get('settle_price')

        if m.get('ticket_no') is not None:
            self.ticket_no = m.get('ticket_no')

        if m.get('ticket_price') is not None:
            self.ticket_price = m.get('ticket_price')

        if m.get('ticket_status') is not None:
            self.ticket_status = m.get('ticket_status')

        if m.get('ticket_status_code') is not None:
            self.ticket_status_code = m.get('ticket_status_code')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

class FlightOrderQueryResponseBodyModuleFlightRefundTicketInfoList(DaraModel):
    def __init__(
        self,
        apply_id: str = None,
        arr_airport: str = None,
        arr_airport_code: str = None,
        arr_city: str = None,
        arr_city_code: str = None,
        company_refund_ticket_fee: float = None,
        dep_airport: str = None,
        dep_airport_code: str = None,
        dep_city: str = None,
        dep_city_code: str = None,
        flight_no: str = None,
        gmt_create: str = None,
        gmt_modify: str = None,
        journey_index: int = None,
        out_apply_id: str = None,
        personal_refund_ticket_fee: float = None,
        refund_order_id: int = None,
        refund_reason: str = None,
        refund_ticket_fee: float = None,
        refund_type: int = None,
        segment_index: int = None,
        ticket_no: str = None,
    ):
        self.apply_id = apply_id
        self.arr_airport = arr_airport
        self.arr_airport_code = arr_airport_code
        self.arr_city = arr_city
        self.arr_city_code = arr_city_code
        self.company_refund_ticket_fee = company_refund_ticket_fee
        self.dep_airport = dep_airport
        self.dep_airport_code = dep_airport_code
        self.dep_city = dep_city
        self.dep_city_code = dep_city_code
        self.flight_no = flight_no
        self.gmt_create = gmt_create
        self.gmt_modify = gmt_modify
        self.journey_index = journey_index
        self.out_apply_id = out_apply_id
        self.personal_refund_ticket_fee = personal_refund_ticket_fee
        self.refund_order_id = refund_order_id
        self.refund_reason = refund_reason
        self.refund_ticket_fee = refund_ticket_fee
        self.refund_type = refund_type
        self.segment_index = segment_index
        self.ticket_no = ticket_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_id is not None:
            result['apply_id'] = self.apply_id

        if self.arr_airport is not None:
            result['arr_airport'] = self.arr_airport

        if self.arr_airport_code is not None:
            result['arr_airport_code'] = self.arr_airport_code

        if self.arr_city is not None:
            result['arr_city'] = self.arr_city

        if self.arr_city_code is not None:
            result['arr_city_code'] = self.arr_city_code

        if self.company_refund_ticket_fee is not None:
            result['company_refund_ticket_fee'] = self.company_refund_ticket_fee

        if self.dep_airport is not None:
            result['dep_airport'] = self.dep_airport

        if self.dep_airport_code is not None:
            result['dep_airport_code'] = self.dep_airport_code

        if self.dep_city is not None:
            result['dep_city'] = self.dep_city

        if self.dep_city_code is not None:
            result['dep_city_code'] = self.dep_city_code

        if self.flight_no is not None:
            result['flight_no'] = self.flight_no

        if self.gmt_create is not None:
            result['gmt_create'] = self.gmt_create

        if self.gmt_modify is not None:
            result['gmt_modify'] = self.gmt_modify

        if self.journey_index is not None:
            result['journey_index'] = self.journey_index

        if self.out_apply_id is not None:
            result['out_apply_id'] = self.out_apply_id

        if self.personal_refund_ticket_fee is not None:
            result['personal_refund_ticket_fee'] = self.personal_refund_ticket_fee

        if self.refund_order_id is not None:
            result['refund_order_id'] = self.refund_order_id

        if self.refund_reason is not None:
            result['refund_reason'] = self.refund_reason

        if self.refund_ticket_fee is not None:
            result['refund_ticket_fee'] = self.refund_ticket_fee

        if self.refund_type is not None:
            result['refund_type'] = self.refund_type

        if self.segment_index is not None:
            result['segment_index'] = self.segment_index

        if self.ticket_no is not None:
            result['ticket_no'] = self.ticket_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apply_id') is not None:
            self.apply_id = m.get('apply_id')

        if m.get('arr_airport') is not None:
            self.arr_airport = m.get('arr_airport')

        if m.get('arr_airport_code') is not None:
            self.arr_airport_code = m.get('arr_airport_code')

        if m.get('arr_city') is not None:
            self.arr_city = m.get('arr_city')

        if m.get('arr_city_code') is not None:
            self.arr_city_code = m.get('arr_city_code')

        if m.get('company_refund_ticket_fee') is not None:
            self.company_refund_ticket_fee = m.get('company_refund_ticket_fee')

        if m.get('dep_airport') is not None:
            self.dep_airport = m.get('dep_airport')

        if m.get('dep_airport_code') is not None:
            self.dep_airport_code = m.get('dep_airport_code')

        if m.get('dep_city') is not None:
            self.dep_city = m.get('dep_city')

        if m.get('dep_city_code') is not None:
            self.dep_city_code = m.get('dep_city_code')

        if m.get('flight_no') is not None:
            self.flight_no = m.get('flight_no')

        if m.get('gmt_create') is not None:
            self.gmt_create = m.get('gmt_create')

        if m.get('gmt_modify') is not None:
            self.gmt_modify = m.get('gmt_modify')

        if m.get('journey_index') is not None:
            self.journey_index = m.get('journey_index')

        if m.get('out_apply_id') is not None:
            self.out_apply_id = m.get('out_apply_id')

        if m.get('personal_refund_ticket_fee') is not None:
            self.personal_refund_ticket_fee = m.get('personal_refund_ticket_fee')

        if m.get('refund_order_id') is not None:
            self.refund_order_id = m.get('refund_order_id')

        if m.get('refund_reason') is not None:
            self.refund_reason = m.get('refund_reason')

        if m.get('refund_ticket_fee') is not None:
            self.refund_ticket_fee = m.get('refund_ticket_fee')

        if m.get('refund_type') is not None:
            self.refund_type = m.get('refund_type')

        if m.get('segment_index') is not None:
            self.segment_index = m.get('segment_index')

        if m.get('ticket_no') is not None:
            self.ticket_no = m.get('ticket_no')

        return self

class FlightOrderQueryResponseBodyModuleFlightInfoList(DaraModel):
    def __init__(
        self,
        airline_code: str = None,
        airline_name: str = None,
        arr_airport_city_county: main_models.FlightOrderQueryResponseBodyModuleFlightInfoListArrAirportCityCounty = None,
        arr_airport_code: str = None,
        arr_airport_name: str = None,
        arr_city_ad_code: str = None,
        arr_city_code: str = None,
        arr_city_name: str = None,
        arr_terminal: str = None,
        arr_time: str = None,
        cabin: str = None,
        cabin_level: str = None,
        dep_airport_city_county: main_models.FlightOrderQueryResponseBodyModuleFlightInfoListDepAirportCityCounty = None,
        dep_airport_code: str = None,
        dep_airport_name: str = None,
        dep_city_ad_code: str = None,
        dep_city_code: str = None,
        dep_city_name: str = None,
        dep_terminal: str = None,
        dep_time: str = None,
        flight_mile: int = None,
        flight_no: str = None,
        journey_index: int = None,
        segment_index: int = None,
        stop_city: List[str] = None,
        stop_city_info_list: List[main_models.FlightOrderQueryResponseBodyModuleFlightInfoListStopCityInfoList] = None,
    ):
        self.airline_code = airline_code
        self.airline_name = airline_name
        self.arr_airport_city_county = arr_airport_city_county
        self.arr_airport_code = arr_airport_code
        self.arr_airport_name = arr_airport_name
        self.arr_city_ad_code = arr_city_ad_code
        self.arr_city_code = arr_city_code
        self.arr_city_name = arr_city_name
        self.arr_terminal = arr_terminal
        self.arr_time = arr_time
        self.cabin = cabin
        self.cabin_level = cabin_level
        self.dep_airport_city_county = dep_airport_city_county
        self.dep_airport_code = dep_airport_code
        self.dep_airport_name = dep_airport_name
        self.dep_city_ad_code = dep_city_ad_code
        self.dep_city_code = dep_city_code
        self.dep_city_name = dep_city_name
        self.dep_terminal = dep_terminal
        self.dep_time = dep_time
        self.flight_mile = flight_mile
        self.flight_no = flight_no
        self.journey_index = journey_index
        self.segment_index = segment_index
        self.stop_city = stop_city
        self.stop_city_info_list = stop_city_info_list

    def validate(self):
        if self.arr_airport_city_county:
            self.arr_airport_city_county.validate()
        if self.dep_airport_city_county:
            self.dep_airport_city_county.validate()
        if self.stop_city_info_list:
            for v1 in self.stop_city_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.airline_code is not None:
            result['airline_code'] = self.airline_code

        if self.airline_name is not None:
            result['airline_name'] = self.airline_name

        if self.arr_airport_city_county is not None:
            result['arr_airport_city_county'] = self.arr_airport_city_county.to_map()

        if self.arr_airport_code is not None:
            result['arr_airport_code'] = self.arr_airport_code

        if self.arr_airport_name is not None:
            result['arr_airport_name'] = self.arr_airport_name

        if self.arr_city_ad_code is not None:
            result['arr_city_ad_code'] = self.arr_city_ad_code

        if self.arr_city_code is not None:
            result['arr_city_code'] = self.arr_city_code

        if self.arr_city_name is not None:
            result['arr_city_name'] = self.arr_city_name

        if self.arr_terminal is not None:
            result['arr_terminal'] = self.arr_terminal

        if self.arr_time is not None:
            result['arr_time'] = self.arr_time

        if self.cabin is not None:
            result['cabin'] = self.cabin

        if self.cabin_level is not None:
            result['cabin_level'] = self.cabin_level

        if self.dep_airport_city_county is not None:
            result['dep_airport_city_county'] = self.dep_airport_city_county.to_map()

        if self.dep_airport_code is not None:
            result['dep_airport_code'] = self.dep_airport_code

        if self.dep_airport_name is not None:
            result['dep_airport_name'] = self.dep_airport_name

        if self.dep_city_ad_code is not None:
            result['dep_city_ad_code'] = self.dep_city_ad_code

        if self.dep_city_code is not None:
            result['dep_city_code'] = self.dep_city_code

        if self.dep_city_name is not None:
            result['dep_city_name'] = self.dep_city_name

        if self.dep_terminal is not None:
            result['dep_terminal'] = self.dep_terminal

        if self.dep_time is not None:
            result['dep_time'] = self.dep_time

        if self.flight_mile is not None:
            result['flight_mile'] = self.flight_mile

        if self.flight_no is not None:
            result['flight_no'] = self.flight_no

        if self.journey_index is not None:
            result['journey_index'] = self.journey_index

        if self.segment_index is not None:
            result['segment_index'] = self.segment_index

        if self.stop_city is not None:
            result['stop_city'] = self.stop_city

        result['stop_city_info_list'] = []
        if self.stop_city_info_list is not None:
            for k1 in self.stop_city_info_list:
                result['stop_city_info_list'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('airline_code') is not None:
            self.airline_code = m.get('airline_code')

        if m.get('airline_name') is not None:
            self.airline_name = m.get('airline_name')

        if m.get('arr_airport_city_county') is not None:
            temp_model = main_models.FlightOrderQueryResponseBodyModuleFlightInfoListArrAirportCityCounty()
            self.arr_airport_city_county = temp_model.from_map(m.get('arr_airport_city_county'))

        if m.get('arr_airport_code') is not None:
            self.arr_airport_code = m.get('arr_airport_code')

        if m.get('arr_airport_name') is not None:
            self.arr_airport_name = m.get('arr_airport_name')

        if m.get('arr_city_ad_code') is not None:
            self.arr_city_ad_code = m.get('arr_city_ad_code')

        if m.get('arr_city_code') is not None:
            self.arr_city_code = m.get('arr_city_code')

        if m.get('arr_city_name') is not None:
            self.arr_city_name = m.get('arr_city_name')

        if m.get('arr_terminal') is not None:
            self.arr_terminal = m.get('arr_terminal')

        if m.get('arr_time') is not None:
            self.arr_time = m.get('arr_time')

        if m.get('cabin') is not None:
            self.cabin = m.get('cabin')

        if m.get('cabin_level') is not None:
            self.cabin_level = m.get('cabin_level')

        if m.get('dep_airport_city_county') is not None:
            temp_model = main_models.FlightOrderQueryResponseBodyModuleFlightInfoListDepAirportCityCounty()
            self.dep_airport_city_county = temp_model.from_map(m.get('dep_airport_city_county'))

        if m.get('dep_airport_code') is not None:
            self.dep_airport_code = m.get('dep_airport_code')

        if m.get('dep_airport_name') is not None:
            self.dep_airport_name = m.get('dep_airport_name')

        if m.get('dep_city_ad_code') is not None:
            self.dep_city_ad_code = m.get('dep_city_ad_code')

        if m.get('dep_city_code') is not None:
            self.dep_city_code = m.get('dep_city_code')

        if m.get('dep_city_name') is not None:
            self.dep_city_name = m.get('dep_city_name')

        if m.get('dep_terminal') is not None:
            self.dep_terminal = m.get('dep_terminal')

        if m.get('dep_time') is not None:
            self.dep_time = m.get('dep_time')

        if m.get('flight_mile') is not None:
            self.flight_mile = m.get('flight_mile')

        if m.get('flight_no') is not None:
            self.flight_no = m.get('flight_no')

        if m.get('journey_index') is not None:
            self.journey_index = m.get('journey_index')

        if m.get('segment_index') is not None:
            self.segment_index = m.get('segment_index')

        if m.get('stop_city') is not None:
            self.stop_city = m.get('stop_city')

        self.stop_city_info_list = []
        if m.get('stop_city_info_list') is not None:
            for k1 in m.get('stop_city_info_list'):
                temp_model = main_models.FlightOrderQueryResponseBodyModuleFlightInfoListStopCityInfoList()
                self.stop_city_info_list.append(temp_model.from_map(k1))

        return self

class FlightOrderQueryResponseBodyModuleFlightInfoListStopCityInfoList(DaraModel):
    def __init__(
        self,
        stop_airport_city_county: main_models.FlightOrderQueryResponseBodyModuleFlightInfoListStopCityInfoListStopAirportCityCounty = None,
        stop_airport_code: str = None,
    ):
        self.stop_airport_city_county = stop_airport_city_county
        self.stop_airport_code = stop_airport_code

    def validate(self):
        if self.stop_airport_city_county:
            self.stop_airport_city_county.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.stop_airport_city_county is not None:
            result['stop_airport_city_county'] = self.stop_airport_city_county.to_map()

        if self.stop_airport_code is not None:
            result['stop_airport_code'] = self.stop_airport_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('stop_airport_city_county') is not None:
            temp_model = main_models.FlightOrderQueryResponseBodyModuleFlightInfoListStopCityInfoListStopAirportCityCounty()
            self.stop_airport_city_county = temp_model.from_map(m.get('stop_airport_city_county'))

        if m.get('stop_airport_code') is not None:
            self.stop_airport_code = m.get('stop_airport_code')

        return self

class FlightOrderQueryResponseBodyModuleFlightInfoListStopCityInfoListStopAirportCityCounty(DaraModel):
    def __init__(
        self,
        adcode: str = None,
        airport_city_code: str = None,
        airport_city_name: str = None,
        airport_code: str = None,
        airport_name: str = None,
        airport_parent_city_name: str = None,
        county_city_adcode: str = None,
        county_city_name: str = None,
        prefecture_city_adcode: str = None,
        prefecture_city_name: str = None,
    ):
        self.adcode = adcode
        self.airport_city_code = airport_city_code
        self.airport_city_name = airport_city_name
        self.airport_code = airport_code
        self.airport_name = airport_name
        self.airport_parent_city_name = airport_parent_city_name
        self.county_city_adcode = county_city_adcode
        self.county_city_name = county_city_name
        self.prefecture_city_adcode = prefecture_city_adcode
        self.prefecture_city_name = prefecture_city_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adcode is not None:
            result['adcode'] = self.adcode

        if self.airport_city_code is not None:
            result['airport_city_code'] = self.airport_city_code

        if self.airport_city_name is not None:
            result['airport_city_name'] = self.airport_city_name

        if self.airport_code is not None:
            result['airport_code'] = self.airport_code

        if self.airport_name is not None:
            result['airport_name'] = self.airport_name

        if self.airport_parent_city_name is not None:
            result['airport_parent_city_name'] = self.airport_parent_city_name

        if self.county_city_adcode is not None:
            result['county_city_adcode'] = self.county_city_adcode

        if self.county_city_name is not None:
            result['county_city_name'] = self.county_city_name

        if self.prefecture_city_adcode is not None:
            result['prefecture_city_adcode'] = self.prefecture_city_adcode

        if self.prefecture_city_name is not None:
            result['prefecture_city_name'] = self.prefecture_city_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('adcode') is not None:
            self.adcode = m.get('adcode')

        if m.get('airport_city_code') is not None:
            self.airport_city_code = m.get('airport_city_code')

        if m.get('airport_city_name') is not None:
            self.airport_city_name = m.get('airport_city_name')

        if m.get('airport_code') is not None:
            self.airport_code = m.get('airport_code')

        if m.get('airport_name') is not None:
            self.airport_name = m.get('airport_name')

        if m.get('airport_parent_city_name') is not None:
            self.airport_parent_city_name = m.get('airport_parent_city_name')

        if m.get('county_city_adcode') is not None:
            self.county_city_adcode = m.get('county_city_adcode')

        if m.get('county_city_name') is not None:
            self.county_city_name = m.get('county_city_name')

        if m.get('prefecture_city_adcode') is not None:
            self.prefecture_city_adcode = m.get('prefecture_city_adcode')

        if m.get('prefecture_city_name') is not None:
            self.prefecture_city_name = m.get('prefecture_city_name')

        return self

class FlightOrderQueryResponseBodyModuleFlightInfoListDepAirportCityCounty(DaraModel):
    def __init__(
        self,
        adcode: str = None,
        airport_city_code: str = None,
        airport_city_name: str = None,
        airport_code: str = None,
        airport_name: str = None,
        airport_parent_city_name: str = None,
        county_city_adcode: str = None,
        county_city_name: str = None,
        prefecture_city_adcode: str = None,
        prefecture_city_name: str = None,
    ):
        self.adcode = adcode
        self.airport_city_code = airport_city_code
        self.airport_city_name = airport_city_name
        self.airport_code = airport_code
        self.airport_name = airport_name
        self.airport_parent_city_name = airport_parent_city_name
        self.county_city_adcode = county_city_adcode
        self.county_city_name = county_city_name
        self.prefecture_city_adcode = prefecture_city_adcode
        self.prefecture_city_name = prefecture_city_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adcode is not None:
            result['adcode'] = self.adcode

        if self.airport_city_code is not None:
            result['airport_city_code'] = self.airport_city_code

        if self.airport_city_name is not None:
            result['airport_city_name'] = self.airport_city_name

        if self.airport_code is not None:
            result['airport_code'] = self.airport_code

        if self.airport_name is not None:
            result['airport_name'] = self.airport_name

        if self.airport_parent_city_name is not None:
            result['airport_parent_city_name'] = self.airport_parent_city_name

        if self.county_city_adcode is not None:
            result['county_city_adcode'] = self.county_city_adcode

        if self.county_city_name is not None:
            result['county_city_name'] = self.county_city_name

        if self.prefecture_city_adcode is not None:
            result['prefecture_city_adcode'] = self.prefecture_city_adcode

        if self.prefecture_city_name is not None:
            result['prefecture_city_name'] = self.prefecture_city_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('adcode') is not None:
            self.adcode = m.get('adcode')

        if m.get('airport_city_code') is not None:
            self.airport_city_code = m.get('airport_city_code')

        if m.get('airport_city_name') is not None:
            self.airport_city_name = m.get('airport_city_name')

        if m.get('airport_code') is not None:
            self.airport_code = m.get('airport_code')

        if m.get('airport_name') is not None:
            self.airport_name = m.get('airport_name')

        if m.get('airport_parent_city_name') is not None:
            self.airport_parent_city_name = m.get('airport_parent_city_name')

        if m.get('county_city_adcode') is not None:
            self.county_city_adcode = m.get('county_city_adcode')

        if m.get('county_city_name') is not None:
            self.county_city_name = m.get('county_city_name')

        if m.get('prefecture_city_adcode') is not None:
            self.prefecture_city_adcode = m.get('prefecture_city_adcode')

        if m.get('prefecture_city_name') is not None:
            self.prefecture_city_name = m.get('prefecture_city_name')

        return self

class FlightOrderQueryResponseBodyModuleFlightInfoListArrAirportCityCounty(DaraModel):
    def __init__(
        self,
        adcode: str = None,
        airport_city_code: str = None,
        airport_city_name: str = None,
        airport_code: str = None,
        airport_name: str = None,
        airport_parent_city_name: str = None,
        county_city_adcode: str = None,
        county_city_name: str = None,
        prefecture_city_adcode: str = None,
        prefecture_city_name: str = None,
    ):
        self.adcode = adcode
        self.airport_city_code = airport_city_code
        self.airport_city_name = airport_city_name
        self.airport_code = airport_code
        self.airport_name = airport_name
        self.airport_parent_city_name = airport_parent_city_name
        self.county_city_adcode = county_city_adcode
        self.county_city_name = county_city_name
        self.prefecture_city_adcode = prefecture_city_adcode
        self.prefecture_city_name = prefecture_city_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adcode is not None:
            result['adcode'] = self.adcode

        if self.airport_city_code is not None:
            result['airport_city_code'] = self.airport_city_code

        if self.airport_city_name is not None:
            result['airport_city_name'] = self.airport_city_name

        if self.airport_code is not None:
            result['airport_code'] = self.airport_code

        if self.airport_name is not None:
            result['airport_name'] = self.airport_name

        if self.airport_parent_city_name is not None:
            result['airport_parent_city_name'] = self.airport_parent_city_name

        if self.county_city_adcode is not None:
            result['county_city_adcode'] = self.county_city_adcode

        if self.county_city_name is not None:
            result['county_city_name'] = self.county_city_name

        if self.prefecture_city_adcode is not None:
            result['prefecture_city_adcode'] = self.prefecture_city_adcode

        if self.prefecture_city_name is not None:
            result['prefecture_city_name'] = self.prefecture_city_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('adcode') is not None:
            self.adcode = m.get('adcode')

        if m.get('airport_city_code') is not None:
            self.airport_city_code = m.get('airport_city_code')

        if m.get('airport_city_name') is not None:
            self.airport_city_name = m.get('airport_city_name')

        if m.get('airport_code') is not None:
            self.airport_code = m.get('airport_code')

        if m.get('airport_name') is not None:
            self.airport_name = m.get('airport_name')

        if m.get('airport_parent_city_name') is not None:
            self.airport_parent_city_name = m.get('airport_parent_city_name')

        if m.get('county_city_adcode') is not None:
            self.county_city_adcode = m.get('county_city_adcode')

        if m.get('county_city_name') is not None:
            self.county_city_name = m.get('county_city_name')

        if m.get('prefecture_city_adcode') is not None:
            self.prefecture_city_adcode = m.get('prefecture_city_adcode')

        if m.get('prefecture_city_name') is not None:
            self.prefecture_city_name = m.get('prefecture_city_name')

        return self

class FlightOrderQueryResponseBodyModuleFlightChangeTicketInfoList(DaraModel):
    def __init__(
        self,
        apply_id: str = None,
        arr_airport: str = None,
        arr_airport_code: str = None,
        arr_city: str = None,
        arr_city_code: str = None,
        arr_time: str = None,
        change_cabin: str = None,
        change_cabin_level: str = None,
        change_fee: float = None,
        change_flight_no: str = None,
        change_order_id: int = None,
        change_reason: str = None,
        change_type: int = None,
        dep_airport: str = None,
        dep_airport_code: str = None,
        dep_city: str = None,
        dep_city_code: str = None,
        dep_time: str = None,
        discount: str = None,
        gmt_create: str = None,
        gmt_modify: str = None,
        journey_index: int = None,
        origin_ticket_no: str = None,
        out_apply_id: str = None,
        segment_index: int = None,
        stop_city: str = None,
        ticket_no: str = None,
        ticket_status: str = None,
        ticket_status_code: int = None,
        upgrade_fee: float = None,
    ):
        self.apply_id = apply_id
        self.arr_airport = arr_airport
        self.arr_airport_code = arr_airport_code
        self.arr_city = arr_city
        self.arr_city_code = arr_city_code
        self.arr_time = arr_time
        self.change_cabin = change_cabin
        self.change_cabin_level = change_cabin_level
        self.change_fee = change_fee
        self.change_flight_no = change_flight_no
        self.change_order_id = change_order_id
        self.change_reason = change_reason
        self.change_type = change_type
        self.dep_airport = dep_airport
        self.dep_airport_code = dep_airport_code
        self.dep_city = dep_city
        self.dep_city_code = dep_city_code
        self.dep_time = dep_time
        self.discount = discount
        self.gmt_create = gmt_create
        self.gmt_modify = gmt_modify
        self.journey_index = journey_index
        self.origin_ticket_no = origin_ticket_no
        self.out_apply_id = out_apply_id
        self.segment_index = segment_index
        self.stop_city = stop_city
        self.ticket_no = ticket_no
        self.ticket_status = ticket_status
        self.ticket_status_code = ticket_status_code
        self.upgrade_fee = upgrade_fee

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_id is not None:
            result['apply_id'] = self.apply_id

        if self.arr_airport is not None:
            result['arr_airport'] = self.arr_airport

        if self.arr_airport_code is not None:
            result['arr_airport_code'] = self.arr_airport_code

        if self.arr_city is not None:
            result['arr_city'] = self.arr_city

        if self.arr_city_code is not None:
            result['arr_city_code'] = self.arr_city_code

        if self.arr_time is not None:
            result['arr_time'] = self.arr_time

        if self.change_cabin is not None:
            result['change_cabin'] = self.change_cabin

        if self.change_cabin_level is not None:
            result['change_cabin_level'] = self.change_cabin_level

        if self.change_fee is not None:
            result['change_fee'] = self.change_fee

        if self.change_flight_no is not None:
            result['change_flight_no'] = self.change_flight_no

        if self.change_order_id is not None:
            result['change_order_id'] = self.change_order_id

        if self.change_reason is not None:
            result['change_reason'] = self.change_reason

        if self.change_type is not None:
            result['change_type'] = self.change_type

        if self.dep_airport is not None:
            result['dep_airport'] = self.dep_airport

        if self.dep_airport_code is not None:
            result['dep_airport_code'] = self.dep_airport_code

        if self.dep_city is not None:
            result['dep_city'] = self.dep_city

        if self.dep_city_code is not None:
            result['dep_city_code'] = self.dep_city_code

        if self.dep_time is not None:
            result['dep_time'] = self.dep_time

        if self.discount is not None:
            result['discount'] = self.discount

        if self.gmt_create is not None:
            result['gmt_create'] = self.gmt_create

        if self.gmt_modify is not None:
            result['gmt_modify'] = self.gmt_modify

        if self.journey_index is not None:
            result['journey_index'] = self.journey_index

        if self.origin_ticket_no is not None:
            result['origin_ticket_no'] = self.origin_ticket_no

        if self.out_apply_id is not None:
            result['out_apply_id'] = self.out_apply_id

        if self.segment_index is not None:
            result['segment_index'] = self.segment_index

        if self.stop_city is not None:
            result['stop_city'] = self.stop_city

        if self.ticket_no is not None:
            result['ticket_no'] = self.ticket_no

        if self.ticket_status is not None:
            result['ticket_status'] = self.ticket_status

        if self.ticket_status_code is not None:
            result['ticket_status_code'] = self.ticket_status_code

        if self.upgrade_fee is not None:
            result['upgrade_fee'] = self.upgrade_fee

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apply_id') is not None:
            self.apply_id = m.get('apply_id')

        if m.get('arr_airport') is not None:
            self.arr_airport = m.get('arr_airport')

        if m.get('arr_airport_code') is not None:
            self.arr_airport_code = m.get('arr_airport_code')

        if m.get('arr_city') is not None:
            self.arr_city = m.get('arr_city')

        if m.get('arr_city_code') is not None:
            self.arr_city_code = m.get('arr_city_code')

        if m.get('arr_time') is not None:
            self.arr_time = m.get('arr_time')

        if m.get('change_cabin') is not None:
            self.change_cabin = m.get('change_cabin')

        if m.get('change_cabin_level') is not None:
            self.change_cabin_level = m.get('change_cabin_level')

        if m.get('change_fee') is not None:
            self.change_fee = m.get('change_fee')

        if m.get('change_flight_no') is not None:
            self.change_flight_no = m.get('change_flight_no')

        if m.get('change_order_id') is not None:
            self.change_order_id = m.get('change_order_id')

        if m.get('change_reason') is not None:
            self.change_reason = m.get('change_reason')

        if m.get('change_type') is not None:
            self.change_type = m.get('change_type')

        if m.get('dep_airport') is not None:
            self.dep_airport = m.get('dep_airport')

        if m.get('dep_airport_code') is not None:
            self.dep_airport_code = m.get('dep_airport_code')

        if m.get('dep_city') is not None:
            self.dep_city = m.get('dep_city')

        if m.get('dep_city_code') is not None:
            self.dep_city_code = m.get('dep_city_code')

        if m.get('dep_time') is not None:
            self.dep_time = m.get('dep_time')

        if m.get('discount') is not None:
            self.discount = m.get('discount')

        if m.get('gmt_create') is not None:
            self.gmt_create = m.get('gmt_create')

        if m.get('gmt_modify') is not None:
            self.gmt_modify = m.get('gmt_modify')

        if m.get('journey_index') is not None:
            self.journey_index = m.get('journey_index')

        if m.get('origin_ticket_no') is not None:
            self.origin_ticket_no = m.get('origin_ticket_no')

        if m.get('out_apply_id') is not None:
            self.out_apply_id = m.get('out_apply_id')

        if m.get('segment_index') is not None:
            self.segment_index = m.get('segment_index')

        if m.get('stop_city') is not None:
            self.stop_city = m.get('stop_city')

        if m.get('ticket_no') is not None:
            self.ticket_no = m.get('ticket_no')

        if m.get('ticket_status') is not None:
            self.ticket_status = m.get('ticket_status')

        if m.get('ticket_status_code') is not None:
            self.ticket_status_code = m.get('ticket_status_code')

        if m.get('upgrade_fee') is not None:
            self.upgrade_fee = m.get('upgrade_fee')

        return self

