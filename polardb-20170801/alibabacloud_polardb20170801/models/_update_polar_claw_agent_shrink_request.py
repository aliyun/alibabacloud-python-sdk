# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdatePolarClawAgentShrinkRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        application_id: str = None,
        avatar: str = None,
        files_shrink: str = None,
        model: str = None,
        name: str = None,
        restart: bool = None,
        workspace: str = None,
    ):
        # The ID of the agent to update.
        # 
        # This parameter is required.
        self.agent_id = agent_id
        # The application ID.
        # 
        # This parameter is required.
        self.application_id = application_id
        # The new avatar for the agent.
        self.avatar = avatar
        # The file list to update.
        self.files_shrink = files_shrink
        # The model to override the agent\\"s default setting.
        self.model = model
        # The new display name for the agent.
        self.name = name
        # Specifies whether to restart the gateway after the update. The default value is true.
        self.restart = restart
        # The new path for the agent\\"s workspace.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.avatar is not None:
            result['Avatar'] = self.avatar

        if self.files_shrink is not None:
            result['Files'] = self.files_shrink

        if self.model is not None:
            result['Model'] = self.model

        if self.name is not None:
            result['Name'] = self.name

        if self.restart is not None:
            result['Restart'] = self.restart

        if self.workspace is not None:
            result['Workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('Avatar') is not None:
            self.avatar = m.get('Avatar')

        if m.get('Files') is not None:
            self.files_shrink = m.get('Files')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Restart') is not None:
            self.restart = m.get('Restart')

        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')

        return self

