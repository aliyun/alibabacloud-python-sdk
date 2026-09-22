# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_green20220926 import models as main_models
from darabonba.model import DaraModel

class GetAiAppTraceDetailResponseBody(DaraModel):
    def __init__(
        self,
        analysis: str = None,
        app_id: str = None,
        app_name: str = None,
        channel: str = None,
        labels: List[main_models.GetAiAppTraceDetailResponseBodyLabels] = None,
        request_id: str = None,
        trace_id: str = None,
        warning_time: str = None,
    ):
        # The AI analysis result.
        self.analysis = analysis
        # The application ID.
        self.app_id = app_id
        # The application name.
        self.app_name = app_name
        # The application channel.
        self.channel = channel
        # The list of labels.
        self.labels = labels
        # The ID assigned by the backend to uniquely identify a request. You can use this ID to troubleshoot issues.
        self.request_id = request_id
        # The trace ID, which is used to correlate and track alert events.
        self.trace_id = trace_id
        # The alert time. Format: YYYY-MM-DD HH:mm:ss.
        self.warning_time = warning_time

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
        if self.analysis is not None:
            result['Analysis'] = self.analysis

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.channel is not None:
            result['Channel'] = self.channel

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        if self.warning_time is not None:
            result['WarningTime'] = self.warning_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Analysis') is not None:
            self.analysis = m.get('Analysis')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Channel') is not None:
            self.channel = m.get('Channel')

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.GetAiAppTraceDetailResponseBodyLabels()
                self.labels.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        if m.get('WarningTime') is not None:
            self.warning_time = m.get('WarningTime')

        return self

class GetAiAppTraceDetailResponseBodyLabels(DaraModel):
    def __init__(
        self,
        count: int = None,
        label: str = None,
        label_desc: str = None,
        type: str = None,
    ):
        # The count.
        self.count = count
        # The label name.
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
        if self.count is not None:
            result['Count'] = self.count

        if self.label is not None:
            result['Label'] = self.label

        if self.label_desc is not None:
            result['LabelDesc'] = self.label_desc

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('LabelDesc') is not None:
            self.label_desc = m.get('LabelDesc')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

