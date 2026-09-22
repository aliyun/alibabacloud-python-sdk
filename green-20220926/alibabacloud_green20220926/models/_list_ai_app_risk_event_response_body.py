# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_green20220926 import models as main_models
from darabonba.model import DaraModel

class ListAiAppRiskEventResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListAiAppRiskEventResponseBodyData] = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The ID assigned by the backend that uniquely identifies a request. This ID can be used for troubleshooting.
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListAiAppRiskEventResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListAiAppRiskEventResponseBodyData(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        event_code: str = None,
        event_desc: str = None,
        event_desc_en: str = None,
        event_id: str = None,
        event_name: str = None,
        label: str = None,
        label_desc: str = None,
        level: str = None,
        start_time: str = None,
        status: str = None,
        type: str = None,
    ):
        # The end time. Format: YYYY-MM-DD HH:mm:ss.
        self.end_time = end_time
        # The event code that identifies the type or category of the event.
        self.event_code = event_code
        # The event description that provides details about the risk event.
        self.event_desc = event_desc
        # The event description in English.
        self.event_desc_en = event_desc_en
        # The event ID that uniquely identifies a risk event.
        self.event_id = event_id
        # The event name that briefly describes the risk event.
        self.event_name = event_name
        # The label used to mark or categorize the event.
        self.label = label
        # The label description that provides details about the label.
        self.label_desc = label_desc
        # The risk level that indicates the severity of the event, such as high, medium, or low.
        self.level = level
        # The effective period. Format: YYYY-MM-DD HH:mm:ss (default time zone: UTC+08:00).
        self.start_time = start_time
        # The event status that indicates the current processing state of the event, such as pending or resolved.
        self.status = status
        # The event type that indicates the category of the risk event, such as security or performance.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.event_code is not None:
            result['EventCode'] = self.event_code

        if self.event_desc is not None:
            result['EventDesc'] = self.event_desc

        if self.event_desc_en is not None:
            result['EventDescEn'] = self.event_desc_en

        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.event_name is not None:
            result['EventName'] = self.event_name

        if self.label is not None:
            result['Label'] = self.label

        if self.label_desc is not None:
            result['LabelDesc'] = self.label_desc

        if self.level is not None:
            result['Level'] = self.level

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EventCode') is not None:
            self.event_code = m.get('EventCode')

        if m.get('EventDesc') is not None:
            self.event_desc = m.get('EventDesc')

        if m.get('EventDescEn') is not None:
            self.event_desc_en = m.get('EventDescEn')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('LabelDesc') is not None:
            self.label_desc = m.get('LabelDesc')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

