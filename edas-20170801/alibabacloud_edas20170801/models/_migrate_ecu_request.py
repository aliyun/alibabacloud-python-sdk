# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MigrateEcuRequest(DaraModel):
    def __init__(
        self,
        instance_ids: str = None,
        logical_region_id: str = None,
    ):
        # The IDs of the instances. To specify multiple instances, separate the IDs with commas (,).
        # 
        # This parameter is required.
        self.instance_ids = instance_ids
        # The ID of the namespace.
        # 
        # - A custom namespace ID is in the format `Region ID:Namespace identifier`. Example: cn-beijing:tdy218.
        # 
        # - A default namespace ID is the same as its region ID. Example: cn-beijing.
        self.logical_region_id = logical_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.logical_region_id is not None:
            result['LogicalRegionId'] = self.logical_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('LogicalRegionId') is not None:
            self.logical_region_id = m.get('LogicalRegionId')

        return self

