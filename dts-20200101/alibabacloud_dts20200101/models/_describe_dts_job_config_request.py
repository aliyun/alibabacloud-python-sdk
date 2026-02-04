# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDtsJobConfigRequest(DaraModel):
    def __init__(
        self,
        dts_job_id: str = None,
        for_acceleration: str = None,
        module: str = None,
        owner_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        self.dts_job_id = dts_job_id
        self.for_acceleration = for_acceleration
        self.module = module
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id

        if self.for_acceleration is not None:
            result['ForAcceleration'] = self.for_acceleration

        if self.module is not None:
            result['Module'] = self.module

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')

        if m.get('ForAcceleration') is not None:
            self.for_acceleration = m.get('ForAcceleration')

        if m.get('Module') is not None:
            self.module = m.get('Module')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

