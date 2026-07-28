# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateJobRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        sub_command: str = None,
        task_type: str = None,
    ):
        # The idempotence token. Format: [0-9a-zA-Z-]{1,64}. We recommend that you use a UUID.
        # 
        # This parameter is required.
        self.client_token = client_token
        # The job description. Length: 1 to 64 characters.
        # 
        # This parameter is required.
        self.description = description
        # The operation command. Valid values:
        # 
        # - plan: performs a preview. This is the default value.
        # - refresh: refreshes the resource status.
        # - destroy: destroys resources.
        self.sub_command = sub_command
        # The task type. Valid values:
        # 
        # - Task: regular task. This is the default value.
        # - SceneTestingTask: scenario-based testing task.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['clientToken'] = self.client_token

        if self.description is not None:
            result['description'] = self.description

        if self.sub_command is not None:
            result['subCommand'] = self.sub_command

        if self.task_type is not None:
            result['taskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('subCommand') is not None:
            self.sub_command = m.get('subCommand')

        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')

        return self

