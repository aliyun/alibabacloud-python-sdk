# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from darabonba.model import DaraModel

class UpdateAgentRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        display_name: str = None,
        expected_version: int = None,
        knowledge_bases: Any = None,
        name: str = None,
        skills: Any = None,
        system_prompt: str = None,
        tools: Any = None,
        visibility: str = None,
    ):
        # The new description. If not specified, the existing value is retained.
        self.description = description
        # The new display name. If not specified, the existing value is retained.
        self.display_name = display_name
        # The expected current configuration revision number. This parameter is omitted by default. For concurrency protection, pass in the `AgentVersion` returned by the most recent `GetAgent` call.
        self.expected_version = expected_version
        # The list of knowledge base bindings, which contains at most one element. If not specified, the existing value is retained. A non-empty array replaces the entire value. Passing `[ ]` removes all bindings.
        self.knowledge_bases = knowledge_bases
        # The name of the Agent to update.
        # 
        # This parameter is required.
        self.name = name
        # The list of Skill references. If not specified, the existing value is retained. A non-empty array replaces the entire value. Passing `[ ]` removes all bindings.
        self.skills = skills
        # The new system prompt. If not specified, the existing value is retained.
        self.system_prompt = system_prompt
        # The list of MCP Server and Connector name references. The same array supports both types of entries. Each entry specifies one type of reference. If items is omitted for an MCP entry, all public tools are included. Previously specified items retain their existing values.
        self.tools = tools
        # The new visibility scope. Valid values:
        # - user
        # - tenant
        # 
        # If not specified, the existing value is retained.
        self.visibility = visibility

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.expected_version is not None:
            result['ExpectedVersion'] = self.expected_version

        if self.knowledge_bases is not None:
            result['KnowledgeBases'] = self.knowledge_bases

        if self.name is not None:
            result['Name'] = self.name

        if self.skills is not None:
            result['Skills'] = self.skills

        if self.system_prompt is not None:
            result['SystemPrompt'] = self.system_prompt

        if self.tools is not None:
            result['Tools'] = self.tools

        if self.visibility is not None:
            result['Visibility'] = self.visibility

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('ExpectedVersion') is not None:
            self.expected_version = m.get('ExpectedVersion')

        if m.get('KnowledgeBases') is not None:
            self.knowledge_bases = m.get('KnowledgeBases')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Skills') is not None:
            self.skills = m.get('Skills')

        if m.get('SystemPrompt') is not None:
            self.system_prompt = m.get('SystemPrompt')

        if m.get('Tools') is not None:
            self.tools = m.get('Tools')

        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')

        return self

