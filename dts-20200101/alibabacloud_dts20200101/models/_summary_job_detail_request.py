# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SummaryJobDetailRequest(DaraModel):
    def __init__(
        self,
        dts_instance_id: str = None,
        dts_job_id: str = None,
        job_code: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        struct_type: str = None,
        synchronization_direction: str = None,
        zero_etl_job: bool = None,
    ):
        # The ID of the data migration or data synchronization instance.
        # 
        # >  You must specify at least one of the DtsJobId and DtsInstanceId parameters.
        self.dts_instance_id = dts_instance_id
        # The ID of the data migration or data synchronization task.
        # 
        # >  You must specify at least one of the DtsJobId and DtsInstanceId parameters.
        # 
        # This parameter is required.
        self.dts_job_id = dts_job_id
        # The phase of the data migration task. Valid values:
        # 
        # *   **02**: The task is in the schema migration phase.
        # *   **03**: The task is in the incremental migration phase.
        # 
        # This parameter is required.
        self.job_code = job_code
        # The region ID of the DTS instance. For more information, see [List of supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region_id = region_id
        # Resource group ID.
        self.resource_group_id = resource_group_id
        # The type of schema definition. Valid values:
        # 
        # *   **before**: schema migration or initial schema synchronization
        # *   **after**: DDL operations performed during incremental data migration or synchronization
        self.struct_type = struct_type
        # The synchronization direction of the data synchronization task. Valid values:
        # 
        # *   **Forward**: Data is synchronized from the source database to the destination database.
        # *   **Reverse**: Data is synchronized from the destination database to the source database.
        # 
        # > 
        # *   Default value: **Forward**.
        # *   You can set this parameter to **Reverse** to delete the reverse synchronization task only if the topology is two-way synchronization.
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

        if self.job_code is not None:
            result['JobCode'] = self.job_code

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.struct_type is not None:
            result['StructType'] = self.struct_type

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

        if m.get('JobCode') is not None:
            self.job_code = m.get('JobCode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('StructType') is not None:
            self.struct_type = m.get('StructType')

        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')

        if m.get('ZeroEtlJob') is not None:
            self.zero_etl_job = m.get('ZeroEtlJob')

        return self

