# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from darabonba.model import DaraModel

class CreateAgentRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        display_name: str = None,
        knowledge_bases: Any = None,
        name: str = None,
        skills: Any = None,
        system_prompt: str = None,
        tools: Any = None,
        visibility: str = None,
    ):
        # The description of the agent.
        self.description = description
        # The display name of the agent.
        self.display_name = display_name
        # The list of knowledge base references, which can contain at most one element.
        self.knowledge_bases = knowledge_bases
        # The name of the agent, which is also the unique identifier that cannot be modified after creation.
        # 
        # This parameter is required.
        self.name = name
        # The list of skill references. For specific fields, refer to the supplementary description of request parameters.
        self.skills = skills
        # The system prompt.
        self.system_prompt = system_prompt
        # The list of MCP server and connector name references. The same array supports both types of entries. Specify only one type of reference for each entry. For MCP, omitting items indicates all public tools, and historically specified items retain their original values.
        self.tools = tools
        # The visibility scope of the agent. Valid values: `user` and `tenant`. Default value: `user`.
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

