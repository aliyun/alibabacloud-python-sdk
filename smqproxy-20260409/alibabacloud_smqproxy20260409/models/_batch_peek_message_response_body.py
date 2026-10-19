# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_smqproxy20260409 import models as main_models
from darabonba.model import DaraModel

class BatchPeekMessageResponseBody(DaraModel):
    def __init__(
        self,
        messages: List[main_models.BatchPeekMessageResponseBodyMessages] = None,
    ):
        # The message list.
        self.messages = messages

    def validate(self):
        if self.messages:
            for v1 in self.messages:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Messages'] = []
        if self.messages is not None:
            for k1 in self.messages:
                result['Messages'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.messages = []
        if m.get('Messages') is not None:
            for k1 in m.get('Messages'):
                temp_model = main_models.BatchPeekMessageResponseBodyMessages()
                self.messages.append(temp_model.from_map(k1))

        return self



class BatchPeekMessageResponseBodyMessages(DaraModel):
    def __init__(
        self,
        dequeue_count: int = None,
        enqueue_time: int = None,
        first_dequeue_time: int = None,
        message_body: str = None,
        message_body_md5: str = None,
        message_group_id: str = None,
        message_id: str = None,
        priority: int = None,
        user_properties: Dict[str, main_models.MessagesUserPropertiesValue] = None,
    ):
        # The total number of times the message has been consumed.
        self.dequeue_count = dequeue_count
        # The time when the message was sent to the queue. The value is a UNIX timestamp that starts from 1970-01-01 00:00:00.000.
        self.enqueue_time = enqueue_time
        # The time when the message was first consumed. The value is a UNIX timestamp in milliseconds that starts from 1970-01-01 00:00:00.000. If DequeueCount is 0, this value is the same as EnqueueTime.
        self.first_dequeue_time = first_dequeue_time
        # The message body.
        self.message_body = message_body
        # The MD5 hash of the message body.
        self.message_body_md5 = message_body_md5
        # The message group ID (FIFO queues only).
        self.message_group_id = message_group_id
        # The message ID.
        self.message_id = message_id
        # The priority. Valid values: 1 to 16. Default value: 8. A value of 1 indicates the highest priority.
        self.priority = priority
        # The user-defined properties (JSON-formatted string).
        self.user_properties = user_properties

    def validate(self):
        if self.user_properties:
            for v1 in self.user_properties.values():
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dequeue_count is not None:
            result['DequeueCount'] = self.dequeue_count

        if self.enqueue_time is not None:
            result['EnqueueTime'] = self.enqueue_time

        if self.first_dequeue_time is not None:
            result['FirstDequeueTime'] = self.first_dequeue_time

        if self.message_body is not None:
            result['MessageBody'] = self.message_body

        if self.message_body_md5 is not None:
            result['MessageBodyMD5'] = self.message_body_md5

        if self.message_group_id is not None:
            result['MessageGroupId'] = self.message_group_id

        if self.message_id is not None:
            result['MessageId'] = self.message_id

        if self.priority is not None:
            result['Priority'] = self.priority

        result['UserProperties'] = {}
        if self.user_properties is not None:
            for k1, v1 in self.user_properties.items():
                result['UserProperties'][k1] = v1.to_map() if v1 else None

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DequeueCount') is not None:
            self.dequeue_count = m.get('DequeueCount')

        if m.get('EnqueueTime') is not None:
            self.enqueue_time = m.get('EnqueueTime')

        if m.get('FirstDequeueTime') is not None:
            self.first_dequeue_time = m.get('FirstDequeueTime')

        if m.get('MessageBody') is not None:
            self.message_body = m.get('MessageBody')

        if m.get('MessageBodyMD5') is not None:
            self.message_body_md5 = m.get('MessageBodyMD5')

        if m.get('MessageGroupId') is not None:
            self.message_group_id = m.get('MessageGroupId')

        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        self.user_properties = {}
        if m.get('UserProperties') is not None:
            for k1, v1 in m.get('UserProperties').items():
                temp_model = main_models.MessagesUserPropertiesValue()
                self.user_properties[k1] = temp_model.from_map(v1)

        return self

