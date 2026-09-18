# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class SubscriptionAndNotifyStrategyForModify(DaraModel):
    def __init__(
        self,
        description: str = None,
        enabled: bool = None,
        name: str = None,
        notify_strategy: main_models.NotifyStrategyForSNSModify = None,
        response_plan: main_models.IncidentResponsePlanForSNSModify = None,
        subscription: main_models.SubscriptionForSNSModify = None,
        subscriptions: List[main_models.SubscriptionOp] = None,
        uuid: str = None,
        version: int = None,
    ):
        # The description of the alert policy.
        self.description = description
        # Read-only. This parameter does not take effect even if specified. The backend forcibly sets this parameter to true during creation and retains the current value during updates. To enable or disable the policy, call the EnableAlertPolicy or DisableAlertPolicy operation.
        self.enabled = enabled
        # Policy Name of the alert policy. If this parameter is not specified, the backend derives Policy Name from notifyStrategy.
        self.name = name
        # The notification configuration that defines noise reduction rules, notification channel routing, and templates. This parameter is required for Create operations.
        self.notify_strategy = notify_strategy
        # The event management configuration that defines recovery notifications, repeat notifications, automatic recovery, and escalation policies.
        self.response_plan = response_plan
        # The single primary subscription configuration that defines event filter conditions. This parameter is mutually exclusive with subscriptions. Do not specify both parameters at the same time.
        self.subscription = subscription
        # Dedicated to Update operations. Performs batch create, update, or remove adjustments on member subscriptions.
        self.subscriptions = subscriptions
        # The unique identifier of the alert policy. This parameter is required for Update operations. Do not specify this parameter for Create operations because the backend automatically generates the value.
        self.uuid = uuid
        # The optimistic lock version number. This parameter is required for Update operations and must match the current value on the backend. Otherwise, a 409 VersionConflict error is returned. The version number increments by 1 after each successful update.
        self.version = version

    def validate(self):
        if self.notify_strategy:
            self.notify_strategy.validate()
        if self.response_plan:
            self.response_plan.validate()
        if self.subscription:
            self.subscription.validate()
        if self.subscriptions:
            for v1 in self.subscriptions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.name is not None:
            result['name'] = self.name

        if self.notify_strategy is not None:
            result['notifyStrategy'] = self.notify_strategy.to_map()

        if self.response_plan is not None:
            result['responsePlan'] = self.response_plan.to_map()

        if self.subscription is not None:
            result['subscription'] = self.subscription.to_map()

        result['subscriptions'] = []
        if self.subscriptions is not None:
            for k1 in self.subscriptions:
                result['subscriptions'].append(k1.to_map() if k1 else None)

        if self.uuid is not None:
            result['uuid'] = self.uuid

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('notifyStrategy') is not None:
            temp_model = main_models.NotifyStrategyForSNSModify()
            self.notify_strategy = temp_model.from_map(m.get('notifyStrategy'))

        if m.get('responsePlan') is not None:
            temp_model = main_models.IncidentResponsePlanForSNSModify()
            self.response_plan = temp_model.from_map(m.get('responsePlan'))

        if m.get('subscription') is not None:
            temp_model = main_models.SubscriptionForSNSModify()
            self.subscription = temp_model.from_map(m.get('subscription'))

        self.subscriptions = []
        if m.get('subscriptions') is not None:
            for k1 in m.get('subscriptions'):
                temp_model = main_models.SubscriptionOp()
                self.subscriptions.append(temp_model.from_map(k1))

        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

