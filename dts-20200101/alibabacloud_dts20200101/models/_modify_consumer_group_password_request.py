# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyConsumerGroupPasswordRequest(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        consumer_group_id: str = None,
        consumer_group_name: str = None,
        consumer_group_password: str = None,
        consumer_group_user_name: str = None,
        owner_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        subscription_instance_id: str = None,
        consumer_group_new_password: str = None,
    ):
        # The ID of the Alibaba Cloud account. You do not need to specify this parameter because this parameter will be removed in the future.
        self.account_id = account_id
        # The ID of the consumer group. You can call the [DescribeConsumerGroup](https://help.aliyun.com/document_detail/122886.html) operation to query the consumer group ID.
        # 
        # This parameter is required.
        self.consumer_group_id = consumer_group_id
        # The name of the consumer group. The name cannot exceed 128 characters in length. We recommend that you use an informative name for easy identification.
        self.consumer_group_name = consumer_group_name
        # The new password of the consumer group.
        # 
        # *   A password must contain two or more of the following characters: uppercase letters, lowercase letters, digits, and special characters.
        # *   A password must be 8 to 32 characters in length.
        # 
        # This parameter is required.
        self.consumer_group_password = consumer_group_password
        # The username of the consumer group. You can call the [DescribeConsumerGroup](https://help.aliyun.com/document_detail/122886.html) operation to query the username.
        self.consumer_group_user_name = consumer_group_user_name
        self.owner_id = owner_id
        # The ID of the region where the change tracking instance resides. For more information, see [List of supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region_id = region_id
        # Resource group ID.
        self.resource_group_id = resource_group_id
        # The ID of the change tracking instance. You can call the **DescribeSubscriptionInstances** operation to query the instance ID.
        # 
        # This parameter is required.
        self.subscription_instance_id = subscription_instance_id
        # The new password of the consumer group.
        #  
        # *   A password must contain two or more of the following characters: uppercase letters, lowercase letters, digits, and special characters.
        # *   A password must be 8 to 32 characters in length.
        # 
        # This parameter is required.
        self.consumer_group_new_password = consumer_group_new_password

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.consumer_group_id is not None:
            result['ConsumerGroupID'] = self.consumer_group_id

        if self.consumer_group_name is not None:
            result['ConsumerGroupName'] = self.consumer_group_name

        if self.consumer_group_password is not None:
            result['ConsumerGroupPassword'] = self.consumer_group_password

        if self.consumer_group_user_name is not None:
            result['ConsumerGroupUserName'] = self.consumer_group_user_name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.subscription_instance_id is not None:
            result['SubscriptionInstanceId'] = self.subscription_instance_id

        if self.consumer_group_new_password is not None:
            result['consumerGroupNewPassword'] = self.consumer_group_new_password

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('ConsumerGroupID') is not None:
            self.consumer_group_id = m.get('ConsumerGroupID')

        if m.get('ConsumerGroupName') is not None:
            self.consumer_group_name = m.get('ConsumerGroupName')

        if m.get('ConsumerGroupPassword') is not None:
            self.consumer_group_password = m.get('ConsumerGroupPassword')

        if m.get('ConsumerGroupUserName') is not None:
            self.consumer_group_user_name = m.get('ConsumerGroupUserName')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SubscriptionInstanceId') is not None:
            self.subscription_instance_id = m.get('SubscriptionInstanceId')

        if m.get('consumerGroupNewPassword') is not None:
            self.consumer_group_new_password = m.get('consumerGroupNewPassword')

        return self

