# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class NotifyPolicy(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        enabled: bool = None,
        name: str = None,
        notify_strategy: main_models.NotifyStrategyDetail = None,
        response_plan: main_models.ResponsePlanDetail = None,
        subscription: main_models.SubscriptionDetail = None,
        update_time: str = None,
        user_id: str = None,
        uuid: str = None,
        version: int = None,
        workspace: str = None,
    ):
        # The creation time. The value is a UNIX timestamp string in milliseconds.
        self.create_time = create_time
        # The policy description.
        self.description = description
        # Indicates whether the policy is enabled. This is a read-only field controlled by the Enable or Disable operation.
        self.enabled = enabled
        # The policy name.
        self.name = name
        # The notification policy sub-entity details.
        self.notify_strategy = notify_strategy
        # The response plan sub-entity details.
        self.response_plan = response_plan
        # The subscription sub-entity details.
        self.subscription = subscription
        # The update time. The value is a UNIX timestamp string in milliseconds.
        self.update_time = update_time
        # The Alibaba Cloud account UID.
        self.user_id = user_id
        # The unique identifier of the policy.
        self.uuid = uuid
        # The optimistic locking version number.
        self.version = version
        # The workspace identifier.
        self.workspace = workspace

    def validate(self):
        if self.notify_strategy:
            self.notify_strategy.validate()
        if self.response_plan:
            self.response_plan.validate()
        if self.subscription:
            self.subscription.validate()

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

        if self.name is not None:
            result['name'] = self.name

        if self.notify_strategy is not None:
            result['notifyStrategy'] = self.notify_strategy.to_map()

        if self.response_plan is not None:
            result['responsePlan'] = self.response_plan.to_map()

        if self.subscription is not None:
            result['subscription'] = self.subscription.to_map()

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

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('notifyStrategy') is not None:
            temp_model = main_models.NotifyStrategyDetail()
            self.notify_strategy = temp_model.from_map(m.get('notifyStrategy'))

        if m.get('responsePlan') is not None:
            temp_model = main_models.ResponsePlanDetail()
            self.response_plan = temp_model.from_map(m.get('responsePlan'))

        if m.get('subscription') is not None:
            temp_model = main_models.SubscriptionDetail()
            self.subscription = temp_model.from_map(m.get('subscription'))

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

