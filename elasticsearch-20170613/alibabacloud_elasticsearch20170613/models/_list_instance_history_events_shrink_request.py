# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class ListInstanceHistoryEventsShrinkRequest(DaraModel):
    def __init__(
        self,
        body: List[main_models.ListInstanceHistoryEventsShrinkRequestBody] = None,
        event_create_end_time: str = None,
        event_create_start_time: str = None,
        event_cycle_status_shrink: str = None,
        event_execute_end_time: str = None,
        event_execute_start_time: str = None,
        event_finash_end_time: str = None,
        event_finash_start_time: str = None,
        event_level_shrink: str = None,
        event_type_shrink: str = None,
        instance_id: str = None,
        node_ip: str = None,
        page: int = None,
        size: int = None,
    ):
        self.body = body
        self.event_create_end_time = event_create_end_time
        self.event_create_start_time = event_create_start_time
        self.event_cycle_status_shrink = event_cycle_status_shrink
        self.event_execute_end_time = event_execute_end_time
        self.event_execute_start_time = event_execute_start_time
        self.event_finash_end_time = event_finash_end_time
        self.event_finash_start_time = event_finash_start_time
        self.event_level_shrink = event_level_shrink
        self.event_type_shrink = event_type_shrink
        self.instance_id = instance_id
        self.node_ip = node_ip
        self.page = page
        self.size = size

    def validate(self):
        if self.body:
            for v1 in self.body:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['body'] = []
        if self.body is not None:
            for k1 in self.body:
                result['body'].append(k1.to_map() if k1 else None)

        if self.event_create_end_time is not None:
            result['eventCreateEndTime'] = self.event_create_end_time

        if self.event_create_start_time is not None:
            result['eventCreateStartTime'] = self.event_create_start_time

        if self.event_cycle_status_shrink is not None:
            result['eventCycleStatus'] = self.event_cycle_status_shrink

        if self.event_execute_end_time is not None:
            result['eventExecuteEndTime'] = self.event_execute_end_time

        if self.event_execute_start_time is not None:
            result['eventExecuteStartTime'] = self.event_execute_start_time

        if self.event_finash_end_time is not None:
            result['eventFinashEndTime'] = self.event_finash_end_time

        if self.event_finash_start_time is not None:
            result['eventFinashStartTime'] = self.event_finash_start_time

        if self.event_level_shrink is not None:
            result['eventLevel'] = self.event_level_shrink

        if self.event_type_shrink is not None:
            result['eventType'] = self.event_type_shrink

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.node_ip is not None:
            result['nodeIP'] = self.node_ip

        if self.page is not None:
            result['page'] = self.page

        if self.size is not None:
            result['size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.body = []
        if m.get('body') is not None:
            for k1 in m.get('body'):
                temp_model = main_models.ListInstanceHistoryEventsShrinkRequestBody()
                self.body.append(temp_model.from_map(k1))

        if m.get('eventCreateEndTime') is not None:
            self.event_create_end_time = m.get('eventCreateEndTime')

        if m.get('eventCreateStartTime') is not None:
            self.event_create_start_time = m.get('eventCreateStartTime')

        if m.get('eventCycleStatus') is not None:
            self.event_cycle_status_shrink = m.get('eventCycleStatus')

        if m.get('eventExecuteEndTime') is not None:
            self.event_execute_end_time = m.get('eventExecuteEndTime')

        if m.get('eventExecuteStartTime') is not None:
            self.event_execute_start_time = m.get('eventExecuteStartTime')

        if m.get('eventFinashEndTime') is not None:
            self.event_finash_end_time = m.get('eventFinashEndTime')

        if m.get('eventFinashStartTime') is not None:
            self.event_finash_start_time = m.get('eventFinashStartTime')

        if m.get('eventLevel') is not None:
            self.event_level_shrink = m.get('eventLevel')

        if m.get('eventType') is not None:
            self.event_type_shrink = m.get('eventType')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('nodeIP') is not None:
            self.node_ip = m.get('nodeIP')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('size') is not None:
            self.size = m.get('size')

        return self

class ListInstanceHistoryEventsShrinkRequestBody(DaraModel):
    def __init__(
        self,
        desc: bool = None,
        sort_field: str = None,
    ):
        self.desc = desc
        self.sort_field = sort_field

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desc is not None:
            result['desc'] = self.desc

        if self.sort_field is not None:
            result['sortField'] = self.sort_field

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('desc') is not None:
            self.desc = m.get('desc')

        if m.get('sortField') is not None:
            self.sort_field = m.get('sortField')

        return self

