# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_smqproxy20260409 import models as main_models
from darabonba.model import DaraModel

class BatchSendMessageRequest(DaraModel):
    def __init__(
        self,
        messages: List[main_models.BatchSendMessageRequestMessages] = None,
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
                temp_model = main_models.BatchSendMessageRequestMessages()
                self.messages.append(temp_model.from_map(k1))

        return self

class BatchSendMessageRequestMessages(DaraModel):
    def __init__(
        self,
        delay_seconds: int = None,
        message_body: str = None,
        message_group_id: str = None,
        priority: int = None,
    ):
        self.delay_seconds = delay_seconds
        self.message_body = message_body
        self.message_group_id = message_group_id
        self.priority = priority

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delay_seconds is not None:
            result['DelaySeconds'] = self.delay_seconds

        if self.message_body is not None:
            result['MessageBody'] = self.message_body

        if self.message_group_id is not None:
            result['MessageGroupId'] = self.message_group_id

        if self.priority is not None:
            result['Priority'] = self.priority

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DelaySeconds') is not None:
            self.delay_seconds = m.get('DelaySeconds')

        if m.get('MessageBody') is not None:
            self.message_body = m.get('MessageBody')

        if m.get('MessageGroupId') is not None:
            self.message_group_id = m.get('MessageGroupId')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        return self

