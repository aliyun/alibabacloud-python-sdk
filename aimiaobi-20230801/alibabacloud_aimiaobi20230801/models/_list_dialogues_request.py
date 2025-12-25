# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDialoguesRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        current: int = None,
        dialogue_type: int = None,
        end_time: str = None,
        size: int = None,
        start_time: str = None,
        task_id: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.current = current
        self.dialogue_type = dialogue_type
        self.end_time = end_time
        self.size = size
        self.start_time = start_time
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.current is not None:
            result['Current'] = self.current

        if self.dialogue_type is not None:
            result['DialogueType'] = self.dialogue_type

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.size is not None:
            result['Size'] = self.size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('Current') is not None:
            self.current = m.get('Current')

        if m.get('DialogueType') is not None:
            self.dialogue_type = m.get('DialogueType')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

