# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mns_open20220119 import models as main_models
from darabonba.model import DaraModel

class CreateQueueShrinkRequest(DaraModel):
    def __init__(
        self,
        delay_seconds: int = None,
        dlq_policy_shrink: str = None,
        enable_logging: bool = None,
        enable_sse: bool = None,
        kms_key_id: str = None,
        maximum_message_size: int = None,
        message_retention_period: int = None,
        polling_wait_seconds: int = None,
        queue_name: str = None,
        queue_type: str = None,
        sse_algorithm: str = None,
        sse_type: str = None,
        tag: List[main_models.CreateQueueShrinkRequestTag] = None,
        tenant_rate_limit_policy_shrink: str = None,
        visibility_timeout: int = None,
    ):
        # The delay period for all messages sent to the queue. A message sent to the queue can be consumed only after the delay period specified by this parameter elapses. Unit: seconds.
        # 
        # Valid values: 0 to 604800.
        # 
        # Default value: 0.
        self.delay_seconds = delay_seconds
        # The dead-letter policy.
        self.dlq_policy_shrink = dlq_policy_shrink
        # Specifies whether to enable the log management feature. Valid values:
        # 
        # - true: Enabled.
        # 
        # - false: Disabled.
        # 
        # Default value: false.
        self.enable_logging = enable_logging
        self.enable_sse = enable_sse
        self.kms_key_id = kms_key_id
        # The maximum size of a message body that can be sent to the queue. Unit: bytes.
        # 
        # Valid values: 1024 to 65536.
        # 
        # Default value: 65536.
        self.maximum_message_size = maximum_message_size
        # The maximum duration for which a message is retained in the queue. After the specified duration elapses from the time the message is sent to the queue, the message is deleted regardless of whether it has been consumed. Unit: seconds.
        # 
        # Valid values: 60 to 604800.
        # 
        # Default value: 345600.
        self.message_retention_period = message_retention_period
        # The maximum wait time for a ReceiveMessage request when the queue is empty. Unit: seconds.
        # 
        # Valid values: 0 to 30.
        # 
        # Default value: 0.
        self.polling_wait_seconds = polling_wait_seconds
        # The name of the queue.
        # 
        # This parameter is required.
        self.queue_name = queue_name
        # The type of the queue. Valid values:
        #    * normal: standard queue.
        #    * fifo: FIFO queue.
        self.queue_type = queue_type
        self.sse_algorithm = sse_algorithm
        self.sse_type = sse_type
        # The list of resource tags.
        self.tag = tag
        # The rate limiting policy.
        self.tenant_rate_limit_policy_shrink = tenant_rate_limit_policy_shrink
        # The duration for which a consumed message stays in the Inactive state after it is changed from the Active state. Unit: seconds.
        # 
        # Valid values: 1 to 43200.
        # 
        # Default value: 30.
        self.visibility_timeout = visibility_timeout

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delay_seconds is not None:
            result['DelaySeconds'] = self.delay_seconds

        if self.dlq_policy_shrink is not None:
            result['DlqPolicy'] = self.dlq_policy_shrink

        if self.enable_logging is not None:
            result['EnableLogging'] = self.enable_logging

        if self.enable_sse is not None:
            result['EnableSSE'] = self.enable_sse

        if self.kms_key_id is not None:
            result['KmsKeyId'] = self.kms_key_id

        if self.maximum_message_size is not None:
            result['MaximumMessageSize'] = self.maximum_message_size

        if self.message_retention_period is not None:
            result['MessageRetentionPeriod'] = self.message_retention_period

        if self.polling_wait_seconds is not None:
            result['PollingWaitSeconds'] = self.polling_wait_seconds

        if self.queue_name is not None:
            result['QueueName'] = self.queue_name

        if self.queue_type is not None:
            result['QueueType'] = self.queue_type

        if self.sse_algorithm is not None:
            result['SseAlgorithm'] = self.sse_algorithm

        if self.sse_type is not None:
            result['SseType'] = self.sse_type

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.tenant_rate_limit_policy_shrink is not None:
            result['TenantRateLimitPolicy'] = self.tenant_rate_limit_policy_shrink

        if self.visibility_timeout is not None:
            result['VisibilityTimeout'] = self.visibility_timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DelaySeconds') is not None:
            self.delay_seconds = m.get('DelaySeconds')

        if m.get('DlqPolicy') is not None:
            self.dlq_policy_shrink = m.get('DlqPolicy')

        if m.get('EnableLogging') is not None:
            self.enable_logging = m.get('EnableLogging')

        if m.get('EnableSSE') is not None:
            self.enable_sse = m.get('EnableSSE')

        if m.get('KmsKeyId') is not None:
            self.kms_key_id = m.get('KmsKeyId')

        if m.get('MaximumMessageSize') is not None:
            self.maximum_message_size = m.get('MaximumMessageSize')

        if m.get('MessageRetentionPeriod') is not None:
            self.message_retention_period = m.get('MessageRetentionPeriod')

        if m.get('PollingWaitSeconds') is not None:
            self.polling_wait_seconds = m.get('PollingWaitSeconds')

        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')

        if m.get('QueueType') is not None:
            self.queue_type = m.get('QueueType')

        if m.get('SseAlgorithm') is not None:
            self.sse_algorithm = m.get('SseAlgorithm')

        if m.get('SseType') is not None:
            self.sse_type = m.get('SseType')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateQueueShrinkRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('TenantRateLimitPolicy') is not None:
            self.tenant_rate_limit_policy_shrink = m.get('TenantRateLimitPolicy')

        if m.get('VisibilityTimeout') is not None:
            self.visibility_timeout = m.get('VisibilityTimeout')

        return self

class CreateQueueShrinkRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

