# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_rocketmq20220801 import models as main_models
from darabonba.model import DaraModel

class CreateConsumerGroupRequest(DaraModel):
    def __init__(
        self,
        consume_retry_policy: main_models.CreateConsumerGroupRequestConsumeRetryPolicy = None,
        delivery_order_type: str = None,
        exclusive: bool = None,
        max_receive_tps: int = None,
        message_model: str = None,
        remark: str = None,
        topic_name: str = None,
    ):
        # The consumption retry policy of the consumer group to be created. For more information, see [Consumption retry](https://help.aliyun.com/document_detail/440356.html).
        # 
        # This parameter is required.
        self.consume_retry_policy = consume_retry_policy
        # The delivery order type of the consumer group to be created.
        # 
        # Valid parameter values:
        # - Concurrently: concurrent delivery
        # - Orderly: ordered delivery
        # 
        # This parameter is required.
        self.delivery_order_type = delivery_order_type
        # Specifies whether to enable exclusive subscription, which means a LiteTopic can only be subscribed to by one consumer. Set to true to enable or false to shutdown.
        self.exclusive = exclusive
        # The maximum TPS for consuming messages.
        self.max_receive_tps = max_receive_tps
        # The subscribe pattern for consumers:
        # - CLUSTERING: clustering consumption pattern. All consumers in the ConsumerGroup share the same subscription.
        # - LITE_SELECTIVE: lightweight consumption pattern. Consumers in the ConsumerGroup can have different subscriptions.
        self.message_model = message_model
        # The remarks for the consumer group to be created.
        self.remark = remark
        # The name of the lite-type topic to subscribe to when using the LITE_SELECTIVE consumption pattern.
        self.topic_name = topic_name

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

        if self.exclusive is not None:
            result['exclusive'] = self.exclusive

        if self.max_receive_tps is not None:
            result['maxReceiveTps'] = self.max_receive_tps

        if self.message_model is not None:
            result['messageModel'] = self.message_model

        if self.remark is not None:
            result['remark'] = self.remark

        if self.topic_name is not None:
            result['topicName'] = self.topic_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consumeRetryPolicy') is not None:
            temp_model = main_models.CreateConsumerGroupRequestConsumeRetryPolicy()
            self.consume_retry_policy = temp_model.from_map(m.get('consumeRetryPolicy'))

        if m.get('deliveryOrderType') is not None:
            self.delivery_order_type = m.get('deliveryOrderType')

        if m.get('exclusive') is not None:
            self.exclusive = m.get('exclusive')

        if m.get('maxReceiveTps') is not None:
            self.max_receive_tps = m.get('maxReceiveTps')

        if m.get('messageModel') is not None:
            self.message_model = m.get('messageModel')

        if m.get('remark') is not None:
            self.remark = m.get('remark')

        if m.get('topicName') is not None:
            self.topic_name = m.get('topicName')

        return self

class CreateConsumerGroupRequestConsumeRetryPolicy(DaraModel):
    def __init__(
        self,
        dead_letter_target_topic: str = None,
        fixed_interval_retry_time: int = None,
        max_retry_times: int = None,
        retry_policy: str = None,
    ):
        # The dead-letter topic.
        # 
        # If a consumer fails to consume a message and the message still failed after retries, the message is delivered to the dead-letter topic for subsequent business recovery or backtracking. For more information, see [Consumption retry and dead-letter messages](https://help.aliyun.com/document_detail/440356.html).
        self.dead_letter_target_topic = dead_letter_target_topic
        # The fixed retry interval, in seconds. This parameter takes effect when the retry policy is set to FixedRetryPolicy.
        # 
        # Valid values:
        # - Concurrent delivery: 10 to 1800
        # - Ordered delivery: 1 to 600
        self.fixed_interval_retry_time = fixed_interval_retry_time
        # The maximum number of retry attempts.
        self.max_retry_times = max_retry_times
        # The retry policy type. For more information, see [Message retry](https://help.aliyun.com/document_detail/440356.html).
        # 
        # Valid parameter values:
        # - FixedRetryPolicy: fixed-interval retry, supported only for ordered delivery
        # - DefaultRetryPolicy: progressive backoff retry, supported only for concurrent delivery
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

