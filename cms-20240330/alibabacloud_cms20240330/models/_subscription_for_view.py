# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class SubscriptionForView(DaraModel):
    def __init__(
        self,
        agent_config: main_models.SubscriptionForViewAgentConfig = None,
        create_time: str = None,
        description: str = None,
        enable: bool = None,
        filter_setting: main_models.FilterSetting = None,
        notify_strategy_id: str = None,
        pushing_setting: main_models.SubscriptionForViewPushingSetting = None,
        subscription_id: str = None,
        subscription_name: str = None,
        subscription_type: str = None,
        sync_from_type: str = None,
        update_time: str = None,
        user_id: str = None,
        workspace: str = None,
        workspace_filter_setting: main_models.WorkspaceFilterSetting = None,
    ):
        self.agent_config = agent_config
        # The creation time.
        self.create_time = create_time
        # The description.
        self.description = description
        # Indicates whether the subscription is enabled.
        self.enable = enable
        # The filter settings.
        self.filter_setting = filter_setting
        # The UUID of the notification policy.
        self.notify_strategy_id = notify_strategy_id
        # The push settings.
        self.pushing_setting = pushing_setting
        # The UUID.
        self.subscription_id = subscription_id
        # The name.
        # 
        # This parameter is required.
        self.subscription_name = subscription_name
        self.subscription_type = subscription_type
        # The source type of the synchronization policy.
        self.sync_from_type = sync_from_type
        # The update time.
        self.update_time = update_time
        # The user ID.
        self.user_id = user_id
        # Specifies the workspace.
        self.workspace = workspace
        self.workspace_filter_setting = workspace_filter_setting

    def validate(self):
        if self.agent_config:
            self.agent_config.validate()
        if self.filter_setting:
            self.filter_setting.validate()
        if self.pushing_setting:
            self.pushing_setting.validate()
        if self.workspace_filter_setting:
            self.workspace_filter_setting.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_config is not None:
            result['agentConfig'] = self.agent_config.to_map()

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.description is not None:
            result['description'] = self.description

        if self.enable is not None:
            result['enable'] = self.enable

        if self.filter_setting is not None:
            result['filterSetting'] = self.filter_setting.to_map()

        if self.notify_strategy_id is not None:
            result['notifyStrategyId'] = self.notify_strategy_id

        if self.pushing_setting is not None:
            result['pushingSetting'] = self.pushing_setting.to_map()

        if self.subscription_id is not None:
            result['subscriptionId'] = self.subscription_id

        if self.subscription_name is not None:
            result['subscriptionName'] = self.subscription_name

        if self.subscription_type is not None:
            result['subscriptionType'] = self.subscription_type

        if self.sync_from_type is not None:
            result['syncFromType'] = self.sync_from_type

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        if self.user_id is not None:
            result['userId'] = self.user_id

        if self.workspace is not None:
            result['workspace'] = self.workspace

        if self.workspace_filter_setting is not None:
            result['workspaceFilterSetting'] = self.workspace_filter_setting.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentConfig') is not None:
            temp_model = main_models.SubscriptionForViewAgentConfig()
            self.agent_config = temp_model.from_map(m.get('agentConfig'))

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('filterSetting') is not None:
            temp_model = main_models.FilterSetting()
            self.filter_setting = temp_model.from_map(m.get('filterSetting'))

        if m.get('notifyStrategyId') is not None:
            self.notify_strategy_id = m.get('notifyStrategyId')

        if m.get('pushingSetting') is not None:
            temp_model = main_models.SubscriptionForViewPushingSetting()
            self.pushing_setting = temp_model.from_map(m.get('pushingSetting'))

        if m.get('subscriptionId') is not None:
            self.subscription_id = m.get('subscriptionId')

        if m.get('subscriptionName') is not None:
            self.subscription_name = m.get('subscriptionName')

        if m.get('subscriptionType') is not None:
            self.subscription_type = m.get('subscriptionType')

        if m.get('syncFromType') is not None:
            self.sync_from_type = m.get('syncFromType')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        if m.get('workspaceFilterSetting') is not None:
            temp_model = main_models.WorkspaceFilterSetting()
            self.workspace_filter_setting = temp_model.from_map(m.get('workspaceFilterSetting'))

        return self

class SubscriptionForViewPushingSetting(DaraModel):
    def __init__(
        self,
        alert_action_ids: List[str] = None,
        response_plan_id: str = None,
        restore_action_ids: List[str] = None,
        template_uuid: str = None,
    ):
        # A list of action integration IDs for alert pushes.
        self.alert_action_ids = alert_action_ids
        # The action plan ID.
        self.response_plan_id = response_plan_id
        # A list of action integration IDs for recovery pushes.
        self.restore_action_ids = restore_action_ids
        # The template UUID.
        self.template_uuid = template_uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_action_ids is not None:
            result['alertActionIds'] = self.alert_action_ids

        if self.response_plan_id is not None:
            result['responsePlanId'] = self.response_plan_id

        if self.restore_action_ids is not None:
            result['restoreActionIds'] = self.restore_action_ids

        if self.template_uuid is not None:
            result['templateUuid'] = self.template_uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alertActionIds') is not None:
            self.alert_action_ids = m.get('alertActionIds')

        if m.get('responsePlanId') is not None:
            self.response_plan_id = m.get('responsePlanId')

        if m.get('restoreActionIds') is not None:
            self.restore_action_ids = m.get('restoreActionIds')

        if m.get('templateUuid') is not None:
            self.template_uuid = m.get('templateUuid')

        return self

class SubscriptionForViewAgentConfig(DaraModel):
    def __init__(
        self,
        agent_uuid: str = None,
        routes: List[main_models.NotifyRouteForSubscription] = None,
    ):
        self.agent_uuid = agent_uuid
        self.routes = routes

    def validate(self):
        if self.routes:
            for v1 in self.routes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_uuid is not None:
            result['agentUuid'] = self.agent_uuid

        result['routes'] = []
        if self.routes is not None:
            for k1 in self.routes:
                result['routes'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentUuid') is not None:
            self.agent_uuid = m.get('agentUuid')

        self.routes = []
        if m.get('routes') is not None:
            for k1 in m.get('routes'):
                temp_model = main_models.NotifyRouteForSubscription()
                self.routes.append(temp_model.from_map(k1))

        return self

