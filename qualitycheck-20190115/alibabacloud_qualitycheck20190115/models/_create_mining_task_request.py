# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateMiningTaskRequest(DaraModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        callback_url: str = None,
        file_path: str = None,
        param: str = None,
        task_type: str = None,
    ):
        self.base_me_agent_id = base_me_agent_id
        self.callback_url = callback_url
        self.file_path = file_path
        self.param = param
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id

        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url

        if self.file_path is not None:
            result['FilePath'] = self.file_path

        if self.param is not None:
            result['Param'] = self.param

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')

        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')

        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')

        if m.get('Param') is not None:
            self.param = m.get('Param')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

