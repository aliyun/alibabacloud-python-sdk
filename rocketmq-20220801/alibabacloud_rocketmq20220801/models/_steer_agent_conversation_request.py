# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SteerAgentConversationRequest(DaraModel):
    def __init__(
        self,
        command_id: str = None,
        message: str = None,
    ):
        # This parameter is required.
        self.command_id = command_id
        # This parameter is required.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.command_id is not None:
            result['commandId'] = self.command_id

        if self.message is not None:
            result['message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commandId') is not None:
            self.command_id = m.get('commandId')

        if m.get('message') is not None:
            self.message = m.get('message')

        return self

