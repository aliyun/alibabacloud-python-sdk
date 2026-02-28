# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class DescribeFaultDiagnosisOverallDataResponseBody(DaraModel):
    def __init__(
        self,
        metric_data: main_models.DescribeFaultDiagnosisOverallDataResponseBodyMetricData = None,
        overall_data: main_models.DescribeFaultDiagnosisOverallDataResponseBodyOverallData = None,
        request_id: str = None,
    ):
        self.metric_data = metric_data
        self.overall_data = overall_data
        self.request_id = request_id

    def validate(self):
        if self.metric_data:
            self.metric_data.validate()
        if self.overall_data:
            self.overall_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.metric_data is not None:
            result['MetricData'] = self.metric_data.to_map()

        if self.overall_data is not None:
            result['OverallData'] = self.overall_data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetricData') is not None:
            temp_model = main_models.DescribeFaultDiagnosisOverallDataResponseBodyMetricData()
            self.metric_data = temp_model.from_map(m.get('MetricData'))

        if m.get('OverallData') is not None:
            temp_model = main_models.DescribeFaultDiagnosisOverallDataResponseBodyOverallData()
            self.overall_data = temp_model.from_map(m.get('OverallData'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeFaultDiagnosisOverallDataResponseBodyOverallData(DaraModel):
    def __init__(
        self,
        fault_user_count: int = None,
        fault_user_ratio: float = None,
        total_user_count: int = None,
    ):
        self.fault_user_count = fault_user_count
        self.fault_user_ratio = fault_user_ratio
        self.total_user_count = total_user_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fault_user_count is not None:
            result['FaultUserCount'] = self.fault_user_count

        if self.fault_user_ratio is not None:
            result['FaultUserRatio'] = self.fault_user_ratio

        if self.total_user_count is not None:
            result['TotalUserCount'] = self.total_user_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaultUserCount') is not None:
            self.fault_user_count = m.get('FaultUserCount')

        if m.get('FaultUserRatio') is not None:
            self.fault_user_ratio = m.get('FaultUserRatio')

        if m.get('TotalUserCount') is not None:
            self.total_user_count = m.get('TotalUserCount')

        return self

class DescribeFaultDiagnosisOverallDataResponseBodyMetricData(DaraModel):
    def __init__(
        self,
        nodes: List[main_models.DescribeFaultDiagnosisOverallDataResponseBodyMetricDataNodes] = None,
    ):
        self.nodes = nodes

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k1 in m.get('Nodes'):
                temp_model = main_models.DescribeFaultDiagnosisOverallDataResponseBodyMetricDataNodes()
                self.nodes.append(temp_model.from_map(k1))

        return self

class DescribeFaultDiagnosisOverallDataResponseBodyMetricDataNodes(DaraModel):
    def __init__(
        self,
        ext: Dict[str, Any] = None,
        x: str = None,
        y: str = None,
    ):
        self.ext = ext
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ext is not None:
            result['Ext'] = self.ext

        if self.x is not None:
            result['X'] = self.x

        if self.y is not None:
            result['Y'] = self.y

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')

        if m.get('X') is not None:
            self.x = m.get('X')

        if m.get('Y') is not None:
            self.y = m.get('Y')

        return self

