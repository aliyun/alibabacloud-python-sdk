# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSubscriptionsRequest(DaraModel):
    def __init__(
        self,
        agent_uuid: str = None,
        direction: str = None,
        enable: bool = None,
        max_results: int = None,
        next_token: str = None,
        notify_strategy_uuid: str = None,
        order_by: str = None,
        subscription_id: str = None,
        subscription_name: str = None,
        subscription_type: str = None,
        unbound: bool = None,
        workspace: str = None,
    ):
        # The UUID of the AI agent. This parameter is used to filter subscriptions of a specified AI agent.
        self.agent_uuid = agent_uuid
        # The sort order of the returned versions. Valid values:
        # - asc: Ascending order. 
        # - desc: Descending order.
        self.direction = direction
        # Specifies whether the subscription is enabled.
        self.enable = enable
        # The maximum number of results per page.
        self.max_results = max_results
        # The pagination token.
        self.next_token = next_token
        # The UUID of the notification policy. This parameter is used to filter subscriptions that are bound to a specified notification policy. The value is a 32-character string.
        self.notify_strategy_uuid = notify_strategy_uuid
        # The field by which to sort the results.
        self.order_by = order_by
        # The ID of the subscription.
        self.subscription_id = subscription_id
        # The name of the subscription.
        self.subscription_name = subscription_name
        # The type of the subscription. Valid values:
        # - NORMAL: Standard subscription.
        # - AI_AGENT: AI agent subscription.
        self.subscription_type = subscription_type
        # **[Deprecated]** This is an internal reserved parameter. Do not use it.
        self.unbound = unbound
        # The name of the workspace.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_uuid is not None:
            result['agentUuid'] = self.agent_uuid

        if self.direction is not None:
            result['direction'] = self.direction

        if self.enable is not None:
            result['enable'] = self.enable

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.notify_strategy_uuid is not None:
            result['notifyStrategyUuid'] = self.notify_strategy_uuid

        if self.order_by is not None:
            result['orderBy'] = self.order_by

        if self.subscription_id is not None:
            result['subscriptionId'] = self.subscription_id

        if self.subscription_name is not None:
            result['subscriptionName'] = self.subscription_name

        if self.subscription_type is not None:
            result['subscriptionType'] = self.subscription_type

        if self.unbound is not None:
            result['unbound'] = self.unbound

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentUuid') is not None:
            self.agent_uuid = m.get('agentUuid')

        if m.get('direction') is not None:
            self.direction = m.get('direction')

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('notifyStrategyUuid') is not None:
            self.notify_strategy_uuid = m.get('notifyStrategyUuid')

        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')

        if m.get('subscriptionId') is not None:
            self.subscription_id = m.get('subscriptionId')

        if m.get('subscriptionName') is not None:
            self.subscription_name = m.get('subscriptionName')

        if m.get('subscriptionType') is not None:
            self.subscription_type = m.get('subscriptionType')

        if m.get('unbound') is not None:
            self.unbound = m.get('unbound')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

