# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class ListInstanceHistoryEventsResponseBody(DaraModel):
    def __init__(
        self,
        headers: main_models.ListInstanceHistoryEventsResponseBodyHeaders = None,
        request_id: str = None,
        result: List[main_models.ListInstanceHistoryEventsResponseBodyResult] = None,
    ):
        self.headers = headers
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.headers:
            self.headers.validate()
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.headers is not None:
            result['Headers'] = self.headers.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Headers') is not None:
            temp_model = main_models.ListInstanceHistoryEventsResponseBodyHeaders()
            self.headers = temp_model.from_map(m.get('Headers'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListInstanceHistoryEventsResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class ListInstanceHistoryEventsResponseBodyResult(DaraModel):
    def __init__(
        self,
        ecs_id: str = None,
        event_create_time: str = None,
        event_cycle_status: str = None,
        event_execute_time: str = None,
        event_finash_time: str = None,
        event_level: str = None,
        event_type: str = None,
        instance_id: str = None,
        node_ip: str = None,
        region_id: str = None,
    ):
        self.ecs_id = ecs_id
        self.event_create_time = event_create_time
        self.event_cycle_status = event_cycle_status
        self.event_execute_time = event_execute_time
        self.event_finash_time = event_finash_time
        self.event_level = event_level
        self.event_type = event_type
        self.instance_id = instance_id
        self.node_ip = node_ip
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ecs_id is not None:
            result['ecsId'] = self.ecs_id

        if self.event_create_time is not None:
            result['eventCreateTime'] = self.event_create_time

        if self.event_cycle_status is not None:
            result['eventCycleStatus'] = self.event_cycle_status

        if self.event_execute_time is not None:
            result['eventExecuteTime'] = self.event_execute_time

        if self.event_finash_time is not None:
            result['eventFinashTime'] = self.event_finash_time

        if self.event_level is not None:
            result['eventLevel'] = self.event_level

        if self.event_type is not None:
            result['eventType'] = self.event_type

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.node_ip is not None:
            result['nodeIP'] = self.node_ip

        if self.region_id is not None:
            result['regionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ecsId') is not None:
            self.ecs_id = m.get('ecsId')

        if m.get('eventCreateTime') is not None:
            self.event_create_time = m.get('eventCreateTime')

        if m.get('eventCycleStatus') is not None:
            self.event_cycle_status = m.get('eventCycleStatus')

        if m.get('eventExecuteTime') is not None:
            self.event_execute_time = m.get('eventExecuteTime')

        if m.get('eventFinashTime') is not None:
            self.event_finash_time = m.get('eventFinashTime')

        if m.get('eventLevel') is not None:
            self.event_level = m.get('eventLevel')

        if m.get('eventType') is not None:
            self.event_type = m.get('eventType')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('nodeIP') is not None:
            self.node_ip = m.get('nodeIP')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        return self

class ListInstanceHistoryEventsResponseBodyHeaders(DaraModel):
    def __init__(
        self,
        x_total_count: int = None,
        x_total_failed: int = None,
        x_total_success: int = None,
    ):
        self.x_total_count = x_total_count
        self.x_total_failed = x_total_failed
        self.x_total_success = x_total_success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.x_total_count is not None:
            result['X-Total-Count'] = self.x_total_count

        if self.x_total_failed is not None:
            result['X-Total-Failed'] = self.x_total_failed

        if self.x_total_success is not None:
            result['X-Total-Success'] = self.x_total_success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Total-Count') is not None:
            self.x_total_count = m.get('X-Total-Count')

        if m.get('X-Total-Failed') is not None:
            self.x_total_failed = m.get('X-Total-Failed')

        if m.get('X-Total-Success') is not None:
            self.x_total_success = m.get('X-Total-Success')

        return self

