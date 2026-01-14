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
        # The new consumption retry policy of the consumer group. For more information, see [Consumption retry](https://help.aliyun.com/document_detail/440356.html).
        # 
        # This parameter is required.
        self.consume_retry_policy = consume_retry_policy
        # The new message delivery method of the consumer group.
        # 
        # Valid values:
        # 
        # *   Concurrently: concurrent delivery
        # *   Orderly: ordered delivery
        self.delivery_order_type = delivery_order_type
        # The maximum number of messages that can be processed by consumers per second.
        self.max_receive_tps = max_receive_tps
        # The new description of the consumer group.
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
        # If a message still fails to be consumed after the maximum number of retries specified in the consumption retry policy is reached, the message is delivered to the dead-letter topic for subsequent business recovery or backtracking. For more information, see [Consumption retry and dead-letter messages](https://help.aliyun.com/document_detail/440356.html).
        self.dead_letter_target_topic = dead_letter_target_topic
        # Fixed retry interval, unit: seconds.This option is effective when retryPolicy is FixedRetryPolicy.Value range：
        #   - Concurrently:10-1800
        #   - Orderly:1-600
        self.fixed_interval_retry_time = fixed_interval_retry_time
        # The maximum number of retries.
        self.max_retry_times = max_retry_times
        # The retry policy. For more information, see [Message retry](https://help.aliyun.com/document_detail/440356.html).
        # 
        # Valid values:
        # 
        # *   FixedRetryPolicy: fixed-interval retry. This value is valid only if you set deliveryOrderType to Orderly.
        # *   DefaultRetryPolicy: exponential backoff retry. This value is valid only if you set deliveryOrderType to Concurrently.
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

