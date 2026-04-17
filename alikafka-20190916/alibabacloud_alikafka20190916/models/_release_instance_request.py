# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReleaseInstanceRequest(DaraModel):
    def __init__(
        self,
        force_delete_instance: bool = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # Specifies whether to immediately release the physical resources of the instance. Valid values:
        # 
        # *   **true**: The physical resources of the instance are immediately released.
        # *   **false**: The physical resources of the instance are retained for a period of time before they are released.
        self.force_delete_instance = force_delete_instance
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.force_delete_instance is not None:
            result['ForceDeleteInstance'] = self.force_delete_instance

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForceDeleteInstance') is not None:
            self.force_delete_instance = m.get('ForceDeleteInstance')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

