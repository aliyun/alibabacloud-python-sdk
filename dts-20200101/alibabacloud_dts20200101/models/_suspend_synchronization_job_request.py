# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SuspendSynchronizationJobRequest(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        owner_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        synchronization_direction: str = None,
        synchronization_job_id: str = None,
    ):
        # The ID of the Alibaba Cloud account. You do not need to specify this parameter because this parameter will be removed in the future.
        self.account_id = account_id
        self.owner_id = owner_id
        # The ID of the region where the data synchronization instance resides. For more information, see [List of supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region_id = region_id
        # Resource GroupId
        self.resource_group_id = resource_group_id
        # The synchronization direction. Valid values:
        # 
        # *   **Forward**
        # *   **Reverse**
        # 
        # > 
        # *   Default value: **Forward**.
        # *   You can set this parameter to **Reverse** to pause reverse synchronization only when the topology is two-way synchronization.
        self.synchronization_direction = synchronization_direction
        # The ID of the data synchronization instance. You can call the **DescribeSynchronizationJobs** operation to query the instance ID.
        # 
        # This parameter is required.
        self.synchronization_job_id = synchronization_job_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction

        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')

        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')

        return self

