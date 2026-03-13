# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class HotelSuggestV2ResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.HotelSuggestV2ResponseBodyModule = None,
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
            temp_model = main_models.HotelSuggestV2ResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class HotelSuggestV2ResponseBodyModule(DaraModel):
    def __init__(
        self,
        guess_suggest_infos: List[main_models.HotelSuggestV2ResponseBodyModuleGuessSuggestInfos] = None,
        keyword_suggest_infos: List[main_models.HotelSuggestV2ResponseBodyModuleKeywordSuggestInfos] = None,
        popular_suggest_infos: List[main_models.HotelSuggestV2ResponseBodyModulePopularSuggestInfos] = None,
        tips: str = None,
    ):
        self.guess_suggest_infos = guess_suggest_infos
        self.keyword_suggest_infos = keyword_suggest_infos
        self.popular_suggest_infos = popular_suggest_infos
        self.tips = tips

    def validate(self):
        if self.guess_suggest_infos:
            for v1 in self.guess_suggest_infos:
                 if v1:
                    v1.validate()
        if self.keyword_suggest_infos:
            for v1 in self.keyword_suggest_infos:
                 if v1:
                    v1.validate()
        if self.popular_suggest_infos:
            for v1 in self.popular_suggest_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['guess_suggest_infos'] = []
        if self.guess_suggest_infos is not None:
            for k1 in self.guess_suggest_infos:
                result['guess_suggest_infos'].append(k1.to_map() if k1 else None)

        result['keyword_suggest_infos'] = []
        if self.keyword_suggest_infos is not None:
            for k1 in self.keyword_suggest_infos:
                result['keyword_suggest_infos'].append(k1.to_map() if k1 else None)

        result['popular_suggest_infos'] = []
        if self.popular_suggest_infos is not None:
            for k1 in self.popular_suggest_infos:
                result['popular_suggest_infos'].append(k1.to_map() if k1 else None)

        if self.tips is not None:
            result['tips'] = self.tips

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.guess_suggest_infos = []
        if m.get('guess_suggest_infos') is not None:
            for k1 in m.get('guess_suggest_infos'):
                temp_model = main_models.HotelSuggestV2ResponseBodyModuleGuessSuggestInfos()
                self.guess_suggest_infos.append(temp_model.from_map(k1))

        self.keyword_suggest_infos = []
        if m.get('keyword_suggest_infos') is not None:
            for k1 in m.get('keyword_suggest_infos'):
                temp_model = main_models.HotelSuggestV2ResponseBodyModuleKeywordSuggestInfos()
                self.keyword_suggest_infos.append(temp_model.from_map(k1))

        self.popular_suggest_infos = []
        if m.get('popular_suggest_infos') is not None:
            for k1 in m.get('popular_suggest_infos'):
                temp_model = main_models.HotelSuggestV2ResponseBodyModulePopularSuggestInfos()
                self.popular_suggest_infos.append(temp_model.from_map(k1))

        if m.get('tips') is not None:
            self.tips = m.get('tips')

        return self

class HotelSuggestV2ResponseBodyModulePopularSuggestInfos(DaraModel):
    def __init__(
        self,
        icon: str = None,
        popular_infos: List[main_models.HotelSuggestV2ResponseBodyModulePopularSuggestInfosPopularInfos] = None,
        title: str = None,
    ):
        self.icon = icon
        self.popular_infos = popular_infos
        self.title = title

    def validate(self):
        if self.popular_infos:
            for v1 in self.popular_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.icon is not None:
            result['icon'] = self.icon

        result['popular_infos'] = []
        if self.popular_infos is not None:
            for k1 in self.popular_infos:
                result['popular_infos'].append(k1.to_map() if k1 else None)

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('icon') is not None:
            self.icon = m.get('icon')

        self.popular_infos = []
        if m.get('popular_infos') is not None:
            for k1 in m.get('popular_infos'):
                temp_model = main_models.HotelSuggestV2ResponseBodyModulePopularSuggestInfosPopularInfos()
                self.popular_infos.append(temp_model.from_map(k1))

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class HotelSuggestV2ResponseBodyModulePopularSuggestInfosPopularInfos(DaraModel):
    def __init__(
        self,
        display_name: str = None,
    ):
        self.display_name = display_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['display_name'] = self.display_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('display_name') is not None:
            self.display_name = m.get('display_name')

        return self

