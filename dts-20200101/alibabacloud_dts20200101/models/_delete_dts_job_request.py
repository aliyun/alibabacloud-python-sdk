# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteDtsJobRequest(DaraModel):
    def __init__(
        self,
        dts_instance_id: str = None,
        dts_job_id: str = None,
        job_type: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        synchronization_direction: str = None,
        zero_etl_job: bool = None,
    ):
        # The instance ID of the data migration, synchronization, or subscribe instance.
        self.dts_instance_id = dts_instance_id
        # The ID of the data migration, synchronization, or change tracking task.
        self.dts_job_id = dts_job_id
        # The node type of the DTS instance. Valid values:
        # 
        # - **MIGRATION**: data migration.
        # - **SYNC**: data synchronization.
        # - **SUBSCRIBE**: change tracking.
        self.job_type = job_type
        # The ID of the region where the data migration or synchronization instance resides. For more information, see [List of supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region_id = region_id
        # A special business-specific field. You do not need to pass this parameter.
        self.resource_group_id = resource_group_id
        # The synchronization direction. Valid values:
        # - **Forward**: forward.
        # - **Reverse**: reverse.
        # 
        # > - Default value: **Forward**.
        # - You can set this parameter to **Reverse** to release the reverse synchronization link only if the topology of the data synchronization instance is two-way synchronization.
        self.synchronization_direction = synchronization_direction
        # A special business-specific field. You do not need to pass this parameter.
        self.zero_etl_job = zero_etl_job

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

        if self.job_type is not None:
            result['JobType'] = self.job_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction

        if self.zero_etl_job is not None:
            result['ZeroEtlJob'] = self.zero_etl_job

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')

        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')

        if m.get('ZeroEtlJob') is not None:
            self.zero_etl_job = m.get('ZeroEtlJob')

        return self

