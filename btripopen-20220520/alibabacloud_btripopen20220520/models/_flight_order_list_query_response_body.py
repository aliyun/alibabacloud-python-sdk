# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class FlightOrderListQueryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: List[main_models.FlightOrderListQueryResponseBodyModule] = None,
        page_info: main_models.FlightOrderListQueryResponseBodyPageInfo = None,
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
            result['page_info'] = self.page_info.to_map()

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
                temp_model = main_models.FlightOrderListQueryResponseBodyModule()
                self.module.append(temp_model.from_map(k1))

        if m.get('page_info') is not None:
            temp_model = main_models.FlightOrderListQueryResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('page_info'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class FlightOrderListQueryResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        page: int = None,
        page_size: int = None,
        total_number: int = None,
    ):
        self.page = page
        self.page_size = page_size
        self.total_number = total_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['page_size'] = self.page_size

        if self.total_number is not None:
            result['total_number'] = self.total_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')

        if m.get('total_number') is not None:
            self.total_number = m.get('total_number')

        return self

class FlightOrderListQueryResponseBodyModule(DaraModel):
    def __init__(
        self,
        apply_id: int = None,
        arr_airport: str = None,
        arr_apt_prefecture_ad_code: str = None,
        arr_apt_prefecture_name: str = None,
        arr_city: str = None,
        arr_city_ad_code: str = None,
        btrip_title: str = None,
        cabin_class: str = None,
        contact_name: str = None,
        corp_id: str = None,
        corp_name: str = None,
        cost_center: main_models.FlightOrderListQueryResponseBodyModuleCostCenter = None,
        dep_airport: str = None,
        dep_apt_prefecture_ad_code: str = None,
        dep_apt_prefecture_name: str = None,
        dep_city: str = None,
        dep_city_ad_code: str = None,
        dep_date: str = None,
        depart_id: str = None,
        depart_name: str = None,
        discount: str = None,
        flight_no: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        insure_info_list: List[main_models.FlightOrderListQueryResponseBodyModuleInsureInfoList] = None,
        invoice: main_models.FlightOrderListQueryResponseBodyModuleInvoice = None,
        passenger_count: int = None,
        passenger_name: str = None,
        price_info_list: List[main_models.FlightOrderListQueryResponseBodyModulePriceInfoList] = None,
        project_code: str = None,
        project_id: int = None,
        project_title: str = None,
        ret_date: str = None,
        status: int = None,
        third_part_project_id: str = None,
        thirdpart_apply_id: str = None,
        thirdpart_business_id: str = None,
        thirdpart_itinerary_id: str = None,
        trip_type: int = None,
        user_affiliate_list: List[main_models.FlightOrderListQueryResponseBodyModuleUserAffiliateList] = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.apply_id = apply_id
        self.arr_airport = arr_airport
        self.arr_apt_prefecture_ad_code = arr_apt_prefecture_ad_code
        self.arr_apt_prefecture_name = arr_apt_prefecture_name
        self.arr_city = arr_city
        self.arr_city_ad_code = arr_city_ad_code
        self.btrip_title = btrip_title
        self.cabin_class = cabin_class
        self.contact_name = contact_name
        self.corp_id = corp_id
        self.corp_name = corp_name
        self.cost_center = cost_center
        self.dep_airport = dep_airport
        self.dep_apt_prefecture_ad_code = dep_apt_prefecture_ad_code
        self.dep_apt_prefecture_name = dep_apt_prefecture_name
        self.dep_city = dep_city
        self.dep_city_ad_code = dep_city_ad_code
        self.dep_date = dep_date
        self.depart_id = depart_id
        self.depart_name = depart_name
        self.discount = discount
        self.flight_no = flight_no
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.insure_info_list = insure_info_list
        self.invoice = invoice
        self.passenger_count = passenger_count
        self.passenger_name = passenger_name
        self.price_info_list = price_info_list
        self.project_code = project_code
        self.project_id = project_id
        self.project_title = project_title
        self.ret_date = ret_date
        self.status = status
        self.third_part_project_id = third_part_project_id
        self.thirdpart_apply_id = thirdpart_apply_id
        self.thirdpart_business_id = thirdpart_business_id
        self.thirdpart_itinerary_id = thirdpart_itinerary_id
        self.trip_type = trip_type
        self.user_affiliate_list = user_affiliate_list
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        if self.cost_center:
            self.cost_center.validate()
        if self.insure_info_list:
            for v1 in self.insure_info_list:
                 if v1:
                    v1.validate()
        if self.invoice:
            self.invoice.validate()
        if self.price_info_list:
            for v1 in self.price_info_list:
                 if v1:
                    v1.validate()
        if self.user_affiliate_list:
            for v1 in self.user_affiliate_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_id is not None:
            result['apply_id'] = self.apply_id

        if self.arr_airport is not None:
            result['arr_airport'] = self.arr_airport

        if self.arr_apt_prefecture_ad_code is not None:
            result['arr_apt_prefecture_ad_code'] = self.arr_apt_prefecture_ad_code

        if self.arr_apt_prefecture_name is not None:
            result['arr_apt_prefecture_name'] = self.arr_apt_prefecture_name

        if self.arr_city is not None:
            result['arr_city'] = self.arr_city

        if self.arr_city_ad_code is not None:
            result['arr_city_ad_code'] = self.arr_city_ad_code

        if self.btrip_title is not None:
            result['btrip_title'] = self.btrip_title

        if self.cabin_class is not None:
            result['cabin_class'] = self.cabin_class

        if self.contact_name is not None:
            result['contact_name'] = self.contact_name

        if self.corp_id is not None:
            result['corp_id'] = self.corp_id

        if self.corp_name is not None:
            result['corp_name'] = self.corp_name

        if self.cost_center is not None:
            result['cost_center'] = self.cost_center.to_map()

        if self.dep_airport is not None:
            result['dep_airport'] = self.dep_airport

        if self.dep_apt_prefecture_ad_code is not None:
            result['dep_apt_prefecture_ad_code'] = self.dep_apt_prefecture_ad_code

        if self.dep_apt_prefecture_name is not None:
            result['dep_apt_prefecture_name'] = self.dep_apt_prefecture_name

        if self.dep_city is not None:
            result['dep_city'] = self.dep_city

        if self.dep_city_ad_code is not None:
            result['dep_city_ad_code'] = self.dep_city_ad_code

        if self.dep_date is not None:
            result['dep_date'] = self.dep_date

        if self.depart_id is not None:
            result['depart_id'] = self.depart_id

        if self.depart_name is not None:
            result['depart_name'] = self.depart_name

        if self.discount is not None:
            result['discount'] = self.discount

        if self.flight_no is not None:
            result['flight_no'] = self.flight_no

        if self.gmt_create is not None:
            result['gmt_create'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmt_modified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        result['insure_info_list'] = []
        if self.insure_info_list is not None:
            for k1 in self.insure_info_list:
                result['insure_info_list'].append(k1.to_map() if k1 else None)

        if self.invoice is not None:
            result['invoice'] = self.invoice.to_map()

        if self.passenger_count is not None:
            result['passenger_count'] = self.passenger_count

        if self.passenger_name is not None:
            result['passenger_name'] = self.passenger_name

        result['price_info_list'] = []
        if self.price_info_list is not None:
            for k1 in self.price_info_list:
                result['price_info_list'].append(k1.to_map() if k1 else None)

        if self.project_code is not None:
            result['project_code'] = self.project_code

        if self.project_id is not None:
            result['project_id'] = self.project_id

        if self.project_title is not None:
            result['project_title'] = self.project_title

        if self.ret_date is not None:
            result['ret_date'] = self.ret_date

        if self.status is not None:
            result['status'] = self.status

        if self.third_part_project_id is not None:
            result['third_part_project_id'] = self.third_part_project_id

        if self.thirdpart_apply_id is not None:
            result['thirdpart_apply_id'] = self.thirdpart_apply_id

        if self.thirdpart_business_id is not None:
            result['thirdpart_business_id'] = self.thirdpart_business_id

        if self.thirdpart_itinerary_id is not None:
            result['thirdpart_itinerary_id'] = self.thirdpart_itinerary_id

        if self.trip_type is not None:
            result['trip_type'] = self.trip_type

        result['user_affiliate_list'] = []
        if self.user_affiliate_list is not None:
            for k1 in self.user_affiliate_list:
                result['user_affiliate_list'].append(k1.to_map() if k1 else None)

        if self.user_id is not None:
            result['user_id'] = self.user_id

        if self.user_name is not None:
            result['user_name'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apply_id') is not None:
            self.apply_id = m.get('apply_id')

        if m.get('arr_airport') is not None:
            self.arr_airport = m.get('arr_airport')

        if m.get('arr_apt_prefecture_ad_code') is not None:
            self.arr_apt_prefecture_ad_code = m.get('arr_apt_prefecture_ad_code')

        if m.get('arr_apt_prefecture_name') is not None:
            self.arr_apt_prefecture_name = m.get('arr_apt_prefecture_name')

        if m.get('arr_city') is not None:
            self.arr_city = m.get('arr_city')

        if m.get('arr_city_ad_code') is not None:
            self.arr_city_ad_code = m.get('arr_city_ad_code')

        if m.get('btrip_title') is not None:
            self.btrip_title = m.get('btrip_title')

        if m.get('cabin_class') is not None:
            self.cabin_class = m.get('cabin_class')

        if m.get('contact_name') is not None:
            self.contact_name = m.get('contact_name')

        if m.get('corp_id') is not None:
            self.corp_id = m.get('corp_id')

        if m.get('corp_name') is not None:
            self.corp_name = m.get('corp_name')

        if m.get('cost_center') is not None:
            temp_model = main_models.FlightOrderListQueryResponseBodyModuleCostCenter()
            self.cost_center = temp_model.from_map(m.get('cost_center'))

        if m.get('dep_airport') is not None:
            self.dep_airport = m.get('dep_airport')

        if m.get('dep_apt_prefecture_ad_code') is not None:
            self.dep_apt_prefecture_ad_code = m.get('dep_apt_prefecture_ad_code')

        if m.get('dep_apt_prefecture_name') is not None:
            self.dep_apt_prefecture_name = m.get('dep_apt_prefecture_name')

        if m.get('dep_city') is not None:
            self.dep_city = m.get('dep_city')

        if m.get('dep_city_ad_code') is not None:
            self.dep_city_ad_code = m.get('dep_city_ad_code')

        if m.get('dep_date') is not None:
            self.dep_date = m.get('dep_date')

        if m.get('depart_id') is not None:
            self.depart_id = m.get('depart_id')

        if m.get('depart_name') is not None:
            self.depart_name = m.get('depart_name')

        if m.get('discount') is not None:
            self.discount = m.get('discount')

        if m.get('flight_no') is not None:
            self.flight_no = m.get('flight_no')

        if m.get('gmt_create') is not None:
            self.gmt_create = m.get('gmt_create')

        if m.get('gmt_modified') is not None:
            self.gmt_modified = m.get('gmt_modified')

        if m.get('id') is not None:
            self.id = m.get('id')

        self.insure_info_list = []
        if m.get('insure_info_list') is not None:
            for k1 in m.get('insure_info_list'):
                temp_model = main_models.FlightOrderListQueryResponseBodyModuleInsureInfoList()
                self.insure_info_list.append(temp_model.from_map(k1))

        if m.get('invoice') is not None:
            temp_model = main_models.FlightOrderListQueryResponseBodyModuleInvoice()
            self.invoice = temp_model.from_map(m.get('invoice'))

        if m.get('passenger_count') is not None:
            self.passenger_count = m.get('passenger_count')

        if m.get('passenger_name') is not None:
            self.passenger_name = m.get('passenger_name')

        self.price_info_list = []
        if m.get('price_info_list') is not None:
            for k1 in m.get('price_info_list'):
                temp_model = main_models.FlightOrderListQueryResponseBodyModulePriceInfoList()
                self.price_info_list.append(temp_model.from_map(k1))

        if m.get('project_code') is not None:
            self.project_code = m.get('project_code')

        if m.get('project_id') is not None:
            self.project_id = m.get('project_id')

        if m.get('project_title') is not None:
            self.project_title = m.get('project_title')

        if m.get('ret_date') is not None:
            self.ret_date = m.get('ret_date')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('third_part_project_id') is not None:
            self.third_part_project_id = m.get('third_part_project_id')

        if m.get('thirdpart_apply_id') is not None:
            self.thirdpart_apply_id = m.get('thirdpart_apply_id')

        if m.get('thirdpart_business_id') is not None:
            self.thirdpart_business_id = m.get('thirdpart_business_id')

        if m.get('thirdpart_itinerary_id') is not None:
            self.thirdpart_itinerary_id = m.get('thirdpart_itinerary_id')

        if m.get('trip_type') is not None:
            self.trip_type = m.get('trip_type')

        self.user_affiliate_list = []
        if m.get('user_affiliate_list') is not None:
            for k1 in m.get('user_affiliate_list'):
                temp_model = main_models.FlightOrderListQueryResponseBodyModuleUserAffiliateList()
                self.user_affiliate_list.append(temp_model.from_map(k1))

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')

        return self

class FlightOrderListQueryResponseBodyModuleUserAffiliateList(DaraModel):
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

class FlightOrderListQueryResponseBodyModulePriceInfoList(DaraModel):
    def __init__(
        self,
        category_code: int = None,
        category_type: int = None,
        change_flight_no: str = None,
        discount: str = None,
        end_time: str = None,
        gmt_create: str = None,
        original_ticket_no: str = None,
        passenger_name: str = None,
        pay_type: int = None,
        price: float = None,
        start_time: str = None,
        ticket_no: str = None,
        trade_id: str = None,
        type: int = None,
    ):
        self.category_code = category_code
        self.category_type = category_type
        self.change_flight_no = change_flight_no
        self.discount = discount
        self.end_time = end_time
        self.gmt_create = gmt_create
        self.original_ticket_no = original_ticket_no
        self.passenger_name = passenger_name
        self.pay_type = pay_type
        self.price = price
        self.start_time = start_time
        self.ticket_no = ticket_no
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

        if self.category_type is not None:
            result['category_type'] = self.category_type

        if self.change_flight_no is not None:
            result['change_flight_no'] = self.change_flight_no

        if self.discount is not None:
            result['discount'] = self.discount

        if self.end_time is not None:
            result['end_time'] = self.end_time

        if self.gmt_create is not None:
            result['gmt_create'] = self.gmt_create

        if self.original_ticket_no is not None:
            result['original_ticket_no'] = self.original_ticket_no

        if self.passenger_name is not None:
            result['passenger_name'] = self.passenger_name

        if self.pay_type is not None:
            result['pay_type'] = self.pay_type

        if self.price is not None:
            result['price'] = self.price

        if self.start_time is not None:
            result['start_time'] = self.start_time

        if self.ticket_no is not None:
            result['ticket_no'] = self.ticket_no

        if self.trade_id is not None:
            result['trade_id'] = self.trade_id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category_code') is not None:
            self.category_code = m.get('category_code')

        if m.get('category_type') is not None:
            self.category_type = m.get('category_type')

        if m.get('change_flight_no') is not None:
            self.change_flight_no = m.get('change_flight_no')

        if m.get('discount') is not None:
            self.discount = m.get('discount')

        if m.get('end_time') is not None:
            self.end_time = m.get('end_time')

        if m.get('gmt_create') is not None:
            self.gmt_create = m.get('gmt_create')

        if m.get('original_ticket_no') is not None:
            self.original_ticket_no = m.get('original_ticket_no')

        if m.get('passenger_name') is not None:
            self.passenger_name = m.get('passenger_name')

        if m.get('pay_type') is not None:
            self.pay_type = m.get('pay_type')

        if m.get('price') is not None:
            self.price = m.get('price')

        if m.get('start_time') is not None:
            self.start_time = m.get('start_time')

        if m.get('ticket_no') is not None:
            self.ticket_no = m.get('ticket_no')

        if m.get('trade_id') is not None:
            self.trade_id = m.get('trade_id')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class FlightOrderListQueryResponseBodyModuleInvoice(DaraModel):
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

class FlightOrderListQueryResponseBodyModuleInsureInfoList(DaraModel):
    def __init__(
        self,
        insure_no: str = None,
        name: str = None,
        status: int = None,
    ):
        self.insure_no = insure_no
        self.name = name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.insure_no is not None:
            result['insure_no'] = self.insure_no

        if self.name is not None:
            result['name'] = self.name

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('insure_no') is not None:
            self.insure_no = m.get('insure_no')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

class FlightOrderListQueryResponseBodyModuleCostCenter(DaraModel):
    def __init__(
        self,
        corp_id: str = None,
        id: int = None,
        name: str = None,
        number: str = None,
    ):
        self.corp_id = corp_id
        self.id = id
        self.name = name
        self.number = number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.corp_id is not None:
            result['corp_id'] = self.corp_id

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.number is not None:
            result['number'] = self.number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corp_id') is not None:
            self.corp_id = m.get('corp_id')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('number') is not None:
            self.number = m.get('number')

        return self

