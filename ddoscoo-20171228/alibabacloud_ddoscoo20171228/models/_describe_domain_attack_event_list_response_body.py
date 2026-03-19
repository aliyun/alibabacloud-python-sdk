# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20171228 import models as main_models
from darabonba.model import DaraModel

class DescribeDomainAttackEventListResponseBody(DaraModel):
    def __init__(
        self,
        data_list: List[main_models.DescribeDomainAttackEventListResponseBodyDataList] = None,
        request_id: str = None,
        total: int = None,
    ):
        self.data_list = data_list
        self.request_id = request_id
        self.total = total

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k1 in m.get('DataList'):
                temp_model = main_models.DescribeDomainAttackEventListResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeDomainAttackEventListResponseBodyDataList(DaraModel):
    def __init__(
        self,
        domain: str = None,
        end_time: int = None,
        max_qps: int = None,
        start_time: int = None,
    ):
        self.domain = domain
        self.end_time = end_time
        self.max_qps = max_qps
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.max_qps is not None:
            result['MaxQps'] = self.max_qps

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('MaxQps') is not None:
            self.max_qps = m.get('MaxQps')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

