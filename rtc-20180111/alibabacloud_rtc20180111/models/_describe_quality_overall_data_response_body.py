# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class DescribeQualityOverallDataResponseBody(DaraModel):
    def __init__(
        self,
        quality_overall_data: List[main_models.DescribeQualityOverallDataResponseBodyQualityOverallData] = None,
        request_id: str = None,
    ):
        self.quality_overall_data = quality_overall_data
        self.request_id = request_id

    def validate(self):
        if self.quality_overall_data:
            for v1 in self.quality_overall_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['QualityOverallData'] = []
        if self.quality_overall_data is not None:
            for k1 in self.quality_overall_data:
                result['QualityOverallData'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.quality_overall_data = []
        if m.get('QualityOverallData') is not None:
            for k1 in m.get('QualityOverallData'):
                temp_model = main_models.DescribeQualityOverallDataResponseBodyQualityOverallData()
                self.quality_overall_data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeQualityOverallDataResponseBodyQualityOverallData(DaraModel):
    def __init__(
        self,
        average: str = None,
        nodes: List[main_models.DescribeQualityOverallDataResponseBodyQualityOverallDataNodes] = None,
        type: str = None,
    ):
        self.average = average
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
        if self.average is not None:
            result['Average'] = self.average

        result['Nodes'] = []
        if self.nodes is not None:
            for k1 in self.nodes:
                result['Nodes'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Average') is not None:
            self.average = m.get('Average')

        self.nodes = []
        if m.get('Nodes') is not None:
            for k1 in m.get('Nodes'):
                temp_model = main_models.DescribeQualityOverallDataResponseBodyQualityOverallDataNodes()
                self.nodes.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeQualityOverallDataResponseBodyQualityOverallDataNodes(DaraModel):
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

