# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyConsumerChannelRequest(DaraModel):
    def __init__(
        self,
        consumer_group_id: str = None,
        consumer_group_name: str = None,
        consumer_group_password: str = None,
        consumer_group_user_name: str = None,
        dts_instance_id: str = None,
        dts_job_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # The ID of the consumer group. You can call the [DescribeConsumerChannel](https://help.aliyun.com/document_detail/264169.html) operation to query the consumer group ID.
        # 
        # This parameter is required.
        self.consumer_group_id = consumer_group_id
        # The name of the consumer group. The name cannot exceed 128 characters in length. We recommend that you use an informative name for easy identification.
        self.consumer_group_name = consumer_group_name
        # The new password of the consumer group.
        # 
        # *   A password must contain two or more of the following characters: uppercase letters, lowercase letters, digits, and special characters.
        # *   A password must be 8 to 32 characters in length.
        self.consumer_group_password = consumer_group_password
        # The new username of the consumer group.
        # 
        # *   A username can contain one or more of the following character types: uppercase letters, lowercase letters, digits, and underscores (_).
        # *   A username cannot exceed 16 characters in length.
        self.consumer_group_user_name = consumer_group_user_name
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
        # Resource group ID.
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

        if self.consumer_group_name is not None:
            result['ConsumerGroupName'] = self.consumer_group_name

        if self.consumer_group_password is not None:
            result['ConsumerGroupPassword'] = self.consumer_group_password

        if self.consumer_group_user_name is not None:
            result['ConsumerGroupUserName'] = self.consumer_group_user_name

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

        if m.get('ConsumerGroupName') is not None:
            self.consumer_group_name = m.get('ConsumerGroupName')

        if m.get('ConsumerGroupPassword') is not None:
            self.consumer_group_password = m.get('ConsumerGroupPassword')

        if m.get('ConsumerGroupUserName') is not None:
            self.consumer_group_user_name = m.get('ConsumerGroupUserName')

        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')

        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

