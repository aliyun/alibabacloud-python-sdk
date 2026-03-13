# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class HotelOrderListQueryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: List[main_models.HotelOrderListQueryResponseBodyModule] = None,
        page_info: main_models.HotelOrderListQueryResponseBodyPageInfo = None,
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
                temp_model = main_models.HotelOrderListQueryResponseBodyModule()
                self.module.append(temp_model.from_map(k1))

        if m.get('page_info') is not None:
            temp_model = main_models.HotelOrderListQueryResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('page_info'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class HotelOrderListQueryResponseBodyPageInfo(DaraModel):
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

class HotelOrderListQueryResponseBodyModule(DaraModel):
    def __init__(
        self,
        apply_id: int = None,
        btrip_title: str = None,
        category: int = None,
        check_in: str = None,
        check_out: str = None,
        city: str = None,
        city_ad_code: str = None,
        contact_name: str = None,
        corp_id: str = None,
        corp_name: str = None,
        cost_center: main_models.HotelOrderListQueryResponseBodyModuleCostCenter = None,
        country_code: str = None,
        country_name: str = None,
        depart_id: str = None,
        depart_name: str = None,
        extend_field: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        guest: str = None,
        hotel_name: str = None,
        hotel_support_vat_invoice_type: int = None,
        id: int = None,
        invoice: main_models.HotelOrderListQueryResponseBodyModuleInvoice = None,
        night: int = None,
        order_status: int = None,
        order_status_desc: str = None,
        order_type: int = None,
        order_type_desc: str = None,
        price_info_list: List[main_models.HotelOrderListQueryResponseBodyModulePriceInfoList] = None,
        project_code: str = None,
        project_id: int = None,
        project_title: str = None,
        room_num: int = None,
        room_type: str = None,
        supplier: str = None,
        thirdpart_apply_id: str = None,
        thirdpart_business_id: str = None,
        thirdpart_itinerary_id: str = None,
        thirdpart_project_id: str = None,
        user_affiliate_list: List[main_models.HotelOrderListQueryResponseBodyModuleUserAffiliateList] = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.apply_id = apply_id
        self.btrip_title = btrip_title
        self.category = category
        self.check_in = check_in
        self.check_out = check_out
        self.city = city
        self.city_ad_code = city_ad_code
        self.contact_name = contact_name
        self.corp_id = corp_id
        self.corp_name = corp_name
        self.cost_center = cost_center
        self.country_code = country_code
        self.country_name = country_name
        self.depart_id = depart_id
        self.depart_name = depart_name
        self.extend_field = extend_field
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.guest = guest
        self.hotel_name = hotel_name
        self.hotel_support_vat_invoice_type = hotel_support_vat_invoice_type
        self.id = id
        self.invoice = invoice
        self.night = night
        self.order_status = order_status
        self.order_status_desc = order_status_desc
        self.order_type = order_type
        self.order_type_desc = order_type_desc
        self.price_info_list = price_info_list
        self.project_code = project_code
        self.project_id = project_id
        self.project_title = project_title
        self.room_num = room_num
        self.room_type = room_type
        self.supplier = supplier
        self.thirdpart_apply_id = thirdpart_apply_id
        self.thirdpart_business_id = thirdpart_business_id
        self.thirdpart_itinerary_id = thirdpart_itinerary_id
        self.thirdpart_project_id = thirdpart_project_id
        self.user_affiliate_list = user_affiliate_list
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        if self.cost_center:
            self.cost_center.validate()
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

        if self.btrip_title is not None:
            result['btrip_title'] = self.btrip_title

        if self.category is not None:
            result['category'] = self.category

        if self.check_in is not None:
            result['check_in'] = self.check_in

        if self.check_out is not None:
            result['check_out'] = self.check_out

        if self.city is not None:
            result['city'] = self.city

        if self.city_ad_code is not None:
            result['city_ad_code'] = self.city_ad_code

        if self.contact_name is not None:
            result['contact_name'] = self.contact_name

        if self.corp_id is not None:
            result['corp_id'] = self.corp_id

        if self.corp_name is not None:
            result['corp_name'] = self.corp_name

        if self.cost_center is not None:
            result['cost_center'] = self.cost_center.to_map()

        if self.country_code is not None:
            result['country_code'] = self.country_code

        if self.country_name is not None:
            result['country_name'] = self.country_name

        if self.depart_id is not None:
            result['depart_id'] = self.depart_id

        if self.depart_name is not None:
            result['depart_name'] = self.depart_name

        if self.extend_field is not None:
            result['extend_field'] = self.extend_field

        if self.gmt_create is not None:
            result['gmt_create'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmt_modified'] = self.gmt_modified

        if self.guest is not None:
            result['guest'] = self.guest

        if self.hotel_name is not None:
            result['hotel_name'] = self.hotel_name

        if self.hotel_support_vat_invoice_type is not None:
            result['hotel_support_vat_invoice_type'] = self.hotel_support_vat_invoice_type

        if self.id is not None:
            result['id'] = self.id

        if self.invoice is not None:
            result['invoice'] = self.invoice.to_map()

        if self.night is not None:
            result['night'] = self.night

        if self.order_status is not None:
            result['order_status'] = self.order_status

        if self.order_status_desc is not None:
            result['order_status_desc'] = self.order_status_desc

        if self.order_type is not None:
            result['order_type'] = self.order_type

        if self.order_type_desc is not None:
            result['order_type_desc'] = self.order_type_desc

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

        if self.room_num is not None:
            result['room_num'] = self.room_num

        if self.room_type is not None:
            result['room_type'] = self.room_type

        if self.supplier is not None:
            result['supplier'] = self.supplier

        if self.thirdpart_apply_id is not None:
            result['thirdpart_apply_id'] = self.thirdpart_apply_id

        if self.thirdpart_business_id is not None:
            result['thirdpart_business_id'] = self.thirdpart_business_id

        if self.thirdpart_itinerary_id is not None:
            result['thirdpart_itinerary_id'] = self.thirdpart_itinerary_id

        if self.thirdpart_project_id is not None:
            result['thirdpart_project_id'] = self.thirdpart_project_id

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

        if m.get('btrip_title') is not None:
            self.btrip_title = m.get('btrip_title')

        if m.get('category') is not None:
            self.category = m.get('category')

        if m.get('check_in') is not None:
            self.check_in = m.get('check_in')

        if m.get('check_out') is not None:
            self.check_out = m.get('check_out')

        if m.get('city') is not None:
            self.city = m.get('city')

        if m.get('city_ad_code') is not None:
            self.city_ad_code = m.get('city_ad_code')

        if m.get('contact_name') is not None:
            self.contact_name = m.get('contact_name')

        if m.get('corp_id') is not None:
            self.corp_id = m.get('corp_id')

        if m.get('corp_name') is not None:
            self.corp_name = m.get('corp_name')

        if m.get('cost_center') is not None:
            temp_model = main_models.HotelOrderListQueryResponseBodyModuleCostCenter()
            self.cost_center = temp_model.from_map(m.get('cost_center'))

        if m.get('country_code') is not None:
            self.country_code = m.get('country_code')

        if m.get('country_name') is not None:
            self.country_name = m.get('country_name')

        if m.get('depart_id') is not None:
            self.depart_id = m.get('depart_id')

        if m.get('depart_name') is not None:
            self.depart_name = m.get('depart_name')

        if m.get('extend_field') is not None:
            self.extend_field = m.get('extend_field')

        if m.get('gmt_create') is not None:
            self.gmt_create = m.get('gmt_create')

        if m.get('gmt_modified') is not None:
            self.gmt_modified = m.get('gmt_modified')

        if m.get('guest') is not None:
            self.guest = m.get('guest')

        if m.get('hotel_name') is not None:
            self.hotel_name = m.get('hotel_name')

        if m.get('hotel_support_vat_invoice_type') is not None:
            self.hotel_support_vat_invoice_type = m.get('hotel_support_vat_invoice_type')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('invoice') is not None:
            temp_model = main_models.HotelOrderListQueryResponseBodyModuleInvoice()
            self.invoice = temp_model.from_map(m.get('invoice'))

        if m.get('night') is not None:
            self.night = m.get('night')

        if m.get('order_status') is not None:
            self.order_status = m.get('order_status')

        if m.get('order_status_desc') is not None:
            self.order_status_desc = m.get('order_status_desc')

        if m.get('order_type') is not None:
            self.order_type = m.get('order_type')

        if m.get('order_type_desc') is not None:
            self.order_type_desc = m.get('order_type_desc')

        self.price_info_list = []
        if m.get('price_info_list') is not None:
            for k1 in m.get('price_info_list'):
                temp_model = main_models.HotelOrderListQueryResponseBodyModulePriceInfoList()
                self.price_info_list.append(temp_model.from_map(k1))

        if m.get('project_code') is not None:
            self.project_code = m.get('project_code')

        if m.get('project_id') is not None:
            self.project_id = m.get('project_id')

        if m.get('project_title') is not None:
            self.project_title = m.get('project_title')

        if m.get('room_num') is not None:
            self.room_num = m.get('room_num')

        if m.get('room_type') is not None:
            self.room_type = m.get('room_type')

        if m.get('supplier') is not None:
            self.supplier = m.get('supplier')

        if m.get('thirdpart_apply_id') is not None:
            self.thirdpart_apply_id = m.get('thirdpart_apply_id')

        if m.get('thirdpart_business_id') is not None:
            self.thirdpart_business_id = m.get('thirdpart_business_id')

        if m.get('thirdpart_itinerary_id') is not None:
            self.thirdpart_itinerary_id = m.get('thirdpart_itinerary_id')

        if m.get('thirdpart_project_id') is not None:
            self.thirdpart_project_id = m.get('thirdpart_project_id')

        self.user_affiliate_list = []
        if m.get('user_affiliate_list') is not None:
            for k1 in m.get('user_affiliate_list'):
                temp_model = main_models.HotelOrderListQueryResponseBodyModuleUserAffiliateList()
                self.user_affiliate_list.append(temp_model.from_map(k1))

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')

        return self

class HotelOrderListQueryResponseBodyModuleUserAffiliateList(DaraModel):
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

class HotelOrderListQueryResponseBodyModulePriceInfoList(DaraModel):
    def __init__(
        self,
        category: str = None,
        category_code: int = None,
        category_type: int = None,
        gmt_create: str = None,
        passenger_name: str = None,
        pay_type: int = None,
        price: float = None,
        trade_id: str = None,
        type: int = None,
    ):
        self.category = category
        self.category_code = category_code
        self.category_type = category_type
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
        if self.category is not None:
            result['category'] = self.category

        if self.category_code is not None:
            result['category_code'] = self.category_code

        if self.category_type is not None:
            result['category_type'] = self.category_type

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
        if m.get('category') is not None:
            self.category = m.get('category')

        if m.get('category_code') is not None:
            self.category_code = m.get('category_code')

        if m.get('category_type') is not None:
            self.category_type = m.get('category_type')

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

class HotelOrderListQueryResponseBodyModuleInvoice(DaraModel):
    def __init__(
        self,
        id: int = None,
        invoice_type: int = None,
        title: str = None,
    ):
        self.id = id
        self.invoice_type = invoice_type
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

        if self.invoice_type is not None:
            result['invoice_type'] = self.invoice_type

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('invoice_type') is not None:
            self.invoice_type = m.get('invoice_type')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class HotelOrderListQueryResponseBodyModuleCostCenter(DaraModel):
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

