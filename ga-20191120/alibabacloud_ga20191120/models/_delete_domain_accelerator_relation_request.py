# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteDomainAcceleratorRelationRequest(DaraModel):
    def __init__(
        self,
        accelerator_ids: List[str] = None,
        domain: str = None,
        region_id: str = None,
    ):
        # The ID of the GA instance to be disassociated. You can specify up to 50 IDs.
        # 
        # If you leave this parameter empty, all GA instances associated with the specified domain name are disassociated.
        self.accelerator_ids = accelerator_ids
        # The accelerated domain name to be disassociated.
        # 
        # This parameter is required.
        self.domain = domain
        # The ID of the region where the Global Accelerator (GA) instance is deployed. Set the value to **cn-hangzhou**.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerator_ids is not None:
            result['AcceleratorIds'] = self.accelerator_ids

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorIds') is not None:
            self.accelerator_ids = m.get('AcceleratorIds')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

