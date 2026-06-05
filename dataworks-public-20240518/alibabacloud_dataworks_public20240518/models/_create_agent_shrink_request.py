# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAgentShrinkRequest(DaraModel):
    def __init__(
        self,
        callable_agents_shrink: str = None,
        description: str = None,
        display_name: str = None,
        metadata_shrink: str = None,
        model_shrink: str = None,
        name: str = None,
        skills_shrink: str = None,
        system_prompt: str = None,
        tools_shrink: str = None,
        visibility: str = None,
        visibility_scope_shrink: str = None,
    ):
        self.callable_agents_shrink = callable_agents_shrink
        self.description = description
        self.display_name = display_name
        self.metadata_shrink = metadata_shrink
        self.model_shrink = model_shrink
        # This parameter is required.
        self.name = name
        self.skills_shrink = skills_shrink
        self.system_prompt = system_prompt
        self.tools_shrink = tools_shrink
        self.visibility = visibility
        self.visibility_scope_shrink = visibility_scope_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.callable_agents_shrink is not None:
            result['CallableAgents'] = self.callable_agents_shrink

        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.metadata_shrink is not None:
            result['Metadata'] = self.metadata_shrink

        if self.model_shrink is not None:
            result['Model'] = self.model_shrink

        if self.name is not None:
            result['Name'] = self.name

        if self.skills_shrink is not None:
            result['Skills'] = self.skills_shrink

        if self.system_prompt is not None:
            result['SystemPrompt'] = self.system_prompt

        if self.tools_shrink is not None:
            result['Tools'] = self.tools_shrink

        if self.visibility is not None:
            result['Visibility'] = self.visibility

        if self.visibility_scope_shrink is not None:
            result['VisibilityScope'] = self.visibility_scope_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallableAgents') is not None:
            self.callable_agents_shrink = m.get('CallableAgents')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Metadata') is not None:
            self.metadata_shrink = m.get('Metadata')

        if m.get('Model') is not None:
            self.model_shrink = m.get('Model')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Skills') is not None:
            self.skills_shrink = m.get('Skills')

        if m.get('SystemPrompt') is not None:
            self.system_prompt = m.get('SystemPrompt')

        if m.get('Tools') is not None:
            self.tools_shrink = m.get('Tools')

        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')

        if m.get('VisibilityScope') is not None:
            self.visibility_scope_shrink = m.get('VisibilityScope')

        return self

