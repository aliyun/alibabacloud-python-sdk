# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ess20220222 import models as main_models
from darabonba.model import DaraModel

class DescribeLifecycleHooksResponseBody(DaraModel):
    def __init__(
        self,
        lifecycle_hooks: List[main_models.DescribeLifecycleHooksResponseBodyLifecycleHooks] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of lifecycle hooks.
        self.lifecycle_hooks = lifecycle_hooks
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of lifecycle hooks.
        self.total_count = total_count

    def validate(self):
        if self.lifecycle_hooks:
            for v1 in self.lifecycle_hooks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LifecycleHooks'] = []
        if self.lifecycle_hooks is not None:
            for k1 in self.lifecycle_hooks:
                result['LifecycleHooks'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.lifecycle_hooks = []
        if m.get('LifecycleHooks') is not None:
            for k1 in m.get('LifecycleHooks'):
                temp_model = main_models.DescribeLifecycleHooksResponseBodyLifecycleHooks()
                self.lifecycle_hooks.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeLifecycleHooksResponseBodyLifecycleHooks(DaraModel):
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
        scaling_group_id: str = None,
    ):
        # The next action to perform after the wait state of the instance ends.
        self.default_result = default_result
        # The wait time configured in the lifecycle hook for the scaling activity. The next action is performed when the wait time expires.
        self.heartbeat_timeout = heartbeat_timeout
        # The specific scenarios that trigger the lifecycle hook.
        self.lifecycle_action_sources = lifecycle_action_sources
        # The ID of the lifecycle hook.
        self.lifecycle_hook_id = lifecycle_hook_id
        # The name of the lifecycle hook.
        self.lifecycle_hook_name = lifecycle_hook_name
        # The status of the lifecycle hook. Valid values:
        # - Active: The lifecycle hook is active.
        # - InActive: The lifecycle hook is inactive.
        self.lifecycle_hook_status = lifecycle_hook_status
        # The scaling activity type associated with the lifecycle hook.
        self.lifecycle_transition = lifecycle_transition
        # The notification recipient identifier for the lifecycle hook. The parameter format is as follows:
        # - No notification configured: `acs:ess:{region-id}:{account-id}:null/null`.
        # - MNS queue: `acs:mns:{region-id}:{account-id}:queue/{queuename}`.
        # - MNS topic: `acs:mns:{region-id}:{account-id}:topic/{topicname}`.
        # - OOS template: `acs:oos:{region-id}:{account-id}:template/{templatename}`.
        # - EventBridge: `acs:eventbridge:{region-id}:{account-id}:eventbus/default`.
        # 
        # The variables in the parameter format have the following meanings:
        # - region-id: The ID of the region where the scaling group resides.
        # - account-id: The Alibaba Cloud account ID.
        # - queuename: The name of the MNS queue.
        # - topicname: The name of the MNS topic.
        # - templatename: The name of the OOS template.
        self.notification_arn = notification_arn
        # The fixed string information for the wait state of the scaling activity.
        self.notification_metadata = notification_metadata
        # The ID of the scaling group.
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

        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')

        return self

