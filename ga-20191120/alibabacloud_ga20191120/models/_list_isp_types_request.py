# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListIspTypesRequest(DaraModel):
    def __init__(
        self,
        accelerator_id: str = None,
        accelerator_type: str = None,
        business_region_id: str = None,
    ):
        # The ID of the GA instance that you want to query.
        self.accelerator_id = accelerator_id
        # The type of the Global Accelerator (GA) instance to be queried. Valid values:
        # 
        # *   **basic**: basic GA instance
        # *   **standard**: standard GA instance
        self.accelerator_type = accelerator_type
        # The ID of the acceleration region to be queried.
        # 
        # This parameter is required.
        self.business_region_id = business_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id

        if self.accelerator_type is not None:
            result['AcceleratorType'] = self.accelerator_type

        if self.business_region_id is not None:
            result['BusinessRegionId'] = self.business_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')

        if m.get('AcceleratorType') is not None:
            self.accelerator_type = m.get('AcceleratorType')

        if m.get('BusinessRegionId') is not None:
            self.business_region_id = m.get('BusinessRegionId')

        return self

