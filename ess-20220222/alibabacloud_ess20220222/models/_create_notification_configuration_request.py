# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateNotificationConfigurationRequest(DaraModel):
    def __init__(
        self,
        message_encoding: str = None,
        notification_arn: str = None,
        notification_types: List[str] = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        scaling_group_id: str = None,
        time_zone: str = None,
    ):
        # The encoding method for the notification content. Valid values:
        # 
        # - PlainText: no encoding. The content is transmitted in plaintext.
        # - Base64: Base64 encoding.
        # 
        # Default value: Base64.
        # > The Settings for this parameter are supported only for MNS notification recipients.
        self.message_encoding = message_encoding
        # The identifier of the notification recipient. The following notification methods are supported when you configure the Settings for this parameter:
        # 
        # - Cloud monitoring. Format: `acs:ess:{region-id}:{account-id}:cloudmonitor`.
        # - MNS queue. Format: `acs:mns:{region-id}:{account-id}:queue/{queuename}`.
        # - MNS topic. Format: `acs:mns:{region-id}:{account-id}:topic/{topicname}`.
        # 
        # Variables in the formats:
        # - `region-id`: the ID of the region where the scaling group resides.
        # - `account-id`: the Alibaba Cloud account ID. You can invoke the STS GetCallerIdentity operation to obtain the AccountId response parameter, or view it by clicking your profile picture in the upper-right corner of the Alibaba Cloud Management Console.
        # - `queuename`: the name of the MNS queue.
        # - `topicname`: the name of the MNS topic.
        # 
        # This parameter is required.
        self.notification_arn = notification_arn
        # The types of Auto Scaling events and resource changes for which you want to receive notifications. You can specify multiple values by using a repeated list.
        # 
        # You can invoke the DescribeNotificationTypes operation to query parameter values.
        # 
        # This parameter is required.
        self.notification_types = notification_types
        self.owner_id = owner_id
        # The ID of the region to which the scaling group belongs.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        # The ID of the scaling group.
        # 
        # This parameter is required.
        self.scaling_group_id = scaling_group_id
        # The time zone for notifications.
        # Specify the time zone offset from Coordinated Universal Time (UTC), such as UTC+8 or UTC-7.
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message_encoding is not None:
            result['MessageEncoding'] = self.message_encoding

        if self.notification_arn is not None:
            result['NotificationArn'] = self.notification_arn

        if self.notification_types is not None:
            result['NotificationTypes'] = self.notification_types

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id

        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MessageEncoding') is not None:
            self.message_encoding = m.get('MessageEncoding')

        if m.get('NotificationArn') is not None:
            self.notification_arn = m.get('NotificationArn')

        if m.get('NotificationTypes') is not None:
            self.notification_types = m.get('NotificationTypes')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')

        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')

        return self

