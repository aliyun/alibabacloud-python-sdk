# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_rocketmq20220801 import models as main_models
from darabonba.model import DaraModel

class GetConsumerGroupResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetConsumerGroupResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The fault code.
        self.code = code
        # The returned result.
        self.data = data
        # The dynamic fault code.
        self.dynamic_code = dynamic_code
        # The dynamic fault message.
        self.dynamic_message = dynamic_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The fault message.
        self.message = message
        # The request ID. Each request has a unique ID, which can be used to troubleshoot and locate faults.
        self.request_id = request_id
        # Indicates whether the execute operation was successful.
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
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.dynamic_code is not None:
            result['dynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['dynamicMessage'] = self.dynamic_message

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetConsumerGroupResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('dynamicCode') is not None:
            self.dynamic_code = m.get('dynamicCode')

        if m.get('dynamicMessage') is not None:
            self.dynamic_message = m.get('dynamicMessage')

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class GetConsumerGroupResponseBodyData(DaraModel):
    def __init__(
        self,
        consume_retry_policy: main_models.GetConsumerGroupResponseBodyDataConsumeRetryPolicy = None,
        consumer_group_id: str = None,
        create_time: str = None,
        delivery_order_type: str = None,
        exclusive: bool = None,
        instance_id: str = None,
        max_receive_tps: int = None,
        message_model: str = None,
        region_id: str = None,
        remark: str = None,
        status: str = None,
        topic_name: str = None,
        update_time: str = None,
    ):
        # The consumption retry policy of the consumer group. For more information, see [Consumption retry](https://help.aliyun.com/document_detail/440356.html).
        self.consume_retry_policy = consume_retry_policy
        # The ID of the consumer group.
        self.consumer_group_id = consumer_group_id
        # The time when the consumer group was created, in the format of YYYY-MM-DD HH:mm:ss.
        self.create_time = create_time
        # The delivery order of the consumer group.
        self.delivery_order_type = delivery_order_type
        # Indicates whether exclusive consumption is enabled.
        self.exclusive = exclusive
        # The ID of the instance to which the consumer group belongs.
        self.instance_id = instance_id
        # The maximum TPS for consuming messages.
        self.max_receive_tps = max_receive_tps
        # The consumption pattern. Valid values:
        #  - CLUSTERING: clustering consumption.
        #  - LITE_SELECTIVE: LITE_SELECTIVE.
        self.message_model = message_model
        # The region ID of the instance.
        self.region_id = region_id
        # The remarks of the consumer group.
        self.remark = remark
        # The status of the consumer group.
        self.status = status
        # The topic name for the lite type.
        self.topic_name = topic_name
        # The time when the consumer group was last updated, in the format of YYYY-MM-DD HH:mm:ss.
        self.update_time = update_time

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

        if self.consumer_group_id is not None:
            result['consumerGroupId'] = self.consumer_group_id

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.delivery_order_type is not None:
            result['deliveryOrderType'] = self.delivery_order_type

        if self.exclusive is not None:
            result['exclusive'] = self.exclusive

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.max_receive_tps is not None:
            result['maxReceiveTps'] = self.max_receive_tps

        if self.message_model is not None:
            result['messageModel'] = self.message_model

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.remark is not None:
            result['remark'] = self.remark

        if self.status is not None:
            result['status'] = self.status

        if self.topic_name is not None:
            result['topicName'] = self.topic_name

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consumeRetryPolicy') is not None:
            temp_model = main_models.GetConsumerGroupResponseBodyDataConsumeRetryPolicy()
            self.consume_retry_policy = temp_model.from_map(m.get('consumeRetryPolicy'))

        if m.get('consumerGroupId') is not None:
            self.consumer_group_id = m.get('consumerGroupId')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('deliveryOrderType') is not None:
            self.delivery_order_type = m.get('deliveryOrderType')

        if m.get('exclusive') is not None:
            self.exclusive = m.get('exclusive')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('maxReceiveTps') is not None:
            self.max_receive_tps = m.get('maxReceiveTps')

        if m.get('messageModel') is not None:
            self.message_model = m.get('messageModel')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('remark') is not None:
            self.remark = m.get('remark')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('topicName') is not None:
            self.topic_name = m.get('topicName')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        return self

class GetConsumerGroupResponseBodyDataConsumeRetryPolicy(DaraModel):
    def __init__(
        self,
        dead_letter_target_topic: str = None,
        fixed_interval_retry_time: int = None,
        max_retry_times: int = None,
        retry_policy: str = None,
    ):
        # The dead-letter topic.
        # 
        # If a consumer fails to consume a message due to an exception and the message still cannot be consumed after retries, the message is delivered to the dead-letter topic for subsequent business recovery or review. For more information, see [Consumption retry and dead-letter messages](https://help.aliyun.com/document_detail/440356.html).
        self.dead_letter_target_topic = dead_letter_target_topic
        # The fixed retry interval. Unit: seconds.
        #  - Concurrently (concurrent delivery): 10-1800
        #  - Orderly (ordered delivery): 1-600
        self.fixed_interval_retry_time = fixed_interval_retry_time
        # The maximum number of retry attempts.
        self.max_retry_times = max_retry_times
        # The retry policy type.
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

