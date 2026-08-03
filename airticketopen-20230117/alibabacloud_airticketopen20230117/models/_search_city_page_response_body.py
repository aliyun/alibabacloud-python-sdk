# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_airticketopen20230117 import models as main_models
from darabonba.model import DaraModel

class SearchCityPageResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.SearchCityPageResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
        tracer_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success
        self.tracer_id = tracer_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.tracer_id is not None:
            result['TracerId'] = self.tracer_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.SearchCityPageResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TracerId') is not None:
            self.tracer_id = m.get('TracerId')

        return self

class SearchCityPageResponseBodyData(DaraModel):
    def __init__(
        self,
        cities: List[main_models.SearchCityPageResponseBodyDataCities] = None,
        has_next: bool = None,
        total: int = None,
    ):
        self.cities = cities
        self.has_next = has_next
        self.total = total

    def validate(self):
        if self.cities:
            for v1 in self.cities:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Cities'] = []
        if self.cities is not None:
            for k1 in self.cities:
                result['Cities'].append(k1.to_map() if k1 else None)

        if self.has_next is not None:
            result['HasNext'] = self.has_next

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cities = []
        if m.get('Cities') is not None:
            for k1 in m.get('Cities'):
                temp_model = main_models.SearchCityPageResponseBodyDataCities()
                self.cities.append(temp_model.from_map(k1))

        if m.get('HasNext') is not None:
            self.has_next = m.get('HasNext')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class SearchCityPageResponseBodyDataCities(DaraModel):
    def __init__(
        self,
        cn_name: str = None,
        code: int = None,
        country: int = None,
        country_code: str = None,
        en_name: str = None,
        level: int = None,
        parent_code: int = None,
        region: int = None,
        type: int = None,
    ):
        self.cn_name = cn_name
        self.code = code
        self.country = country
        self.country_code = country_code
        self.en_name = en_name
        self.level = level
        self.parent_code = parent_code
        self.region = region
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cn_name is not None:
            result['CnName'] = self.cn_name

        if self.code is not None:
            result['Code'] = self.code

        if self.country is not None:
            result['Country'] = self.country

        if self.country_code is not None:
            result['CountryCode'] = self.country_code

        if self.en_name is not None:
            result['EnName'] = self.en_name

        if self.level is not None:
            result['Level'] = self.level

        if self.parent_code is not None:
            result['ParentCode'] = self.parent_code

        if self.region is not None:
            result['Region'] = self.region

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CnName') is not None:
            self.cn_name = m.get('CnName')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Country') is not None:
            self.country = m.get('Country')

        if m.get('CountryCode') is not None:
            self.country_code = m.get('CountryCode')

        if m.get('EnName') is not None:
            self.en_name = m.get('EnName')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('ParentCode') is not None:
            self.parent_code = m.get('ParentCode')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

