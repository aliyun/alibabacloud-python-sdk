# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RunScriptChatRequest(DaraModel):
    def __init__(
        self,
        prompt: str = None,
        task_id: str = None,
    ):
        # This parameter is required.
        self.prompt = prompt
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.prompt is not None:
            result['prompt'] = self.prompt

        if self.task_id is not None:
            result['taskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('prompt') is not None:
            self.prompt = m.get('prompt')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        return self

