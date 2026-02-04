# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDtsJobConfigRequest(DaraModel):
    def __init__(
        self,
        dts_job_id: str = None,
        owner_id: str = None,
        parameters: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # DTS job ID, which can be queried by calling [DescribeDtsJobs](https://help.aliyun.com/document_detail/209702.html).
        self.dts_job_id = dts_job_id
        self.owner_id = owner_id
        # The parameters that you want to modify. Specify a JSON string. For more information, see [Parameters](https://help.aliyun.com/document_detail/2536412.html).
        self.parameters = parameters
        # The region where the instance is located. For more details, see [List of Supported Regions](https://help.aliyun.com/document_detail/141033.html).
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

