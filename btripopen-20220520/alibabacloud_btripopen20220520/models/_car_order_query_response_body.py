# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class CarOrderQueryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.CarOrderQueryResponseBodyModule = None,
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
            temp_model = main_models.CarOrderQueryResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class CarOrderQueryResponseBodyModule(DaraModel):
    def __init__(
        self,
        car_info: main_models.CarOrderQueryResponseBodyModuleCarInfo = None,
        invoice_info: main_models.CarOrderQueryResponseBodyModuleInvoiceInfo = None,
        order_base_info: main_models.CarOrderQueryResponseBodyModuleOrderBaseInfo = None,
        passenger_list: List[main_models.CarOrderQueryResponseBodyModulePassengerList] = None,
        price_info_list: List[main_models.CarOrderQueryResponseBodyModulePriceInfoList] = None,
    ):
        self.car_info = car_info
        self.invoice_info = invoice_info
        self.order_base_info = order_base_info
        self.passenger_list = passenger_list
        self.price_info_list = price_info_list

    def validate(self):
        if self.car_info:
            self.car_info.validate()
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
        if self.car_info is not None:
            result['car_info'] = self.car_info.to_map()

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
        if m.get('car_info') is not None:
            temp_model = main_models.CarOrderQueryResponseBodyModuleCarInfo()
            self.car_info = temp_model.from_map(m.get('car_info'))

        if m.get('invoice_info') is not None:
            temp_model = main_models.CarOrderQueryResponseBodyModuleInvoiceInfo()
            self.invoice_info = temp_model.from_map(m.get('invoice_info'))

        if m.get('order_base_info') is not None:
            temp_model = main_models.CarOrderQueryResponseBodyModuleOrderBaseInfo()
            self.order_base_info = temp_model.from_map(m.get('order_base_info'))

        self.passenger_list = []
        if m.get('passenger_list') is not None:
            for k1 in m.get('passenger_list'):
                temp_model = main_models.CarOrderQueryResponseBodyModulePassengerList()
                self.passenger_list.append(temp_model.from_map(k1))

        self.price_info_list = []
        if m.get('price_info_list') is not None:
            for k1 in m.get('price_info_list'):
                temp_model = main_models.CarOrderQueryResponseBodyModulePriceInfoList()
                self.price_info_list.append(temp_model.from_map(k1))

        return self

class CarOrderQueryResponseBodyModulePriceInfoList(DaraModel):
    def __init__(
        self,
        category_code: int = None,
        gmt_create: int = None,
        pay_type: int = None,
        person_price: int = None,
        price: int = None,
        trade_id: str = None,
        type: int = None,
    ):
        self.category_code = category_code
        self.gmt_create = gmt_create
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

        if self.gmt_create is not None:
            result['gmt_create'] = self.gmt_create

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

        if m.get('gmt_create') is not None:
            self.gmt_create = m.get('gmt_create')

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

