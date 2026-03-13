# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class HotelCityCodeListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: List[main_models.HotelCityCodeListResponseBodyModule] = None,
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
            for v1 in self.module:
                 if v1:
                    v1.validate()

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
                temp_model = main_models.HotelCityCodeListResponseBodyModule()
                self.module.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class HotelCityCodeListResponseBodyModule(DaraModel):
    def __init__(
        self,
        citys: List[main_models.HotelCityCodeListResponseBodyModuleCitys] = None,
        provice_code: str = None,
        province_name: str = None,
    ):
        self.citys = citys
        self.provice_code = provice_code
        self.province_name = province_name

    def validate(self):
        if self.citys:
            for v1 in self.citys:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['citys'] = []
        if self.citys is not None:
            for k1 in self.citys:
                result['citys'].append(k1.to_map() if k1 else None)

        if self.provice_code is not None:
            result['provice_code'] = self.provice_code

        if self.province_name is not None:
            result['province_name'] = self.province_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.citys = []
        if m.get('citys') is not None:
            for k1 in m.get('citys'):
                temp_model = main_models.HotelCityCodeListResponseBodyModuleCitys()
                self.citys.append(temp_model.from_map(k1))

        if m.get('provice_code') is not None:
            self.provice_code = m.get('provice_code')

        if m.get('province_name') is not None:
            self.province_name = m.get('province_name')

        return self

class HotelCityCodeListResponseBodyModuleCitys(DaraModel):
    def __init__(
        self,
        city_code: str = None,
        city_name: str = None,
        districts: List[main_models.HotelCityCodeListResponseBodyModuleCitysDistricts] = None,
    ):
        self.city_code = city_code
        self.city_name = city_name
        self.districts = districts

    def validate(self):
        if self.districts:
            for v1 in self.districts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.city_code is not None:
            result['city_code'] = self.city_code

        if self.city_name is not None:
            result['city_name'] = self.city_name

        result['districts'] = []
        if self.districts is not None:
            for k1 in self.districts:
                result['districts'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('city_code') is not None:
            self.city_code = m.get('city_code')

        if m.get('city_name') is not None:
            self.city_name = m.get('city_name')

        self.districts = []
        if m.get('districts') is not None:
            for k1 in m.get('districts'):
                temp_model = main_models.HotelCityCodeListResponseBodyModuleCitysDistricts()
                self.districts.append(temp_model.from_map(k1))

        return self

class HotelCityCodeListResponseBodyModuleCitysDistricts(DaraModel):
    def __init__(
        self,
        district_code: str = None,
        district_name: str = None,
    ):
        self.district_code = district_code
        self.district_name = district_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.district_code is not None:
            result['district_code'] = self.district_code

        if self.district_name is not None:
            result['district_name'] = self.district_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('district_code') is not None:
            self.district_code = m.get('district_code')

        if m.get('district_name') is not None:
            self.district_name = m.get('district_name')

        return self

