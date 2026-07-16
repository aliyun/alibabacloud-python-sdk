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
        self.description = description
        self.enabled = enabled
        # Optional. If omitted, the backend derives the name from `notifyStrategy`.
        self.name = name
        self.notify_strategy = notify_strategy
        self.response_plan = response_plan
        self.subscription = subscription
        # For update operations only. Use this parameter to batch create, update, and remove member subscriptions.
        self.subscriptions = subscriptions
        # Required for update operations but optional for create operations. If omitted during creation, the backend automatically generates a UUID.
        self.uuid = uuid
        # Required for update operations. The value must match the current version of the record. If the versions do not match, the request fails with an `OPTIMISTIC_LOCK_FAILED` error.
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

