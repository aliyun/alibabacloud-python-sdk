# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeConsumerChannelRequest(DaraModel):
    def __init__(
        self,
        dts_instance_id: str = None,
        dts_job_id: str = None,
        page_number: int = None,
        page_size: int = None,
        parent_channel_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # The ID of the change tracking instance. You can call the [DescribeDtsJobs](https://help.aliyun.com/document_detail/209702.html) operation to query the instance ID.
        # 
        # >  You must specify at least one of the **DtsInstanceId** and **DtsJobId** parameters.
        self.dts_instance_id = dts_instance_id
        # The ID of the change tracking task. You can call the [DescribeDtsJobs](https://help.aliyun.com/document_detail/209702.html) operation to query the task ID.
        # 
        # >  You must specify at least one of the **DtsInstanceId** and **DtsJobId** parameters.
        self.dts_job_id = dts_job_id
        # The number of the page to return. The value must be an integer that is greater than **0** and does not exceed the maximum value of the Integer data type. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page. Valid values: **1** to **100**. Default value: **20**.
        self.page_size = page_size
        # The parent task ID of the distributed task.
        self.parent_channel_id = parent_channel_id
        # The ID of the region in which the change tracking instance resides. For more information, see [List of supported regions](https://help.aliyun.com/document_detail/141033.html).
        # 
        # This parameter is required.
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
        if self.dts_instance_id is not None:
            result['DtsInstanceId'] = self.dts_instance_id

        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.parent_channel_id is not None:
            result['ParentChannelId'] = self.parent_channel_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')

        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ParentChannelId') is not None:
            self.parent_channel_id = m.get('ParentChannelId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

