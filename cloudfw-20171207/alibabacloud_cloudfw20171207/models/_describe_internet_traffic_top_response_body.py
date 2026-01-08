# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeInternetTrafficTopResponseBody(DaraModel):
    def __init__(
        self,
        data_count: int = None,
        data_list: List[main_models.DescribeInternetTrafficTopResponseBodyDataList] = None,
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
                temp_model = main_models.DescribeInternetTrafficTopResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k1))

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeInternetTrafficTopResponseBodyDataList(DaraModel):
    def __init__(
        self,
        data_name: str = None,
        data_value: str = None,
        is_subscribed: bool = None,
        label_list: List[str] = None,
        session_count: int = None,
        total_bytes: int = None,
    ):
        self.data_name = data_name
        self.data_value = data_value
        self.is_subscribed = is_subscribed
        self.label_list = label_list
        self.session_count = session_count
        self.total_bytes = total_bytes

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

        if self.is_subscribed is not None:
            result['IsSubscribed'] = self.is_subscribed

        if self.label_list is not None:
            result['LabelList'] = self.label_list

        if self.session_count is not None:
            result['SessionCount'] = self.session_count

        if self.total_bytes is not None:
            result['TotalBytes'] = self.total_bytes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataName') is not None:
            self.data_name = m.get('DataName')

        if m.get('DataValue') is not None:
            self.data_value = m.get('DataValue')

        if m.get('IsSubscribed') is not None:
            self.is_subscribed = m.get('IsSubscribed')

        if m.get('LabelList') is not None:
            self.label_list = m.get('LabelList')

        if m.get('SessionCount') is not None:
            self.session_count = m.get('SessionCount')

        if m.get('TotalBytes') is not None:
            self.total_bytes = m.get('TotalBytes')

        return self

