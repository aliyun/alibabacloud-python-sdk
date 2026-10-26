# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SteerAgentConversationResponseBody(DaraModel):
    def __init__(
        self,
        accepted: bool = None,
        message_id: str = None,
    ):
        self.accepted = accepted
        self.message_id = message_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accepted is not None:
            result['accepted'] = self.accepted

        if self.message_id is not None:
            result['messageId'] = self.message_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accepted') is not None:
            self.accepted = m.get('accepted')

        if m.get('messageId') is not None:
            self.message_id = m.get('messageId')

        return self

