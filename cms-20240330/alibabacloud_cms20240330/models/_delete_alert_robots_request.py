# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteAlertRobotsRequest(DaraModel):
    def __init__(
        self,
        robot_ids: List[str] = None,
        type: str = None,
    ):
        # The chatbot ID.
        # 
        # This parameter is required.
        self.robot_ids = robot_ids
        # The chatbot type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.robot_ids is not None:
            result['robotIds'] = self.robot_ids

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('robotIds') is not None:
            self.robot_ids = m.get('robotIds')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

