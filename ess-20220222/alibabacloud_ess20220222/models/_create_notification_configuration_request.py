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
        self.message_encoding = message_encoding
        # The Alibaba Cloud Resource Name (ARN) of the notification recipient. The following list describes the value formats of this parameter:
        # 
        # *   If you specify CloudMonitor as the notification recipient, specify the value in the `acs:ess:{region-id}:{account-id}:cloudmonitor` format.
        # *   If you specify an SMQ queue as the notification recipient, specify the value in the `acs:mns:{region-id}:{account-id}:queue/{queuename}` format.
        # *   If you specify an SMQ topic as the notification recipient, specify the value in the `acs:mns:{region-id}:{account-id}:topic/{topicname}` format.
        # 
        # The variables in the preceding formats have the following meanings:
        # 
        # *   `region-id`: the region ID of the scaling group.
        # *   `account-id`: the ID of the Alibaba Cloud account.
        # *   `queuename`: the name of the SMQ queue.
        # *   `topicname`: the name of the SMQ topic.
        # 
        # This parameter is required.
        self.notification_arn = notification_arn
        # The notification types. Specify multiple IDs in the repeated list form.
        # 
        # You can call the DescribeNotificationTypes operation to query the values of this parameter.
        # 
        # This parameter is required.
        self.notification_types = notification_types
        self.owner_id = owner_id
        # The region ID of the scaling group.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        # The ID of the scaling group.
        # 
        # This parameter is required.
        self.scaling_group_id = scaling_group_id
        # The time zone of the notification. Specify the value in UTC. For example, a value of UTC+8 specifies that the time is 8 hours ahead of Coordinated Universal Time, and a value of UTC-7 specifies that the time is 7 hours behind Coordinated Universal Time.
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

