# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeNetworkTrafficTopRatioResponseBody(DaraModel):
    def __init__(
        self,
        data_count: int = None,
        data_list: List[main_models.DescribeNetworkTrafficTopRatioResponseBodyDataList] = None,
        data_type: str = None,
        request_id: str = None,
    ):
        self.data_count = data_count
        self.data_list = data_list
        self.data_type = data_type
        self.request_id = request_id

    def validate(self):
        if self.data_list:
            for v1 in self.data_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_count is not None:
            result['DataCount'] = self.data_count

        result['DataList'] = []
        if self.data_list is not None:
            for k1 in self.data_list:
                result['DataList'].append(k1.to_map() if k1 else None)

        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataCount') is not None:
            self.data_count = m.get('DataCount')

        self.data_list = []
        if m.get('DataList') is not None:
            for k1 in m.get('DataList'):
                temp_model = main_models.DescribeNetworkTrafficTopRatioResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k1))

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeNetworkTrafficTopRatioResponseBodyDataList(DaraModel):
    def __init__(
        self,
        data_name: str = None,
        data_value: str = None,
    ):
        self.data_name = data_name
        self.data_value = data_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_name is not None:
            result['DataName'] = self.data_name

        if self.data_value is not None:
            result['DataValue'] = self.data_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataName') is not None:
            self.data_name = m.get('DataName')

        if m.get('DataValue') is not None:
            self.data_value = m.get('DataValue')

        return self

