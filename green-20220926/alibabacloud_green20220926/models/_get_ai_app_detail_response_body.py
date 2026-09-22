# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_green20220926 import models as main_models
from darabonba.model import DaraModel

class GetAiAppDetailResponseBody(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        chart: main_models.GetAiAppDetailResponseBodyChart = None,
        request_id: str = None,
        risk_events: List[main_models.GetAiAppDetailResponseBodyRiskEvents] = None,
        score: int = None,
        uid: str = None,
    ):
        # appId。
        self.app_id = app_id
        # The application name.
        self.app_name = app_name
        # The chart.
        self.chart = chart
        # The ID assigned by the backend to uniquely identify a request. You can use this ID to troubleshoot issues.
        self.request_id = request_id
        # The risk events.
        self.risk_events = risk_events
        # The score.
        self.score = score
        # UID。
        self.uid = uid

    def validate(self):
        if self.chart:
            self.chart.validate()
        if self.risk_events:
            for v1 in self.risk_events:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.chart is not None:
            result['Chart'] = self.chart.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['RiskEvents'] = []
        if self.risk_events is not None:
            for k1 in self.risk_events:
                result['RiskEvents'].append(k1.to_map() if k1 else None)

        if self.score is not None:
            result['Score'] = self.score

        if self.uid is not None:
            result['Uid'] = self.uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Chart') is not None:
            temp_model = main_models.GetAiAppDetailResponseBodyChart()
            self.chart = temp_model.from_map(m.get('Chart'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.risk_events = []
        if m.get('RiskEvents') is not None:
            for k1 in m.get('RiskEvents'):
                temp_model = main_models.GetAiAppDetailResponseBodyRiskEvents()
                self.risk_events.append(temp_model.from_map(k1))

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        return self

class GetAiAppDetailResponseBodyRiskEvents(DaraModel):
    def __init__(
        self,
        event_code: str = None,
        event_count: int = None,
        event_ids: List[str] = None,
        event_name: str = None,
        event_status: str = None,
        labels: List[main_models.GetAiAppDetailResponseBodyRiskEventsLabels] = None,
    ):
        # The risk event code.
        self.event_code = event_code
        # The number of events.
        self.event_count = event_count
        # The list of risk event IDs.
        self.event_ids = event_ids
        # The risk event name.
        self.event_name = event_name
        # The event status. Valid values:
        # - **unhandled**: Not handled.
        # - **resolved**: Handled.
        self.event_status = event_status
        # The labels.
        self.labels = labels

    def validate(self):
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_code is not None:
            result['EventCode'] = self.event_code

        if self.event_count is not None:
            result['EventCount'] = self.event_count

        if self.event_ids is not None:
            result['EventIds'] = self.event_ids

        if self.event_name is not None:
            result['EventName'] = self.event_name

        if self.event_status is not None:
            result['EventStatus'] = self.event_status

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventCode') is not None:
            self.event_code = m.get('EventCode')

        if m.get('EventCount') is not None:
            self.event_count = m.get('EventCount')

        if m.get('EventIds') is not None:
            self.event_ids = m.get('EventIds')

        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')

        if m.get('EventStatus') is not None:
            self.event_status = m.get('EventStatus')

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.GetAiAppDetailResponseBodyRiskEventsLabels()
                self.labels.append(temp_model.from_map(k1))

        return self

class GetAiAppDetailResponseBodyRiskEventsLabels(DaraModel):
    def __init__(
        self,
        label: str = None,
        label_desc: str = None,
        type: str = None,
    ):
        # The labels.
        self.label = label
        # The label description.
        self.label_desc = label_desc
        # The type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label is not None:
            result['Label'] = self.label

        if self.label_desc is not None:
            result['LabelDesc'] = self.label_desc

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('LabelDesc') is not None:
            self.label_desc = m.get('LabelDesc')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetAiAppDetailResponseBodyChart(DaraModel):
    def __init__(
        self,
        x: List[str] = None,
        y: List[main_models.GetAiAppDetailResponseBodyChartY] = None,
    ):
        # The X value of the coordinate point.
        self.x = x
        # The Y value of the coordinate point.
        self.y = y

    def validate(self):
        if self.y:
            for v1 in self.y:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.x is not None:
            result['X'] = self.x

        result['Y'] = []
        if self.y is not None:
            for k1 in self.y:
                result['Y'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X') is not None:
            self.x = m.get('X')

        self.y = []
        if m.get('Y') is not None:
            for k1 in m.get('Y'):
                temp_model = main_models.GetAiAppDetailResponseBodyChartY()
                self.y.append(temp_model.from_map(k1))

        return self

class GetAiAppDetailResponseBodyChartY(DaraModel):
    def __init__(
        self,
        data: List[int] = None,
        name: str = None,
    ):
        # The returned collection.
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

