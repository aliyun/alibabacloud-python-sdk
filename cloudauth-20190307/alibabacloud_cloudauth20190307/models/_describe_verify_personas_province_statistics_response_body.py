# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudauth20190307 import models as main_models
from darabonba.model import DaraModel

class DescribeVerifyPersonasProvinceStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_object: main_models.DescribeVerifyPersonasProvinceStatisticsResponseBodyResultObject = None,
    ):
        # ID of this request.
        self.request_id = request_id
        # Query result.
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultObject') is not None:
            temp_model = main_models.DescribeVerifyPersonasProvinceStatisticsResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('ResultObject'))

        return self

class DescribeVerifyPersonasProvinceStatisticsResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        all_user_cnt: int = None,
        items: List[main_models.DescribeVerifyPersonasProvinceStatisticsResponseBodyResultObjectItems] = None,
    ):
        # Total number of devices.
        self.all_user_cnt = all_user_cnt
        # Data items.
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
        if self.all_user_cnt is not None:
            result['AllUserCnt'] = self.all_user_cnt

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllUserCnt') is not None:
            self.all_user_cnt = m.get('AllUserCnt')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeVerifyPersonasProvinceStatisticsResponseBodyResultObjectItems()
                self.items.append(temp_model.from_map(k1))

        return self

class DescribeVerifyPersonasProvinceStatisticsResponseBodyResultObjectItems(DaraModel):
    def __init__(
        self,
        province_cnt: int = None,
        province_name: str = None,
        province_rate: str = None,
    ):
        # Total number of devices in the province.
        self.province_cnt = province_cnt
        # Province name.
        self.province_name = province_name
        # Percentage of the total for this province.
        self.province_rate = province_rate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.province_cnt is not None:
            result['ProvinceCnt'] = self.province_cnt

        if self.province_name is not None:
            result['ProvinceName'] = self.province_name

        if self.province_rate is not None:
            result['ProvinceRate'] = self.province_rate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProvinceCnt') is not None:
            self.province_cnt = m.get('ProvinceCnt')

        if m.get('ProvinceName') is not None:
            self.province_name = m.get('ProvinceName')

        if m.get('ProvinceRate') is not None:
            self.province_rate = m.get('ProvinceRate')

        return self