class CarOrderQueryResponseBodyModulePassengerList(DaraModel):
    def __init__(
        self,
        cost_center_id: int = None,
        cost_center_name: str = None,
        cost_center_number: str = None,
        project_code: str = None,
        project_id: int = None,
        project_title: str = None,
        thirdpart_cost_center_id: str = None,
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

class CarOrderQueryResponseBodyModuleOrderBaseInfo(DaraModel):
    def __init__(
        self,
        apply_id: str = None,
        btrip_cause: str = None,
        btrip_title: str = None,
        car_order_source_type: int = None,
        corp_id: str = None,
        corp_name: str = None,
        depart_id: str = None,
        depart_name: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        itinerary_id: str = None,
        order_id: int = None,
        order_status: int = None,
        sub_order_id: int = None,
        third_depart_id: str = None,
        thirdpart_apply_id: str = None,
        thirdpart_business_id: str = None,
        thirdpart_itinerary_id: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.apply_id = apply_id
        self.btrip_cause = btrip_cause
        self.btrip_title = btrip_title
        self.car_order_source_type = car_order_source_type
        self.corp_id = corp_id
        self.corp_name = corp_name
        self.depart_id = depart_id
        self.depart_name = depart_name
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.itinerary_id = itinerary_id
        self.order_id = order_id
        self.order_status = order_status
        self.sub_order_id = sub_order_id
        self.third_depart_id = third_depart_id
        self.thirdpart_apply_id = thirdpart_apply_id
        self.thirdpart_business_id = thirdpart_business_id
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

        if self.btrip_cause is not None:
            result['btrip_cause'] = self.btrip_cause

        if self.btrip_title is not None:
            result['btrip_title'] = self.btrip_title

        if self.car_order_source_type is not None:
            result['car_order_source_type'] = self.car_order_source_type

        if self.corp_id is not None:
            result['corp_id'] = self.corp_id

        if self.corp_name is not None:
            result['corp_name'] = self.corp_name

        if self.depart_id is not None:
            result['depart_id'] = self.depart_id

        if self.depart_name is not None:
            result['depart_name'] = self.depart_name

        if self.gmt_create is not None:
            result['gmt_create'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmt_modified'] = self.gmt_modified

        if self.itinerary_id is not None:
            result['itinerary_id'] = self.itinerary_id

        if self.order_id is not None:
            result['order_id'] = self.order_id

        if self.order_status is not None:
            result['order_status'] = self.order_status

        if self.sub_order_id is not None:
            result['sub_order_id'] = self.sub_order_id

        if self.third_depart_id is not None:
            result['third_depart_id'] = self.third_depart_id

        if self.thirdpart_apply_id is not None:
            result['thirdpart_apply_id'] = self.thirdpart_apply_id

        if self.thirdpart_business_id is not None:
            result['thirdpart_business_id'] = self.thirdpart_business_id

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

        if m.get('btrip_cause') is not None:
            self.btrip_cause = m.get('btrip_cause')

        if m.get('btrip_title') is not None:
            self.btrip_title = m.get('btrip_title')

        if m.get('car_order_source_type') is not None:
            self.car_order_source_type = m.get('car_order_source_type')

        if m.get('corp_id') is not None:
            self.corp_id = m.get('corp_id')

        if m.get('corp_name') is not None:
            self.corp_name = m.get('corp_name')

        if m.get('depart_id') is not None:
            self.depart_id = m.get('depart_id')

        if m.get('depart_name') is not None:
            self.depart_name = m.get('depart_name')

        if m.get('gmt_create') is not None:
            self.gmt_create = m.get('gmt_create')

        if m.get('gmt_modified') is not None:
            self.gmt_modified = m.get('gmt_modified')

        if m.get('itinerary_id') is not None:
            self.itinerary_id = m.get('itinerary_id')

        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')

        if m.get('order_status') is not None:
            self.order_status = m.get('order_status')

        if m.get('sub_order_id') is not None:
            self.sub_order_id = m.get('sub_order_id')

        if m.get('third_depart_id') is not None:
            self.third_depart_id = m.get('third_depart_id')

        if m.get('thirdpart_apply_id') is not None:
            self.thirdpart_apply_id = m.get('thirdpart_apply_id')

        if m.get('thirdpart_business_id') is not None:
            self.thirdpart_business_id = m.get('thirdpart_business_id')

        if m.get('thirdpart_itinerary_id') is not None:
            self.thirdpart_itinerary_id = m.get('thirdpart_itinerary_id')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')

        return self

class CarOrderQueryResponseBodyModuleInvoiceInfo(DaraModel):
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

class CarOrderQueryResponseBodyModuleCarInfo(DaraModel):
    def __init__(
        self,
        business_category: str = None,
        cancel_time: int = None,
        car_info: str = None,
        car_level: int = None,
        driver_card: str = None,
        driver_confirm_time: int = None,
        driver_name: str = None,
        estimate_price: int = None,
        from_address: str = None,
        from_city_ad_code: str = None,
        from_city_name: str = None,
        is_special: bool = None,
        memo: str = None,
        pay_time: int = None,
        publish_time: int = None,
        real_from_address: str = None,
        real_from_city_ad_code: str = None,
        real_from_city_name: str = None,
        real_to_address: str = None,
        real_to_city_ad_code: str = None,
        real_to_city_name: str = None,
        service_type: int = None,
        special_types: str = None,
        taken_time: int = None,
        to_address: str = None,
        to_city_ad_code: str = None,
        to_city_name: str = None,
        travel_distance: str = None,
        way_points: List[main_models.CarOrderQueryResponseBodyModuleCarInfoWayPoints] = None,
    ):
        self.business_category = business_category
        self.cancel_time = cancel_time
        self.car_info = car_info
        self.car_level = car_level
        self.driver_card = driver_card
        self.driver_confirm_time = driver_confirm_time
        self.driver_name = driver_name
        self.estimate_price = estimate_price
        self.from_address = from_address
        self.from_city_ad_code = from_city_ad_code
        self.from_city_name = from_city_name
        self.is_special = is_special
        self.memo = memo
        self.pay_time = pay_time
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
        self.to_address = to_address
        self.to_city_ad_code = to_city_ad_code
        self.to_city_name = to_city_name
        self.travel_distance = travel_distance
        self.way_points = way_points

    def validate(self):
        if self.way_points:
            for v1 in self.way_points:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_category is not None:
            result['business_category'] = self.business_category

        if self.cancel_time is not None:
            result['cancel_time'] = self.cancel_time

        if self.car_info is not None:
            result['car_info'] = self.car_info

        if self.car_level is not None:
            result['car_level'] = self.car_level

        if self.driver_card is not None:
            result['driver_card'] = self.driver_card

        if self.driver_confirm_time is not None:
            result['driver_confirm_time'] = self.driver_confirm_time

        if self.driver_name is not None:
            result['driver_name'] = self.driver_name

        if self.estimate_price is not None:
            result['estimate_price'] = self.estimate_price

        if self.from_address is not None:
            result['from_address'] = self.from_address

        if self.from_city_ad_code is not None:
            result['from_city_ad_code'] = self.from_city_ad_code

        if self.from_city_name is not None:
            result['from_city_name'] = self.from_city_name

        if self.is_special is not None:
            result['is_special'] = self.is_special

        if self.memo is not None:
            result['memo'] = self.memo

        if self.pay_time is not None:
            result['pay_time'] = self.pay_time

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

        if self.to_address is not None:
            result['to_address'] = self.to_address

        if self.to_city_ad_code is not None:
            result['to_city_ad_code'] = self.to_city_ad_code

        if self.to_city_name is not None:
            result['to_city_name'] = self.to_city_name

        if self.travel_distance is not None:
            result['travel_distance'] = self.travel_distance

        result['way_points'] = []
        if self.way_points is not None:
            for k1 in self.way_points:
                result['way_points'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('business_category') is not None:
            self.business_category = m.get('business_category')

        if m.get('cancel_time') is not None:
            self.cancel_time = m.get('cancel_time')

        if m.get('car_info') is not None:
            self.car_info = m.get('car_info')

        if m.get('car_level') is not None:
            self.car_level = m.get('car_level')

        if m.get('driver_card') is not None:
            self.driver_card = m.get('driver_card')

        if m.get('driver_confirm_time') is not None:
            self.driver_confirm_time = m.get('driver_confirm_time')

        if m.get('driver_name') is not None:
            self.driver_name = m.get('driver_name')

        if m.get('estimate_price') is not None:
            self.estimate_price = m.get('estimate_price')

        if m.get('from_address') is not None:
            self.from_address = m.get('from_address')

        if m.get('from_city_ad_code') is not None:
            self.from_city_ad_code = m.get('from_city_ad_code')

        if m.get('from_city_name') is not None:
            self.from_city_name = m.get('from_city_name')

        if m.get('is_special') is not None:
            self.is_special = m.get('is_special')

        if m.get('memo') is not None:
            self.memo = m.get('memo')

        if m.get('pay_time') is not None:
            self.pay_time = m.get('pay_time')

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

        if m.get('to_address') is not None:
            self.to_address = m.get('to_address')

        if m.get('to_city_ad_code') is not None:
            self.to_city_ad_code = m.get('to_city_ad_code')

        if m.get('to_city_name') is not None:
            self.to_city_name = m.get('to_city_name')

        if m.get('travel_distance') is not None:
            self.travel_distance = m.get('travel_distance')

        self.way_points = []
        if m.get('way_points') is not None:
            for k1 in m.get('way_points'):
                temp_model = main_models.CarOrderQueryResponseBodyModuleCarInfoWayPoints()
                self.way_points.append(temp_model.from_map(k1))

        return self

class CarOrderQueryResponseBodyModuleCarInfoWayPoints(DaraModel):
    def __init__(
        self,
        address: str = None,
        index: str = None,
        latitude: str = None,
        longitude: str = None,
    ):
        self.address = address
        self.index = index
        self.latitude = latitude
        self.longitude = longitude

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['address'] = self.address

        if self.index is not None:
            result['index'] = self.index

        if self.latitude is not None:
            result['latitude'] = self.latitude

        if self.longitude is not None:
            result['longitude'] = self.longitude

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address') is not None:
            self.address = m.get('address')

        if m.get('index') is not None:
            self.index = m.get('index')

        if m.get('latitude') is not None:
            self.latitude = m.get('latitude')

        if m.get('longitude') is not None:
            self.longitude = m.get('longitude')

        return self

