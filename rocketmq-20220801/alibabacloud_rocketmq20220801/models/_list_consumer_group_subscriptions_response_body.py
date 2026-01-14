# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rocketmq20220801 import models as main_models
from darabonba.model import DaraModel

class ListConsumerGroupSubscriptionsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListConsumerGroupSubscriptionsResponseBodyData] = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.code = code
        # The returned data.
        self.data = data
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic error message.
        self.dynamic_message = dynamic_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

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

        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.ListConsumerGroupSubscriptionsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

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

class ListConsumerGroupSubscriptionsResponseBodyData(DaraModel):
    def __init__(
        self,
        consistency: bool = None,
        consumer_group_id: str = None,
        filter_expression: str = None,
        filter_expression_type: str = None,
        message_model: str = None,
        subscription_status: str = None,
        topic_created: bool = None,
        topic_name: str = None,
    ):
        # Indicates whether message consumption is consistent. Valid values:
        # 
        # *   false: Unconsumed messages exist in the consumer group.
        # *   true: No unconsumed message exists in the consumer group.
        self.consistency = consistency
        # The ID of the consumer group.
        self.consumer_group_id = consumer_group_id
        # The filter expression.
        self.filter_expression = filter_expression
        # The type of the filter expression. Valid values:
        # 
        # *   SQL: filters messages by using SQL expressions.
        # *   TAG: filters messages by using tags.
        self.filter_expression_type = filter_expression_type
        # The consumption mode of the consumer group. Valid values:
        # 
        # *   BROADCASTING: broadcasting consumption
        # *   CLUSTERING: clustering consumption
        self.message_model = message_model
        # The subscription status. Valid values:
        # 
        # *   ONLINE: The consumer group is online. If the consumer group contains multiple consumers, this value is returned as long as one of the consumers is online.
        # *   OFFLINE: The consumer group is offline. If the consumer group contains multiple consumers, this value is returned only if all consumers are offline.
        self.subscription_status = subscription_status
        # Indicates whether the topic is created.
        self.topic_created = topic_created
        # The topic to which the consumer group subscribes.
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consistency is not None:
            result['consistency'] = self.consistency

        if self.consumer_group_id is not None:
            result['consumerGroupId'] = self.consumer_group_id

        if self.filter_expression is not None:
            result['filterExpression'] = self.filter_expression

        if self.filter_expression_type is not None:
            result['filterExpressionType'] = self.filter_expression_type

        if self.message_model is not None:
            result['messageModel'] = self.message_model

        if self.subscription_status is not None:
            result['subscriptionStatus'] = self.subscription_status

        if self.topic_created is not None:
            result['topicCreated'] = self.topic_created

        if self.topic_name is not None:
            result['topicName'] = self.topic_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consistency') is not None:
            self.consistency = m.get('consistency')

        if m.get('consumerGroupId') is not None:
            self.consumer_group_id = m.get('consumerGroupId')

        if m.get('filterExpression') is not None:
            self.filter_expression = m.get('filterExpression')

        if m.get('filterExpressionType') is not None:
            self.filter_expression_type = m.get('filterExpressionType')

        if m.get('messageModel') is not None:
            self.message_model = m.get('messageModel')

        if m.get('subscriptionStatus') is not None:
            self.subscription_status = m.get('subscriptionStatus')

        if m.get('topicCreated') is not None:
            self.topic_created = m.get('topicCreated')

        if m.get('topicName') is not None:
            self.topic_name = m.get('topicName')

        return self

