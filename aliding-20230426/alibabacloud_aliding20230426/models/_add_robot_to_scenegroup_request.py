# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddRobotToScenegroupRequest(DaraModel):
    def __init__(
        self,
        open_conversation_id: str = None,
        robot_code: str = None,
    ):
        # This parameter is required.
        self.open_conversation_id = open_conversation_id
        # This parameter is required.
        self.robot_code = robot_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.open_conversation_id is not None:
            result['OpenConversationId'] = self.open_conversation_id

        if self.robot_code is not None:
            result['RobotCode'] = self.robot_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpenConversationId') is not None:
            self.open_conversation_id = m.get('OpenConversationId')

        if m.get('RobotCode') is not None:
            self.robot_code = m.get('RobotCode')

        return self

