# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class CarOrderListQueryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: List[main_models.CarOrderListQueryResponseBodyModule] = None,
        page_info: main_models.CarOrderListQueryResponseBodyPageInfo = None,
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
        # traceId
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
                temp_model = main_models.CarOrderListQueryResponseBodyModule()
                self.module.append(temp_model.from_map(k1))

        if m.get('page_info') is not None:
            temp_model = main_models.CarOrderListQueryResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('page_info'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class CarOrderListQueryResponseBodyPageInfo(DaraModel):
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

class CarOrderListQueryResponseBodyModule(DaraModel):
    def __init__(
        self,
        apply_id: int = None,
        apply_show_id: str = None,
        btrip_title: str = None,
        business_category: str = None,
        cancel_time: str = None,
        car_info: str = None,
        car_level: int = None,
        corp_id: str = None,
        corp_name: str = None,
        cost_center_id: int = None,
        cost_center_name: str = None,
        cost_center_number: str = None,
        dept_id: int = None,
        dept_name: str = None,
        driver_confirm_time: str = None,
        estimate_price: float = None,
        from_address: str = None,
        from_city_ad_code: str = None,
        from_city_name: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        invoice_id: int = None,
        invoice_title: str = None,
        is_special: bool = None,
        memo: str = None,
        order_id: str = None,
        order_status: int = None,
        passenger_name: str = None,
        pay_time: str = None,
        price_info_list: List[main_models.CarOrderListQueryResponseBodyModulePriceInfoList] = None,
        project_code: str = None,
        project_id: int = None,
        project_title: str = None,
        provider: int = None,
        publish_time: str = None,
        real_from_address: str = None,
        real_from_city_ad_code: str = None,
        real_from_city_name: str = None,
        real_to_address: str = None,
        real_to_city_ad_code: str = None,
        real_to_city_name: str = None,
        service_type: int = None,
        special_types: List[str] = None,
        taken_time: str = None,
        thirdpart_apply_id: str = None,
        thirdpart_business_id: str = None,
        thirdpart_itinerary_id: str = None,
        to_address: str = None,
        to_city_ad_code: str = None,
        to_city_name: str = None,
        travel_distance: float = None,
        user_affiliate_list: List[main_models.CarOrderListQueryResponseBodyModuleUserAffiliateList] = None,
        user_confirm: int = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.apply_id = apply_id
        self.apply_show_id = apply_show_id
        self.btrip_title = btrip_title
        self.business_category = business_category
        self.cancel_time = cancel_time
        self.car_info = car_info
        self.car_level = car_level
        self.corp_id = corp_id
        self.corp_name = corp_name
        self.cost_center_id = cost_center_id
        self.cost_center_name = cost_center_name
        self.cost_center_number = cost_center_number
        self.dept_id = dept_id
        self.dept_name = dept_name
        self.driver_confirm_time = driver_confirm_time
        self.estimate_price = estimate_price
        self.from_address = from_address
        self.from_city_ad_code = from_city_ad_code
        self.from_city_name = from_city_name
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.invoice_id = invoice_id
        self.invoice_title = invoice_title
        self.is_special = is_special
        self.memo = memo
        self.order_id = order_id
        self.order_status = order_status
        self.passenger_name = passenger_name
        self.pay_time = pay_time
        self.price_info_list = price_info_list
        self.project_code = project_code
        self.project_id = project_id
        self.project_title = project_title
        self.provider = provider
        self.publish_time = publish_time
        self.real_from_address = real_from_address
        self.real_from_city_ad_code = real_from_city_ad_code
        self.real_from_city_name = real_from_city_name
        self.real_to_address = real_to_address
        self.real_to_city_ad_code = real_to_city_ad_code
        self.real_to_city_name = real_to_city_name
        self.service_type = service_type
        self.special_types = special_types
        self.taken_time = taken_time
        self.thirdpart_apply_id = thirdpart_apply_id
        self.thirdpart_business_id = thirdpart_business_id
        self.thirdpart_itinerary_id = thirdpart_itinerary_id
        self.to_address = to_address
        self.to_city_ad_code = to_city_ad_code
        self.to_city_name = to_city_name
        self.travel_distance = travel_distance
        self.user_affiliate_list = user_affiliate_list
        self.user_confirm = user_confirm
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
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

        if self.apply_show_id is not None:
            result['apply_show_id'] = self.apply_show_id

        if self.btrip_title is not None:
            result['btrip_title'] = self.btrip_title

        if self.business_category is not None:
            result['business_category'] = self.business_category

        if self.cancel_time is not None:
            result['cancel_time'] = self.cancel_time

        if self.car_info is not None:
            result['car_info'] = self.car_info

        if self.car_level is not None:
            result['car_level'] = self.car_level

        if self.corp_id is not None:
            result['corp_id'] = self.corp_id

        if self.corp_name is not None:
            result['corp_name'] = self.corp_name

        if self.cost_center_id is not None:
            result['cost_center_id'] = self.cost_center_id

        if self.cost_center_name is not None:
            result['cost_center_name'] = self.cost_center_name

        if self.cost_center_number is not None:
            result['cost_center_number'] = self.cost_center_number

        if self.dept_id is not None:
            result['dept_id'] = self.dept_id

        if self.dept_name is not None:
            result['dept_name'] = self.dept_name

        if self.driver_confirm_time is not None:
            result['driver_confirm_time'] = self.driver_confirm_time

        if self.estimate_price is not None:
            result['estimate_price'] = self.estimate_price

        if self.from_address is not None:
            result['from_address'] = self.from_address

        if self.from_city_ad_code is not None:
            result['from_city_ad_code'] = self.from_city_ad_code

        if self.from_city_name is not None:
            result['from_city_name'] = self.from_city_name

        if self.gmt_create is not None:
            result['gmt_create'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmt_modified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.invoice_id is not None:
            result['invoice_id'] = self.invoice_id

        if self.invoice_title is not None:
            result['invoice_title'] = self.invoice_title

        if self.is_special is not None:
            result['is_special'] = self.is_special

        if self.memo is not None:
            result['memo'] = self.memo

        if self.order_id is not None:
            result['order_id'] = self.order_id

        if self.order_status is not None:
            result['order_status'] = self.order_status

        if self.passenger_name is not None:
            result['passenger_name'] = self.passenger_name

        if self.pay_time is not None:
            result['pay_time'] = self.pay_time

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

        if self.provider is not None:
            result['provider'] = self.provider

        if self.publish_time is not None:
            result['publish_time'] = self.publish_time

        if self.real_from_address is not None:
            result['real_from_address'] = self.real_from_address

        if self.real_from_city_ad_code is not None:
            result['real_from_city_ad_code'] = self.real_from_city_ad_code

        if self.real_from_city_name is not None:
            result['real_from_city_name'] = self.real_from_city_name

        if self.real_to_address is not None:
            result['real_to_address'] = self.real_to_address

        if self.real_to_city_ad_code is not None:
            result['real_to_city_ad_code'] = self.real_to_city_ad_code

        if self.real_to_city_name is not None:
            result['real_to_city_name'] = self.real_to_city_name

        if self.service_type is not None:
            result['service_type'] = self.service_type

        if self.special_types is not None:
            result['special_types'] = self.special_types

        if self.taken_time is not None:
            result['taken_time'] = self.taken_time

        if self.thirdpart_apply_id is not None:
            result['thirdpart_apply_id'] = self.thirdpart_apply_id

        if self.thirdpart_business_id is not None:
            result['thirdpart_business_id'] = self.thirdpart_business_id

        if self.thirdpart_itinerary_id is not None:
            result['thirdpart_itinerary_id'] = self.thirdpart_itinerary_id

        if self.to_address is not None:
            result['to_address'] = self.to_address

        if self.to_city_ad_code is not None:
            result['to_city_ad_code'] = self.to_city_ad_code

        if self.to_city_name is not None:
            result['to_city_name'] = self.to_city_name

        if self.travel_distance is not None:
            result['travel_distance'] = self.travel_distance

        result['user_affiliate_list'] = []
        if self.user_affiliate_list is not None:
            for k1 in self.user_affiliate_list:
                result['user_affiliate_list'].append(k1.to_map() if k1 else None)

        if self.user_confirm is not None:
            result['user_confirm'] = self.user_confirm

        if self.user_id is not None:
            result['user_id'] = self.user_id

        if self.user_name is not None:
            result['user_name'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apply_id') is not None:
            self.apply_id = m.get('apply_id')

        if m.get('apply_show_id') is not None:
            self.apply_show_id = m.get('apply_show_id')

        if m.get('btrip_title') is not None:
            self.btrip_title = m.get('btrip_title')

        if m.get('business_category') is not None:
            self.business_category = m.get('business_category')

        if m.get('cancel_time') is not None:
            self.cancel_time = m.get('cancel_time')

        if m.get('car_info') is not None:
            self.car_info = m.get('car_info')

        if m.get('car_level') is not None:
            self.car_level = m.get('car_level')

        if m.get('corp_id') is not None:
            self.corp_id = m.get('corp_id')

        if m.get('corp_name') is not None:
            self.corp_name = m.get('corp_name')

        if m.get('cost_center_id') is not None:
            self.cost_center_id = m.get('cost_center_id')

        if m.get('cost_center_name') is not None:
            self.cost_center_name = m.get('cost_center_name')

        if m.get('cost_center_number') is not None:
            self.cost_center_number = m.get('cost_center_number')

        if m.get('dept_id') is not None:
            self.dept_id = m.get('dept_id')

        if m.get('dept_name') is not None:
            self.dept_name = m.get('dept_name')

        if m.get('driver_confirm_time') is not None:
            self.driver_confirm_time = m.get('driver_confirm_time')

        if m.get('estimate_price') is not None:
            self.estimate_price = m.get('estimate_price')

        if m.get('from_address') is not None:
            self.from_address = m.get('from_address')

        if m.get('from_city_ad_code') is not None:
            self.from_city_ad_code = m.get('from_city_ad_code')

        if m.get('from_city_name') is not None:
            self.from_city_name = m.get('from_city_name')

        if m.get('gmt_create') is not None:
            self.gmt_create = m.get('gmt_create')

        if m.get('gmt_modified') is not None:
            self.gmt_modified = m.get('gmt_modified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('invoice_id') is not None:
            self.invoice_id = m.get('invoice_id')

        if m.get('invoice_title') is not None:
            self.invoice_title = m.get('invoice_title')

        if m.get('is_special') is not None:
            self.is_special = m.get('is_special')

        if m.get('memo') is not None:
            self.memo = m.get('memo')

        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')

        if m.get('order_status') is not None:
            self.order_status = m.get('order_status')

        if m.get('passenger_name') is not None:
            self.passenger_name = m.get('passenger_name')

        if m.get('pay_time') is not None:
            self.pay_time = m.get('pay_time')

        self.price_info_list = []
        if m.get('price_info_list') is not None:
            for k1 in m.get('price_info_list'):
                temp_model = main_models.CarOrderListQueryResponseBodyModulePriceInfoList()
                self.price_info_list.append(temp_model.from_map(k1))

        if m.get('project_code') is not None:
            self.project_code = m.get('project_code')

        if m.get('project_id') is not None:
            self.project_id = m.get('project_id')

        if m.get('project_title') is not None:
            self.project_title = m.get('project_title')

        if m.get('provider') is not None:
            self.provider = m.get('provider')

        if m.get('publish_time') is not None:
            self.publish_time = m.get('publish_time')

        if m.get('real_from_address') is not None:
            self.real_from_address = m.get('real_from_address')

        if m.get('real_from_city_ad_code') is not None:
            self.real_from_city_ad_code = m.get('real_from_city_ad_code')

        if m.get('real_from_city_name') is not None:
            self.real_from_city_name = m.get('real_from_city_name')

        if m.get('real_to_address') is not None:
            self.real_to_address = m.get('real_to_address')

        if m.get('real_to_city_ad_code') is not None:
            self.real_to_city_ad_code = m.get('real_to_city_ad_code')

        if m.get('real_to_city_name') is not None:
            self.real_to_city_name = m.get('real_to_city_name')

        if m.get('service_type') is not None:
            self.service_type = m.get('service_type')

        if m.get('special_types') is not None:
            self.special_types = m.get('special_types')

        if m.get('taken_time') is not None:
            self.taken_time = m.get('taken_time')

        if m.get('thirdpart_apply_id') is not None:
            self.thirdpart_apply_id = m.get('thirdpart_apply_id')

        if m.get('thirdpart_business_id') is not None:
            self.thirdpart_business_id = m.get('thirdpart_business_id')

        if m.get('thirdpart_itinerary_id') is not None:
            self.thirdpart_itinerary_id = m.get('thirdpart_itinerary_id')

        if m.get('to_address') is not None:
            self.to_address = m.get('to_address')

        if m.get('to_city_ad_code') is not None:
            self.to_city_ad_code = m.get('to_city_ad_code')

        if m.get('to_city_name') is not None:
            self.to_city_name = m.get('to_city_name')

        if m.get('travel_distance') is not None:
            self.travel_distance = m.get('travel_distance')

        self.user_affiliate_list = []
        if m.get('user_affiliate_list') is not None:
            for k1 in m.get('user_affiliate_list'):
                temp_model = main_models.CarOrderListQueryResponseBodyModuleUserAffiliateList()
                self.user_affiliate_list.append(temp_model.from_map(k1))

        if m.get('user_confirm') is not None:
            self.user_confirm = m.get('user_confirm')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')

        return self

class CarOrderListQueryResponseBodyModuleUserAffiliateList(DaraModel):
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

class CarOrderListQueryResponseBodyModulePriceInfoList(DaraModel):
    def __init__(
        self,
        category_code: int = None,
        category_type: int = None,
        gmt_create: str = None,
        passenger_name: str = None,
        pay_type: int = None,
        person_price: float = None,
        price: float = None,
        trade_id: str = None,
        type: int = None,
    ):
        self.category_code = category_code
        self.category_type = category_type
        self.gmt_create = gmt_create
        self.passenger_name = passenger_name
        self.pay_type = pay_type
        self.person_price = person_price
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

        if self.category_type is not None:
            result['category_type'] = self.category_type

        if self.gmt_create is not None:
            result['gmt_create'] = self.gmt_create

        if self.passenger_name is not None:
            result['passenger_name'] = self.passenger_name

        if self.pay_type is not None:
            result['pay_type'] = self.pay_type

        if self.person_price is not None:
            result['person_price'] = self.person_price

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

        if m.get('category_type') is not None:
            self.category_type = m.get('category_type')

        if m.get('gmt_create') is not None:
            self.gmt_create = m.get('gmt_create')

        if m.get('passenger_name') is not None:
            self.passenger_name = m.get('passenger_name')

        if m.get('pay_type') is not None:
            self.pay_type = m.get('pay_type')

        if m.get('person_price') is not None:
            self.person_price = m.get('person_price')

        if m.get('price') is not None:
            self.price = m.get('price')

        if m.get('trade_id') is not None:
            self.trade_id = m.get('trade_id')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

