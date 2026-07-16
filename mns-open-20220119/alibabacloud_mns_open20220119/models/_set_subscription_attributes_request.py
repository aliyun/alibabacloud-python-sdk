# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_mns_open20220119 import models as main_models
from darabonba.model import DaraModel

class SetSubscriptionAttributesRequest(DaraModel):
    def __init__(
        self,
        dlq_policy: main_models.SetSubscriptionAttributesRequestDlqPolicy = None,
        notify_strategy: str = None,
        sts_role_arn: str = None,
        subscription_name: str = None,
        tenant_rate_limit_policy: main_models.SetSubscriptionAttributesRequestTenantRateLimitPolicy = None,
        topic_name: str = None,
    ):
        # The dead-letter queue policy.
        self.dlq_policy = dlq_policy
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
        self.tenant_rate_limit_policy = tenant_rate_limit_policy
        # The name of the topic.
        # 
        # This parameter is required.
        self.topic_name = topic_name

    def validate(self):
        if self.dlq_policy:
            self.dlq_policy.validate()
        if self.tenant_rate_limit_policy:
            self.tenant_rate_limit_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dlq_policy is not None:
            result['DlqPolicy'] = self.dlq_policy.to_map()

        if self.notify_strategy is not None:
            result['NotifyStrategy'] = self.notify_strategy

        if self.sts_role_arn is not None:
            result['StsRoleArn'] = self.sts_role_arn

        if self.subscription_name is not None:
            result['SubscriptionName'] = self.subscription_name

        if self.tenant_rate_limit_policy is not None:
            result['TenantRateLimitPolicy'] = self.tenant_rate_limit_policy.to_map()

        if self.topic_name is not None:
            result['TopicName'] = self.topic_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DlqPolicy') is not None:
            temp_model = main_models.SetSubscriptionAttributesRequestDlqPolicy()
            self.dlq_policy = temp_model.from_map(m.get('DlqPolicy'))

        if m.get('NotifyStrategy') is not None:
            self.notify_strategy = m.get('NotifyStrategy')

        if m.get('StsRoleArn') is not None:
            self.sts_role_arn = m.get('StsRoleArn')

        if m.get('SubscriptionName') is not None:
            self.subscription_name = m.get('SubscriptionName')

        if m.get('TenantRateLimitPolicy') is not None:
            temp_model = main_models.SetSubscriptionAttributesRequestTenantRateLimitPolicy()
            self.tenant_rate_limit_policy = temp_model.from_map(m.get('TenantRateLimitPolicy'))

        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')

        return self

class SetSubscriptionAttributesRequestTenantRateLimitPolicy(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        max_receives_per_second: int = None,
    ):
        self.enabled = enabled
        self.max_receives_per_second = max_receives_per_second

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.max_receives_per_second is not None:
            result['MaxReceivesPerSecond'] = self.max_receives_per_second

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('MaxReceivesPerSecond') is not None:
            self.max_receives_per_second = m.get('MaxReceivesPerSecond')

        return self

class SetSubscriptionAttributesRequestDlqPolicy(DaraModel):
    def __init__(
        self,
        dead_letter_target_queue: str = None,
        enabled: bool = None,
    ):
        # The destination queue for dead-letter messages.
        self.dead_letter_target_queue = dead_letter_target_queue
        # Whether to enable dead-letter message delivery.
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dead_letter_target_queue is not None:
            result['DeadLetterTargetQueue'] = self.dead_letter_target_queue

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeadLetterTargetQueue') is not None:
            self.dead_letter_target_queue = m.get('DeadLetterTargetQueue')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        return self

