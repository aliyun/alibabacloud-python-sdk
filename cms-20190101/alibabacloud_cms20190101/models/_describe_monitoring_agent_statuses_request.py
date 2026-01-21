# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeMonitoringAgentStatusesRequest(DaraModel):
    def __init__(
        self,
        host_availability_task_id: str = None,
        instance_ids: str = None,
        region_id: str = None,
    ):
        # The ID of the availability monitoring task.
        self.host_availability_task_id = host_availability_task_id
        # The instance IDs. Separate multiple instance IDs with commas (,).
        self.instance_ids = instance_ids
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.host_availability_task_id is not None:
            result['HostAvailabilityTaskId'] = self.host_availability_task_id

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostAvailabilityTaskId') is not None:
            self.host_availability_task_id = m.get('HostAvailabilityTaskId')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

