# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_rocketmq20220801 import models as main_models
from darabonba.model import DaraModel

class UpdateConsumerGroupRequest(DaraModel):
    def __init__(
        self,
        consume_retry_policy: main_models.UpdateConsumerGroupRequestConsumeRetryPolicy = None,
        delivery_order_type: str = None,
        max_receive_tps: int = None,
        remark: str = None,
    ):
        # The updated consumption retry policy of the consumer group. For more information, see [Consumption retry](https://help.aliyun.com/document_detail/440356.html).
        # 
        # This parameter is required.
        self.consume_retry_policy = consume_retry_policy
        # Modification is not supported.
        self.delivery_order_type = delivery_order_type
        # The upper limit of TPS for consuming messages.
        self.max_receive_tps = max_receive_tps
        # The updated remarks of the consumer group.
        self.remark = remark

    def validate(self):
        if self.consume_retry_policy:
            self.consume_retry_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consume_retry_policy is not None:
            result['consumeRetryPolicy'] = self.consume_retry_policy.to_map()

        if self.delivery_order_type is not None:
            result['deliveryOrderType'] = self.delivery_order_type

        if self.max_receive_tps is not None:
            result['maxReceiveTps'] = self.max_receive_tps

        if self.remark is not None:
            result['remark'] = self.remark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consumeRetryPolicy') is not None:
            temp_model = main_models.UpdateConsumerGroupRequestConsumeRetryPolicy()
            self.consume_retry_policy = temp_model.from_map(m.get('consumeRetryPolicy'))

        if m.get('deliveryOrderType') is not None:
            self.delivery_order_type = m.get('deliveryOrderType')

        if m.get('maxReceiveTps') is not None:
            self.max_receive_tps = m.get('maxReceiveTps')

        if m.get('remark') is not None:
            self.remark = m.get('remark')

        return self

class UpdateConsumerGroupRequestConsumeRetryPolicy(DaraModel):
    def __init__(
        self,
        dead_letter_target_topic: str = None,
        fixed_interval_retry_time: int = None,
        max_retry_times: int = None,
        retry_policy: str = None,
    ):
        # The dead-letter topic.
        # 
        # If a consumer fails to consume a message and the message still fails after retries, the message is delivered to the dead-letter topic for subsequent business recovery or review. For more information, see [Consumption retry and dead-letter messages](https://help.aliyun.com/document_detail/440356.html).
        self.dead_letter_target_topic = dead_letter_target_topic
        # The fixed retry interval. Unit: seconds. This parameter takes effect only when the retry policy is set to FixedRetryPolicy (fixed-interval retry).
        # Valid values:
        #   - Concurrent delivery: 10-1800
        #   - Ordered delivery: 1-600
        self.fixed_interval_retry_time = fixed_interval_retry_time
        # The maximum number of retries.
        self.max_retry_times = max_retry_times
        # The retry policy type. For more information, see [Message retry](https://help.aliyun.com/document_detail/440356.html).
        # 
        # Valid values:
        # - FixedRetryPolicy: fixed-interval retry. Only ordered delivery is supported.
        # - DefaultRetryPolicy: incremental backoff retry. Only concurrent delivery is supported.
        # 
        # This parameter is required.
        self.retry_policy = retry_policy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dead_letter_target_topic is not None:
            result['deadLetterTargetTopic'] = self.dead_letter_target_topic

        if self.fixed_interval_retry_time is not None:
            result['fixedIntervalRetryTime'] = self.fixed_interval_retry_time

        if self.max_retry_times is not None:
            result['maxRetryTimes'] = self.max_retry_times

        if self.retry_policy is not None:
            result['retryPolicy'] = self.retry_policy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deadLetterTargetTopic') is not None:
            self.dead_letter_target_topic = m.get('deadLetterTargetTopic')

        if m.get('fixedIntervalRetryTime') is not None:
            self.fixed_interval_retry_time = m.get('fixedIntervalRetryTime')

        if m.get('maxRetryTimes') is not None:
            self.max_retry_times = m.get('maxRetryTimes')

        if m.get('retryPolicy') is not None:
            self.retry_policy = m.get('retryPolicy')

        return self

