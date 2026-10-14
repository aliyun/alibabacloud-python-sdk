# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class GetOptimizeTaskResponseBody(DaraModel):
    def __init__(
        self,
        checkpoint: Dict[str, Any] = None,
        config: Dict[str, Any] = None,
        create_time: str = None,
        next_trigger_time: str = None,
        optimize_task_name: str = None,
        region_id: str = None,
        request_id: str = None,
        status: str = None,
        type: str = None,
        update_time: str = None,
    ):
        self.checkpoint = checkpoint
        self.config = config
        self.create_time = create_time
        self.next_trigger_time = next_trigger_time
        self.optimize_task_name = optimize_task_name
        self.region_id = region_id
        self.request_id = request_id
        self.status = status
        self.type = type
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.checkpoint is not None:
            result['checkpoint'] = self.checkpoint

        if self.config is not None:
            result['config'] = self.config

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.next_trigger_time is not None:
            result['nextTriggerTime'] = self.next_trigger_time

        if self.optimize_task_name is not None:
            result['optimizeTaskName'] = self.optimize_task_name

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.status is not None:
            result['status'] = self.status

        if self.type is not None:
            result['type'] = self.type

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('checkpoint') is not None:
            self.checkpoint = m.get('checkpoint')

        if m.get('config') is not None:
            self.config = m.get('config')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('nextTriggerTime') is not None:
            self.next_trigger_time = m.get('nextTriggerTime')

        if m.get('optimizeTaskName') is not None:
            self.optimize_task_name = m.get('optimizeTaskName')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        return self

