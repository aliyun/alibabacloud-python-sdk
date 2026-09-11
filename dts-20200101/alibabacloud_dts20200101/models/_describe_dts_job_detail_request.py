# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDtsJobDetailRequest(DaraModel):
    def __init__(
        self,
        db_object_output_type: str = None,
        dts_instance_id: str = None,
        dts_job_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        sync_sub_job_history: bool = None,
        synchronization_direction: str = None,
        zero_etl_job: bool = None,
    ):
        self.db_object_output_type = db_object_output_type
        # The instance ID of the data migration, data synchronization, or subscribe instance.
        self.dts_instance_id = dts_instance_id
        # The ID of the data migration, data synchronization, or change tracking task.
        self.dts_job_id = dts_job_id
        # The ID of the region in which the task resides. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # Specifies whether to return information about all synchronization subtasks. Default value: **false**, which returns only the synchronization subtask that is in progress or the most recently executed synchronization subtask.
        self.sync_sub_job_history = sync_sub_job_history
        # The synchronization direction. Valid values:
        # - **Forward**: forward.
        # - **Reverse**: reverse.
        # 
        # > - Default value: **Forward**.
        # - The value **Reverse** takes effect only when the synchronization topology of the data synchronization instance is two-way synchronization.
        self.synchronization_direction = synchronization_direction
        # Specifies whether the task is a zero-ETL task. Valid values:
        # - **true**: The task is a zero-ETL task.
        # - **false**: The task is not a zero-ETL task.
        self.zero_etl_job = zero_etl_job

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_object_output_type is not None:
            result['DbObjectOutputType'] = self.db_object_output_type

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
        if m.get('DbObjectOutputType') is not None:
            self.db_object_output_type = m.get('DbObjectOutputType')

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

