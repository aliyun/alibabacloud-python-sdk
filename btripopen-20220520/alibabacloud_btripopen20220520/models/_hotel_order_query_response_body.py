# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class HotelOrderQueryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.HotelOrderQueryResponseBodyModule = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.message = message
        # module。
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
            temp_model = main_models.HotelOrderQueryResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class HotelOrderQueryResponseBodyModule(DaraModel):
    def __init__(
        self,
        hotel_info: main_models.HotelOrderQueryResponseBodyModuleHotelInfo = None,
        invoice_info: main_models.HotelOrderQueryResponseBodyModuleInvoiceInfo = None,
        order_base_info: main_models.HotelOrderQueryResponseBodyModuleOrderBaseInfo = None,
        passenger_list: List[main_models.HotelOrderQueryResponseBodyModulePassengerList] = None,
        price_info_list: List[main_models.HotelOrderQueryResponseBodyModulePriceInfoList] = None,
    ):
        self.hotel_info = hotel_info
        self.invoice_info = invoice_info
        self.order_base_info = order_base_info
        self.passenger_list = passenger_list
        self.price_info_list = price_info_list

    def validate(self):
        if self.hotel_info:
            self.hotel_info.validate()
        if self.invoice_info:
            self.invoice_info.validate()
        if self.order_base_info:
            self.order_base_info.validate()
        if self.passenger_list:
            for v1 in self.passenger_list:
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
        if self.hotel_info is not None:
            result['hotel_info'] = self.hotel_info.to_map()

        if self.invoice_info is not None:
            result['invoice_info'] = self.invoice_info.to_map()

        if self.order_base_info is not None:
            result['order_base_info'] = self.order_base_info.to_map()

        result['passenger_list'] = []
        if self.passenger_list is not None:
            for k1 in self.passenger_list:
                result['passenger_list'].append(k1.to_map() if k1 else None)

        result['price_info_list'] = []
        if self.price_info_list is not None:
            for k1 in self.price_info_list:
                result['price_info_list'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hotel_info') is not None:
            temp_model = main_models.HotelOrderQueryResponseBodyModuleHotelInfo()
            self.hotel_info = temp_model.from_map(m.get('hotel_info'))

        if m.get('invoice_info') is not None:
            temp_model = main_models.HotelOrderQueryResponseBodyModuleInvoiceInfo()
            self.invoice_info = temp_model.from_map(m.get('invoice_info'))

        if m.get('order_base_info') is not None:
            temp_model = main_models.HotelOrderQueryResponseBodyModuleOrderBaseInfo()
            self.order_base_info = temp_model.from_map(m.get('order_base_info'))

        self.passenger_list = []
        if m.get('passenger_list') is not None:
            for k1 in m.get('passenger_list'):
                temp_model = main_models.HotelOrderQueryResponseBodyModulePassengerList()
                self.passenger_list.append(temp_model.from_map(k1))

        self.price_info_list = []
        if m.get('price_info_list') is not None:
            for k1 in m.get('price_info_list'):
                temp_model = main_models.HotelOrderQueryResponseBodyModulePriceInfoList()
                self.price_info_list.append(temp_model.from_map(k1))

        return self

class HotelOrderQueryResponseBodyModulePriceInfoList(DaraModel):
    def __init__(
        self,
        category_code: int = None,
        gmt_create: int = None,
        pay_type: int = None,
        price: float = None,
        trade_id: str = None,
        type: int = None,
    ):
        self.category_code = category_code
        self.gmt_create = gmt_create
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

        if m.get('pay_type') is not None:
            self.pay_type = m.get('pay_type')

        if m.get('price') is not None:
            self.price = m.get('price')

        if m.get('trade_id') is not None:
            self.trade_id = m.get('trade_id')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class HotelOrderQueryResponseBodyModulePassengerList(DaraModel):
    def __init__(
        self,
        apply_id: str = None,
        cost_center_id: int = None,
        cost_center_name: str = None,
        cost_center_number: str = None,
        itinerary_id: str = None,
        occupant_type: int = None,
        project_code: str = None,
        project_id: int = None,
        project_title: str = None,
        thirdpart_apply_id: str = None,
        thirdpart_cost_center_id: str = None,
        thirdpart_project_id: str = None,
        user_id: str = None,
        user_name: str = None,
        user_type: int = None,
    ):
        self.apply_id = apply_id
        self.cost_center_id = cost_center_id
        self.cost_center_name = cost_center_name
        self.cost_center_number = cost_center_number
        self.itinerary_id = itinerary_id
        self.occupant_type = occupant_type
        self.project_code = project_code
        self.project_id = project_id
        self.project_title = project_title
        self.thirdpart_apply_id = thirdpart_apply_id
        self.thirdpart_cost_center_id = thirdpart_cost_center_id
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
        if self.apply_id is not None:
            result['apply_id'] = self.apply_id

        if self.cost_center_id is not None:
            result['cost_center_id'] = self.cost_center_id

        if self.cost_center_name is not None:
            result['cost_center_name'] = self.cost_center_name

        if self.cost_center_number is not None:
            result['cost_center_number'] = self.cost_center_number

        if self.itinerary_id is not None:
            result['itinerary_id'] = self.itinerary_id

        if self.occupant_type is not None:
            result['occupant_type'] = self.occupant_type

        if self.project_code is not None:
            result['project_code'] = self.project_code

        if self.project_id is not None:
            result['project_id'] = self.project_id

        if self.project_title is not None:
            result['project_title'] = self.project_title

        if self.thirdpart_apply_id is not None:
            result['thirdpart_apply_id'] = self.thirdpart_apply_id

        if self.thirdpart_cost_center_id is not None:
            result['thirdpart_cost_center_id'] = self.thirdpart_cost_center_id

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
        if m.get('apply_id') is not None:
            self.apply_id = m.get('apply_id')

        if m.get('cost_center_id') is not None:
            self.cost_center_id = m.get('cost_center_id')

        if m.get('cost_center_name') is not None:
            self.cost_center_name = m.get('cost_center_name')

        if m.get('cost_center_number') is not None:
            self.cost_center_number = m.get('cost_center_number')

        if m.get('itinerary_id') is not None:
            self.itinerary_id = m.get('itinerary_id')

        if m.get('occupant_type') is not None:
            self.occupant_type = m.get('occupant_type')

        if m.get('project_code') is not None:
            self.project_code = m.get('project_code')

        if m.get('project_id') is not None:
            self.project_id = m.get('project_id')

        if m.get('project_title') is not None:
            self.project_title = m.get('project_title')

        if m.get('thirdpart_apply_id') is not None:
            self.thirdpart_apply_id = m.get('thirdpart_apply_id')

        if m.get('thirdpart_cost_center_id') is not None:
            self.thirdpart_cost_center_id = m.get('thirdpart_cost_center_id')

        if m.get('thirdpart_project_id') is not None:
            self.thirdpart_project_id = m.get('thirdpart_project_id')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')

        if m.get('user_type') is not None:
            self.user_type = m.get('user_type')

        return self

class HotelOrderQueryResponseBodyModuleOrderBaseInfo(DaraModel):
    def __init__(
        self,
        apply_id: str = None,
        btrip_title: str = None,
        category: int = None,
        corp_id: str = None,
        corp_name: str = None,
        depart_id: str = None,
        depart_name: str = None,
        exceed_apply_nos: List[str] = None,
        extend_field: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        id: int = None,
        itinerary_id: str = None,
        order_status: int = None,
        order_type: int = None,
        supplier: str = None,
        thirdpart_apply_id: str = None,
        thirdpart_business_id: str = None,
        thirdpart_depart_id: str = None,
        thirdpart_itinerary_id: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.apply_id = apply_id
        self.btrip_title = btrip_title
        self.category = category
        self.corp_id = corp_id
        self.corp_name = corp_name
        self.depart_id = depart_id
        self.depart_name = depart_name
        self.exceed_apply_nos = exceed_apply_nos
        self.extend_field = extend_field
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.itinerary_id = itinerary_id
        self.order_status = order_status
        self.order_type = order_type
        self.supplier = supplier
        self.thirdpart_apply_id = thirdpart_apply_id
        self.thirdpart_business_id = thirdpart_business_id
        self.thirdpart_depart_id = thirdpart_depart_id
        self.thirdpart_itinerary_id = thirdpart_itinerary_id
        self.user_id = user_id
        self.user_name = user_name

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

        if self.category is not None:
            result['category'] = self.category

        if self.corp_id is not None:
            result['corp_id'] = self.corp_id

        if self.corp_name is not None:
            result['corp_name'] = self.corp_name

        if self.depart_id is not None:
            result['depart_id'] = self.depart_id

        if self.depart_name is not None:
            result['depart_name'] = self.depart_name

        if self.exceed_apply_nos is not None:
            result['exceed_apply_nos'] = self.exceed_apply_nos

        if self.extend_field is not None:
            result['extend_field'] = self.extend_field

        if self.gmt_create is not None:
            result['gmt_create'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmt_modified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.itinerary_id is not None:
            result['itinerary_id'] = self.itinerary_id

        if self.order_status is not None:
            result['order_status'] = self.order_status

        if self.order_type is not None:
            result['order_type'] = self.order_type

        if self.supplier is not None:
            result['supplier'] = self.supplier

        if self.thirdpart_apply_id is not None:
            result['thirdpart_apply_id'] = self.thirdpart_apply_id

        if self.thirdpart_business_id is not None:
            result['thirdpart_business_id'] = self.thirdpart_business_id

        if self.thirdpart_depart_id is not None:
            result['thirdpart_depart_id'] = self.thirdpart_depart_id

        if self.thirdpart_itinerary_id is not None:
            result['thirdpart_itinerary_id'] = self.thirdpart_itinerary_id

        if self.user_id is not None:
            result['user_id'] = self.user_id

        if self.user_name is not None:
            result['user_name'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apply_id') is not None:
            self.apply_id = m.get('apply_id')

        if m.get('btrip_title') is not None:
            self.btrip_title = m.get('btrip_title')

        if m.get('category') is not None:
            self.category = m.get('category')

        if m.get('corp_id') is not None:
            self.corp_id = m.get('corp_id')

        if m.get('corp_name') is not None:
            self.corp_name = m.get('corp_name')

        if m.get('depart_id') is not None:
            self.depart_id = m.get('depart_id')

        if m.get('depart_name') is not None:
            self.depart_name = m.get('depart_name')

        if m.get('exceed_apply_nos') is not None:
            self.exceed_apply_nos = m.get('exceed_apply_nos')

        if m.get('extend_field') is not None:
            self.extend_field = m.get('extend_field')

        if m.get('gmt_create') is not None:
            self.gmt_create = m.get('gmt_create')

        if m.get('gmt_modified') is not None:
            self.gmt_modified = m.get('gmt_modified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('itinerary_id') is not None:
            self.itinerary_id = m.get('itinerary_id')

        if m.get('order_status') is not None:
            self.order_status = m.get('order_status')

        if m.get('order_type') is not None:
            self.order_type = m.get('order_type')

        if m.get('supplier') is not None:
            self.supplier = m.get('supplier')

        if m.get('thirdpart_apply_id') is not None:
            self.thirdpart_apply_id = m.get('thirdpart_apply_id')

        if m.get('thirdpart_business_id') is not None:
            self.thirdpart_business_id = m.get('thirdpart_business_id')

        if m.get('thirdpart_depart_id') is not None:
            self.thirdpart_depart_id = m.get('thirdpart_depart_id')

        if m.get('thirdpart_itinerary_id') is not None:
            self.thirdpart_itinerary_id = m.get('thirdpart_itinerary_id')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')

        return self

class HotelOrderQueryResponseBodyModuleInvoiceInfo(DaraModel):
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

class HotelOrderQueryResponseBodyModuleHotelInfo(DaraModel):
    def __init__(
        self,
        brand_code: str = None,
        brand_group: str = None,
        brand_name: str = None,
        check_in: int = None,
        check_out: int = None,
        city: str = None,
        city_ad_code: str = None,
        country_code: str = None,
        country_name: str = None,
        hotel_address: str = None,
        hotel_name: str = None,
        hotel_phone: str = None,
        hotel_support_vat_invoice_type: int = None,
        night: int = None,
        room_num: int = None,
        room_type: str = None,
        star: str = None,
    ):
        self.brand_code = brand_code
        self.brand_group = brand_group
        self.brand_name = brand_name
        self.check_in = check_in
        self.check_out = check_out
        self.city = city
        self.city_ad_code = city_ad_code
        self.country_code = country_code
        self.country_name = country_name
        self.hotel_address = hotel_address
        self.hotel_name = hotel_name
        self.hotel_phone = hotel_phone
        self.hotel_support_vat_invoice_type = hotel_support_vat_invoice_type
        self.night = night
        self.room_num = room_num
        self.room_type = room_type
        self.star = star

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.brand_code is not None:
            result['brand_code'] = self.brand_code

        if self.brand_group is not None:
            result['brand_group'] = self.brand_group

        if self.brand_name is not None:
            result['brand_name'] = self.brand_name

        if self.check_in is not None:
            result['check_in'] = self.check_in

        if self.check_out is not None:
            result['check_out'] = self.check_out

        if self.city is not None:
            result['city'] = self.city

        if self.city_ad_code is not None:
            result['city_ad_code'] = self.city_ad_code

        if self.country_code is not None:
            result['country_code'] = self.country_code

        if self.country_name is not None:
            result['country_name'] = self.country_name

        if self.hotel_address is not None:
            result['hotel_address'] = self.hotel_address

        if self.hotel_name is not None:
            result['hotel_name'] = self.hotel_name

        if self.hotel_phone is not None:
            result['hotel_phone'] = self.hotel_phone

        if self.hotel_support_vat_invoice_type is not None:
            result['hotel_support_vat_invoice_type'] = self.hotel_support_vat_invoice_type

        if self.night is not None:
            result['night'] = self.night

        if self.room_num is not None:
            result['room_num'] = self.room_num

        if self.room_type is not None:
            result['room_type'] = self.room_type

        if self.star is not None:
            result['star'] = self.star

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('brand_code') is not None:
            self.brand_code = m.get('brand_code')

        if m.get('brand_group') is not None:
            self.brand_group = m.get('brand_group')

        if m.get('brand_name') is not None:
            self.brand_name = m.get('brand_name')

        if m.get('check_in') is not None:
            self.check_in = m.get('check_in')

        if m.get('check_out') is not None:
            self.check_out = m.get('check_out')

        if m.get('city') is not None:
            self.city = m.get('city')

        if m.get('city_ad_code') is not None:
            self.city_ad_code = m.get('city_ad_code')

        if m.get('country_code') is not None:
            self.country_code = m.get('country_code')

        if m.get('country_name') is not None:
            self.country_name = m.get('country_name')

        if m.get('hotel_address') is not None:
            self.hotel_address = m.get('hotel_address')

        if m.get('hotel_name') is not None:
            self.hotel_name = m.get('hotel_name')

        if m.get('hotel_phone') is not None:
            self.hotel_phone = m.get('hotel_phone')

        if m.get('hotel_support_vat_invoice_type') is not None:
            self.hotel_support_vat_invoice_type = m.get('hotel_support_vat_invoice_type')

        if m.get('night') is not None:
            self.night = m.get('night')

        if m.get('room_num') is not None:
            self.room_num = m.get('room_num')

        if m.get('room_type') is not None:
            self.room_type = m.get('room_type')

        if m.get('star') is not None:
            self.star = m.get('star')

        return self

