# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class DescribeUsageOverallDataResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        usage_overall_data: List[main_models.DescribeUsageOverallDataResponseBodyUsageOverallData] = None,
    ):
        self.request_id = request_id
        self.usage_overall_data = usage_overall_data

    def validate(self):
        if self.usage_overall_data:
            for v1 in self.usage_overall_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['UsageOverallData'] = []
        if self.usage_overall_data is not None:
            for k1 in self.usage_overall_data:
                result['UsageOverallData'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.usage_overall_data = []
        if m.get('UsageOverallData') is not None:
            for k1 in m.get('UsageOverallData'):
                temp_model = main_models.DescribeUsageOverallDataResponseBodyUsageOverallData()
                self.usage_overall_data.append(temp_model.from_map(k1))

        return self

class DescribeUsageOverallDataResponseBodyUsageOverallData(DaraModel):
    def __init__(
        self,
        nodes: List[main_models.DescribeUsageOverallDataResponseBodyUsageOverallDataNodes] = None,
        type: str = None,
    ):
        self.nodes = nodes
        self.type = type

    def validate(self):
        if self.nodes:
            for v1 in self.nodes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Nodes'] = []
        if self.nodes is not None:
            for k1 in self.nodes:
                result['Nodes'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k1 in m.get('Nodes'):
                temp_model = main_models.DescribeUsageOverallDataResponseBodyUsageOverallDataNodes()
                self.nodes.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeUsageOverallDataResponseBodyUsageOverallDataNodes(DaraModel):
    def __init__(
        self,
        x: str = None,
        y: str = None,
    ):
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.x is not None:
            result['X'] = self.x

        if self.y is not None:
            result['Y'] = self.y

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X') is not None:
            self.x = m.get('X')

        if m.get('Y') is not None:
            self.y = m.get('Y')

        return self

