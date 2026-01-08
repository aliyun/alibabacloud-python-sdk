# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeLocationInfoResponseBody(DaraModel):
    def __init__(
        self,
        cn_count: int = None,
        cn_list: List[main_models.DescribeLocationInfoResponseBodyCnList] = None,
        cn_province_list: List[main_models.DescribeLocationInfoResponseBodyCnProvinceList] = None,
        overseas_count: int = None,
        overseas_list: List[main_models.DescribeLocationInfoResponseBodyOverseasList] = None,
        request_id: str = None,
    ):
        self.cn_count = cn_count
        self.cn_list = cn_list
        self.cn_province_list = cn_province_list
        self.overseas_count = overseas_count
        self.overseas_list = overseas_list
        self.request_id = request_id

    def validate(self):
        if self.cn_list:
            for v1 in self.cn_list:
                 if v1:
                    v1.validate()
        if self.cn_province_list:
            for v1 in self.cn_province_list:
                 if v1:
                    v1.validate()
        if self.overseas_list:
            for v1 in self.overseas_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cn_count is not None:
            result['CnCount'] = self.cn_count

        result['CnList'] = []
        if self.cn_list is not None:
            for k1 in self.cn_list:
                result['CnList'].append(k1.to_map() if k1 else None)

        result['CnProvinceList'] = []
        if self.cn_province_list is not None:
            for k1 in self.cn_province_list:
                result['CnProvinceList'].append(k1.to_map() if k1 else None)

        if self.overseas_count is not None:
            result['OverseasCount'] = self.overseas_count

        result['OverseasList'] = []
        if self.overseas_list is not None:
            for k1 in self.overseas_list:
                result['OverseasList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CnCount') is not None:
            self.cn_count = m.get('CnCount')

        self.cn_list = []
        if m.get('CnList') is not None:
            for k1 in m.get('CnList'):
                temp_model = main_models.DescribeLocationInfoResponseBodyCnList()
                self.cn_list.append(temp_model.from_map(k1))

        self.cn_province_list = []
        if m.get('CnProvinceList') is not None:
            for k1 in m.get('CnProvinceList'):
                temp_model = main_models.DescribeLocationInfoResponseBodyCnProvinceList()
                self.cn_province_list.append(temp_model.from_map(k1))

        if m.get('OverseasCount') is not None:
            self.overseas_count = m.get('OverseasCount')

        self.overseas_list = []
        if m.get('OverseasList') is not None:
            for k1 in m.get('OverseasList'):
                temp_model = main_models.DescribeLocationInfoResponseBodyOverseasList()
                self.overseas_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeLocationInfoResponseBodyOverseasList(DaraModel):
    def __init__(
        self,
        loc_id: str = None,
        loc_name: str = None,
    ):
        self.loc_id = loc_id
        self.loc_name = loc_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.loc_id is not None:
            result['LocId'] = self.loc_id

        if self.loc_name is not None:
            result['LocName'] = self.loc_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocId') is not None:
            self.loc_id = m.get('LocId')

        if m.get('LocName') is not None:
            self.loc_name = m.get('LocName')

        return self

class DescribeLocationInfoResponseBodyCnProvinceList(DaraModel):
    def __init__(
        self,
        cities: List[main_models.DescribeLocationInfoResponseBodyCnProvinceListCities] = None,
        province_name: str = None,
    ):
        self.cities = cities
        self.province_name = province_name

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

        if self.province_name is not None:
            result['ProvinceName'] = self.province_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cities = []
        if m.get('Cities') is not None:
            for k1 in m.get('Cities'):
                temp_model = main_models.DescribeLocationInfoResponseBodyCnProvinceListCities()
                self.cities.append(temp_model.from_map(k1))

        if m.get('ProvinceName') is not None:
            self.province_name = m.get('ProvinceName')

        return self

class DescribeLocationInfoResponseBodyCnProvinceListCities(DaraModel):
    def __init__(
        self,
        loc_id: str = None,
        loc_name: str = None,
    ):
        self.loc_id = loc_id
        self.loc_name = loc_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.loc_id is not None:
            result['LocId'] = self.loc_id

        if self.loc_name is not None:
            result['LocName'] = self.loc_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocId') is not None:
            self.loc_id = m.get('LocId')

        if m.get('LocName') is not None:
            self.loc_name = m.get('LocName')

        return self

class DescribeLocationInfoResponseBodyCnList(DaraModel):
    def __init__(
        self,
        loc_id: str = None,
        loc_name: str = None,
    ):
        self.loc_id = loc_id
        self.loc_name = loc_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.loc_id is not None:
            result['LocId'] = self.loc_id

        if self.loc_name is not None:
            result['LocName'] = self.loc_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocId') is not None:
            self.loc_id = m.get('LocId')

        if m.get('LocName') is not None:
            self.loc_name = m.get('LocName')

        return self

