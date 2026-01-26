# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteIMRobotRequest(DaraModel):
    def __init__(
        self,
        robot_id: int = None,
    ):
        # The ID of the IM chatbot.
        # 
        # This parameter is required.
        self.robot_id = robot_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.robot_id is not None:
            result['RobotId'] = self.robot_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RobotId') is not None:
            self.robot_id = m.get('RobotId')

        return self

