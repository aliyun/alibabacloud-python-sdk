# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_iqs20241111 import models as main_models
from darabonba.model import DaraModel

class QueryResult(DaraModel):
    def __init__(
        self,
        data: List[main_models.QueryResultData] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.QueryResultData()
                self.data.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class QueryResultData(DaraModel):
    def __init__(
        self,
        address: str = None,
        city_code: str = None,
        city_name: str = None,
        distance_meter: str = None,
        district_code: str = None,
        district_name: str = None,
        id: str = None,
        images: List[main_models.QueryResultDataImages] = None,
        latitude: str = None,
        longitude: str = None,
        metadata: main_models.QueryResultDataMetadata = None,
        name: str = None,
        province_code: str = None,
        province_name: str = None,
        type_code: str = None,
        types: str = None,
    ):
        self.address = address
        self.city_code = city_code
        self.city_name = city_name
        self.distance_meter = distance_meter
        self.district_code = district_code
        self.district_name = district_name
        self.id = id
        self.images = images
        self.latitude = latitude
        self.longitude = longitude
        self.metadata = metadata
        self.name = name
        self.province_code = province_code
        self.province_name = province_name
        self.type_code = type_code
        self.types = types

    def validate(self):
        if self.images:
            for v1 in self.images:
                 if v1:
                    v1.validate()
        if self.metadata:
            self.metadata.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['address'] = self.address

        if self.city_code is not None:
            result['cityCode'] = self.city_code

        if self.city_name is not None:
            result['cityName'] = self.city_name

        if self.distance_meter is not None:
            result['distanceMeter'] = self.distance_meter

        if self.district_code is not None:
            result['districtCode'] = self.district_code

        if self.district_name is not None:
            result['districtName'] = self.district_name

        if self.id is not None:
            result['id'] = self.id

        result['images'] = []
        if self.images is not None:
            for k1 in self.images:
                result['images'].append(k1.to_map() if k1 else None)

        if self.latitude is not None:
            result['latitude'] = self.latitude

        if self.longitude is not None:
            result['longitude'] = self.longitude

        if self.metadata is not None:
            result['metadata'] = self.metadata.to_map()

        if self.name is not None:
            result['name'] = self.name

        if self.province_code is not None:
            result['provinceCode'] = self.province_code

        if self.province_name is not None:
            result['provinceName'] = self.province_name

        if self.type_code is not None:
            result['typeCode'] = self.type_code

        if self.types is not None:
            result['types'] = self.types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address') is not None:
            self.address = m.get('address')

        if m.get('cityCode') is not None:
            self.city_code = m.get('cityCode')

        if m.get('cityName') is not None:
            self.city_name = m.get('cityName')

        if m.get('distanceMeter') is not None:
            self.distance_meter = m.get('distanceMeter')

        if m.get('districtCode') is not None:
            self.district_code = m.get('districtCode')

        if m.get('districtName') is not None:
            self.district_name = m.get('districtName')

        if m.get('id') is not None:
            self.id = m.get('id')

        self.images = []
        if m.get('images') is not None:
            for k1 in m.get('images'):
                temp_model = main_models.QueryResultDataImages()
                self.images.append(temp_model.from_map(k1))

        if m.get('latitude') is not None:
            self.latitude = m.get('latitude')

        if m.get('longitude') is not None:
            self.longitude = m.get('longitude')

        if m.get('metadata') is not None:
            temp_model = main_models.QueryResultDataMetadata()
            self.metadata = temp_model.from_map(m.get('metadata'))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('provinceCode') is not None:
            self.province_code = m.get('provinceCode')

        if m.get('provinceName') is not None:
            self.province_name = m.get('provinceName')

        if m.get('typeCode') is not None:
            self.type_code = m.get('typeCode')

        if m.get('types') is not None:
            self.types = m.get('types')

        return self

class QueryResultDataMetadata(DaraModel):
    def __init__(
        self,
        average_spend: str = None,
        business_area: str = None,
        daily_opening_hours: str = None,
        main_tag: str = None,
        phone: str = None,
        score: str = None,
        weekly_opening_days: str = None,
    ):
        self.average_spend = average_spend
        self.business_area = business_area
        self.daily_opening_hours = daily_opening_hours
        self.main_tag = main_tag
        self.phone = phone
        self.score = score
        self.weekly_opening_days = weekly_opening_days

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.average_spend is not None:
            result['averageSpend'] = self.average_spend

        if self.business_area is not None:
            result['businessArea'] = self.business_area

        if self.daily_opening_hours is not None:
            result['dailyOpeningHours'] = self.daily_opening_hours

        if self.main_tag is not None:
            result['mainTag'] = self.main_tag

        if self.phone is not None:
            result['phone'] = self.phone

        if self.score is not None:
            result['score'] = self.score

        if self.weekly_opening_days is not None:
            result['weeklyOpeningDays'] = self.weekly_opening_days

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('averageSpend') is not None:
            self.average_spend = m.get('averageSpend')

        if m.get('businessArea') is not None:
            self.business_area = m.get('businessArea')

        if m.get('dailyOpeningHours') is not None:
            self.daily_opening_hours = m.get('dailyOpeningHours')

        if m.get('mainTag') is not None:
            self.main_tag = m.get('mainTag')

        if m.get('phone') is not None:
            self.phone = m.get('phone')

        if m.get('score') is not None:
            self.score = m.get('score')

        if m.get('weeklyOpeningDays') is not None:
            self.weekly_opening_days = m.get('weeklyOpeningDays')

        return self

class QueryResultDataImages(DaraModel):
    def __init__(
        self,
        title: str = None,
        url: str = None,
    ):
        self.title = title
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.title is not None:
            result['title'] = self.title

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

