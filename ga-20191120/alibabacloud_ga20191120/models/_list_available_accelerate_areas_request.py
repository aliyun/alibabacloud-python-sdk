# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAvailableAccelerateAreasRequest(DaraModel):
    def __init__(
        self,
        accelerator_id: str = None,
        access_mode: str = None,
        region_id: str = None,
    ):
        # The ID of the GA instance.
        self.accelerator_id = accelerator_id
        self.access_mode = access_mode
        # The ID of the region where the Global Accelerator (GA) instance is deployed. Set the value to **cn-hangzhou**.
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
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id

        if self.access_mode is not None:
            result['AccessMode'] = self.access_mode

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')

        if m.get('AccessMode') is not None:
            self.access_mode = m.get('AccessMode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

