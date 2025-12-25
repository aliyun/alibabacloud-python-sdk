# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class SubscriptionForModify(DaraModel):
    def __init__(
        self,
        description: str = None,
        filter_setting: main_models.FilterSetting = None,
        notify_strategy_id: str = None,
        pushing_setting: main_models.SubscriptionForModifyPushingSetting = None,
        subscription_name: str = None,
    ):
        self.description = description
        self.filter_setting = filter_setting
        self.notify_strategy_id = notify_strategy_id
        self.pushing_setting = pushing_setting
        # This parameter is required.
        self.subscription_name = subscription_name

    def validate(self):
        if self.filter_setting:
            self.filter_setting.validate()
        if self.pushing_setting:
            self.pushing_setting.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        return self

class SubscriptionForModifyPushingSetting(DaraModel):
    def __init__(
        self,
        alert_action_ids: List[str] = None,
        response_plan_id: str = None,
        restore_action_ids: List[str] = None,
        template_uuid: str = None,
    ):
        self.alert_action_ids = alert_action_ids
        self.response_plan_id = response_plan_id
        self.restore_action_ids = restore_action_ids
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

