# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class VerifySendMessageRequest(DaraModel):
    def __init__(
        self,
        delivery_time_stamp: int = None,
        lite_topic_name: str = None,
        message: str = None,
        message_group: str = None,
        message_key: str = None,
        message_tag: str = None,
        user_properties: Dict[str, Any] = None,
    ):
        self.delivery_time_stamp = delivery_time_stamp
        self.lite_topic_name = lite_topic_name
        # The message body.
        self.message = message
        self.message_group = message_group
        # The message key.
        self.message_key = message_key
        # The message tag.
        self.message_tag = message_tag
        self.user_properties = user_properties

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delivery_time_stamp is not None:
            result['deliveryTimeStamp'] = self.delivery_time_stamp

        if self.lite_topic_name is not None:
            result['liteTopicName'] = self.lite_topic_name

        if self.message is not None:
            result['message'] = self.message

        if self.message_group is not None:
            result['messageGroup'] = self.message_group

        if self.message_key is not None:
            result['messageKey'] = self.message_key

        if self.message_tag is not None:
            result['messageTag'] = self.message_tag

        if self.user_properties is not None:
            result['userProperties'] = self.user_properties

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deliveryTimeStamp') is not None:
            self.delivery_time_stamp = m.get('deliveryTimeStamp')

        if m.get('liteTopicName') is not None:
            self.lite_topic_name = m.get('liteTopicName')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('messageGroup') is not None:
            self.message_group = m.get('messageGroup')

        if m.get('messageKey') is not None:
            self.message_key = m.get('messageKey')

        if m.get('messageTag') is not None:
            self.message_tag = m.get('messageTag')

        if m.get('userProperties') is not None:
            self.user_properties = m.get('userProperties')

        return self

