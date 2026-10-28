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
        # The output type of the migration object information.
        self.db_object_output_type = db_object_output_type
        # The data migration, data synchronization, or subscribe instance ID.
        self.dts_instance_id = dts_instance_id
        # The ID of the data migration, data synchronization, or change tracking task.
        self.dts_job_id = dts_job_id
        # The region ID of the task. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # Specifies whether to return the information about all synchronization subtasks. Default value: **false**. If this parameter is set to false, only the information about the ongoing or most recently executed synchronization subtask is returned.
        self.sync_sub_job_history = sync_sub_job_history
        # The synchronization direction. Valid values:
        # - **Forward**: forward.
        # - **Reverse**: reverse.
        # 
        # > - Default value: **Forward**.
        # - This parameter takes effect only when you set it to **Reverse** and the synchronization topology of the data synchronization instance is two-way synchronization.
        self.synchronization_direction = synchronization_direction
        # Specifies whether the node is a seamless integration (Zero-ETL) node. Valid values:
        # - **true**: yes.
        # - **false**: no.
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

