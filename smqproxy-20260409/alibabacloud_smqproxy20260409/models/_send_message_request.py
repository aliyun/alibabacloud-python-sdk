# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SendMessageRequest(DaraModel):
    def __init__(
        self,
        delay_seconds: int = None,
        message_body: str = None,
        message_group_id: str = None,
        priority: int = None,
        user_properties: str = None,
    ):
        self.delay_seconds = delay_seconds
        self.message_body = message_body
        self.message_group_id = message_group_id
        self.priority = priority
        self.user_properties = user_properties

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

        if self.user_properties is not None:
            result['UserProperties'] = self.user_properties

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

        if m.get('UserProperties') is not None:
            self.user_properties = m.get('UserProperties')

        return self

