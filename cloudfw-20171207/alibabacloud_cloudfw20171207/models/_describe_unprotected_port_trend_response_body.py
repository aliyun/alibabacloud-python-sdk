# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeUnprotectedPortTrendResponseBody(DaraModel):
    def __init__(
        self,
        data_list: List[main_models.DescribeUnprotectedPortTrendResponseBodyDataList] = None,
        interval: int = None,
        request_id: str = None,
    ):
        self.data_list = data_list
        self.interval = interval
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
        result['DataList'] = []
        if self.data_list is not None:
            for k1 in self.data_list:
                result['DataList'].append(k1.to_map() if k1 else None)

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k1 in m.get('DataList'):
                temp_model = main_models.DescribeUnprotectedPortTrendResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k1))

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeUnprotectedPortTrendResponseBodyDataList(DaraModel):
    def __init__(
        self,
        count: int = None,
        time: int = None,
    ):
        self.count = count
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.time is not None:
            result['Time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        return self

