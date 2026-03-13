# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class IFlightOrderListQueryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: List[main_models.IFlightOrderListQueryResponseBodyModule] = None,
        page_info: main_models.IFlightOrderListQueryResponseBodyPageInfo = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.message = message
        self.module = module
        self.page_info = page_info
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.module:
            for v1 in self.module:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        result['module'] = []
        if self.module is not None:
            for k1 in self.module:
                result['module'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['pageInfo'] = self.page_info.to_map()

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

        self.module = []
        if m.get('module') is not None:
            for k1 in m.get('module'):
                temp_model = main_models.IFlightOrderListQueryResponseBodyModule()
                self.module.append(temp_model.from_map(k1))

        if m.get('pageInfo') is not None:
            temp_model = main_models.IFlightOrderListQueryResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('pageInfo'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class IFlightOrderListQueryResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        number: int = None,
        scroll_id: str = None,
        total_number: int = None,
    ):
        self.number = number
        self.scroll_id = scroll_id
        self.total_number = total_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.number is not None:
            result['number'] = self.number

        if self.scroll_id is not None:
            result['scroll_id'] = self.scroll_id

        if self.total_number is not None:
            result['total_number'] = self.total_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('number') is not None:
            self.number = m.get('number')

        if m.get('scroll_id') is not None:
            self.scroll_id = m.get('scroll_id')

        if m.get('total_number') is not None:
            self.total_number = m.get('total_number')

        return self

class IFlightOrderListQueryResponseBodyModule(DaraModel):
    def __init__(
        self,
        flight_modify_order_list: List[main_models.IFlightOrderListQueryResponseBodyModuleFlightModifyOrderList] = None,
        flight_refund_order_list: List[main_models.IFlightOrderListQueryResponseBodyModuleFlightRefundOrderList] = None,
        flight_sale_order: main_models.IFlightOrderListQueryResponseBodyModuleFlightSaleOrder = None,
    ):
        self.flight_modify_order_list = flight_modify_order_list
        self.flight_refund_order_list = flight_refund_order_list
        self.flight_sale_order = flight_sale_order

    def validate(self):
        if self.flight_modify_order_list:
            for v1 in self.flight_modify_order_list:
                 if v1:
                    v1.validate()
        if self.flight_refund_order_list:
            for v1 in self.flight_refund_order_list:
                 if v1:
                    v1.validate()
        if self.flight_sale_order:
            self.flight_sale_order.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['flight_modify_order_list'] = []
        if self.flight_modify_order_list is not None:
            for k1 in self.flight_modify_order_list:
                result['flight_modify_order_list'].append(k1.to_map() if k1 else None)

        result['flight_refund_order_list'] = []
        if self.flight_refund_order_list is not None:
            for k1 in self.flight_refund_order_list:
                result['flight_refund_order_list'].append(k1.to_map() if k1 else None)

        if self.flight_sale_order is not None:
            result['flight_sale_order'] = self.flight_sale_order.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.flight_modify_order_list = []
        if m.get('flight_modify_order_list') is not None:
            for k1 in m.get('flight_modify_order_list'):
                temp_model = main_models.IFlightOrderListQueryResponseBodyModuleFlightModifyOrderList()
                self.flight_modify_order_list.append(temp_model.from_map(k1))

        self.flight_refund_order_list = []
        if m.get('flight_refund_order_list') is not None:
            for k1 in m.get('flight_refund_order_list'):
                temp_model = main_models.IFlightOrderListQueryResponseBodyModuleFlightRefundOrderList()
                self.flight_refund_order_list.append(temp_model.from_map(k1))

        if m.get('flight_sale_order') is not None:
            temp_model = main_models.IFlightOrderListQueryResponseBodyModuleFlightSaleOrder()
            self.flight_sale_order = temp_model.from_map(m.get('flight_sale_order'))

        return self

class IFlightOrderListQueryResponseBodyModuleFlightSaleOrder(DaraModel):
    def __init__(
        self,
        apply_id: int = None,
        book_type: int = None,
        booker_info: main_models.IFlightOrderListQueryResponseBodyModuleFlightSaleOrderBookerInfo = None,
        corp_pay_price: int = None,
        exceed_apply_id: str = None,
        flight_order_insure_list: List[main_models.IFlightOrderListQueryResponseBodyModuleFlightSaleOrderFlightOrderInsureList] = None,
        flight_order_ticket_list: List[main_models.IFlightOrderListQueryResponseBodyModuleFlightSaleOrderFlightOrderTicketList] = None,
        flight_segment_list: List[main_models.IFlightOrderListQueryResponseBodyModuleFlightSaleOrderFlightSegmentList] = None,
        mix_pay: bool = None,
        order_create_time: str = None,
        order_id: str = None,
        order_pay_time: str = None,
        order_reserve_price: int = None,
        order_status: int = None,
        order_status_desc: str = None,
        order_type: int = None,
        passenger_list: List[main_models.IFlightOrderListQueryResponseBodyModuleFlightSaleOrderPassengerList] = None,
        pay_type: int = None,
        person_pay_price: int = None,
        service_fee: int = None,
        third_part_apply_id: str = None,
        trip_type: int = None,
    ):
        self.apply_id = apply_id
        self.book_type = book_type
        self.booker_info = booker_info
        self.corp_pay_price = corp_pay_price
        self.exceed_apply_id = exceed_apply_id
        self.flight_order_insure_list = flight_order_insure_list
        self.flight_order_ticket_list = flight_order_ticket_list
        self.flight_segment_list = flight_segment_list
        self.mix_pay = mix_pay
        self.order_create_time = order_create_time
        self.order_id = order_id
        self.order_pay_time = order_pay_time
        self.order_reserve_price = order_reserve_price
        self.order_status = order_status
        self.order_status_desc = order_status_desc
        self.order_type = order_type
        self.passenger_list = passenger_list
        self.pay_type = pay_type
        self.person_pay_price = person_pay_price
        self.service_fee = service_fee
        self.third_part_apply_id = third_part_apply_id
        self.trip_type = trip_type

    def validate(self):
        if self.booker_info:
            self.booker_info.validate()
        if self.flight_order_insure_list:
            for v1 in self.flight_order_insure_list:
                 if v1:
                    v1.validate()
        if self.flight_order_ticket_list:
            for v1 in self.flight_order_ticket_list:
                 if v1:
                    v1.validate()
        if self.flight_segment_list:
            for v1 in self.flight_segment_list:
                 if v1:
                    v1.validate()
        if self.passenger_list:
            for v1 in self.passenger_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_id is not None:
            result['apply_id'] = self.apply_id

        if self.book_type is not None:
            result['book_type'] = self.book_type

        if self.booker_info is not None:
            result['booker_info'] = self.booker_info.to_map()

        if self.corp_pay_price is not None:
            result['corp_pay_price'] = self.corp_pay_price

        if self.exceed_apply_id is not None:
            result['exceed_apply_id'] = self.exceed_apply_id

        result['flight_order_insure_list'] = []
        if self.flight_order_insure_list is not None:
            for k1 in self.flight_order_insure_list:
                result['flight_order_insure_list'].append(k1.to_map() if k1 else None)

        result['flight_order_ticket_list'] = []
        if self.flight_order_ticket_list is not None:
            for k1 in self.flight_order_ticket_list:
                result['flight_order_ticket_list'].append(k1.to_map() if k1 else None)

        result['flight_segment_list'] = []
        if self.flight_segment_list is not None:
            for k1 in self.flight_segment_list:
                result['flight_segment_list'].append(k1.to_map() if k1 else None)

        if self.mix_pay is not None:
            result['mix_pay'] = self.mix_pay

        if self.order_create_time is not None:
            result['order_create_time'] = self.order_create_time

        if self.order_id is not None:
            result['order_id'] = self.order_id

        if self.order_pay_time is not None:
            result['order_pay_time'] = self.order_pay_time

        if self.order_reserve_price is not None:
            result['order_reserve_price'] = self.order_reserve_price

        if self.order_status is not None:
            result['order_status'] = self.order_status

        if self.order_status_desc is not None:
            result['order_status_desc'] = self.order_status_desc

        if self.order_type is not None:
            result['order_type'] = self.order_type

        result['passenger_list'] = []
        if self.passenger_list is not None:
            for k1 in self.passenger_list:
                result['passenger_list'].append(k1.to_map() if k1 else None)

        if self.pay_type is not None:
            result['pay_type'] = self.pay_type

        if self.person_pay_price is not None:
            result['person_pay_price'] = self.person_pay_price

        if self.service_fee is not None:
            result['service_fee'] = self.service_fee

        if self.third_part_apply_id is not None:
            result['third_part_apply_id'] = self.third_part_apply_id

        if self.trip_type is not None:
            result['trip_type'] = self.trip_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apply_id') is not None:
            self.apply_id = m.get('apply_id')

        if m.get('book_type') is not None:
            self.book_type = m.get('book_type')

        if m.get('booker_info') is not None:
            temp_model = main_models.IFlightOrderListQueryResponseBodyModuleFlightSaleOrderBookerInfo()
            self.booker_info = temp_model.from_map(m.get('booker_info'))

        if m.get('corp_pay_price') is not None:
            self.corp_pay_price = m.get('corp_pay_price')

        if m.get('exceed_apply_id') is not None:
            self.exceed_apply_id = m.get('exceed_apply_id')

        self.flight_order_insure_list = []
        if m.get('flight_order_insure_list') is not None:
            for k1 in m.get('flight_order_insure_list'):
                temp_model = main_models.IFlightOrderListQueryResponseBodyModuleFlightSaleOrderFlightOrderInsureList()
                self.flight_order_insure_list.append(temp_model.from_map(k1))

        self.flight_order_ticket_list = []
        if m.get('flight_order_ticket_list') is not None:
            for k1 in m.get('flight_order_ticket_list'):
                temp_model = main_models.IFlightOrderListQueryResponseBodyModuleFlightSaleOrderFlightOrderTicketList()
                self.flight_order_ticket_list.append(temp_model.from_map(k1))

        self.flight_segment_list = []
        if m.get('flight_segment_list') is not None:
            for k1 in m.get('flight_segment_list'):
                temp_model = main_models.IFlightOrderListQueryResponseBodyModuleFlightSaleOrderFlightSegmentList()
                self.flight_segment_list.append(temp_model.from_map(k1))

        if m.get('mix_pay') is not None:
            self.mix_pay = m.get('mix_pay')

        if m.get('order_create_time') is not None:
            self.order_create_time = m.get('order_create_time')

        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')

        if m.get('order_pay_time') is not None:
            self.order_pay_time = m.get('order_pay_time')

        if m.get('order_reserve_price') is not None:
            self.order_reserve_price = m.get('order_reserve_price')

        if m.get('order_status') is not None:
            self.order_status = m.get('order_status')

        if m.get('order_status_desc') is not None:
            self.order_status_desc = m.get('order_status_desc')

        if m.get('order_type') is not None:
            self.order_type = m.get('order_type')

        self.passenger_list = []
        if m.get('passenger_list') is not None:
            for k1 in m.get('passenger_list'):
                temp_model = main_models.IFlightOrderListQueryResponseBodyModuleFlightSaleOrderPassengerList()
                self.passenger_list.append(temp_model.from_map(k1))

        if m.get('pay_type') is not None:
            self.pay_type = m.get('pay_type')

        if m.get('person_pay_price') is not None:
            self.person_pay_price = m.get('person_pay_price')

        if m.get('service_fee') is not None:
            self.service_fee = m.get('service_fee')

        if m.get('third_part_apply_id') is not None:
            self.third_part_apply_id = m.get('third_part_apply_id')

        if m.get('trip_type') is not None:
            self.trip_type = m.get('trip_type')

        return self

class IFlightOrderListQueryResponseBodyModuleFlightSaleOrderPassengerList(DaraModel):
    def __init__(
        self,
        cost_center_id: str = None,
        cost_center_name: str = None,
        department_id: str = None,
        department_name: str = None,
        invoice_id: str = None,
        invoice_title: str = None,
        job_no: str = None,
        passenger_type: int = None,
        project_code: str = None,
        project_title: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.cost_center_id = cost_center_id
        self.cost_center_name = cost_center_name
        self.department_id = department_id
        self.department_name = department_name
        self.invoice_id = invoice_id
        self.invoice_title = invoice_title
        self.job_no = job_no
        self.passenger_type = passenger_type
        self.project_code = project_code
        self.project_title = project_title
        self.user_id = user_id
        self.user_name = user_name

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

        if self.department_id is not None:
            result['department_id'] = self.department_id

        if self.department_name is not None:
            result['department_name'] = self.department_name

        if self.invoice_id is not None:
            result['invoice_id'] = self.invoice_id

        if self.invoice_title is not None:
            result['invoice_title'] = self.invoice_title

        if self.job_no is not None:
            result['job_no'] = self.job_no

        if self.passenger_type is not None:
            result['passenger_type'] = self.passenger_type

        if self.project_code is not None:
            result['project_code'] = self.project_code

        if self.project_title is not None:
            result['project_title'] = self.project_title

        if self.user_id is not None:
            result['user_id'] = self.user_id

        if self.user_name is not None:
            result['user_name'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost_center_id') is not None:
            self.cost_center_id = m.get('cost_center_id')

        if m.get('cost_center_name') is not None:
            self.cost_center_name = m.get('cost_center_name')

        if m.get('department_id') is not None:
            self.department_id = m.get('department_id')

        if m.get('department_name') is not None:
            self.department_name = m.get('department_name')

        if m.get('invoice_id') is not None:
            self.invoice_id = m.get('invoice_id')

        if m.get('invoice_title') is not None:
            self.invoice_title = m.get('invoice_title')

        if m.get('job_no') is not None:
            self.job_no = m.get('job_no')

        if m.get('passenger_type') is not None:
            self.passenger_type = m.get('passenger_type')

        if m.get('project_code') is not None:
            self.project_code = m.get('project_code')

        if m.get('project_title') is not None:
            self.project_title = m.get('project_title')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')

        return self

class IFlightOrderListQueryResponseBodyModuleFlightSaleOrderFlightSegmentList(DaraModel):
    def __init__(
        self,
        airline_code: str = None,
        airline_name: str = None,
        arr_apt: str = None,
        arr_apt_code: str = None,
        arr_city: str = None,
        arr_city_code: str = None,
        arr_terminal: str = None,
        arr_time: str = None,
        carrier_airline_code: str = None,
        carrier_airline_name: str = None,
        dep_apt: str = None,
        dep_apt_code: str = None,
        dep_city: str = None,
        dep_city_code: str = None,
        dep_terminal: str = None,
        dep_time: str = None,
        flight_no: str = None,
        journey_index: int = None,
        segment_index: int = None,
        share: bool = None,
        stop_apt_code: str = None,
        stop_arr_time: str = None,
        stop_city: str = None,
        stop_city_code: str = None,
        stop_dep_time: str = None,
    ):
        self.airline_code = airline_code
        self.airline_name = airline_name
        self.arr_apt = arr_apt
        self.arr_apt_code = arr_apt_code
        self.arr_city = arr_city
        self.arr_city_code = arr_city_code
        self.arr_terminal = arr_terminal
        self.arr_time = arr_time
        self.carrier_airline_code = carrier_airline_code
        self.carrier_airline_name = carrier_airline_name
        self.dep_apt = dep_apt
        self.dep_apt_code = dep_apt_code
        self.dep_city = dep_city
        self.dep_city_code = dep_city_code
        self.dep_terminal = dep_terminal
        self.dep_time = dep_time
        self.flight_no = flight_no
        self.journey_index = journey_index
        self.segment_index = segment_index
        self.share = share
        self.stop_apt_code = stop_apt_code
        self.stop_arr_time = stop_arr_time
        self.stop_city = stop_city
        self.stop_city_code = stop_city_code
        self.stop_dep_time = stop_dep_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.airline_code is not None:
            result['airline_code'] = self.airline_code

        if self.airline_name is not None:
            result['airline_name'] = self.airline_name

        if self.arr_apt is not None:
            result['arr_apt'] = self.arr_apt

        if self.arr_apt_code is not None:
            result['arr_apt_code'] = self.arr_apt_code

        if self.arr_city is not None:
            result['arr_city'] = self.arr_city

        if self.arr_city_code is not None:
            result['arr_city_code'] = self.arr_city_code

        if self.arr_terminal is not None:
            result['arr_terminal'] = self.arr_terminal

        if self.arr_time is not None:
            result['arr_time'] = self.arr_time

        if self.carrier_airline_code is not None:
            result['carrier_airline_code'] = self.carrier_airline_code

        if self.carrier_airline_name is not None:
            result['carrier_airline_name'] = self.carrier_airline_name

        if self.dep_apt is not None:
            result['dep_apt'] = self.dep_apt

        if self.dep_apt_code is not None:
            result['dep_apt_code'] = self.dep_apt_code

        if self.dep_city is not None:
            result['dep_city'] = self.dep_city

        if self.dep_city_code is not None:
            result['dep_city_code'] = self.dep_city_code

        if self.dep_terminal is not None:
            result['dep_terminal'] = self.dep_terminal

        if self.dep_time is not None:
            result['dep_time'] = self.dep_time

        if self.flight_no is not None:
            result['flight_no'] = self.flight_no

        if self.journey_index is not None:
            result['journey_index'] = self.journey_index

        if self.segment_index is not None:
            result['segment_index'] = self.segment_index

        if self.share is not None:
            result['share'] = self.share

        if self.stop_apt_code is not None:
            result['stop_apt_code'] = self.stop_apt_code

        if self.stop_arr_time is not None:
            result['stop_arr_time'] = self.stop_arr_time

        if self.stop_city is not None:
            result['stop_city'] = self.stop_city

        if self.stop_city_code is not None:
            result['stop_city_code'] = self.stop_city_code

        if self.stop_dep_time is not None:
            result['stop_dep_time'] = self.stop_dep_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('airline_code') is not None:
            self.airline_code = m.get('airline_code')

        if m.get('airline_name') is not None:
            self.airline_name = m.get('airline_name')

        if m.get('arr_apt') is not None:
            self.arr_apt = m.get('arr_apt')

        if m.get('arr_apt_code') is not None:
            self.arr_apt_code = m.get('arr_apt_code')

        if m.get('arr_city') is not None:
            self.arr_city = m.get('arr_city')

        if m.get('arr_city_code') is not None:
            self.arr_city_code = m.get('arr_city_code')

        if m.get('arr_terminal') is not None:
            self.arr_terminal = m.get('arr_terminal')

        if m.get('arr_time') is not None:
            self.arr_time = m.get('arr_time')

        if m.get('carrier_airline_code') is not None:
            self.carrier_airline_code = m.get('carrier_airline_code')

        if m.get('carrier_airline_name') is not None:
            self.carrier_airline_name = m.get('carrier_airline_name')

        if m.get('dep_apt') is not None:
            self.dep_apt = m.get('dep_apt')

        if m.get('dep_apt_code') is not None:
            self.dep_apt_code = m.get('dep_apt_code')

        if m.get('dep_city') is not None:
            self.dep_city = m.get('dep_city')

        if m.get('dep_city_code') is not None:
            self.dep_city_code = m.get('dep_city_code')

        if m.get('dep_terminal') is not None:
            self.dep_terminal = m.get('dep_terminal')

        if m.get('dep_time') is not None:
            self.dep_time = m.get('dep_time')

        if m.get('flight_no') is not None:
            self.flight_no = m.get('flight_no')

        if m.get('journey_index') is not None:
            self.journey_index = m.get('journey_index')

        if m.get('segment_index') is not None:
            self.segment_index = m.get('segment_index')

        if m.get('share') is not None:
            self.share = m.get('share')

        if m.get('stop_apt_code') is not None:
            self.stop_apt_code = m.get('stop_apt_code')

        if m.get('stop_arr_time') is not None:
            self.stop_arr_time = m.get('stop_arr_time')

        if m.get('stop_city') is not None:
            self.stop_city = m.get('stop_city')

        if m.get('stop_city_code') is not None:
            self.stop_city_code = m.get('stop_city_code')

        if m.get('stop_dep_time') is not None:
            self.stop_dep_time = m.get('stop_dep_time')

        return self

class IFlightOrderListQueryResponseBodyModuleFlightSaleOrderFlightOrderTicketList(DaraModel):
    def __init__(
        self,
        cabin_class: List[main_models.IFlightOrderListQueryResponseBodyModuleFlightSaleOrderFlightOrderTicketListCabinClass] = None,
        tax: int = None,
        ticket_no: str = None,
        ticket_price: int = None,
        user_id: str = None,
    ):
        self.cabin_class = cabin_class
        self.tax = tax
        self.ticket_no = ticket_no
        self.ticket_price = ticket_price
        self.user_id = user_id

    def validate(self):
        if self.cabin_class:
            for v1 in self.cabin_class:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['cabin_class'] = []
        if self.cabin_class is not None:
            for k1 in self.cabin_class:
                result['cabin_class'].append(k1.to_map() if k1 else None)

        if self.tax is not None:
            result['tax'] = self.tax

        if self.ticket_no is not None:
            result['ticket_no'] = self.ticket_no

        if self.ticket_price is not None:
            result['ticket_price'] = self.ticket_price

        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cabin_class = []
        if m.get('cabin_class') is not None:
            for k1 in m.get('cabin_class'):
                temp_model = main_models.IFlightOrderListQueryResponseBodyModuleFlightSaleOrderFlightOrderTicketListCabinClass()
                self.cabin_class.append(temp_model.from_map(k1))

        if m.get('tax') is not None:
            self.tax = m.get('tax')

        if m.get('ticket_no') is not None:
            self.ticket_no = m.get('ticket_no')

        if m.get('ticket_price') is not None:
            self.ticket_price = m.get('ticket_price')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

class IFlightOrderListQueryResponseBodyModuleFlightSaleOrderFlightOrderTicketListCabinClass(DaraModel):
    def __init__(
        self,
        cabin: str = None,
        cabin_class: str = None,
        flight_no: str = None,
    ):
        self.cabin = cabin
        self.cabin_class = cabin_class
        self.flight_no = flight_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cabin is not None:
            result['cabin'] = self.cabin

        if self.cabin_class is not None:
            result['cabin_class'] = self.cabin_class

        if self.flight_no is not None:
            result['flight_no'] = self.flight_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cabin') is not None:
            self.cabin = m.get('cabin')

        if m.get('cabin_class') is not None:
            self.cabin_class = m.get('cabin_class')

        if m.get('flight_no') is not None:
            self.flight_no = m.get('flight_no')

        return self

class IFlightOrderListQueryResponseBodyModuleFlightSaleOrderFlightOrderInsureList(DaraModel):
    def __init__(
        self,
        ins_order_id: str = None,
        ins_pay_type: str = None,
        ins_total_price: int = None,
        trade_action: str = None,
    ):
        self.ins_order_id = ins_order_id
        self.ins_pay_type = ins_pay_type
        self.ins_total_price = ins_total_price
        self.trade_action = trade_action

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ins_order_id is not None:
            result['ins_order_id'] = self.ins_order_id

        if self.ins_pay_type is not None:
            result['ins_pay_type'] = self.ins_pay_type

        if self.ins_total_price is not None:
            result['ins_total_price'] = self.ins_total_price

        if self.trade_action is not None:
            result['trade_action'] = self.trade_action

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ins_order_id') is not None:
            self.ins_order_id = m.get('ins_order_id')

        if m.get('ins_pay_type') is not None:
            self.ins_pay_type = m.get('ins_pay_type')

        if m.get('ins_total_price') is not None:
            self.ins_total_price = m.get('ins_total_price')

        if m.get('trade_action') is not None:
            self.trade_action = m.get('trade_action')

        return self

class IFlightOrderListQueryResponseBodyModuleFlightSaleOrderBookerInfo(DaraModel):
    def __init__(
        self,
        user_id: str = None,
        user_name: str = None,
    ):
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_id is not None:
            result['user_id'] = self.user_id

        if self.user_name is not None:
            result['user_name'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')

        return self

class IFlightOrderListQueryResponseBodyModuleFlightRefundOrderList(DaraModel):
    def __init__(
        self,
        corp_refund_amount: int = None,
        flight_order_refund_ticket_list: List[main_models.IFlightOrderListQueryResponseBodyModuleFlightRefundOrderListFlightOrderRefundTicketList] = None,
        flight_refund_segment_list: List[main_models.IFlightOrderListQueryResponseBodyModuleFlightRefundOrderListFlightRefundSegmentList] = None,
        passenger_fee: List[main_models.IFlightOrderListQueryResponseBodyModuleFlightRefundOrderListPassengerFee] = None,
        passenger_info: List[str] = None,
        person_refund_amount: int = None,
        refund_amount: int = None,
        refund_apply_id: int = None,
        refund_hand_fee: int = None,
        service_fee: int = None,
    ):
        self.corp_refund_amount = corp_refund_amount
        self.flight_order_refund_ticket_list = flight_order_refund_ticket_list
        self.flight_refund_segment_list = flight_refund_segment_list
        self.passenger_fee = passenger_fee
        self.passenger_info = passenger_info
        self.person_refund_amount = person_refund_amount
        self.refund_amount = refund_amount
        self.refund_apply_id = refund_apply_id
        self.refund_hand_fee = refund_hand_fee
        self.service_fee = service_fee

    def validate(self):
        if self.flight_order_refund_ticket_list:
            for v1 in self.flight_order_refund_ticket_list:
                 if v1:
                    v1.validate()
        if self.flight_refund_segment_list:
            for v1 in self.flight_refund_segment_list:
                 if v1:
                    v1.validate()
        if self.passenger_fee:
            for v1 in self.passenger_fee:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.corp_refund_amount is not None:
            result['corp_refund_Amount'] = self.corp_refund_amount

        result['flight_order_refund_ticket_list'] = []
        if self.flight_order_refund_ticket_list is not None:
            for k1 in self.flight_order_refund_ticket_list:
                result['flight_order_refund_ticket_list'].append(k1.to_map() if k1 else None)

        result['flight_refund_segment_list'] = []
        if self.flight_refund_segment_list is not None:
            for k1 in self.flight_refund_segment_list:
                result['flight_refund_segment_list'].append(k1.to_map() if k1 else None)

        result['passenger_fee'] = []
        if self.passenger_fee is not None:
            for k1 in self.passenger_fee:
                result['passenger_fee'].append(k1.to_map() if k1 else None)

        if self.passenger_info is not None:
            result['passenger_info'] = self.passenger_info

        if self.person_refund_amount is not None:
            result['person_refund_Amount'] = self.person_refund_amount

        if self.refund_amount is not None:
            result['refund_Amount'] = self.refund_amount

        if self.refund_apply_id is not None:
            result['refund_apply_id'] = self.refund_apply_id

        if self.refund_hand_fee is not None:
            result['refund_hand_fee'] = self.refund_hand_fee

        if self.service_fee is not None:
            result['service_fee'] = self.service_fee

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corp_refund_Amount') is not None:
            self.corp_refund_amount = m.get('corp_refund_Amount')

        self.flight_order_refund_ticket_list = []
        if m.get('flight_order_refund_ticket_list') is not None:
            for k1 in m.get('flight_order_refund_ticket_list'):
                temp_model = main_models.IFlightOrderListQueryResponseBodyModuleFlightRefundOrderListFlightOrderRefundTicketList()
                self.flight_order_refund_ticket_list.append(temp_model.from_map(k1))

        self.flight_refund_segment_list = []
        if m.get('flight_refund_segment_list') is not None:
            for k1 in m.get('flight_refund_segment_list'):
                temp_model = main_models.IFlightOrderListQueryResponseBodyModuleFlightRefundOrderListFlightRefundSegmentList()
                self.flight_refund_segment_list.append(temp_model.from_map(k1))

        self.passenger_fee = []
        if m.get('passenger_fee') is not None:
            for k1 in m.get('passenger_fee'):
                temp_model = main_models.IFlightOrderListQueryResponseBodyModuleFlightRefundOrderListPassengerFee()
                self.passenger_fee.append(temp_model.from_map(k1))

        if m.get('passenger_info') is not None:
            self.passenger_info = m.get('passenger_info')

        if m.get('person_refund_Amount') is not None:
            self.person_refund_amount = m.get('person_refund_Amount')

        if m.get('refund_Amount') is not None:
            self.refund_amount = m.get('refund_Amount')

        if m.get('refund_apply_id') is not None:
            self.refund_apply_id = m.get('refund_apply_id')

        if m.get('refund_hand_fee') is not None:
            self.refund_hand_fee = m.get('refund_hand_fee')

        if m.get('service_fee') is not None:
            self.service_fee = m.get('service_fee')

        return self

class IFlightOrderListQueryResponseBodyModuleFlightRefundOrderListPassengerFee(DaraModel):
    def __init__(
        self,
        no_refund_modify_hand_fee: int = None,
        no_refund_modify_upgrade_fee: int = None,
        refund_amount: int = None,
        refund_hand_fee: int = None,
        refund_modify_amount: int = None,
        refund_modify_hand_amount: int = None,
        refund_modify_upgrade_amount: int = None,
        refund_tax_hand_fee: int = None,
        user_id: str = None,
    ):
        self.no_refund_modify_hand_fee = no_refund_modify_hand_fee
        self.no_refund_modify_upgrade_fee = no_refund_modify_upgrade_fee
        self.refund_amount = refund_amount
        self.refund_hand_fee = refund_hand_fee
        self.refund_modify_amount = refund_modify_amount
        self.refund_modify_hand_amount = refund_modify_hand_amount
        self.refund_modify_upgrade_amount = refund_modify_upgrade_amount
        self.refund_tax_hand_fee = refund_tax_hand_fee
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.no_refund_modify_hand_fee is not None:
            result['no_refund_modify_hand_fee'] = self.no_refund_modify_hand_fee

        if self.no_refund_modify_upgrade_fee is not None:
            result['no_refund_modify_upgrade_fee'] = self.no_refund_modify_upgrade_fee

        if self.refund_amount is not None:
            result['refund_amount'] = self.refund_amount

        if self.refund_hand_fee is not None:
            result['refund_hand_fee'] = self.refund_hand_fee

        if self.refund_modify_amount is not None:
            result['refund_modify_amount'] = self.refund_modify_amount

        if self.refund_modify_hand_amount is not None:
            result['refund_modify_hand_amount'] = self.refund_modify_hand_amount

        if self.refund_modify_upgrade_amount is not None:
            result['refund_modify_upgrade_amount'] = self.refund_modify_upgrade_amount

        if self.refund_tax_hand_fee is not None:
            result['refund_tax_hand_fee'] = self.refund_tax_hand_fee

        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('no_refund_modify_hand_fee') is not None:
            self.no_refund_modify_hand_fee = m.get('no_refund_modify_hand_fee')

        if m.get('no_refund_modify_upgrade_fee') is not None:
            self.no_refund_modify_upgrade_fee = m.get('no_refund_modify_upgrade_fee')

        if m.get('refund_amount') is not None:
            self.refund_amount = m.get('refund_amount')

        if m.get('refund_hand_fee') is not None:
            self.refund_hand_fee = m.get('refund_hand_fee')

        if m.get('refund_modify_amount') is not None:
            self.refund_modify_amount = m.get('refund_modify_amount')

        if m.get('refund_modify_hand_amount') is not None:
            self.refund_modify_hand_amount = m.get('refund_modify_hand_amount')

        if m.get('refund_modify_upgrade_amount') is not None:
            self.refund_modify_upgrade_amount = m.get('refund_modify_upgrade_amount')

        if m.get('refund_tax_hand_fee') is not None:
            self.refund_tax_hand_fee = m.get('refund_tax_hand_fee')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

class IFlightOrderListQueryResponseBodyModuleFlightRefundOrderListFlightRefundSegmentList(DaraModel):
    def __init__(
        self,
        airline_code: str = None,
        airline_name: str = None,
        arr_apt: str = None,
        arr_apt_code: str = None,
        arr_city: str = None,
        arr_city_code: str = None,
        arr_terminal: str = None,
        arr_time: str = None,
        carrier_airline_code: str = None,
        carrier_airline_name: str = None,
        dep_apt: str = None,
        dep_apt_code: str = None,
        dep_city: str = None,
        dep_city_code: str = None,
        dep_terminal: str = None,
        dep_time: str = None,
        flight_no: str = None,
        journey_index: int = None,
        segment_index: int = None,
        share: bool = None,
        stop_apt_code: str = None,
        stop_arr_time: str = None,
        stop_city: str = None,
        stop_city_code: str = None,
        stop_dep_time: str = None,
    ):
        self.airline_code = airline_code
        self.airline_name = airline_name
        self.arr_apt = arr_apt
        self.arr_apt_code = arr_apt_code
        self.arr_city = arr_city
        self.arr_city_code = arr_city_code
        self.arr_terminal = arr_terminal
        self.arr_time = arr_time
        self.carrier_airline_code = carrier_airline_code
        self.carrier_airline_name = carrier_airline_name
        self.dep_apt = dep_apt
        self.dep_apt_code = dep_apt_code
        self.dep_city = dep_city
        self.dep_city_code = dep_city_code
        self.dep_terminal = dep_terminal
        self.dep_time = dep_time
        self.flight_no = flight_no
        self.journey_index = journey_index
        self.segment_index = segment_index
        self.share = share
        self.stop_apt_code = stop_apt_code
        self.stop_arr_time = stop_arr_time
        self.stop_city = stop_city
        self.stop_city_code = stop_city_code
        self.stop_dep_time = stop_dep_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.airline_code is not None:
            result['airline_code'] = self.airline_code

        if self.airline_name is not None:
            result['airline_name'] = self.airline_name

        if self.arr_apt is not None:
            result['arr_apt'] = self.arr_apt

        if self.arr_apt_code is not None:
            result['arr_apt_code'] = self.arr_apt_code

        if self.arr_city is not None:
            result['arr_city'] = self.arr_city

        if self.arr_city_code is not None:
            result['arr_city_code'] = self.arr_city_code

        if self.arr_terminal is not None:
            result['arr_terminal'] = self.arr_terminal

        if self.arr_time is not None:
            result['arr_time'] = self.arr_time

        if self.carrier_airline_code is not None:
            result['carrier_airline_code'] = self.carrier_airline_code

        if self.carrier_airline_name is not None:
            result['carrier_airline_name'] = self.carrier_airline_name

        if self.dep_apt is not None:
            result['dep_apt'] = self.dep_apt

        if self.dep_apt_code is not None:
            result['dep_apt_code'] = self.dep_apt_code

        if self.dep_city is not None:
            result['dep_city'] = self.dep_city

        if self.dep_city_code is not None:
            result['dep_city_code'] = self.dep_city_code

        if self.dep_terminal is not None:
            result['dep_terminal'] = self.dep_terminal

        if self.dep_time is not None:
            result['dep_time'] = self.dep_time

        if self.flight_no is not None:
            result['flight_no'] = self.flight_no

        if self.journey_index is not None:
            result['journey_index'] = self.journey_index

        if self.segment_index is not None:
            result['segment_index'] = self.segment_index

        if self.share is not None:
            result['share'] = self.share

        if self.stop_apt_code is not None:
            result['stop_apt_code'] = self.stop_apt_code

        if self.stop_arr_time is not None:
            result['stop_arr_time'] = self.stop_arr_time

        if self.stop_city is not None:
            result['stop_city'] = self.stop_city

        if self.stop_city_code is not None:
            result['stop_city_code'] = self.stop_city_code

        if self.stop_dep_time is not None:
            result['stop_dep_time'] = self.stop_dep_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('airline_code') is not None:
            self.airline_code = m.get('airline_code')

        if m.get('airline_name') is not None:
            self.airline_name = m.get('airline_name')

        if m.get('arr_apt') is not None:
            self.arr_apt = m.get('arr_apt')

        if m.get('arr_apt_code') is not None:
            self.arr_apt_code = m.get('arr_apt_code')

        if m.get('arr_city') is not None:
            self.arr_city = m.get('arr_city')

        if m.get('arr_city_code') is not None:
            self.arr_city_code = m.get('arr_city_code')

        if m.get('arr_terminal') is not None:
            self.arr_terminal = m.get('arr_terminal')

        if m.get('arr_time') is not None:
            self.arr_time = m.get('arr_time')

        if m.get('carrier_airline_code') is not None:
            self.carrier_airline_code = m.get('carrier_airline_code')

        if m.get('carrier_airline_name') is not None:
            self.carrier_airline_name = m.get('carrier_airline_name')

        if m.get('dep_apt') is not None:
            self.dep_apt = m.get('dep_apt')

        if m.get('dep_apt_code') is not None:
            self.dep_apt_code = m.get('dep_apt_code')

        if m.get('dep_city') is not None:
            self.dep_city = m.get('dep_city')

        if m.get('dep_city_code') is not None:
            self.dep_city_code = m.get('dep_city_code')

        if m.get('dep_terminal') is not None:
            self.dep_terminal = m.get('dep_terminal')

        if m.get('dep_time') is not None:
            self.dep_time = m.get('dep_time')

        if m.get('flight_no') is not None:
            self.flight_no = m.get('flight_no')

        if m.get('journey_index') is not None:
            self.journey_index = m.get('journey_index')

        if m.get('segment_index') is not None:
            self.segment_index = m.get('segment_index')

        if m.get('share') is not None:
            self.share = m.get('share')

        if m.get('stop_apt_code') is not None:
            self.stop_apt_code = m.get('stop_apt_code')

        if m.get('stop_arr_time') is not None:
            self.stop_arr_time = m.get('stop_arr_time')

        if m.get('stop_city') is not None:
            self.stop_city = m.get('stop_city')

        if m.get('stop_city_code') is not None:
            self.stop_city_code = m.get('stop_city_code')

        if m.get('stop_dep_time') is not None:
            self.stop_dep_time = m.get('stop_dep_time')

        return self

class IFlightOrderListQueryResponseBodyModuleFlightRefundOrderListFlightOrderRefundTicketList(DaraModel):
    def __init__(
        self,
        cabin_class: List[main_models.IFlightOrderListQueryResponseBodyModuleFlightRefundOrderListFlightOrderRefundTicketListCabinClass] = None,
        flight_no: str = None,
        ticket_no: str = None,
        user_id: str = None,
    ):
        self.cabin_class = cabin_class
        self.flight_no = flight_no
        self.ticket_no = ticket_no
        self.user_id = user_id

    def validate(self):
        if self.cabin_class:
            for v1 in self.cabin_class:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['cabin_class'] = []
        if self.cabin_class is not None:
            for k1 in self.cabin_class:
                result['cabin_class'].append(k1.to_map() if k1 else None)

        if self.flight_no is not None:
            result['flight_no'] = self.flight_no

        if self.ticket_no is not None:
            result['ticket_no'] = self.ticket_no

        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cabin_class = []
        if m.get('cabin_class') is not None:
            for k1 in m.get('cabin_class'):
                temp_model = main_models.IFlightOrderListQueryResponseBodyModuleFlightRefundOrderListFlightOrderRefundTicketListCabinClass()
                self.cabin_class.append(temp_model.from_map(k1))

        if m.get('flight_no') is not None:
            self.flight_no = m.get('flight_no')

        if m.get('ticket_no') is not None:
            self.ticket_no = m.get('ticket_no')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

class IFlightOrderListQueryResponseBodyModuleFlightRefundOrderListFlightOrderRefundTicketListCabinClass(DaraModel):
    def __init__(
        self,
        cabin: str = None,
        cabin_class: str = None,
        flight_no: str = None,
    ):
        self.cabin = cabin
        self.cabin_class = cabin_class
        self.flight_no = flight_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cabin is not None:
            result['cabin'] = self.cabin

        if self.cabin_class is not None:
            result['cabin_class'] = self.cabin_class

        if self.flight_no is not None:
            result['flight_no'] = self.flight_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cabin') is not None:
            self.cabin = m.get('cabin')

        if m.get('cabin_class') is not None:
            self.cabin_class = m.get('cabin_class')

        if m.get('flight_no') is not None:
            self.flight_no = m.get('flight_no')

        return self

class IFlightOrderListQueryResponseBodyModuleFlightModifyOrderList(DaraModel):
    def __init__(
        self,
        corp_pay_price: int = None,
        flight_modify_segment_list: List[main_models.IFlightOrderListQueryResponseBodyModuleFlightModifyOrderListFlightModifySegmentList] = None,
        flight_order_modify_ticket_list: List[main_models.IFlightOrderListQueryResponseBodyModuleFlightModifyOrderListFlightOrderModifyTicketList] = None,
        modify_apply_id: int = None,
        passenger_fee: List[main_models.IFlightOrderListQueryResponseBodyModuleFlightModifyOrderListPassengerFee] = None,
        passenger_list: List[str] = None,
        person_pay_price: int = None,
        relate_modify_apply_id: int = None,
        service_fee: int = None,
        total_fee: int = None,
    ):
        self.corp_pay_price = corp_pay_price
        self.flight_modify_segment_list = flight_modify_segment_list
        self.flight_order_modify_ticket_list = flight_order_modify_ticket_list
        self.modify_apply_id = modify_apply_id
        self.passenger_fee = passenger_fee
        self.passenger_list = passenger_list
        self.person_pay_price = person_pay_price
        self.relate_modify_apply_id = relate_modify_apply_id
        self.service_fee = service_fee
        self.total_fee = total_fee

    def validate(self):
        if self.flight_modify_segment_list:
            for v1 in self.flight_modify_segment_list:
                 if v1:
                    v1.validate()
        if self.flight_order_modify_ticket_list:
            for v1 in self.flight_order_modify_ticket_list:
                 if v1:
                    v1.validate()
        if self.passenger_fee:
            for v1 in self.passenger_fee:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.corp_pay_price is not None:
            result['corp_pay_price'] = self.corp_pay_price

        result['flight_modify_segment_list'] = []
        if self.flight_modify_segment_list is not None:
            for k1 in self.flight_modify_segment_list:
                result['flight_modify_segment_list'].append(k1.to_map() if k1 else None)

        result['flight_order_modify_ticket_list'] = []
        if self.flight_order_modify_ticket_list is not None:
            for k1 in self.flight_order_modify_ticket_list:
                result['flight_order_modify_ticket_list'].append(k1.to_map() if k1 else None)

        if self.modify_apply_id is not None:
            result['modify_apply_id'] = self.modify_apply_id

        result['passenger_fee'] = []
        if self.passenger_fee is not None:
            for k1 in self.passenger_fee:
                result['passenger_fee'].append(k1.to_map() if k1 else None)

        if self.passenger_list is not None:
            result['passenger_list'] = self.passenger_list

        if self.person_pay_price is not None:
            result['person_pay_price'] = self.person_pay_price

        if self.relate_modify_apply_id is not None:
            result['relate_modify_apply_id'] = self.relate_modify_apply_id

        if self.service_fee is not None:
            result['service_fee'] = self.service_fee

        if self.total_fee is not None:
            result['total_fee'] = self.total_fee

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corp_pay_price') is not None:
            self.corp_pay_price = m.get('corp_pay_price')

        self.flight_modify_segment_list = []
        if m.get('flight_modify_segment_list') is not None:
            for k1 in m.get('flight_modify_segment_list'):
                temp_model = main_models.IFlightOrderListQueryResponseBodyModuleFlightModifyOrderListFlightModifySegmentList()
                self.flight_modify_segment_list.append(temp_model.from_map(k1))

        self.flight_order_modify_ticket_list = []
        if m.get('flight_order_modify_ticket_list') is not None:
            for k1 in m.get('flight_order_modify_ticket_list'):
                temp_model = main_models.IFlightOrderListQueryResponseBodyModuleFlightModifyOrderListFlightOrderModifyTicketList()
                self.flight_order_modify_ticket_list.append(temp_model.from_map(k1))

        if m.get('modify_apply_id') is not None:
            self.modify_apply_id = m.get('modify_apply_id')

        self.passenger_fee = []
        if m.get('passenger_fee') is not None:
            for k1 in m.get('passenger_fee'):
                temp_model = main_models.IFlightOrderListQueryResponseBodyModuleFlightModifyOrderListPassengerFee()
                self.passenger_fee.append(temp_model.from_map(k1))

        if m.get('passenger_list') is not None:
            self.passenger_list = m.get('passenger_list')

        if m.get('person_pay_price') is not None:
            self.person_pay_price = m.get('person_pay_price')

        if m.get('relate_modify_apply_id') is not None:
            self.relate_modify_apply_id = m.get('relate_modify_apply_id')

        if m.get('service_fee') is not None:
            self.service_fee = m.get('service_fee')

        if m.get('total_fee') is not None:
            self.total_fee = m.get('total_fee')

        return self

class IFlightOrderListQueryResponseBodyModuleFlightModifyOrderListPassengerFee(DaraModel):
    def __init__(
        self,
        modify_hand_fee: int = None,
        modify_upgrade_fee: int = None,
        tax_gap: int = None,
        user_id: str = None,
    ):
        self.modify_hand_fee = modify_hand_fee
        self.modify_upgrade_fee = modify_upgrade_fee
        self.tax_gap = tax_gap
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.modify_hand_fee is not None:
            result['modify_hand_fee'] = self.modify_hand_fee

        if self.modify_upgrade_fee is not None:
            result['modify_upgrade_fee'] = self.modify_upgrade_fee

        if self.tax_gap is not None:
            result['tax_gap'] = self.tax_gap

        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modify_hand_fee') is not None:
            self.modify_hand_fee = m.get('modify_hand_fee')

        if m.get('modify_upgrade_fee') is not None:
            self.modify_upgrade_fee = m.get('modify_upgrade_fee')

        if m.get('tax_gap') is not None:
            self.tax_gap = m.get('tax_gap')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

class IFlightOrderListQueryResponseBodyModuleFlightModifyOrderListFlightOrderModifyTicketList(DaraModel):
    def __init__(
        self,
        cabin_class: List[main_models.IFlightOrderListQueryResponseBodyModuleFlightModifyOrderListFlightOrderModifyTicketListCabinClass] = None,
        flight_no: str = None,
        ticket_no: str = None,
        user_id: str = None,
    ):
        self.cabin_class = cabin_class
        self.flight_no = flight_no
        self.ticket_no = ticket_no
        self.user_id = user_id

    def validate(self):
        if self.cabin_class:
            for v1 in self.cabin_class:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['cabin_class'] = []
        if self.cabin_class is not None:
            for k1 in self.cabin_class:
                result['cabin_class'].append(k1.to_map() if k1 else None)

        if self.flight_no is not None:
            result['flight_no'] = self.flight_no

        if self.ticket_no is not None:
            result['ticket_no'] = self.ticket_no

        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cabin_class = []
        if m.get('cabin_class') is not None:
            for k1 in m.get('cabin_class'):
                temp_model = main_models.IFlightOrderListQueryResponseBodyModuleFlightModifyOrderListFlightOrderModifyTicketListCabinClass()
                self.cabin_class.append(temp_model.from_map(k1))

        if m.get('flight_no') is not None:
            self.flight_no = m.get('flight_no')

        if m.get('ticket_no') is not None:
            self.ticket_no = m.get('ticket_no')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

class IFlightOrderListQueryResponseBodyModuleFlightModifyOrderListFlightOrderModifyTicketListCabinClass(DaraModel):
    def __init__(
        self,
        cabin: str = None,
        cabin_class: str = None,
        flight_no: str = None,
    ):
        self.cabin = cabin
        self.cabin_class = cabin_class
        self.flight_no = flight_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cabin is not None:
            result['cabin'] = self.cabin

        if self.cabin_class is not None:
            result['cabin_class'] = self.cabin_class

        if self.flight_no is not None:
            result['flight_no'] = self.flight_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cabin') is not None:
            self.cabin = m.get('cabin')

        if m.get('cabin_class') is not None:
            self.cabin_class = m.get('cabin_class')

        if m.get('flight_no') is not None:
            self.flight_no = m.get('flight_no')

        return self

class IFlightOrderListQueryResponseBodyModuleFlightModifyOrderListFlightModifySegmentList(DaraModel):
    def __init__(
        self,
        airline_code: str = None,
        airline_name: str = None,
        arr_apt: str = None,
        arr_apt_code: str = None,
        arr_city: str = None,
        arr_city_code: str = None,
        arr_terminal: str = None,
        arr_time: str = None,
        carrier_airline_code: str = None,
        carrier_airline_name: str = None,
        dep_apt: str = None,
        dep_apt_code: str = None,
        dep_city: str = None,
        dep_city_code: str = None,
        dep_terminal: str = None,
        dep_time: str = None,
        flight_no: str = None,
        journey_index: int = None,
        segment_index: int = None,
        share: bool = None,
        stop_apt_code: str = None,
        stop_arr_time: str = None,
        stop_city: str = None,
        stop_city_code: str = None,
        stop_dep_time: str = None,
    ):
        self.airline_code = airline_code
        self.airline_name = airline_name
        self.arr_apt = arr_apt
        self.arr_apt_code = arr_apt_code
        self.arr_city = arr_city
        self.arr_city_code = arr_city_code
        self.arr_terminal = arr_terminal
        self.arr_time = arr_time
        self.carrier_airline_code = carrier_airline_code
        self.carrier_airline_name = carrier_airline_name
        self.dep_apt = dep_apt
        self.dep_apt_code = dep_apt_code
        self.dep_city = dep_city
        self.dep_city_code = dep_city_code
        self.dep_terminal = dep_terminal
        self.dep_time = dep_time
        self.flight_no = flight_no
        self.journey_index = journey_index
        self.segment_index = segment_index
        self.share = share
        self.stop_apt_code = stop_apt_code
        self.stop_arr_time = stop_arr_time
        self.stop_city = stop_city
        self.stop_city_code = stop_city_code
        self.stop_dep_time = stop_dep_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.airline_code is not None:
            result['airline_code'] = self.airline_code

        if self.airline_name is not None:
            result['airline_name'] = self.airline_name

        if self.arr_apt is not None:
            result['arr_apt'] = self.arr_apt

        if self.arr_apt_code is not None:
            result['arr_apt_code'] = self.arr_apt_code

        if self.arr_city is not None:
            result['arr_city'] = self.arr_city

        if self.arr_city_code is not None:
            result['arr_city_code'] = self.arr_city_code

        if self.arr_terminal is not None:
            result['arr_terminal'] = self.arr_terminal

        if self.arr_time is not None:
            result['arr_time'] = self.arr_time

        if self.carrier_airline_code is not None:
            result['carrier_airline_code'] = self.carrier_airline_code

        if self.carrier_airline_name is not None:
            result['carrier_airline_name'] = self.carrier_airline_name

        if self.dep_apt is not None:
            result['dep_apt'] = self.dep_apt

        if self.dep_apt_code is not None:
            result['dep_apt_code'] = self.dep_apt_code

        if self.dep_city is not None:
            result['dep_city'] = self.dep_city

        if self.dep_city_code is not None:
            result['dep_city_code'] = self.dep_city_code

        if self.dep_terminal is not None:
            result['dep_terminal'] = self.dep_terminal

        if self.dep_time is not None:
            result['dep_time'] = self.dep_time

        if self.flight_no is not None:
            result['flight_no'] = self.flight_no

        if self.journey_index is not None:
            result['journey_index'] = self.journey_index

        if self.segment_index is not None:
            result['segment_index'] = self.segment_index

        if self.share is not None:
            result['share'] = self.share

        if self.stop_apt_code is not None:
            result['stop_apt_code'] = self.stop_apt_code

        if self.stop_arr_time is not None:
            result['stop_arr_time'] = self.stop_arr_time

        if self.stop_city is not None:
            result['stop_city'] = self.stop_city

        if self.stop_city_code is not None:
            result['stop_city_code'] = self.stop_city_code

        if self.stop_dep_time is not None:
            result['stop_dep_time'] = self.stop_dep_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('airline_code') is not None:
            self.airline_code = m.get('airline_code')

        if m.get('airline_name') is not None:
            self.airline_name = m.get('airline_name')

        if m.get('arr_apt') is not None:
            self.arr_apt = m.get('arr_apt')

        if m.get('arr_apt_code') is not None:
            self.arr_apt_code = m.get('arr_apt_code')

        if m.get('arr_city') is not None:
            self.arr_city = m.get('arr_city')

        if m.get('arr_city_code') is not None:
            self.arr_city_code = m.get('arr_city_code')

        if m.get('arr_terminal') is not None:
            self.arr_terminal = m.get('arr_terminal')

        if m.get('arr_time') is not None:
            self.arr_time = m.get('arr_time')

        if m.get('carrier_airline_code') is not None:
            self.carrier_airline_code = m.get('carrier_airline_code')

        if m.get('carrier_airline_name') is not None:
            self.carrier_airline_name = m.get('carrier_airline_name')

        if m.get('dep_apt') is not None:
            self.dep_apt = m.get('dep_apt')

        if m.get('dep_apt_code') is not None:
            self.dep_apt_code = m.get('dep_apt_code')

        if m.get('dep_city') is not None:
            self.dep_city = m.get('dep_city')

        if m.get('dep_city_code') is not None:
            self.dep_city_code = m.get('dep_city_code')

        if m.get('dep_terminal') is not None:
            self.dep_terminal = m.get('dep_terminal')

        if m.get('dep_time') is not None:
            self.dep_time = m.get('dep_time')

        if m.get('flight_no') is not None:
            self.flight_no = m.get('flight_no')

        if m.get('journey_index') is not None:
            self.journey_index = m.get('journey_index')

        if m.get('segment_index') is not None:
            self.segment_index = m.get('segment_index')

        if m.get('share') is not None:
            self.share = m.get('share')

        if m.get('stop_apt_code') is not None:
            self.stop_apt_code = m.get('stop_apt_code')

        if m.get('stop_arr_time') is not None:
            self.stop_arr_time = m.get('stop_arr_time')

        if m.get('stop_city') is not None:
            self.stop_city = m.get('stop_city')

        if m.get('stop_city_code') is not None:
            self.stop_city_code = m.get('stop_city_code')

        if m.get('stop_dep_time') is not None:
            self.stop_dep_time = m.get('stop_dep_time')

        return self

