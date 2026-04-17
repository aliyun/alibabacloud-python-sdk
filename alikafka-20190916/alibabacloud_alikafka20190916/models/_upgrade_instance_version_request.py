# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpgradeInstanceVersionRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        target_version: str = None,
    ):
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the region where the instance resides.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The major version to be upgraded to. Valid values:
        # 
        # *   **0.10.2**
        # *   **2.2.0**
        # 
        # If you set this parameter to the current major version, the system upgrades the instance to the latest minor version.
        # 
        # This parameter is required.
        self.target_version = target_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.target_version is not None:
            result['TargetVersion'] = self.target_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TargetVersion') is not None:
            self.target_version = m.get('TargetVersion')

        return self

