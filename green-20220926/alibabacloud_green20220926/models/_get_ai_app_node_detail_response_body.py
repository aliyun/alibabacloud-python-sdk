# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_green20220926 import models as main_models
from darabonba.model import DaraModel

class GetAiAppNodeDetailResponseBody(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        channel: str = None,
        event_data: List[main_models.GetAiAppNodeDetailResponseBodyEventData] = None,
        node_id: str = None,
        node_name: str = None,
        node_type: str = None,
        request_id: str = None,
        risk_level: str = None,
    ):
        # The application ID.
        self.app_id = app_id
        # The channel information.
        self.channel = channel
        # The list of event data.
        self.event_data = event_data
        # The node ID.
        self.node_id = node_id
        # The node name.
        self.node_name = node_name
        # The node type.
        self.node_type = node_type
        # The ID assigned by the backend to uniquely identify a request. You can use this ID to troubleshoot issues.
        self.request_id = request_id
        # The risk level.
        self.risk_level = risk_level

    def validate(self):
        if self.event_data:
            for v1 in self.event_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.channel is not None:
            result['Channel'] = self.channel

        result['EventData'] = []
        if self.event_data is not None:
            for k1 in self.event_data:
                result['EventData'].append(k1.to_map() if k1 else None)

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Channel') is not None:
            self.channel = m.get('Channel')

        self.event_data = []
        if m.get('EventData') is not None:
            for k1 in m.get('EventData'):
                temp_model = main_models.GetAiAppNodeDetailResponseBodyEventData()
                self.event_data.append(temp_model.from_map(k1))

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        return self

class GetAiAppNodeDetailResponseBodyEventData(DaraModel):
    def __init__(
        self,
        channel: str = None,
        labels: List[main_models.GetAiAppNodeDetailResponseBodyEventDataLabels] = None,
        name: str = None,
        risk_level: str = None,
        time: str = None,
        trace_id: str = None,
        type: str = None,
    ):
        # The channel.
        self.channel = channel
        # The list of labels.
        self.labels = labels
        # The name.
        self.name = name
        # The risk level.
        self.risk_level = risk_level
        # The time when the event occurred. Format: yyyy-MM-dd HH:mm:ss.
        self.time = time
        # The trace ID, which is used to query the exact call information.
        self.trace_id = trace_id
        # The event type.
        self.type = type

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
        if self.channel is not None:
            result['Channel'] = self.channel

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.time is not None:
            result['Time'] = self.time

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.GetAiAppNodeDetailResponseBodyEventDataLabels()
                self.labels.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetAiAppNodeDetailResponseBodyEventDataLabels(DaraModel):
    def __init__(
        self,
        label: str = None,
        label_desc: str = None,
        risk_level: str = None,
    ):
        # The label name.
        self.label = label
        # The label description.
        self.label_desc = label_desc
        # The risk level.
        self.risk_level = risk_level

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

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('LabelDesc') is not None:
            self.label_desc = m.get('LabelDesc')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        return self

