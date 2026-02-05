# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyScheduledTaskRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        frequency: str = None,
        instance_ids: str = None,
        name: str = None,
        scheduled_id: str = None,
        start_time: str = None,
        time_range: str = None,
    ):
        self.description = description
        self.frequency = frequency
        self.instance_ids = instance_ids
        self.name = name
        # This parameter is required.
        self.scheduled_id = scheduled_id
        self.start_time = start_time
        self.time_range = time_range

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.frequency is not None:
            result['Frequency'] = self.frequency

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.name is not None:
            result['Name'] = self.name

        if self.scheduled_id is not None:
            result['ScheduledId'] = self.scheduled_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.time_range is not None:
            result['TimeRange'] = self.time_range

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Frequency') is not None:
            self.frequency = m.get('Frequency')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ScheduledId') is not None:
            self.scheduled_id = m.get('ScheduledId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TimeRange') is not None:
            self.time_range = m.get('TimeRange')

        return self

