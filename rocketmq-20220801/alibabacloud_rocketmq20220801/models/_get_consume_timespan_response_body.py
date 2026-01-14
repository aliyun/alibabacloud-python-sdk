# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_rocketmq20220801 import models as main_models
from darabonba.model import DaraModel

class GetConsumeTimespanResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetConsumeTimespanResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
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
            temp_model = main_models.GetConsumeTimespanResponseBodyData()
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

class GetConsumeTimespanResponseBodyData(DaraModel):
    def __init__(
        self,
        consume_timestamp: int = None,
        consumer_group_id: str = None,
        instance_id: str = None,
        max_timestamp: int = None,
        min_timestamp: int = None,
        topic_name: str = None,
    ):
        self.consume_timestamp = consume_timestamp
        self.consumer_group_id = consumer_group_id
        self.instance_id = instance_id
        self.max_timestamp = max_timestamp
        self.min_timestamp = min_timestamp
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consume_timestamp is not None:
            result['consumeTimestamp'] = self.consume_timestamp

        if self.consumer_group_id is not None:
            result['consumerGroupId'] = self.consumer_group_id

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.max_timestamp is not None:
            result['maxTimestamp'] = self.max_timestamp

        if self.min_timestamp is not None:
            result['minTimestamp'] = self.min_timestamp

        if self.topic_name is not None:
            result['topicName'] = self.topic_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consumeTimestamp') is not None:
            self.consume_timestamp = m.get('consumeTimestamp')

        if m.get('consumerGroupId') is not None:
            self.consumer_group_id = m.get('consumerGroupId')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('maxTimestamp') is not None:
            self.max_timestamp = m.get('maxTimestamp')

        if m.get('minTimestamp') is not None:
            self.min_timestamp = m.get('minTimestamp')

        if m.get('topicName') is not None:
            self.topic_name = m.get('topicName')

        return self

