# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from darabonba.model import DaraModel

class GetAgentResponseBody(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        agent_version: int = None,
        can_delete: bool = None,
        can_modify: bool = None,
        created_at: int = None,
        description: str = None,
        display_name: str = None,
        knowledge_bases: Any = None,
        metadata: Any = None,
        model: Any = None,
        name: str = None,
        official: bool = None,
        request_id: str = None,
        skills: Any = None,
        status: str = None,
        system_prompt: str = None,
        tools: Any = None,
        updated_at: int = None,
        visibility: str = None,
    ):
        # Agent ID。
        self.agent_id = agent_id
        # The current configuration revision number.
        self.agent_version = agent_version
        # Indicates whether the current identity can delete the agent.
        self.can_delete = can_delete
        # Indicates whether the current identity can modify the agent.
        self.can_modify = can_modify
        # The creation time. The value is a UNIX timestamp in milliseconds.
        self.created_at = created_at
        # The description of the agent. This field may not be returned if it is not configured.
        self.description = description
        # The display name of the agent. This field may not be returned if it is not configured.
        self.display_name = display_name
        # The list of knowledge base references. The list contains at most one element.
        self.knowledge_bases = knowledge_bases
        # The display metadata of the agent. For specific fields, see "Supplementary description of response elements".
        self.metadata = metadata
        # The saved model configuration. This field is returned only for official agents. The value supports an object array and is compatible with legacy single objects and strings. An empty array returns [ \\]. Object arrays preserve the original order, duplicate names, and object fields.
        self.model = model
        # The name of the agent.
        self.name = name
        # Indicates whether the agent is an official agent provided by the platform.
        self.official = official
        # The request ID, which is used for Tracing Analysis and troubleshooting.
        self.request_id = request_id
        # The list of skill references. For specific fields, see "Supplementary description of response elements".
        self.skills = skills
        # The status of the agent. The default status of a newly created agent is `draft`.
        self.status = status
        # The system prompt. This field may not be returned if it is not configured.
        self.system_prompt = system_prompt
        # The list of MCP Server and Connector name references. For element fields, see the following section.
        self.tools = tools
        # The most recent update time. The value is a UNIX timestamp in milliseconds.
        self.updated_at = updated_at
        # The visibility scope of the agent. Valid values: `user` and `tenant`.
        self.visibility = visibility

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.agent_version is not None:
            result['AgentVersion'] = self.agent_version

        if self.can_delete is not None:
            result['CanDelete'] = self.can_delete

        if self.can_modify is not None:
            result['CanModify'] = self.can_modify

        if self.created_at is not None:
            result['CreatedAt'] = self.created_at

        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.knowledge_bases is not None:
            result['KnowledgeBases'] = self.knowledge_bases

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        if self.model is not None:
            result['Model'] = self.model

        if self.name is not None:
            result['Name'] = self.name

        if self.official is not None:
            result['Official'] = self.official

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.skills is not None:
            result['Skills'] = self.skills

        if self.status is not None:
            result['Status'] = self.status

        if self.system_prompt is not None:
            result['SystemPrompt'] = self.system_prompt

        if self.tools is not None:
            result['Tools'] = self.tools

        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at

        if self.visibility is not None:
            result['Visibility'] = self.visibility

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('AgentVersion') is not None:
            self.agent_version = m.get('AgentVersion')

        if m.get('CanDelete') is not None:
            self.can_delete = m.get('CanDelete')

        if m.get('CanModify') is not None:
            self.can_modify = m.get('CanModify')

        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('KnowledgeBases') is not None:
            self.knowledge_bases = m.get('KnowledgeBases')

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Official') is not None:
            self.official = m.get('Official')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Skills') is not None:
            self.skills = m.get('Skills')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SystemPrompt') is not None:
            self.system_prompt = m.get('SystemPrompt')

        if m.get('Tools') is not None:
            self.tools = m.get('Tools')

        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')

        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')

        return self

