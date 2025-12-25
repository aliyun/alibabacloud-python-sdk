# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitDeepWriteTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        agent_orchestration_shrink: str = None,
        files_shrink: str = None,
        input: str = None,
        instructions: str = None,
        workspace_id: str = None,
    ):
        self.agent_orchestration_shrink = agent_orchestration_shrink
        self.files_shrink = files_shrink
        # This parameter is required.
        self.input = input
        self.instructions = instructions
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_orchestration_shrink is not None:
            result['AgentOrchestration'] = self.agent_orchestration_shrink

        if self.files_shrink is not None:
            result['Files'] = self.files_shrink

        if self.input is not None:
            result['Input'] = self.input

        if self.instructions is not None:
            result['Instructions'] = self.instructions

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentOrchestration') is not None:
            self.agent_orchestration_shrink = m.get('AgentOrchestration')

        if m.get('Files') is not None:
            self.files_shrink = m.get('Files')

        if m.get('Input') is not None:
            self.input = m.get('Input')

        if m.get('Instructions') is not None:
            self.instructions = m.get('Instructions')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

