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
        # The description.
        self.description = description
        # Specifies whether to enable the subscription. Enabled by default during creation.
        self.enabled = enabled
        # Optional. The backend derives the name from notifyStrategy if this parameter is not specified.
        self.name = name
        self.notify_strategy = notify_strategy
        self.response_plan = response_plan
        self.subscription = subscription
        # Used exclusively for Update operations. Performs batch create, update, or remove adjustments on member subscriptions.
        self.subscriptions = subscriptions
        # Required for Update. Can be omitted for Create, in which case the backend generates it.
        self.uuid = uuid
        # Required for Update. The value must match the backend record for the write to succeed. If the values do not match, OPTIMISTIC_LOCK_FAILED is returned.
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

