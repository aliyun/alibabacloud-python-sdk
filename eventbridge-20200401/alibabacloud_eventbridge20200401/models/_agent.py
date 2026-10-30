# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class Agent(DaraModel):
    def __init__(
        self,
        created_at: int = None,
        description: str = None,
        mcp_server_id: str = None,
        mcp_server_name: str = None,
        metadata: main_models.Metadata = None,
        name: str = None,
        prompt: str = None,
        updated_at: int = None,
    ):
        # The creation time in UNIX milliseconds.
        self.created_at = created_at
        # The description of the agent.
        self.description = description
        # The ID of the MCP server associated with the agent.
        self.mcp_server_id = mcp_server_id
        # The name of the MCP server.
        self.mcp_server_name = mcp_server_name
        # The associated table metadata.
        self.metadata = metadata
        # The name of the agent.
        self.name = name
        # The custom prompt.
        self.prompt = prompt
        # The update time in UNIX milliseconds.
        self.updated_at = updated_at

    def validate(self):
        if self.metadata:
            self.metadata.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at

        if self.description is not None:
            result['Description'] = self.description

        if self.mcp_server_id is not None:
            result['McpServerId'] = self.mcp_server_id

        if self.mcp_server_name is not None:
            result['McpServerName'] = self.mcp_server_name

        if self.metadata is not None:
            result['Metadata'] = self.metadata.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.prompt is not None:
            result['Prompt'] = self.prompt

        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('McpServerId') is not None:
            self.mcp_server_id = m.get('McpServerId')

        if m.get('McpServerName') is not None:
            self.mcp_server_name = m.get('McpServerName')

        if m.get('Metadata') is not None:
            temp_model = main_models.Metadata()
            self.metadata = temp_model.from_map(m.get('Metadata'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')

        return self

