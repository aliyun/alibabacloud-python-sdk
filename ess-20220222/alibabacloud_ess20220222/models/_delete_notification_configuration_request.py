# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteNotificationConfigurationRequest(DaraModel):
    def __init__(
        self,
        notification_arn: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        scaling_group_id: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the notification recipient. Specify the value in one of the following formats:
        # 
        # *   If you specify CloudMonitor as the notification recipient, specify the value in the acs:ess:{region-id}:{account-id}:cloudmonitor format.
        # *   If you specify a Simple Message Queue (SMQ, formerly MNS) queue as the notification recipient, specify the value in the acs:mns:{region-id}:{account-id}:queue/{queuename} format.
        # *   If you specify an SMQ queue as the notification recipient, specify the value in the acs:mns:{region-id}:{account-id}:topic/{topicname} format.
        # 
        # The variables in the preceding value formats have the following meanings:
        # 
        # *   region-id: the region ID of the scaling group.
        # *   account-id: the ID of your Alibaba Cloud cloud.
        # *   queuename: the name of the SMQ queue.
        # *   topicname: the name of the SMQ topic.
        # 
        # This parameter is required.
        self.notification_arn = notification_arn
        self.owner_id = owner_id
        # The region ID of the scaling group.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        # The ID of the scaling group.
        # 
        # This parameter is required.
        self.scaling_group_id = scaling_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.notification_arn is not None:
            result['NotificationArn'] = self.notification_arn

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NotificationArn') is not None:
            self.notification_arn = m.get('NotificationArn')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')

        return self

