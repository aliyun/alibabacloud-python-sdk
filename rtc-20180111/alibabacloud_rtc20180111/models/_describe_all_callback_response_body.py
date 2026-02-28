# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class DescribeAllCallbackResponseBody(DaraModel):
    def __init__(
        self,
        callbacks: List[main_models.DescribeAllCallbackResponseBodyCallbacks] = None,
        request_id: str = None,
    ):
        self.callbacks = callbacks
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.callbacks:
            for v1 in self.callbacks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Callbacks'] = []
        if self.callbacks is not None:
            for k1 in self.callbacks:
                result['Callbacks'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.callbacks = []
        if m.get('Callbacks') is not None:
            for k1 in m.get('Callbacks'):
                temp_model = main_models.DescribeAllCallbackResponseBodyCallbacks()
                self.callbacks.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeAllCallbackResponseBodyCallbacks(DaraModel):
    def __init__(
        self,
        category: str = None,
        name: str = None,
        sub_event: List[main_models.DescribeAllCallbackResponseBodyCallbacksSubEvent] = None,
    ):
        self.category = category
        self.name = name
        self.sub_event = sub_event

    def validate(self):
        if self.sub_event:
            for v1 in self.sub_event:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.name is not None:
            result['Name'] = self.name

        result['SubEvent'] = []
        if self.sub_event is not None:
            for k1 in self.sub_event:
                result['SubEvent'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.sub_event = []
        if m.get('SubEvent') is not None:
            for k1 in m.get('SubEvent'):
                temp_model = main_models.DescribeAllCallbackResponseBodyCallbacksSubEvent()
                self.sub_event.append(temp_model.from_map(k1))

        return self

class DescribeAllCallbackResponseBodyCallbacksSubEvent(DaraModel):
    def __init__(
        self,
        event: int = None,
        event_name: str = None,
        type: int = None,
    ):
        self.event = event
        self.event_name = event_name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event is not None:
            result['Event'] = self.event

        if self.event_name is not None:
            result['EventName'] = self.event_name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Event') is not None:
            self.event = m.get('Event')

        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

