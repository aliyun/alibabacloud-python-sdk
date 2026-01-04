# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class BatchEventRedeployInstanceRequest(DaraModel):
    def __init__(
        self,
        event_infos: List[main_models.BatchEventRedeployInstanceRequestEventInfos] = None,
    ):
        # List of events.
        self.event_infos = event_infos

    def validate(self):
        if self.event_infos:
            for v1 in self.event_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EventInfos'] = []
        if self.event_infos is not None:
            for k1 in self.event_infos:
                result['EventInfos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.event_infos = []
        if m.get('EventInfos') is not None:
            for k1 in m.get('EventInfos'):
                temp_model = main_models.BatchEventRedeployInstanceRequestEventInfos()
                self.event_infos.append(temp_model.from_map(k1))

        return self

class BatchEventRedeployInstanceRequestEventInfos(DaraModel):
    def __init__(
        self,
        event_id: str = None,
        ops_type: str = None,
        plan_time: int = None,
        resource_id: str = None,
    ):
        # System event ID.
        self.event_id = event_id
        # Operation type, value range:
        # 
        # - immediate: Execute immediately.
        # - scheduled: Scheduled execution.
        self.ops_type = ops_type
        # Scheduled execution time, in timestamp, unit is milliseconds. This field is required when OpsType=scheduled.
        self.plan_time = plan_time
        # Resource ID.
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.ops_type is not None:
            result['OpsType'] = self.ops_type

        if self.plan_time is not None:
            result['PlanTime'] = self.plan_time

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('OpsType') is not None:
            self.ops_type = m.get('OpsType')

        if m.get('PlanTime') is not None:
            self.plan_time = m.get('PlanTime')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        return self

