# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTrafficControlTaskRequest(DaraModel):
    def __init__(
        self,
        control_target_filter: str = None,
        environment: str = None,
        instance_id: str = None,
        region_id: str = None,
        version: str = None,
    ):
        self.control_target_filter = control_target_filter
        self.environment = environment
        self.instance_id = instance_id
        self.region_id = region_id
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.control_target_filter is not None:
            result['ControlTargetFilter'] = self.control_target_filter

        if self.environment is not None:
            result['Environment'] = self.environment

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ControlTargetFilter') is not None:
            self.control_target_filter = m.get('ControlTargetFilter')

        if m.get('Environment') is not None:
            self.environment = m.get('Environment')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

