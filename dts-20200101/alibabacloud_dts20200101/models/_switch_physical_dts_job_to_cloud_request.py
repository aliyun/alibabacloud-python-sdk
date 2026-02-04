# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SwitchPhysicalDtsJobToCloudRequest(DaraModel):
    def __init__(
        self,
        dts_instance_id: str = None,
        dts_job_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        synchronization_direction: str = None,
    ):
        # Migration, synchronization, or subscription instance ID.
        self.dts_instance_id = dts_instance_id
        # Data migration or synchronization instance ID, which can be queried by calling the **describedtsjobs** interface.
        self.dts_job_id = dts_job_id
        # Region ID. Pass this parameter to specify the region where the instance is located. For more details, see the list of supported regions.
        self.region_id = region_id
        # Resource group ID.
        self.resource_group_id = resource_group_id
        # Synchronization direction, values: - **Forward**: Forward. - **Reverse**: Reverse.
        # > - The default value is **Forward**. - **Reverse** can only be passed when the topology of the data synchronization instance is bidirectional, to release the reverse synchronization link.
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

