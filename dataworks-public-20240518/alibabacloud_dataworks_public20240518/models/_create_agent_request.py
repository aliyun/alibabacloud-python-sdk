# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class CreateAgentRequest(DaraModel):
    def __init__(
        self,
        callable_agents: List[str] = None,
        description: str = None,
        display_name: str = None,
        metadata: Dict[str, Any] = None,
        model: Dict[str, Any] = None,
        name: str = None,
        skills: List[str] = None,
        system_prompt: str = None,
        tools: List[str] = None,
        visibility: str = None,
        visibility_scope: main_models.CreateAgentRequestVisibilityScope = None,
    ):
        # The list of sub-Agents that can be called by this Agent.
        self.callable_agents = callable_agents
        # The description of the Agent.
        self.description = description
        # The display name of the Agent.
        self.display_name = display_name
        # Extended metadata (key-value pairs).
        self.metadata = metadata
        # The model configuration.
        self.model = model
        # The name of the Agent. It must be unique under the current account.
        # 
        # This parameter is required.
        self.name = name
        # The list of skills.
        self.skills = skills
        # The system prompt.
        self.system_prompt = system_prompt
        # The list of tools.
        self.tools = tools
        # The visibility level.<br>
        # `TENANT`: Visible within the account.<br>
        # `PROJECT`: Visible to specified projects.<br>
        # `USER`: Visible to specified users.
        self.visibility = visibility
        # The visibility scope. The corresponding field is selected based on Visibility.
        self.visibility_scope = visibility_scope

    def validate(self):
        if self.visibility_scope:
            self.visibility_scope.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.callable_agents is not None:
            result['CallableAgents'] = self.callable_agents

        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        if self.model is not None:
            result['Model'] = self.model

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

        if self.visibility_scope is not None:
            result['VisibilityScope'] = self.visibility_scope.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallableAgents') is not None:
            self.callable_agents = m.get('CallableAgents')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('Model') is not None:
            self.model = m.get('Model')

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

        if m.get('VisibilityScope') is not None:
            temp_model = main_models.CreateAgentRequestVisibilityScope()
            self.visibility_scope = temp_model.from_map(m.get('VisibilityScope'))

        return self

class CreateAgentRequestVisibilityScope(DaraModel):
    def __init__(
        self,
        project_ids: List[str] = None,
        user_ids: List[str] = None,
    ):
        # The list of visible project IDs. Takes effect when Visibility is `PROJECT`.
        self.project_ids = project_ids
        # The list of visible user IDs. Takes effect when Visibility is `USER`.
        self.user_ids = user_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.project_ids is not None:
            result['ProjectIds'] = self.project_ids

        if self.user_ids is not None:
            result['UserIds'] = self.user_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectIds') is not None:
            self.project_ids = m.get('ProjectIds')

        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')

        return self

