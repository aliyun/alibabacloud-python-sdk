# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_smqproxy20260409 import models as main_models
from darabonba.model import DaraModel

class BatchReceiveMessageResponseBody(DaraModel):
    def __init__(
        self,
        messages: List[main_models.BatchReceiveMessageResponseBodyMessages] = None,
    ):
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
                temp_model = main_models.BatchReceiveMessageResponseBodyMessages()
                self.messages.append(temp_model.from_map(k1))

        return self

class BatchReceiveMessageResponseBodyMessages(DaraModel):
    def __init__(
        self,
        dequeue_count: int = None,
        enqueue_time: int = None,
        first_dequeue_time: int = None,
        message_body: str = None,
        message_body_md5: str = None,
        message_group_id: str = None,
        message_id: str = None,
        next_visible_time: int = None,
        priority: int = None,
        receipt_handle: str = None,
        user_properties: str = None,
    ):
        self.dequeue_count = dequeue_count
        self.enqueue_time = enqueue_time
        self.first_dequeue_time = first_dequeue_time
        self.message_body = message_body
        self.message_body_md5 = message_body_md5
        self.message_group_id = message_group_id
        self.message_id = message_id
        self.next_visible_time = next_visible_time
        self.priority = priority
        self.receipt_handle = receipt_handle
        self.user_properties = user_properties

    def validate(self):
        pass

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

        if self.next_visible_time is not None:
            result['NextVisibleTime'] = self.next_visible_time

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.receipt_handle is not None:
            result['ReceiptHandle'] = self.receipt_handle

        if self.user_properties is not None:
            result['UserProperties'] = self.user_properties

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

        if m.get('NextVisibleTime') is not None:
            self.next_visible_time = m.get('NextVisibleTime')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('ReceiptHandle') is not None:
            self.receipt_handle = m.get('ReceiptHandle')

        if m.get('UserProperties') is not None:
            self.user_properties = m.get('UserProperties')

        return self

