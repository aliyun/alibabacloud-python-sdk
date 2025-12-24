# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyLifecycleHookRequest(DaraModel):
    def __init__(
        self,
        default_result: str = None,
        heartbeat_timeout: int = None,
        lifecycle_hook_id: str = None,
        lifecycle_hook_name: str = None,
        lifecycle_hook_status: str = None,
        lifecycle_transition: str = None,
        notification_arn: str = None,
        notification_metadata: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        scaling_group_id: str = None,
    ):
        # The action that you want Auto Scaling to perform after the lifecycle hook ends. Valid values:
        # 
        # *   CONTINUE: Auto Scaling continues to respond to scaling requests.
        # *   ABANDON: Auto Scaling releases Elastic Compute Service (ECS) instances that are created during scale-out activities, or removes ECS instances from the scaling group during scale-in activities.
        # 
        # If multiple lifecycle hooks in a scaling group are triggered during scale-in activities and you set the DefaultResult parameter to ABANDON for the lifecycle hook that you want to modify, Auto Scaling immediately performs the action after the lifecycle hook that you want to modify ends. As a result, other lifecycle hooks end ahead of schedule. In other cases, Auto Scaling performs the action only after all lifecycle hooks end.
        self.default_result = default_result
        # The period of time before the lifecycle hook ends. Auto Scaling performs the specified action after the lifecycle hook ends. Valid values: 30 to 21600. Unit: seconds.
        # 
        # You can call the RecordLifecycleActionHeartbeat operation to prolong the length of a lifecycle hook. You can also call the CompleteLifecycleAction operation to end a lifecycle hook ahead of schedule.
        self.heartbeat_timeout = heartbeat_timeout
        # The ID of the lifecycle hook that you want to modify.
        self.lifecycle_hook_id = lifecycle_hook_id
        # The name of the lifecycle hook that you want to modify.
        self.lifecycle_hook_name = lifecycle_hook_name
        # The status into which you want to put the lifecycle hook. Valid values:
        # 
        # *   Active
        # *   InActive
        # 
        # If you do not specify this parameter, the status of the lifecycle hook remains unchanged after you call this operation.
        # 
        # > By default, a lifecycle hook is in the Active state after you create it.
        self.lifecycle_hook_status = lifecycle_hook_status
        # The type of scaling activity to which the lifecycle hook applies. Valid values:
        # 
        # *   SCALE_OUT
        # *   SCALE_IN
        self.lifecycle_transition = lifecycle_transition
        # The Alibaba Cloud Resource Name (ARN) of the notification recipient. Specify the value in one of the following formats:
        # 
        # *   If you specify a Simple Message Queue (SMQ, formerly MNS) as the notification recipient, specify the value in the acs:mns:{region-id}:{account-id}:queue/{queuename} format.
        # *   If you specify an SMQ topic as the notification recipient, specify the value in the acs:mns:{region-id}:{account-id}:topic/{topicname} format.
        # *   If you specify a CloudOps Orchestration Service (OOS) template as the notification recipient, specify the value in the acs:oos:{region-id}:{account-id}:template/{templatename} format.
        # *   If you specify an event bus as the notification recipient, specify the value in the acs:eventbridge:{region-id}:{account-id}:eventbus/default format.
        # 
        # The variables in the preceding value formats have the following meanings:
        # 
        # *   region-id: the region ID of your scaling group.
        # *   account-id: the ID of your Alibaba Cloud account.
        # *   queuename: the name of the SMQ queue.
        # *   topicname: the name of the SMQ topic.
        # *   templatename: the name of the OOS template.
        self.notification_arn = notification_arn
        # The fixed string that is included in a notification. Auto Scaling sends the notification when the lifecycle hook takes effect. The value of this parameter cannot exceed 4,096 characters in length.
        # 
        # Auto Scaling sends the value specified for the NotificationMetadata parameter together with the notification. This helps you categorize your notifications. The NotificationMetadata parameter takes effect only after you specify the NotificationArn parameter.
        self.notification_metadata = notification_metadata
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the scaling group.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        # The ID of the scaling group to which the lifecycle hook belongs.
        self.scaling_group_id = scaling_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_result is not None:
            result['DefaultResult'] = self.default_result

        if self.heartbeat_timeout is not None:
            result['HeartbeatTimeout'] = self.heartbeat_timeout

        if self.lifecycle_hook_id is not None:
            result['LifecycleHookId'] = self.lifecycle_hook_id

        if self.lifecycle_hook_name is not None:
            result['LifecycleHookName'] = self.lifecycle_hook_name

        if self.lifecycle_hook_status is not None:
            result['LifecycleHookStatus'] = self.lifecycle_hook_status

        if self.lifecycle_transition is not None:
            result['LifecycleTransition'] = self.lifecycle_transition

        if self.notification_arn is not None:
            result['NotificationArn'] = self.notification_arn

        if self.notification_metadata is not None:
            result['NotificationMetadata'] = self.notification_metadata

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

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
        if m.get('DefaultResult') is not None:
            self.default_result = m.get('DefaultResult')

        if m.get('HeartbeatTimeout') is not None:
            self.heartbeat_timeout = m.get('HeartbeatTimeout')

        if m.get('LifecycleHookId') is not None:
            self.lifecycle_hook_id = m.get('LifecycleHookId')

        if m.get('LifecycleHookName') is not None:
            self.lifecycle_hook_name = m.get('LifecycleHookName')

        if m.get('LifecycleHookStatus') is not None:
            self.lifecycle_hook_status = m.get('LifecycleHookStatus')

        if m.get('LifecycleTransition') is not None:
            self.lifecycle_transition = m.get('LifecycleTransition')

        if m.get('NotificationArn') is not None:
            self.notification_arn = m.get('NotificationArn')

        if m.get('NotificationMetadata') is not None:
            self.notification_metadata = m.get('NotificationMetadata')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')

        return self

