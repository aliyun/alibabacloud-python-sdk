# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_mns_open20220119 import models as main_models
from darabonba.model import DaraModel

class GetSubscriptionAttributesResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetSubscriptionAttributesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        # The response code.
        self.code = code
        # The response data.
        self.data = data
        # The response message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # The status of the response.
        self.status = status
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetSubscriptionAttributesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetSubscriptionAttributesResponseBodyData(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        dlq_policy: main_models.GetSubscriptionAttributesResponseBodyDataDlqPolicy = None,
        endpoint: str = None,
        filter_tag: str = None,
        last_modify_time: int = None,
        notify_content_format: str = None,
        notify_strategy: str = None,
        subscription_name: str = None,
        tenant_rate_limit_policy: main_models.GetSubscriptionAttributesResponseBodyDataTenantRateLimitPolicy = None,
        topic_name: str = None,
        topic_owner: str = None,
    ):
        # The time when the subscription was created. The value is a UNIX timestamp that represents the number of seconds that have elapsed since 00:00:00 on January 1, 1970.
        self.create_time = create_time
        # The dead-letter queue policy.
        self.dlq_policy = dlq_policy
        # The endpoint of the subscription.
        self.endpoint = endpoint
        # The tag used for message filtering. Only messages that have a matching tag are pushed.
        self.filter_tag = filter_tag
        # The time when the subscription properties were last modified. The value is a UNIX timestamp that represents the number of seconds that have elapsed since 00:00:00 on January 1, 1970.
        self.last_modify_time = last_modify_time
        # The format of the message content that is pushed to an endpoint.
        # Valid values:
        # 
        # - XML
        # 
        # - JSON
        # 
        # - SIMPLIFIED
        self.notify_content_format = notify_content_format
        # The retry policy that is used when a message fails to be pushed to an endpoint. Valid values:
        # 
        # - BACKOFF_RETRY: backoff retry.
        # 
        # - EXPONENTIAL_DECAY_RETRY: exponential decay retry.
        self.notify_strategy = notify_strategy
        # The name of the subscription.
        self.subscription_name = subscription_name
        self.tenant_rate_limit_policy = tenant_rate_limit_policy
        # The name of the topic to which the subscription belongs.
        self.topic_name = topic_name
        # The AccountId of the owner of the topic to which the subscription belongs.
        self.topic_owner = topic_owner

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
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.dlq_policy is not None:
            result['DlqPolicy'] = self.dlq_policy.to_map()

        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.filter_tag is not None:
            result['FilterTag'] = self.filter_tag

        if self.last_modify_time is not None:
            result['LastModifyTime'] = self.last_modify_time

        if self.notify_content_format is not None:
            result['NotifyContentFormat'] = self.notify_content_format

        if self.notify_strategy is not None:
            result['NotifyStrategy'] = self.notify_strategy

        if self.subscription_name is not None:
            result['SubscriptionName'] = self.subscription_name

        if self.tenant_rate_limit_policy is not None:
            result['TenantRateLimitPolicy'] = self.tenant_rate_limit_policy.to_map()

        if self.topic_name is not None:
            result['TopicName'] = self.topic_name

        if self.topic_owner is not None:
            result['TopicOwner'] = self.topic_owner

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DlqPolicy') is not None:
            temp_model = main_models.GetSubscriptionAttributesResponseBodyDataDlqPolicy()
            self.dlq_policy = temp_model.from_map(m.get('DlqPolicy'))

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('FilterTag') is not None:
            self.filter_tag = m.get('FilterTag')

        if m.get('LastModifyTime') is not None:
            self.last_modify_time = m.get('LastModifyTime')

        if m.get('NotifyContentFormat') is not None:
            self.notify_content_format = m.get('NotifyContentFormat')

        if m.get('NotifyStrategy') is not None:
            self.notify_strategy = m.get('NotifyStrategy')

        if m.get('SubscriptionName') is not None:
            self.subscription_name = m.get('SubscriptionName')

        if m.get('TenantRateLimitPolicy') is not None:
            temp_model = main_models.GetSubscriptionAttributesResponseBodyDataTenantRateLimitPolicy()
            self.tenant_rate_limit_policy = temp_model.from_map(m.get('TenantRateLimitPolicy'))

        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')

        if m.get('TopicOwner') is not None:
            self.topic_owner = m.get('TopicOwner')

        return self

class GetSubscriptionAttributesResponseBodyDataTenantRateLimitPolicy(DaraModel):
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

class GetSubscriptionAttributesResponseBodyDataDlqPolicy(DaraModel):
    def __init__(
        self,
        dead_letter_target_queue: str = None,
        enabled: bool = None,
    ):
        # The target queue to which dead-letter messages are delivered.
        self.dead_letter_target_queue = dead_letter_target_queue
        # Indicates whether dead-letter message delivery is enabled.
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

