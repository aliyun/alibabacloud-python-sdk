# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeResourceTimelineResponseBody(DaraModel):
    def __init__(
        self,
        available_events: List[main_models.DescribeResourceTimelineResponseBodyAvailableEvents] = None,
        biz_events: List[main_models.DescribeResourceTimelineResponseBodyBizEvents] = None,
        desc: str = None,
        inventory_events: List[main_models.DescribeResourceTimelineResponseBodyInventoryEvents] = None,
        msg: str = None,
        request_id: str = None,
        reserve_events: List[main_models.DescribeResourceTimelineResponseBodyReserveEvents] = None,
    ):
        self.available_events = available_events
        self.biz_events = biz_events
        self.desc = desc
        self.inventory_events = inventory_events
        self.msg = msg
        self.request_id = request_id
        self.reserve_events = reserve_events

    def validate(self):
        if self.available_events:
            for v1 in self.available_events:
                 if v1:
                    v1.validate()
        if self.biz_events:
            for v1 in self.biz_events:
                 if v1:
                    v1.validate()
        if self.inventory_events:
            for v1 in self.inventory_events:
                 if v1:
                    v1.validate()
        if self.reserve_events:
            for v1 in self.reserve_events:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AvailableEvents'] = []
        if self.available_events is not None:
            for k1 in self.available_events:
                result['AvailableEvents'].append(k1.to_map() if k1 else None)

        result['BizEvents'] = []
        if self.biz_events is not None:
            for k1 in self.biz_events:
                result['BizEvents'].append(k1.to_map() if k1 else None)

        if self.desc is not None:
            result['Desc'] = self.desc

        result['InventoryEvents'] = []
        if self.inventory_events is not None:
            for k1 in self.inventory_events:
                result['InventoryEvents'].append(k1.to_map() if k1 else None)

        if self.msg is not None:
            result['Msg'] = self.msg

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ReserveEvents'] = []
        if self.reserve_events is not None:
            for k1 in self.reserve_events:
                result['ReserveEvents'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.available_events = []
        if m.get('AvailableEvents') is not None:
            for k1 in m.get('AvailableEvents'):
                temp_model = main_models.DescribeResourceTimelineResponseBodyAvailableEvents()
                self.available_events.append(temp_model.from_map(k1))

        self.biz_events = []
        if m.get('BizEvents') is not None:
            for k1 in m.get('BizEvents'):
                temp_model = main_models.DescribeResourceTimelineResponseBodyBizEvents()
                self.biz_events.append(temp_model.from_map(k1))

        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        self.inventory_events = []
        if m.get('InventoryEvents') is not None:
            for k1 in m.get('InventoryEvents'):
                temp_model = main_models.DescribeResourceTimelineResponseBodyInventoryEvents()
                self.inventory_events.append(temp_model.from_map(k1))

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.reserve_events = []
        if m.get('ReserveEvents') is not None:
            for k1 in m.get('ReserveEvents'):
                temp_model = main_models.DescribeResourceTimelineResponseBodyReserveEvents()
                self.reserve_events.append(temp_model.from_map(k1))

        return self

class DescribeResourceTimelineResponseBodyReserveEvents(DaraModel):
    def __init__(
        self,
        name: str = None,
        occurrence_time: str = None,
        reason: str = None,
        type: str = None,
    ):
        self.name = name
        self.occurrence_time = occurrence_time
        self.reason = reason
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.occurrence_time is not None:
            result['OccurrenceTime'] = self.occurrence_time

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OccurrenceTime') is not None:
            self.occurrence_time = m.get('OccurrenceTime')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeResourceTimelineResponseBodyInventoryEvents(DaraModel):
    def __init__(
        self,
        name: str = None,
        occurrence_time: str = None,
        reason: str = None,
        type: str = None,
    ):
        self.name = name
        self.occurrence_time = occurrence_time
        self.reason = reason
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.occurrence_time is not None:
            result['OccurrenceTime'] = self.occurrence_time

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OccurrenceTime') is not None:
            self.occurrence_time = m.get('OccurrenceTime')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeResourceTimelineResponseBodyBizEvents(DaraModel):
    def __init__(
        self,
        name: str = None,
        occurrence_time: str = None,
        reason: str = None,
        type: str = None,
    ):
        self.name = name
        self.occurrence_time = occurrence_time
        self.reason = reason
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.occurrence_time is not None:
            result['OccurrenceTime'] = self.occurrence_time

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OccurrenceTime') is not None:
            self.occurrence_time = m.get('OccurrenceTime')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeResourceTimelineResponseBodyAvailableEvents(DaraModel):
    def __init__(
        self,
        name: str = None,
        occurrence_time: str = None,
        reason: str = None,
        type: str = None,
    ):
        self.name = name
        self.occurrence_time = occurrence_time
        self.reason = reason
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.occurrence_time is not None:
            result['OccurrenceTime'] = self.occurrence_time

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OccurrenceTime') is not None:
            self.occurrence_time = m.get('OccurrenceTime')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