class HotelSuggestV2ResponseBodyModuleKeywordSuggestInfos(DaraModel):
    def __init__(
        self,
        address: str = None,
        business_area_with_city: List[main_models.HotelSuggestV2ResponseBodyModuleKeywordSuggestInfosBusinessAreaWithCity] = None,
        city_code: int = None,
        city_name: str = None,
        display_name: str = None,
        hotel_id: str = None,
        icon: str = None,
        point: str = None,
        price: str = None,
        region: int = None,
        type: int = None,
        type_desc: str = None,
    ):
        self.address = address
        self.business_area_with_city = business_area_with_city
        self.city_code = city_code
        self.city_name = city_name
        self.display_name = display_name
        self.hotel_id = hotel_id
        self.icon = icon
        self.point = point
        self.price = price
        self.region = region
        self.type = type
        self.type_desc = type_desc

    def validate(self):
        if self.business_area_with_city:
            for v1 in self.business_area_with_city:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['address'] = self.address

        result['business_area_with_city'] = []
        if self.business_area_with_city is not None:
            for k1 in self.business_area_with_city:
                result['business_area_with_city'].append(k1.to_map() if k1 else None)

        if self.city_code is not None:
            result['city_code'] = self.city_code

        if self.city_name is not None:
            result['city_name'] = self.city_name

        if self.display_name is not None:
            result['display_name'] = self.display_name

        if self.hotel_id is not None:
            result['hotel_id'] = self.hotel_id

        if self.icon is not None:
            result['icon'] = self.icon

        if self.point is not None:
            result['point'] = self.point

        if self.price is not None:
            result['price'] = self.price

        if self.region is not None:
            result['region'] = self.region

        if self.type is not None:
            result['type'] = self.type

        if self.type_desc is not None:
            result['type_desc'] = self.type_desc

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address') is not None:
            self.address = m.get('address')

        self.business_area_with_city = []
        if m.get('business_area_with_city') is not None:
            for k1 in m.get('business_area_with_city'):
                temp_model = main_models.HotelSuggestV2ResponseBodyModuleKeywordSuggestInfosBusinessAreaWithCity()
                self.business_area_with_city.append(temp_model.from_map(k1))

        if m.get('city_code') is not None:
            self.city_code = m.get('city_code')

        if m.get('city_name') is not None:
            self.city_name = m.get('city_name')

        if m.get('display_name') is not None:
            self.display_name = m.get('display_name')

        if m.get('hotel_id') is not None:
            self.hotel_id = m.get('hotel_id')

        if m.get('icon') is not None:
            self.icon = m.get('icon')

        if m.get('point') is not None:
            self.point = m.get('point')

        if m.get('price') is not None:
            self.price = m.get('price')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('type_desc') is not None:
            self.type_desc = m.get('type_desc')

        return self

class HotelSuggestV2ResponseBodyModuleKeywordSuggestInfosBusinessAreaWithCity(DaraModel):
    def __init__(
        self,
        address: str = None,
        city_code: int = None,
        city_name: str = None,
        display_name: str = None,
        hotel_id: str = None,
        icon: str = None,
        point: str = None,
        price: str = None,
        region: int = None,
        type: int = None,
        type_desc: str = None,
    ):
        self.address = address
        self.city_code = city_code
        self.city_name = city_name
        self.display_name = display_name
        self.hotel_id = hotel_id
        self.icon = icon
        self.point = point
        self.price = price
        self.region = region
        self.type = type
        self.type_desc = type_desc

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['address'] = self.address

        if self.city_code is not None:
            result['city_code'] = self.city_code

        if self.city_name is not None:
            result['city_name'] = self.city_name

        if self.display_name is not None:
            result['display_name'] = self.display_name

        if self.hotel_id is not None:
            result['hotel_id'] = self.hotel_id

        if self.icon is not None:
            result['icon'] = self.icon

        if self.point is not None:
            result['point'] = self.point

        if self.price is not None:
            result['price'] = self.price

        if self.region is not None:
            result['region'] = self.region

        if self.type is not None:
            result['type'] = self.type

        if self.type_desc is not None:
            result['type_desc'] = self.type_desc

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address') is not None:
            self.address = m.get('address')

        if m.get('city_code') is not None:
            self.city_code = m.get('city_code')

        if m.get('city_name') is not None:
            self.city_name = m.get('city_name')

        if m.get('display_name') is not None:
            self.display_name = m.get('display_name')

        if m.get('hotel_id') is not None:
            self.hotel_id = m.get('hotel_id')

        if m.get('icon') is not None:
            self.icon = m.get('icon')

        if m.get('point') is not None:
            self.point = m.get('point')

        if m.get('price') is not None:
            self.price = m.get('price')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('type_desc') is not None:
            self.type_desc = m.get('type_desc')

        return self

class HotelSuggestV2ResponseBodyModuleGuessSuggestInfos(DaraModel):
    def __init__(
        self,
        address: str = None,
        city_code: int = None,
        city_name: str = None,
        display_name: str = None,
        hotel_id: str = None,
        icon: str = None,
        point: str = None,
        price: str = None,
        region: int = None,
        type: int = None,
        type_desc: str = None,
    ):
        self.address = address
        self.city_code = city_code
        self.city_name = city_name
        self.display_name = display_name
        self.hotel_id = hotel_id
        self.icon = icon
        self.point = point
        self.price = price
        self.region = region
        self.type = type
        self.type_desc = type_desc

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['address'] = self.address

        if self.city_code is not None:
            result['city_code'] = self.city_code

        if self.city_name is not None:
            result['city_name'] = self.city_name

        if self.display_name is not None:
            result['display_name'] = self.display_name

        if self.hotel_id is not None:
            result['hotel_id'] = self.hotel_id

        if self.icon is not None:
            result['icon'] = self.icon

        if self.point is not None:
            result['point'] = self.point

        if self.price is not None:
            result['price'] = self.price

        if self.region is not None:
            result['region'] = self.region

        if self.type is not None:
            result['type'] = self.type

        if self.type_desc is not None:
            result['type_desc'] = self.type_desc

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address') is not None:
            self.address = m.get('address')

        if m.get('city_code') is not None:
            self.city_code = m.get('city_code')

        if m.get('city_name') is not None:
            self.city_name = m.get('city_name')

        if m.get('display_name') is not None:
            self.display_name = m.get('display_name')

        if m.get('hotel_id') is not None:
            self.hotel_id = m.get('hotel_id')

        if m.get('icon') is not None:
            self.icon = m.get('icon')

        if m.get('point') is not None:
            self.point = m.get('point')

        if m.get('price') is not None:
            self.price = m.get('price')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('type_desc') is not None:
            self.type_desc = m.get('type_desc')

        return self

