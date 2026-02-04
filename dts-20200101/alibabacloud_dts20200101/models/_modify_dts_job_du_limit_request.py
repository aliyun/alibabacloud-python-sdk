# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDtsJobDuLimitRequest(DaraModel):
    def __init__(
        self,
        dts_job_id: str = None,
        du_limit: int = None,
        owner_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # The ID of the data migration, data synchronization, or change tracking task.
        # 
        # This parameter is required.
        self.dts_job_id = dts_job_id
        # The upper limit of DUs for the DTS task.
        # 
        # >  Minimum value: **1**.
        # 
        # This parameter is required.
        self.du_limit = du_limit
        self.owner_id = owner_id
        # The ID of the region in which the DTS instance resides.
        self.region_id = region_id
        # Resource group ID.
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

        if self.du_limit is not None:
            result['DuLimit'] = self.du_limit

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

        if m.get('DuLimit') is not None:
            self.du_limit = m.get('DuLimit')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

