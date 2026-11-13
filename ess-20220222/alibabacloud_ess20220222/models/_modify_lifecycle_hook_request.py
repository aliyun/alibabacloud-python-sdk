# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyLifecycleHookRequest(DaraModel):
    def __init__(
        self,
        default_result: str = None,
        heartbeat_timeout: int = None,
        lifecycle_action_sources: List[str] = None,
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
        # The subsequent action after the wait state ends. Valid values:
        # - CONTINUE: continues the response to the scale-out activity or the scale-in activity.
        # - ABANDON: releases the ECS instances created during the scale-out activity or removes the ECS instances from the scaling group during the scale-in activity.
        # - ROLLBACK: rejects the release of ECS instances and rolls back the scale-in activity. For a scale-out activity, this value has the same effect as ABANDON, which releases the created ECS instances.
        # 
        # If a scale-in activity occurs and multiple lifecycle hooks are triggered, and the DefaultResult of one lifecycle hook is set to ABANDON or ROLLBACK, the wait states of other lifecycle hooks are ended in advance when the wait state of this hook ends. In other cases, the subsequent action is determined by the last lifecycle hook that ends its wait state.
        self.default_result = default_result
        # The wait time set by the lifecycle hook for the scaling activity. The subsequent action is performed after the wait state times out. Valid values: 30 to 21600. Unit: seconds.
        # 
        # You can call the RecordLifecycleActionHeartbeat operation to extend the wait time of the ECS instance, or call the CompleteLifecycleAction operation to end the wait state of the scaling activity in advance.
        self.heartbeat_timeout = heartbeat_timeout
        # The specific scenarios that trigger the lifecycle hook.
        self.lifecycle_action_sources = lifecycle_action_sources
        # The ID of the lifecycle hook to be modified.
        self.lifecycle_hook_id = lifecycle_hook_id
        # The name of the lifecycle hook to be modified.
        self.lifecycle_hook_name = lifecycle_hook_name
        # The status of the lifecycle hook. Valid values:
        # - Active: enables the lifecycle hook.
        # - InActive: pauses the lifecycle hook.
        # 
        # If you do not specify this parameter, the status of the lifecycle hook remains unchanged.
        # > After a lifecycle hook is created, it is in the Active state by default.
        self.lifecycle_hook_status = lifecycle_hook_status
        # The type of scaling activity to which the lifecycle hook applies. Valid values:
        # - SCALE_OUT: scale-out activity of the scaling group.
        # - SCALE_IN: scale-in activity of the scaling group.
        self.lifecycle_transition = lifecycle_transition
        # The identity of the Notification Recipient for the lifecycle hook. Settings for this parameter support the following notification methods:
        # - Message Service (MNS) queue. Format: acs:mns:{region-id}:{account-id}:queue/{queuename}.
        # - MNS topic. Format: acs:mns:{region-id}:{account-id}:topic/{topicname}.
        # - Operation Orchestration Service (OOS) template. Format: acs:oos:{region-id}:{account-id}:template/{templatename}.
        # - EventBridge. Format: acs:eventbridge:{region-id}:{account-id}:eventbus/default.
        # 
        # Variables in the parameter formats:
        # - region-id: the ID of the region where the scaling group resides.
        # - account-id: the Alibaba Cloud account ID.
        # - queuename: the name of the MNS queue.
        # - topicname: the name of the MNS topic.
        # - templatename: the name of the OOS template.
        self.notification_arn = notification_arn
        # The fixed string information for the wait state of the scaling activity. The value can be up to 4,096 characters in length.
        # 
        # When Auto Scaling pushes a message to the Notification Recipient, it also sends the predefined NotificationMetadata parameter value to help you manage and mark different types of notifications. This parameter takes effect only when the NotificationArn parameter is specified.
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

        if self.lifecycle_action_sources is not None:
            result['LifecycleActionSources'] = self.lifecycle_action_sources

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

        if m.get('LifecycleActionSources') is not None:
            self.lifecycle_action_sources = m.get('LifecycleActionSources')

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

