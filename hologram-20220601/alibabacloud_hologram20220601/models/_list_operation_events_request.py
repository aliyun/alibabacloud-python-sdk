# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListOperationEventsRequest(DaraModel):
    def __init__(
        self,
        event_name: str = None,
        event_name_desc: bool = None,
        event_type: str = None,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
        schedule_time_desc: bool = None,
        state: str = None,
    ):
        self.event_name = event_name
        self.event_name_desc = event_name_desc
        self.event_type = event_type
        self.instance_id = instance_id
        self.page_number = page_number
        self.page_size = page_size
        self.schedule_time_desc = schedule_time_desc
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_name is not None:
            result['eventName'] = self.event_name

        if self.event_name_desc is not None:
            result['eventNameDesc'] = self.event_name_desc

        if self.event_type is not None:
            result['eventType'] = self.event_type

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.schedule_time_desc is not None:
            result['scheduleTimeDesc'] = self.schedule_time_desc

        if self.state is not None:
            result['state'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('eventName') is not None:
            self.event_name = m.get('eventName')

        if m.get('eventNameDesc') is not None:
            self.event_name_desc = m.get('eventNameDesc')

        if m.get('eventType') is not None:
            self.event_type = m.get('eventType')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('scheduleTimeDesc') is not None:
            self.schedule_time_desc = m.get('scheduleTimeDesc')

        if m.get('state') is not None:
            self.state = m.get('state')

        return self

