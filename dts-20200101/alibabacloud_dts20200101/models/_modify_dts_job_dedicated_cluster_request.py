# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDtsJobDedicatedClusterRequest(DaraModel):
    def __init__(
        self,
        dedicated_cluster_id: str = None,
        dts_job_ids: str = None,
        owner_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # The dedicated cluster ID.
        self.dedicated_cluster_id = dedicated_cluster_id
        # The DTS task IDs. The value can be a JSON array that consists of multiple DTS task IDs. Separate the IDs with commas (,).
        self.dts_job_ids = dts_job_ids
        self.owner_id = owner_id
        # The ID of the region where the DTS instance resides.
        # 
        # > For information about the regions that support dedicated clusters, see [DTS dedicated cluster](https://help.aliyun.com/document_detail/417481.html).
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dedicated_cluster_id is not None:
            result['DedicatedClusterId'] = self.dedicated_cluster_id

        if self.dts_job_ids is not None:
            result['DtsJobIds'] = self.dts_job_ids

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedClusterId') is not None:
            self.dedicated_cluster_id = m.get('DedicatedClusterId')

        if m.get('DtsJobIds') is not None:
            self.dts_job_ids = m.get('DtsJobIds')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

