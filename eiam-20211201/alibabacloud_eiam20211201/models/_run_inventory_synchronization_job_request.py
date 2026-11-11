# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RunInventorySynchronizationJobRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        inventory_source_id: str = None,
        inventory_types: List[str] = None,
    ):
        # The ID of the IDaaS EIAM instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the synchronization target.
        # 
        # This parameter is required.
        self.inventory_source_id = inventory_source_id
        # The resource types.
        self.inventory_types = inventory_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.inventory_source_id is not None:
            result['InventorySourceId'] = self.inventory_source_id

        if self.inventory_types is not None:
            result['InventoryTypes'] = self.inventory_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InventorySourceId') is not None:
            self.inventory_source_id = m.get('InventorySourceId')

        if m.get('InventoryTypes') is not None:
            self.inventory_types = m.get('InventoryTypes')

        return self

