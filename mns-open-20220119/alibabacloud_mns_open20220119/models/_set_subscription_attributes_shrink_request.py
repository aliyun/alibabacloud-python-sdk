# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetSubscriptionAttributesShrinkRequest(DaraModel):
    def __init__(
        self,
        dlq_policy_shrink: str = None,
        notify_strategy: str = None,
        sts_role_arn: str = None,
        subscription_name: str = None,
        tenant_rate_limit_policy_shrink: str = None,
        topic_name: str = None,
    ):
        # The dead-letter queue policy.
        self.dlq_policy_shrink = dlq_policy_shrink
        # The retry policy for message delivery failures to the endpoint. Valid values:
        # 
        # - BACKOFF_RETRY: backoff retry.
        # 
        # - EXPONENTIAL_DECAY_RETRY: exponential decay retry.
        self.notify_strategy = notify_strategy
        self.sts_role_arn = sts_role_arn
        # The name of the subscription.
        # 
        # This parameter is required.
        self.subscription_name = subscription_name
        self.tenant_rate_limit_policy_shrink = tenant_rate_limit_policy_shrink
        # The name of the topic.
        # 
        # This parameter is required.
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dlq_policy_shrink is not None:
            result['DlqPolicy'] = self.dlq_policy_shrink

        if self.notify_strategy is not None:
            result['NotifyStrategy'] = self.notify_strategy

        if self.sts_role_arn is not None:
            result['StsRoleArn'] = self.sts_role_arn

        if self.subscription_name is not None:
            result['SubscriptionName'] = self.subscription_name

        if self.tenant_rate_limit_policy_shrink is not None:
            result['TenantRateLimitPolicy'] = self.tenant_rate_limit_policy_shrink

        if self.topic_name is not None:
            result['TopicName'] = self.topic_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DlqPolicy') is not None:
            self.dlq_policy_shrink = m.get('DlqPolicy')

        if m.get('NotifyStrategy') is not None:
            self.notify_strategy = m.get('NotifyStrategy')

        if m.get('StsRoleArn') is not None:
            self.sts_role_arn = m.get('StsRoleArn')

        if m.get('SubscriptionName') is not None:
            self.subscription_name = m.get('SubscriptionName')

        if m.get('TenantRateLimitPolicy') is not None:
            self.tenant_rate_limit_policy_shrink = m.get('TenantRateLimitPolicy')

        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')

        return self

