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
        # The migration or synchronization instance ID.
        self.dts_instance_id = dts_instance_id
        # The ID of the data migration or synchronization task.
        # 
        # This parameter is required.
        self.dts_job_id = dts_job_id
        # The migration phase. Valid values:
        # - **02**: schema migration phase.
        # - **03**: incremental data migration phase.
        # 
        # This parameter is required.
        self.job_code = job_code
        # The region in which the DTS instance resides. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The type of schema definition. Valid values:
        # 
        # - **before**: schema migration or initial schema synchronization.
        # - **after**: DDL operations during incremental data migration or synchronization.
        self.struct_type = struct_type
        # The synchronization direction. Valid values:
        # - **Forward**: forward.
        # - **Reverse**: reverse.
        # 
        # > - Default value: **Forward**.
        # - You can set this parameter to **Reverse** to release the reverse synchronization link only when the topology of the data synchronization instance is two-way synchronization.
        self.synchronization_direction = synchronization_direction
        # Specifies whether the node is a seamless integration (zero-ETL) node. Valid values:
        # - **true**: The node is a seamless integration node.
        # - **false**: The node is not a seamless integration node.
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

