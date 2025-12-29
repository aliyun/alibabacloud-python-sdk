# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class CreateDataAgentSessionRequest(DaraModel):
    def __init__(
        self,
        dmsunit: str = None,
        file: str = None,
        session_config: main_models.CreateDataAgentSessionRequestSessionConfig = None,
        title: str = None,
        workspace_id: str = None,
    ):
        self.dmsunit = dmsunit
        self.file = file
        self.session_config = session_config
        self.title = title
        self.workspace_id = workspace_id

    def validate(self):
        if self.session_config:
            self.session_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dmsunit is not None:
            result['DMSUnit'] = self.dmsunit

        if self.file is not None:
            result['File'] = self.file

        if self.session_config is not None:
            result['SessionConfig'] = self.session_config.to_map()

        if self.title is not None:
            result['Title'] = self.title

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DMSUnit') is not None:
            self.dmsunit = m.get('DMSUnit')

        if m.get('File') is not None:
            self.file = m.get('File')

        if m.get('SessionConfig') is not None:
            temp_model = main_models.CreateDataAgentSessionRequestSessionConfig()
            self.session_config = temp_model.from_map(m.get('SessionConfig'))

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class CreateDataAgentSessionRequestSessionConfig(DaraModel):
    def __init__(
        self,
        custom_agent_id: str = None,
        custom_agent_stage: str = None,
        enable_search: bool = None,
        language: str = None,
        mcp_server_ids: List[str] = None,
        mode: str = None,
    ):
        self.custom_agent_id = custom_agent_id
        self.custom_agent_stage = custom_agent_stage
        self.enable_search = enable_search
        self.language = language
        self.mcp_server_ids = mcp_server_ids
        self.mode = mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_agent_id is not None:
            result['CustomAgentId'] = self.custom_agent_id

        if self.custom_agent_stage is not None:
            result['CustomAgentStage'] = self.custom_agent_stage

        if self.enable_search is not None:
            result['EnableSearch'] = self.enable_search

        if self.language is not None:
            result['Language'] = self.language

        if self.mcp_server_ids is not None:
            result['McpServerIds'] = self.mcp_server_ids

        if self.mode is not None:
            result['Mode'] = self.mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomAgentId') is not None:
            self.custom_agent_id = m.get('CustomAgentId')

        if m.get('CustomAgentStage') is not None:
            self.custom_agent_stage = m.get('CustomAgentStage')

        if m.get('EnableSearch') is not None:
            self.enable_search = m.get('EnableSearch')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('McpServerIds') is not None:
            self.mcp_server_ids = m.get('McpServerIds')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        return self

