# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class SubscriptionForModify(DaraModel):
    def __init__(
        self,
        agent_config: main_models.SubscriptionForModifyAgentConfig = None,
        description: str = None,
        filter_setting: main_models.FilterSetting = None,
        notify_strategy_id: str = None,
        pushing_setting: main_models.SubscriptionForModifyPushingSetting = None,
        subscription_name: str = None,
        workspace_filter_setting: main_models.WorkspaceFilterSetting = None,
    ):
        self.agent_config = agent_config
        # Description.
        self.description = description
        # Filter settings.
        self.filter_setting = filter_setting
        # Notification policy UUID.
        self.notify_strategy_id = notify_strategy_id
        # Push settings.
        self.pushing_setting = pushing_setting
        # Name.
        # 
        # This parameter is required.
        self.subscription_name = subscription_name
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

        if self.description is not None:
            result['description'] = self.description

        if self.filter_setting is not None:
            result['filterSetting'] = self.filter_setting.to_map()

        if self.notify_strategy_id is not None:
            result['notifyStrategyId'] = self.notify_strategy_id

        if self.pushing_setting is not None:
            result['pushingSetting'] = self.pushing_setting.to_map()

        if self.subscription_name is not None:
            result['subscriptionName'] = self.subscription_name

        if self.workspace_filter_setting is not None:
            result['workspaceFilterSetting'] = self.workspace_filter_setting.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentConfig') is not None:
            temp_model = main_models.SubscriptionForModifyAgentConfig()
            self.agent_config = temp_model.from_map(m.get('agentConfig'))

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('filterSetting') is not None:
            temp_model = main_models.FilterSetting()
            self.filter_setting = temp_model.from_map(m.get('filterSetting'))

        if m.get('notifyStrategyId') is not None:
            self.notify_strategy_id = m.get('notifyStrategyId')

        if m.get('pushingSetting') is not None:
            temp_model = main_models.SubscriptionForModifyPushingSetting()
            self.pushing_setting = temp_model.from_map(m.get('pushingSetting'))

        if m.get('subscriptionName') is not None:
            self.subscription_name = m.get('subscriptionName')

        if m.get('workspaceFilterSetting') is not None:
            temp_model = main_models.WorkspaceFilterSetting()
            self.workspace_filter_setting = temp_model.from_map(m.get('workspaceFilterSetting'))

        return self

class SubscriptionForModifyPushingSetting(DaraModel):
    def __init__(
        self,
        alert_action_ids: List[str] = None,
        response_plan_id: str = None,
        restore_action_ids: List[str] = None,
        template_uuid: str = None,
    ):
        # A list of alert push action plan IDs.
        self.alert_action_ids = alert_action_ids
        # Action plan ID.
        self.response_plan_id = response_plan_id
        # A list of action integration plan IDs.
        self.restore_action_ids = restore_action_ids
        # Template UUID.
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

class SubscriptionForModifyAgentConfig(DaraModel):
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

