# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class PutCustomEventRequest(DaraModel):
    def __init__(
        self,
        event_info: List[main_models.PutCustomEventRequestEventInfo] = None,
        region_id: str = None,
    ):
        # The event details.
        # 
        # This parameter is required.
        self.event_info = event_info
        self.region_id = region_id

    def validate(self):
        if self.event_info:
            for v1 in self.event_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EventInfo'] = []
        if self.event_info is not None:
            for k1 in self.event_info:
                result['EventInfo'].append(k1.to_map() if k1 else None)

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.event_info = []
        if m.get('EventInfo') is not None:
            for k1 in m.get('EventInfo'):
                temp_model = main_models.PutCustomEventRequestEventInfo()
                self.event_info.append(temp_model.from_map(k1))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class PutCustomEventRequestEventInfo(DaraModel):
    def __init__(
        self,
        content: str = None,
        event_name: str = None,
        group_id: str = None,
        time: str = None,
    ):
        # The event content. Valid values of N: 1 to 50.
        # 
        # This parameter is required.
        self.content = content
        # The event name. Valid values of N: 1 to 50.
        # 
        # This parameter is required.
        self.event_name = event_name
        # The ID of the application group. Valid values of N: 1 to 50.
        # 
        # Default value: 0. This value indicates that the event to be reported does not belong to any application group.
        self.group_id = group_id
        # The time when the event occurred.
        # 
        # Format: `yyyyMMddTHHmmss.SSSZ`.
        # 
        # Valid values of N: 1 to 50.
        # 
        # >  You can also specify a UNIX timestamp. Example: 1552199984000. Unit: milliseconds.
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.event_name is not None:
            result['EventName'] = self.event_name

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.time is not None:
            result['Time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        return self

