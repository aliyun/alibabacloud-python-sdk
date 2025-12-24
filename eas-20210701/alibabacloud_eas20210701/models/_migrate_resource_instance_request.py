# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class MigrateResourceInstanceRequest(DaraModel):
    def __init__(
        self,
        dest_resource_id: str = None,
        instance_ids: List[str] = None,
        migrate_to_hybrid: bool = None,
    ):
        # The ID of the destination resource group.
        # 
        # This parameter is required.
        self.dest_resource_id = dest_resource_id
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_ids = instance_ids
        self.migrate_to_hybrid = migrate_to_hybrid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dest_resource_id is not None:
            result['DestResourceId'] = self.dest_resource_id

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.migrate_to_hybrid is not None:
            result['MigrateToHybrid'] = self.migrate_to_hybrid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestResourceId') is not None:
            self.dest_resource_id = m.get('DestResourceId')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('MigrateToHybrid') is not None:
            self.migrate_to_hybrid = m.get('MigrateToHybrid')

        return self

