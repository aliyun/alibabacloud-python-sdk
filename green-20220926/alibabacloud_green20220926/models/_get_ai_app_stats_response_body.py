# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_green20220926 import models as main_models
from darabonba.model import DaraModel

class GetAiAppStatsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetAiAppStatsResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The ID assigned by the backend to uniquely identify a request. You can use this ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetAiAppStatsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetAiAppStatsResponseBodyData(DaraModel):
    def __init__(
        self,
        label_stat_chart: List[main_models.GetAiAppStatsResponseBodyDataLabelStatChart] = None,
        total_stat: Dict[str, main_models.DataTotalStatValue] = None,
        x: List[str] = None,
        y: List[main_models.GetAiAppStatsResponseBodyDataY] = None,
    ):
        # The label usage chart.
        self.label_stat_chart = label_stat_chart
        # The total count categorized statistics.
        self.total_stat = total_stat
        # The X value of the coordinate point.
        self.x = x
        # The Y value of the coordinate point.
        self.y = y

    def validate(self):
        if self.label_stat_chart:
            for v1 in self.label_stat_chart:
                 if v1:
                    v1.validate()
        if self.total_stat:
            for v1 in self.total_stat.values():
                 if v1:
                    v1.validate()
        if self.y:
            for v1 in self.y:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LabelStatChart'] = []
        if self.label_stat_chart is not None:
            for k1 in self.label_stat_chart:
                result['LabelStatChart'].append(k1.to_map() if k1 else None)

        result['TotalStat'] = {}
        if self.total_stat is not None:
            for k1, v1 in self.total_stat.items():
                result['TotalStat'][k1] = v1.to_map() if v1 else None

        if self.x is not None:
            result['X'] = self.x

        result['Y'] = []
        if self.y is not None:
            for k1 in self.y:
                result['Y'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.label_stat_chart = []
        if m.get('LabelStatChart') is not None:
            for k1 in m.get('LabelStatChart'):
                temp_model = main_models.GetAiAppStatsResponseBodyDataLabelStatChart()
                self.label_stat_chart.append(temp_model.from_map(k1))

        self.total_stat = {}
        if m.get('TotalStat') is not None:
            for k1, v1 in m.get('TotalStat').items():
                temp_model = main_models.DataTotalStatValue()
                self.total_stat[k1] = temp_model.from_map(v1)

        if m.get('X') is not None:
            self.x = m.get('X')

        self.y = []
        if m.get('Y') is not None:
            for k1 in m.get('Y'):
                temp_model = main_models.GetAiAppStatsResponseBodyDataY()
                self.y.append(temp_model.from_map(k1))

        return self

class GetAiAppStatsResponseBodyDataY(DaraModel):
    def __init__(
        self,
        data: List[int] = None,
        name: str = None,
    ):
        # The returned data.
        self.data = data
        # The name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class GetAiAppStatsResponseBodyDataLabelStatChart(DaraModel):
    def __init__(
        self,
        tree_chart: List[main_models.GetAiAppStatsResponseBodyDataLabelStatChartTreeChart] = None,
    ):
        # The tree chart.
        self.tree_chart = tree_chart

    def validate(self):
        if self.tree_chart:
            for v1 in self.tree_chart:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TreeChart'] = []
        if self.tree_chart is not None:
            for k1 in self.tree_chart:
                result['TreeChart'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tree_chart = []
        if m.get('TreeChart') is not None:
            for k1 in m.get('TreeChart'):
                temp_model = main_models.GetAiAppStatsResponseBodyDataLabelStatChartTreeChart()
                self.tree_chart.append(temp_model.from_map(k1))

        return self

class GetAiAppStatsResponseBodyDataLabelStatChartTreeChart(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        value: str = None,
    ):
        # The label description.
        self.description = description
        # The label.
        self.name = name
        # The score.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

