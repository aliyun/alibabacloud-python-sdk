# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAcceleratorRequest(DaraModel):
    def __init__(
        self,
        accelerator_id: str = None,
        region_id: str = None,
    ):
        # The ID of the GA instance that you want to query.
        # 
        # This parameter is required.
        self.accelerator_id = accelerator_id
        # The region where the GA instance is deployed. Set the value to **cn-hangzhou**.
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

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

