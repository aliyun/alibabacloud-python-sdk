# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDtsJobDetailRequest(DaraModel):
    def __init__(
        self,
        dts_instance_id: str = None,
        dts_job_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        sync_sub_job_history: bool = None,
        synchronization_direction: str = None,
        zero_etl_job: bool = None,
    ):
        # The ID of the data migration, data synchronization, or change tracking instance.
        self.dts_instance_id = dts_instance_id
        # The ID of the data migration, data synchronization, or change tracking task.
        self.dts_job_id = dts_job_id
        # The ID of the region in which the Data Transmission Service (DTS) instance resides. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # Specifies whether to return the information about all data synchronization subtasks. Default value: **false**. A value of false indicates that the system returns only the information about a data synchronization subtask that is running or was most recently run.
        self.sync_sub_job_history = sync_sub_job_history
        # The synchronization direction. Valid values:
        # 
        # *   **Forward**
        # *   **Reverse**
        # 
        # > 
        # 
        # *   The default value is **Forward**.
        # *   The value **Reverse** takes effect only if the topology of the data synchronization instance is two-way synchronization.
        self.synchronization_direction = synchronization_direction
        # Specifies whether to query only zero-extract, transform, load (ETL) integration tasks. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.zero_etl_job = zero_etl_job

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dts_instance_id is not None:
            result['DtsInstanceID'] = self.dts_instance_id

        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.sync_sub_job_history is not None:
            result['SyncSubJobHistory'] = self.sync_sub_job_history

        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction

        if self.zero_etl_job is not None:
            result['ZeroEtlJob'] = self.zero_etl_job

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DtsInstanceID') is not None:
            self.dts_instance_id = m.get('DtsInstanceID')

        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SyncSubJobHistory') is not None:
            self.sync_sub_job_history = m.get('SyncSubJobHistory')

        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')

        if m.get('ZeroEtlJob') is not None:
            self.zero_etl_job = m.get('ZeroEtlJob')

        return self

