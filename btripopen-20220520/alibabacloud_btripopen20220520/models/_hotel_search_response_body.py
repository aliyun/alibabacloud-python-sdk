# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class HotelSearchResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.HotelSearchResponseBodyModule = None,
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
            temp_model = main_models.HotelSearchResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class HotelSearchResponseBodyModule(DaraModel):
    def __init__(
        self,
        count: int = None,
        items: List[main_models.HotelSearchResponseBodyModuleItems] = None,
    ):
        self.count = count
        self.items = items

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
        if self.count is not None:
            result['count'] = self.count

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.HotelSearchResponseBodyModuleItems()
                self.items.append(temp_model.from_map(k1))

        return self

class HotelSearchResponseBodyModuleItems(DaraModel):
    def __init__(
        self,
        brand_name: str = None,
        btand_code: str = None,
        city_code: str = None,
        discount_desc: main_models.HotelSearchResponseBodyModuleItemsDiscountDesc = None,
        distance: int = None,
        district_code: str = None,
        hotel_address: str = None,
        hotel_code: str = None,
        hotel_en_name: str = None,
        hotel_name: str = None,
        hotel_star: str = None,
        image_url: str = None,
        is_protocol: bool = None,
        location: str = None,
        min_price: float = None,
        original_min_price: float = None,
        score: str = None,
        status: int = None,
        tel: str = None,
    ):
        self.brand_name = brand_name
        self.btand_code = btand_code
        self.city_code = city_code
        self.discount_desc = discount_desc
        self.distance = distance
        self.district_code = district_code
        self.hotel_address = hotel_address
        self.hotel_code = hotel_code
        self.hotel_en_name = hotel_en_name
        self.hotel_name = hotel_name
        self.hotel_star = hotel_star
        self.image_url = image_url
        self.is_protocol = is_protocol
        self.location = location
        self.min_price = min_price
        self.original_min_price = original_min_price
        self.score = score
        self.status = status
        self.tel = tel

    def validate(self):
        if self.discount_desc:
            self.discount_desc.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.brand_name is not None:
            result['brand_name'] = self.brand_name

        if self.btand_code is not None:
            result['btand_code'] = self.btand_code

        if self.city_code is not None:
            result['city_code'] = self.city_code

        if self.discount_desc is not None:
            result['discount_desc'] = self.discount_desc.to_map()

        if self.distance is not None:
            result['distance'] = self.distance

        if self.district_code is not None:
            result['district_code'] = self.district_code

        if self.hotel_address is not None:
            result['hotel_address'] = self.hotel_address

        if self.hotel_code is not None:
            result['hotel_code'] = self.hotel_code

        if self.hotel_en_name is not None:
            result['hotel_en_name'] = self.hotel_en_name

        if self.hotel_name is not None:
            result['hotel_name'] = self.hotel_name

        if self.hotel_star is not None:
            result['hotel_star'] = self.hotel_star

        if self.image_url is not None:
            result['image_url'] = self.image_url

        if self.is_protocol is not None:
            result['is_protocol'] = self.is_protocol

        if self.location is not None:
            result['location'] = self.location

        if self.min_price is not None:
            result['min_price'] = self.min_price

        if self.original_min_price is not None:
            result['original_min_price'] = self.original_min_price

        if self.score is not None:
            result['score'] = self.score

        if self.status is not None:
            result['status'] = self.status

        if self.tel is not None:
            result['tel'] = self.tel

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('brand_name') is not None:
            self.brand_name = m.get('brand_name')

        if m.get('btand_code') is not None:
            self.btand_code = m.get('btand_code')

        if m.get('city_code') is not None:
            self.city_code = m.get('city_code')

        if m.get('discount_desc') is not None:
            temp_model = main_models.HotelSearchResponseBodyModuleItemsDiscountDesc()
            self.discount_desc = temp_model.from_map(m.get('discount_desc'))

        if m.get('distance') is not None:
            self.distance = m.get('distance')

        if m.get('district_code') is not None:
            self.district_code = m.get('district_code')

        if m.get('hotel_address') is not None:
            self.hotel_address = m.get('hotel_address')

        if m.get('hotel_code') is not None:
            self.hotel_code = m.get('hotel_code')

        if m.get('hotel_en_name') is not None:
            self.hotel_en_name = m.get('hotel_en_name')

        if m.get('hotel_name') is not None:
            self.hotel_name = m.get('hotel_name')

        if m.get('hotel_star') is not None:
            self.hotel_star = m.get('hotel_star')

        if m.get('image_url') is not None:
            self.image_url = m.get('image_url')

        if m.get('is_protocol') is not None:
            self.is_protocol = m.get('is_protocol')

        if m.get('location') is not None:
            self.location = m.get('location')

        if m.get('min_price') is not None:
            self.min_price = m.get('min_price')

        if m.get('original_min_price') is not None:
            self.original_min_price = m.get('original_min_price')

        if m.get('score') is not None:
            self.score = m.get('score')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('tel') is not None:
            self.tel = m.get('tel')

        return self

class HotelSearchResponseBodyModuleItemsDiscountDesc(DaraModel):
    def __init__(
        self,
        cash_reduce_total: str = None,
        dinamic_label: str = None,
        discount_detail: List[main_models.HotelSearchResponseBodyModuleItemsDiscountDescDiscountDetail] = None,
        sub_title: str = None,
        title: str = None,
    ):
        self.cash_reduce_total = cash_reduce_total
        self.dinamic_label = dinamic_label
        self.discount_detail = discount_detail
        self.sub_title = sub_title
        self.title = title

    def validate(self):
        if self.discount_detail:
            for v1 in self.discount_detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cash_reduce_total is not None:
            result['cash_reduce_total'] = self.cash_reduce_total

        if self.dinamic_label is not None:
            result['dinamic_label'] = self.dinamic_label

        result['discount_detail'] = []
        if self.discount_detail is not None:
            for k1 in self.discount_detail:
                result['discount_detail'].append(k1.to_map() if k1 else None)

        if self.sub_title is not None:
            result['sub_title'] = self.sub_title

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cash_reduce_total') is not None:
            self.cash_reduce_total = m.get('cash_reduce_total')

        if m.get('dinamic_label') is not None:
            self.dinamic_label = m.get('dinamic_label')

        self.discount_detail = []
        if m.get('discount_detail') is not None:
            for k1 in m.get('discount_detail'):
                temp_model = main_models.HotelSearchResponseBodyModuleItemsDiscountDescDiscountDetail()
                self.discount_detail.append(temp_model.from_map(k1))

        if m.get('sub_title') is not None:
            self.sub_title = m.get('sub_title')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class HotelSearchResponseBodyModuleItemsDiscountDescDiscountDetail(DaraModel):
    def __init__(
        self,
        label_name: List[str] = None,
        money_desc: str = None,
    ):
        self.label_name = label_name
        self.money_desc = money_desc

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label_name is not None:
            result['label_name'] = self.label_name

        if self.money_desc is not None:
            result['money_desc'] = self.money_desc

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('label_name') is not None:
            self.label_name = m.get('label_name')

        if m.get('money_desc') is not None:
            self.money_desc = m.get('money_desc')

        return self

