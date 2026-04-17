# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alikafka20190916 import models as main_models
from darabonba.model import DaraModel

class GetTopicSubscribeStatusResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        topic_subscribe_status: main_models.GetTopicSubscribeStatusResponseBodyTopicSubscribeStatus = None,
    ):
        # The HTTP status code.
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success
        # The subscription details.
        self.topic_subscribe_status = topic_subscribe_status

    def validate(self):
        if self.topic_subscribe_status:
            self.topic_subscribe_status.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.topic_subscribe_status is not None:
            result['TopicSubscribeStatus'] = self.topic_subscribe_status.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TopicSubscribeStatus') is not None:
            temp_model = main_models.GetTopicSubscribeStatusResponseBodyTopicSubscribeStatus()
            self.topic_subscribe_status = temp_model.from_map(m.get('TopicSubscribeStatus'))

        return self

class GetTopicSubscribeStatusResponseBodyTopicSubscribeStatus(DaraModel):
    def __init__(
        self,
        consumer_groups: List[str] = None,
        topic: str = None,
    ):
        # The groups that subscribe to the topic.
        self.consumer_groups = consumer_groups
        # The topic name.
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consumer_groups is not None:
            result['ConsumerGroups'] = self.consumer_groups

        if self.topic is not None:
            result['Topic'] = self.topic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumerGroups') is not None:
            self.consumer_groups = m.get('ConsumerGroups')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        return self

