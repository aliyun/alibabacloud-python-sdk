# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateLifecycleHookRequest(DaraModel):
    def __init__(
        self,
        default_result: str = None,
        heartbeat_timeout: int = None,
        lifecycle_hook_name: str = None,
        lifecycle_transition: str = None,
        notification_arn: str = None,
        notification_metadata: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        scaling_group_id: str = None,
    ):
        # The action that you want Auto Scaling to perform after the lifecycle hook times out. Valid values:
        # 
        # *   CONTINUE: Auto Scaling continues to respond to scale-in or scale-out requests.
        # *   ABANDON: Auto Scaling releases Elastic Compute Service (ECS) instances that are created during scale-out activities, or removes ECS instances from the scaling group during scale-in activities.
        # 
        # If multiple lifecycle hooks in a scaling group are triggered during scale-in activities and you set the DefaultResult parameter to ABANDON for one of the lifecycle hooks, Auto Scaling immediately performs the action after the lifecycle hook whose DefaultResult is set to ABANDON times out. As a result, other lifecycle hooks time out ahead of schedule. In other cases, Auto Scaling performs the action only after all lifecycle hooks time out.
        # 
        # Default value: CONTINUE.
        self.default_result = default_result
        # The period of time before the lifecycle hook times out. After the lifecycle hook times out, Auto Scaling performs the default action. Valid values: 30 to 21600. Unit: seconds.
        # 
        # After you create a lifecycle hook, you can call the RecordLifecycleActionHeartbeat operation to prolong the timeout period of the lifecycle hook. You can also call the CompleteLifecycleAction operation to end the timeout period of the lifecycle hook ahead of schedule.
        # 
        # Default value: 600.
        self.heartbeat_timeout = heartbeat_timeout
        # The name of the lifecycle hook. Each lifecycle hook name must be unique within a scaling group. The name must be 2 to 64 characters in length, and can contain letters, digits, underscores (_), hyphens (-), and periods (.). It must start with a letter or a digit.
        # 
        # If you do not specify this parameter, the value of the LifecycleHookId parameter is used.
        self.lifecycle_hook_name = lifecycle_hook_name
        # The type of the scaling activity to which the lifecycle hook applies. Valid values:
        # 
        # *   SCALE_OUT
        # *   SCALE_IN
        # 
        # This parameter is required.
        self.lifecycle_transition = lifecycle_transition
        # The Alibaba Cloud Resource Name (ARN) of the notification recipient. If you do not specify this parameter, no notification is sent when the lifecycle hook takes effect. If you specify this parameter, the value must be in one of the following formats:
        # 
        # *   If you specify a Simple Message Queue (SMQ, formerly MNS) as the notification recipient, specify the value in the acs:mns:{region-id}:{account-id}:queue/{queuename} format.
        # *   If you specify an SMQ topic as the notification recipient, specify the value in the acs:mns:{region-id}:{account-id}:topic/{topicname} format.
        # *   If you specify a CloudOps Orchestration Service (OOS) template as the notification recipient, specify the value in the acs:oos:{region-id}:{account-id}:template/{templatename} format.
        # *   If you specify an event bus as the notification recipient, specify the value in the acs:eventbridge:{region-id}:{account-id}:eventbus/default format.
        # 
        # The variables in the preceding value formats have the following meanings:
        # 
        # *   region-id: the region ID of your scaling group.
        # *   account-id: the ID of the Alibaba Cloud account. IDs of Resource Access Management (RAM) users are not supported.
        # *   queuename: the name of the SMQ queue.
        # *   topicname: the name of the SMQ topic.
        # *   templatename: the name of the OOS template.
        self.notification_arn = notification_arn
        # The notification metadata that is sent when the lifecycle hook takes effect. This helps you manage and categorize notifications in an efficient manner. If you specify this parameter, you must specify the NotificationArn parameter. The parameter value cannot exceed 4,096 characters in length.
        # 
        # If you use the NotificationArn parameter to specify a public or customOOS template, the value of the NotificationMetadata parameter must be a JSON string that contains the OOS template parameters. For example, your OOS template includes the following parameters: `{"dbInstanceId": "dds-bp17661e0135****", "modifyMode": "Append"}`, `dbInstanceId`, and `modifyMode`. Some parameters defined in your OOS template have default values. When you specify the NotificationMetadata parameter, specify parameters that do not have default values. If you specify parameters that have default values, the default values are overwritten. However, the default values of the following parameters must be retained to obtain information about scaling activities that are in progress:
        # 
        # *   `regionId`: the region ID of the scaling activity that is in progress. Default value: ${regionId}.
        # *   `instanceIds`: the IDs of ECS instances that are scaled in in the scaling activity. Default value: ${instanceIds}.
        # *   `lifecycleHookId`: the ID of the lifecycle hook. Default value: ${lifecycleHookId}.
        # *   `lifecycleActionToken`: the token of the lifecycle action. You can use the token to end the timeout period of the lifecycle hook ahead of schedule. Default value: ${lifecycleActionToken}
        # *   `scalingGroupId`: the ID of the scaling group in which the scaling activity is executed. Default value: ${scalingGroupId}.
        # 
        # > You can obtain template parameter information in the [OOS console](https://oos.console.aliyun.com/).
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

