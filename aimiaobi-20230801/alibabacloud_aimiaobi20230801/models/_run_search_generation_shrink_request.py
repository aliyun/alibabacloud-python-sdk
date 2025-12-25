# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RunSearchGenerationShrinkRequest(DaraModel):
    def __init__(
        self,
        agent_context_shrink: str = None,
        chat_config_shrink: str = None,
        file_url: str = None,
        model_id: str = None,
        original_session_id: str = None,
        prompt: str = None,
        task_id: str = None,
        workspace_id: str = None,
    ):
        self.agent_context_shrink = agent_context_shrink
        self.chat_config_shrink = chat_config_shrink
        self.file_url = file_url
        self.model_id = model_id
        self.original_session_id = original_session_id
        self.prompt = prompt
        self.task_id = task_id
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_context_shrink is not None:
            result['AgentContext'] = self.agent_context_shrink

        if self.chat_config_shrink is not None:
            result['ChatConfig'] = self.chat_config_shrink

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.model_id is not None:
            result['ModelId'] = self.model_id

        if self.original_session_id is not None:
            result['OriginalSessionId'] = self.original_session_id

        if self.prompt is not None:
            result['Prompt'] = self.prompt

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentContext') is not None:
            self.agent_context_shrink = m.get('AgentContext')

        if m.get('ChatConfig') is not None:
            self.chat_config_shrink = m.get('ChatConfig')

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')

        if m.get('OriginalSessionId') is not None:
            self.original_session_id = m.get('OriginalSessionId')

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

