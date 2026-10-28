# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResetDtsJobRequest(DaraModel):
    def __init__(
        self,
        dts_instance_id: str = None,
        dts_job_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        synchronization_direction: str = None,
    ):
        # The ID of the data synchronization or subscribe instance.
        self.dts_instance_id = dts_instance_id
        # The ID of the data synchronization or change tracking task.
        self.dts_job_id = dts_job_id
        # The region where the DTS instance resides. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The synchronization direction. Valid values:
        # 
        # - **Forward**: Forward.
        # - **Reverse**: Reverse.
        # 
        # > - Default value: **Forward**.
        # - You can set this parameter to **Reverse** to reset the reverse synchronization link only when the data synchronization instance uses a two-way synchronization topology.
        self.synchronization_direction = synchronization_direction

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dts_instance_id is not None:
            result['DtsInstanceId'] = self.dts_instance_id

        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')

        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')

        return self

