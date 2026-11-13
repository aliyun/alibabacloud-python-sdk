# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateLifecycleHookRequest(DaraModel):
    def __init__(
        self,
        default_result: str = None,
        heartbeat_timeout: int = None,
        lifecycle_action_sources: List[str] = None,
        lifecycle_hook_name: str = None,
        lifecycle_transition: str = None,
        notification_arn: str = None,
        notification_metadata: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        scaling_group_id: str = None,
    ):
        # The action to be performed after the wait state ends. Valid values:
        # - CONTINUE: continues the response to the scale-out or scale-in activity.
        # - ABANDON: releases the ECS instances created during the scale-out activity or removes the ECS instances from the scaling group during the scale-in activity.
        # - ROLLBACK: rejects the release of ECS instances and rolls back the scale-in activity. For a scale-out activity, this value has the same effect as ABANDON, which releases the created ECS instances.
        # 
        # When a scale-in activity occurs in the scaling group and multiple lifecycle hooks are triggered, if the DefaultResult of one lifecycle hook is set to ABANDON or ROLLBACK and the wait state of the hook ends, the wait states of other lifecycle hooks are ended in advance. In other cases, the action to be performed is determined by the last lifecycle hook whose wait state ends.
        # 
        # Default value: CONTINUE.
        self.default_result = default_result
        # The wait time set by the lifecycle hook for the scaling activity. After the wait state times out, the next action is performed. Valid values: 30 to 21600. Unit: seconds.
        # 
        # After you create a lifecycle hook, you can call the RecordLifecycleActionHeartbeat operation to extend the wait time of the ECS instance, or call the CompleteLifecycleAction operation to end the wait state of the scaling activity in advance. 
        # 
        # Default value: 600.
        self.heartbeat_timeout = heartbeat_timeout
        # The specific scenarios triggered by the lifecycle hook.
        self.lifecycle_action_sources = lifecycle_action_sources
        # The name of the lifecycle hook. The name must be unique within the scaling group. It must be 2 to 64 characters in length, and can contain letters, digits, underscores (_), hyphens (-), and periods (.). It must start with a letter, digit, or Chinese character.
        # 
        # Default value: the value of LifecycleHookId.
        self.lifecycle_hook_name = lifecycle_hook_name
        # The type of scaling activity to which the lifecycle hook applies. Valid values:
        # - SCALE_OUT: scale-out activities of the scaling group.
        # - SCALE_IN: scale-in activities of the scaling group.
        # 
        # This parameter is required.
        self.lifecycle_transition = lifecycle_transition
        # The identifier of the notification recipient for the lifecycle hook. If you do not specify this parameter, no notifications are sent. If you specify this parameter, the following notification methods are supported:
        # - MNS queue. Format: acs:mns:{region-id}:{account-id}:queue/{queuename}.
        # - MNS topic. Format: acs:mns:{region-id}:{account-id}:topic/{topicname}.
        # - OOS template. Format: acs:oos:{region-id}:{account-id}:template/{templatename}.
        # - EventBridge. Format: acs:eventbridge:{region-id}:{account-id}:eventbus/default.
        # 
        # The variables in the formats have the following meanings:
        # - region-id: the ID of the region where the scaling group resides.
        # - account-id: the Alibaba Cloud account ID. The ID of a RAM user is not supported.
        # - queuename: the name of the MNS queue.
        # - topicname: the name of the MNS topic.
        # - templatename: the name of the OOS template.
        self.notification_arn = notification_arn
        # The notification message pushed to the NotificationArn (notification recipient) when the lifecycle hook pauses the scaling activity. This parameter helps you manage and mark different types of notification messages. You must specify NotificationArn together with this parameter. The value can be up to 4,096 characters in length.
        # 
        # If NotificationArn is set to an OOS template, including a public template or a custom template, NotificationMetadata must be specified as a JSON string that matches the parameters of the OOS template. For example, `{"dbInstanceId": "dds-bp17661e0135****", "modifyMode": "Append"}`, where `dbInstanceId` and `modifyMode` are parameters defined in the OOS template. Some parameters of the OOS template have default values. You must specify the parameters that do not have default values in NotificationMetadata. If you specify a parameter that has a default value, the original default value is overwritten. However, keep the default values for the following parameters to obtain relevant information during the runtime of the scaling activity:
        # 
        # - `regionId`: the region where the scaling activity is executed. Default value: ${regionId}.
        # 
        # - `instanceIds`: the list of instances associated with the scaling activity. Default value: ${instanceIds}.
        # 
        # - `lifecycleHookId`: the ID of the lifecycle hook. Default value: ${lifecycleHookId}.
        # 
        # - `lifecycleActionToken`: the identifier of the wait state of the scaling activity, which is used to end the current suspended action in advance. Default value: ${lifecycleActionToken}.
        # 
        # - `scalingGroupId`: the ID of the scaling group to which the scaling activity belongs. Default value: ${scalingGroupId}.
        # 
        # - `lifecycleActionResult`: the action to be performed after the wait state of the lifecycle hook ends. This parameter is used to end the current suspended action in advance when the OOS template execution fails. When DefaultResult is set to ROLLBACK, the default value of this parameter is ROLLBACK. In other cases, the default value is ABANDON.
        # 
        # > - You can adjust the settings of lifecycleActionResult to overwrite the current default value as needed. Valid values: ABANDON, CONTINUE, ROLLBACK, and ${lifecycleActionResult}.
        # ${lifecycleActionResult} indicates that the value of lifecycleActionResult is the same as the value of DefaultResult.
        # - You can obtain detailed information about the parameters of the corresponding template in the [OOS console](https://oos.console.aliyun.com/).
        self.notification_metadata = notification_metadata
        self.owner_account = owner_account
        self.owner_id = owner_id
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
        if self.default_result is not None:
            result['DefaultResult'] = self.default_result

        if self.heartbeat_timeout is not None:
            result['HeartbeatTimeout'] = self.heartbeat_timeout

        if self.lifecycle_action_sources is not None:
            result['LifecycleActionSources'] = self.lifecycle_action_sources

        if self.lifecycle_hook_name is not None:
            result['LifecycleHookName'] = self.lifecycle_hook_name

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

        if m.get('LifecycleHookName') is not None:
            self.lifecycle_hook_name = m.get('LifecycleHookName')

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

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')

        return self

