# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteConsumerChannelRequest(DaraModel):
    def __init__(
        self,
        consumer_group_id: str = None,
        dts_instance_id: str = None,
        dts_job_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # The ID of the consumer group. You can call the [DescribeConsumerChannel](https://help.aliyun.com/document_detail/264169.html) operation to query the consumer group ID.
        # 
        # This parameter is required.
        self.consumer_group_id = consumer_group_id
        # The ID of the change tracking instance. You can call the [DescribeDtsJobs](https://help.aliyun.com/document_detail/209702.html) operation to query the instance ID.
        # 
        # >  You must specify at least one of the **DtsInstanceId** and **DtsJobId** parameters.
        self.dts_instance_id = dts_instance_id
        # The ID of the change tracking task. You can call the [DescribeDtsJobs](https://help.aliyun.com/document_detail/209702.html) operation to query the task ID.
        # 
        # >  You must specify at least one of the **DtsInstanceId** and **DtsJobId** parameters.
        self.dts_job_id = dts_job_id
        # The ID of the region where the change tracking instance resides. For more information, see [List of supported regions](https://help.aliyun.com/document_detail/141033.html).
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consumer_group_id is not None:
            result['ConsumerGroupId'] = self.consumer_group_id

        if self.dts_instance_id is not None:
            result['DtsInstanceId'] = self.dts_instance_id

        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumerGroupId') is not None:
            self.consumer_group_id = m.get('ConsumerGroupId')

        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')

        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

