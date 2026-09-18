# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAlertRobotsShrinkRequest(DaraModel):
    def __init__(
        self,
        robot_ids_shrink: str = None,
        type: str = None,
    ):
        # The chatbot ID.
        # 
        # This parameter is required.
        self.robot_ids_shrink = robot_ids_shrink
        # The chatbot type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.robot_ids_shrink is not None:
            result['robotIds'] = self.robot_ids_shrink

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('robotIds') is not None:
            self.robot_ids_shrink = m.get('robotIds')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

