# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class SubscriptionAndNotifyStrategyForView(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        enabled: bool = None,
        migration_batch_id: str = None,
        migration_meta: str = None,
        name: str = None,
        notify_strategy: main_models.NotifyStrategyForSNSView = None,
        notify_strategy_uuid: str = None,
        response_plan: main_models.IncidentResponsePlanForSNSView = None,
        subscription: main_models.SubscriptionForSNSView = None,
        subscription_uuid: str = None,
        subscriptions: List[main_models.SubscriptionForView] = None,
        update_time: str = None,
        user_id: str = None,
        uuid: str = None,
        version: int = None,
        workspace: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.enabled = enabled
        self.migration_batch_id = migration_batch_id
        self.migration_meta = migration_meta
        self.name = name
        self.notify_strategy = notify_strategy
        self.notify_strategy_uuid = notify_strategy_uuid
        self.response_plan = response_plan
        self.subscription = subscription
        self.subscription_uuid = subscription_uuid
        self.subscriptions = subscriptions
        self.update_time = update_time
        self.user_id = user_id
        self.uuid = uuid
        self.version = version
        self.workspace = workspace

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
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.description is not None:
            result['description'] = self.description

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.migration_batch_id is not None:
            result['migrationBatchId'] = self.migration_batch_id

        if self.migration_meta is not None:
            result['migrationMeta'] = self.migration_meta

        if self.name is not None:
            result['name'] = self.name

        if self.notify_strategy is not None:
            result['notifyStrategy'] = self.notify_strategy.to_map()

        if self.notify_strategy_uuid is not None:
            result['notifyStrategyUuid'] = self.notify_strategy_uuid

        if self.response_plan is not None:
            result['responsePlan'] = self.response_plan.to_map()

        if self.subscription is not None:
            result['subscription'] = self.subscription.to_map()

        if self.subscription_uuid is not None:
            result['subscriptionUuid'] = self.subscription_uuid

        result['subscriptions'] = []
        if self.subscriptions is not None:
            for k1 in self.subscriptions:
                result['subscriptions'].append(k1.to_map() if k1 else None)

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        if self.user_id is not None:
            result['userId'] = self.user_id

        if self.uuid is not None:
            result['uuid'] = self.uuid

        if self.version is not None:
            result['version'] = self.version

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('migrationBatchId') is not None:
            self.migration_batch_id = m.get('migrationBatchId')

        if m.get('migrationMeta') is not None:
            self.migration_meta = m.get('migrationMeta')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('notifyStrategy') is not None:
            temp_model = main_models.NotifyStrategyForSNSView()
            self.notify_strategy = temp_model.from_map(m.get('notifyStrategy'))

        if m.get('notifyStrategyUuid') is not None:
            self.notify_strategy_uuid = m.get('notifyStrategyUuid')

        if m.get('responsePlan') is not None:
            temp_model = main_models.IncidentResponsePlanForSNSView()
            self.response_plan = temp_model.from_map(m.get('responsePlan'))

        if m.get('subscription') is not None:
            temp_model = main_models.SubscriptionForSNSView()
            self.subscription = temp_model.from_map(m.get('subscription'))

        if m.get('subscriptionUuid') is not None:
            self.subscription_uuid = m.get('subscriptionUuid')

        self.subscriptions = []
        if m.get('subscriptions') is not None:
            for k1 in m.get('subscriptions'):
                temp_model = main_models.SubscriptionForView()
                self.subscriptions.append(temp_model.from_map(k1))

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')

        if m.get('version') is not None:
            self.version = m.get('version')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

