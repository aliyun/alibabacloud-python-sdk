# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_smqproxy20260409 import models as main_models
from darabonba.model import DaraModel

class BatchSendMessageResponseBody(DaraModel):
    def __init__(
        self,
        messages: List[main_models.BatchSendMessageResponseBodyMessages] = None,
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
                temp_model = main_models.BatchSendMessageResponseBodyMessages()
                self.messages.append(temp_model.from_map(k1))

        return self

class BatchSendMessageResponseBodyMessages(DaraModel):
    def __init__(
        self,
        message_body_md5: str = None,
        message_id: str = None,
    ):
        self.message_body_md5 = message_body_md5
        self.message_id = message_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message_body_md5 is not None:
            result['MessageBodyMD5'] = self.message_body_md5

        if self.message_id is not None:
            result['MessageId'] = self.message_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MessageBodyMD5') is not None:
            self.message_body_md5 = m.get('MessageBodyMD5')

        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')

        return self

