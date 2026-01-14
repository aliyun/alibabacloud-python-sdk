# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class VerifySendMessageRequest(DaraModel):
    def __init__(
        self,
        lite_topic_name: str = None,
        message: str = None,
        message_key: str = None,
        message_tag: str = None,
    ):
        self.lite_topic_name = lite_topic_name
        # The message body.
        self.message = message
        # The message key.
        self.message_key = message_key
        # The message tag.
        self.message_tag = message_tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lite_topic_name is not None:
            result['liteTopicName'] = self.lite_topic_name

        if self.message is not None:
            result['message'] = self.message

        if self.message_key is not None:
            result['messageKey'] = self.message_key

        if self.message_tag is not None:
            result['messageTag'] = self.message_tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('liteTopicName') is not None:
            self.lite_topic_name = m.get('liteTopicName')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('messageKey') is not None:
            self.message_key = m.get('messageKey')

        if m.get('messageTag') is not None:
            self.message_tag = m.get('messageTag')

        return self

