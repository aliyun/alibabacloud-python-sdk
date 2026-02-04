# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartDtsJobRequest(DaraModel):
    def __init__(
        self,
        dts_instance_id: str = None,
        dts_job_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        synchronization_direction: str = None,
        zero_etl_job: bool = None,
    ):
        # The ID of the data migration, data synchronization, or change tracking instance.
        # 
        # >  You can call the [DescribeMigrationJobs](https://help.aliyun.com/document_detail/208139.html), [DescribeSubscriptionInstances](https://help.aliyun.com/document_detail/49442.html), or [DescribeSynchronizationJobs](https://help.aliyun.com/document_detail/49454.html) operation to query the instance ID
        self.dts_instance_id = dts_instance_id
        # The ID of the data migration, data synchronization, or change tracking task.
        self.dts_job_id = dts_job_id
        # The region ID of the Data Transmission Service (DTS) instance. For more information, see [List of supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region_id = region_id
        # Resource group ID.
        self.resource_group_id = resource_group_id
        # The synchronization direction. Default value: Forward. Valid values:
        # 
        # *   **Forward**: Data is synchronized from the source database to the destination database.
        # 
        # *   **Reverse**: Data is synchronized from the destination database to the source database.
        # 
        # >You can set this parameter to **Reverse** to start the reverse synchronization task only if the topology is two-way synchronization.
        self.synchronization_direction = synchronization_direction
        # Whether it is a seamless integration (Zero-ETL) task, the value can be:
        # - **false**: No. - **true**: Yes.
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

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')

        if m.get('ZeroEtlJob') is not None:
            self.zero_etl_job = m.get('ZeroEtlJob')

        return self

