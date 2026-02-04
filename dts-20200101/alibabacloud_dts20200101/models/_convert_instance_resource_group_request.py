# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConvertInstanceResourceGroupRequest(DaraModel):
    def __init__(
        self,
        dts_job_id: str = None,
        new_resource_group_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_id: str = None,
        zero_etl_job: bool = None,
    ):
        # This historical parameter does not take effect and is not required.
        self.dts_job_id = dts_job_id
        # The ID of new resource group. You can obtain the ID on the Resource Group page in the Resource Management console. For more information, see [View basic information about a resource group](https://help.aliyun.com/document_detail/151181.html).
        self.new_resource_group_id = new_resource_group_id
        # The ID of the region in which the Data Transmission Service (DTS) instance resides.
        self.region_id = region_id
        # This parameter is only for special services and not required.
        self.resource_group_id = resource_group_id
        # The ID of the DTS instance. You can view the ID in the **ID/Name** column on the task page in the console.
        # 
        # >  This parameter is required.
        self.resource_id = resource_id
        # This parameter is only for special services and not required.
        self.zero_etl_job = zero_etl_job

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id

        if self.new_resource_group_id is not None:
            result['NewResourceGroupId'] = self.new_resource_group_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.zero_etl_job is not None:
            result['ZeroEtlJob'] = self.zero_etl_job

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')

        if m.get('NewResourceGroupId') is not None:
            self.new_resource_group_id = m.get('NewResourceGroupId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ZeroEtlJob') is not None:
            self.zero_etl_job = m.get('ZeroEtlJob')

        return self

