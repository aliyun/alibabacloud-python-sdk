# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hologram20220601 import models as main_models
from darabonba.model import DaraModel

class ListOperationEventsResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListOperationEventsResponseBodyData] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.data = data
        self.page_number = page_number
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count

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

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListOperationEventsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListOperationEventsResponseBodyData(DaraModel):
    def __init__(
        self,
        cancelable: bool = None,
        change_schedule_time: bool = None,
        detail: str = None,
        event_name: str = None,
        event_type: str = None,
        follower_instances: List[main_models.ListOperationEventsResponseBodyDataFollowerInstances] = None,
        id: str = None,
        instance_name: str = None,
        maintain_window: str = None,
        resource_id: str = None,
        schedule_time: str = None,
        state: str = None,
        zone_id: str = None,
    ):
        self.cancelable = cancelable
        self.change_schedule_time = change_schedule_time
        self.detail = detail
        self.event_name = event_name
        self.event_type = event_type
        self.follower_instances = follower_instances
        # Id
        self.id = id
        self.instance_name = instance_name
        self.maintain_window = maintain_window
        self.resource_id = resource_id
        # ScheduleTime
        self.schedule_time = schedule_time
        # State
        self.state = state
        self.zone_id = zone_id

    def validate(self):
        if self.follower_instances:
            for v1 in self.follower_instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cancelable is not None:
            result['Cancelable'] = self.cancelable

        if self.change_schedule_time is not None:
            result['ChangeScheduleTime'] = self.change_schedule_time

        if self.detail is not None:
            result['Detail'] = self.detail

        if self.event_name is not None:
            result['EventName'] = self.event_name

        if self.event_type is not None:
            result['EventType'] = self.event_type

        result['FollowerInstances'] = []
        if self.follower_instances is not None:
            for k1 in self.follower_instances:
                result['FollowerInstances'].append(k1.to_map() if k1 else None)

        if self.id is not None:
            result['Id'] = self.id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.maintain_window is not None:
            result['MaintainWindow'] = self.maintain_window

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time

        if self.state is not None:
            result['State'] = self.state

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cancelable') is not None:
            self.cancelable = m.get('Cancelable')

        if m.get('ChangeScheduleTime') is not None:
            self.change_schedule_time = m.get('ChangeScheduleTime')

        if m.get('Detail') is not None:
            self.detail = m.get('Detail')

        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        self.follower_instances = []
        if m.get('FollowerInstances') is not None:
            for k1 in m.get('FollowerInstances'):
                temp_model = main_models.ListOperationEventsResponseBodyDataFollowerInstances()
                self.follower_instances.append(temp_model.from_map(k1))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('MaintainWindow') is not None:
            self.maintain_window = m.get('MaintainWindow')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class ListOperationEventsResponseBodyDataFollowerInstances(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_name: str = None,
    ):
        self.instance_id = instance_id
        self.instance_name = instance_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        return self

