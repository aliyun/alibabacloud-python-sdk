# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteMonitoringAgentProcessRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        process_id: str = None,
        process_name: str = None,
        region_id: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The process ID.
        # 
        # > You must configure either `ProcessId` or `ProcessName`.
        self.process_id = process_id
        # The process name.
        # 
        # > You must configure either `ProcessId` or `ProcessName`.
        self.process_name = process_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.process_id is not None:
            result['ProcessId'] = self.process_id

        if self.process_name is not None:
            result['ProcessName'] = self.process_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ProcessId') is not None:
            self.process_id = m.get('ProcessId')

        if m.get('ProcessName') is not None:
            self.process_name = m.get('ProcessName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

