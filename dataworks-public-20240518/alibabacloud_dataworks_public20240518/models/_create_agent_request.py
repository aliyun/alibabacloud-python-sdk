# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class CreateAgentRequest(DaraModel):
    def __init__(
        self,
        callable_agents: List[main_models.CreateAgentRequestCallableAgents] = None,
        description: str = None,
        display_name: str = None,
        expert_suites: List[main_models.CreateAgentRequestExpertSuites] = None,
        metadata: Dict[str, Any] = None,
        model: Dict[str, Any] = None,
        name: str = None,
        publish_immediately: bool = None,
        skills: List[main_models.CreateAgentRequestSkills] = None,
        system_prompt: str = None,
        tools: List[main_models.CreateAgentRequestTools] = None,
        visibility: str = None,
        visibility_scope: main_models.CreateAgentRequestVisibilityScope = None,
    ):
        # The list of sub-agents that can be called by this agent.
        self.callable_agents = callable_agents
        # The description of the agent.
        self.description = description
        # The display name of the agent.
        self.display_name = display_name
        # The published expert suites bound to the agent. For personal or enterprise suites, use SuiteId, and optionally specify a fixed Version or VersionSelector. For official suites, you must explicitly specify Source=OFFICIAL and the SuiteId from the official catalog, and do not specify Version or VersionSelector. If not specified, an empty list is created, and all official suites are not loaded by default.
        self.expert_suites = expert_suites
        # The extended metadata in key-value pairs.
        self.metadata = metadata
        # The model configuration.
        self.model = model
        # The name of the agent. The name must be unique within the current account.
        # 
        # This parameter is required.
        self.name = name
        # Specifies whether to publish the agent immediately after creation. A value of true publishes the created version. A value of false or omitting this parameter maintains the original behavior of creating a draft only. Saving and publishing are not atomic operations. If publishing fails, the draft may already exist. Before retrying, query the agent first to avoid duplicate creation.
        self.publish_immediately = publish_immediately
        # The list of skills.
        self.skills = skills
        # The system prompt.
        self.system_prompt = system_prompt
        # The list of tools.
        self.tools = tools
        # The visibility level. Valid values:<br>
        # `TENANT`: Visible within the account.<br>
        # `PROJECT`: Visible to specified projects.<br>
        # `USER`: Visible to specified users.
        self.visibility = visibility
        # The visibility scope. Specify the corresponding fields based on the Visibility value.
        self.visibility_scope = visibility_scope

    def validate(self):
        if self.callable_agents:
            for v1 in self.callable_agents:
                 if v1:
                    v1.validate()
        if self.expert_suites:
            for v1 in self.expert_suites:
                 if v1:
                    v1.validate()
        if self.skills:
            for v1 in self.skills:
                 if v1:
                    v1.validate()
        if self.tools:
            for v1 in self.tools:
                 if v1:
                    v1.validate()
        if self.visibility_scope:
            self.visibility_scope.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CallableAgents'] = []
        if self.callable_agents is not None:
            for k1 in self.callable_agents:
                result['CallableAgents'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        result['ExpertSuites'] = []
        if self.expert_suites is not None:
            for k1 in self.expert_suites:
                result['ExpertSuites'].append(k1.to_map() if k1 else None)

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        if self.model is not None:
            result['Model'] = self.model

        if self.name is not None:
            result['Name'] = self.name

        if self.publish_immediately is not None:
            result['PublishImmediately'] = self.publish_immediately

        result['Skills'] = []
        if self.skills is not None:
            for k1 in self.skills:
                result['Skills'].append(k1.to_map() if k1 else None)

        if self.system_prompt is not None:
            result['SystemPrompt'] = self.system_prompt

        result['Tools'] = []
        if self.tools is not None:
            for k1 in self.tools:
                result['Tools'].append(k1.to_map() if k1 else None)

        if self.visibility is not None:
            result['Visibility'] = self.visibility

        if self.visibility_scope is not None:
            result['VisibilityScope'] = self.visibility_scope.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.callable_agents = []
        if m.get('CallableAgents') is not None:
            for k1 in m.get('CallableAgents'):
                temp_model = main_models.CreateAgentRequestCallableAgents()
                self.callable_agents.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        self.expert_suites = []
        if m.get('ExpertSuites') is not None:
            for k1 in m.get('ExpertSuites'):
                temp_model = main_models.CreateAgentRequestExpertSuites()
                self.expert_suites.append(temp_model.from_map(k1))

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PublishImmediately') is not None:
            self.publish_immediately = m.get('PublishImmediately')

        self.skills = []
        if m.get('Skills') is not None:
            for k1 in m.get('Skills'):
                temp_model = main_models.CreateAgentRequestSkills()
                self.skills.append(temp_model.from_map(k1))

        if m.get('SystemPrompt') is not None:
            self.system_prompt = m.get('SystemPrompt')

        self.tools = []
        if m.get('Tools') is not None:
            for k1 in m.get('Tools'):
                temp_model = main_models.CreateAgentRequestTools()
                self.tools.append(temp_model.from_map(k1))

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
        # The list of visible project IDs. This parameter takes effect when Visibility is set to `PROJECT`.
        self.project_ids = project_ids
        # The list of visible user IDs. This parameter takes effect when Visibility is set to `USER`.
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

class CreateAgentRequestTools(DaraModel):
    def __init__(
        self,
        builtin_name: str = None,
        kind: str = None,
        mcp_items: List[str] = None,
        mcp_server_name: str = None,
        name: str = None,
    ):
        # Required when Kind is BUILTIN_TOOLSET. Specifies the name of the built-in toolset supported by the target server. Omit this parameter when Kind is MCP_TOOLSET.
        self.builtin_name = builtin_name
        # Required for valid tool references. BUILTIN_TOOLSET indicates a built-in toolset, and BuiltinName must be specified. MCP_TOOLSET indicates an MCP toolset, and McpServerName must be specified. The target server validates the parameter based on the tool type.
        self.kind = kind
        # Optional when Kind is MCP_TOOLSET. If specified, only the listed tools are used. If omitted or left as an empty array, tools are not filtered by name. Each item must be the name of an actual tool in the target MCP service.
        self.mcp_items = mcp_items
        # Required when Kind is MCP_TOOLSET. Specifies the MCP service name that the current caller has permission to reference and that has an active published version.
        self.mcp_server_name = mcp_server_name
        # The name of the MCP server.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.builtin_name is not None:
            result['BuiltinName'] = self.builtin_name

        if self.kind is not None:
            result['Kind'] = self.kind

        if self.mcp_items is not None:
            result['McpItems'] = self.mcp_items

        if self.mcp_server_name is not None:
            result['McpServerName'] = self.mcp_server_name

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuiltinName') is not None:
            self.builtin_name = m.get('BuiltinName')

        if m.get('Kind') is not None:
            self.kind = m.get('Kind')

        if m.get('McpItems') is not None:
            self.mcp_items = m.get('McpItems')

        if m.get('McpServerName') is not None:
            self.mcp_server_name = m.get('McpServerName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class CreateAgentRequestSkills(DaraModel):
    def __init__(
        self,
        name: str = None,
        skill_id: str = None,
        source: str = None,
        version: int = None,
        version_selector: str = None,
    ):
        # The name of the skill.
        self.name = name
        # When Source is OFFICIAL, specify the official catalog ID. Do not specify Name, Version, or VersionSelector. Do not specify this field for personal or enterprise skills.
        self.skill_id = skill_id
        # OFFICIAL indicates an official catalog resource. DB indicates a personal or enterprise resource. If omitted, the original query-by-name semantics are maintained.
        self.source = source
        # Used only for personal or enterprise skills. Specifies the fixed integer revision number of a published snapshot. This parameter is mutually exclusive with VersionSelector. Publishing a new version does not change the fixed reference. If both are omitted, the latest version is used for each new session. Do not specify this parameter when Source is OFFICIAL.
        self.version = version
        # Used only for personal or enterprise resources. This parameter is mutually exclusive with Version. Supports exact semantic versions, latest, and full npm/node-semver range syntax, such as 1.2.*, ^1.2.3, ~1.2.3, >=1.0.0 <2.0.0, and 1.x || 2.x. If both are omitted, the latest version is used, and the highest matching published version is selected for each new session. Existing fixed integer references remain unchanged. Do not specify this parameter when Source is OFFICIAL.
        self.version_selector = version_selector

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.skill_id is not None:
            result['SkillId'] = self.skill_id

        if self.source is not None:
            result['Source'] = self.source

        if self.version is not None:
            result['Version'] = self.version

        if self.version_selector is not None:
            result['VersionSelector'] = self.version_selector

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SkillId') is not None:
            self.skill_id = m.get('SkillId')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('VersionSelector') is not None:
            self.version_selector = m.get('VersionSelector')

        return self

class CreateAgentRequestExpertSuites(DaraModel):
    def __init__(
        self,
        source: str = None,
        suite_id: str = None,
        version: int = None,
        version_selector: str = None,
    ):
        # OFFICIAL indicates an official catalog resource. DB indicates a personal or enterprise resource. If omitted, the original database resource query semantics are maintained. For official resources, the artifact version is fixed when the agent is published.
        self.source = source
        # When passing expert suite references, each item must provide a SuiteId, which is validated by the server. When Source is OFFICIAL, this is the official catalog ID. Otherwise, this is the ID returned by expert suite management. The referenced resource must be visible to the caller.
        self.suite_id = suite_id
        # Used only for personal or enterprise suites. Specifies the fixed integer revision number of a published snapshot. This parameter is mutually exclusive with VersionSelector. Publishing a new version does not change the fixed reference. If both are omitted, the latest version is used for each new session. Do not specify this parameter when Source is OFFICIAL.
        self.version = version
        # Used only for personal or enterprise resources. This parameter is mutually exclusive with Version. Supports exact semantic versions, latest, and full npm/node-semver range syntax, such as 1.2.*, ^1.2.3, ~1.2.3, >=1.0.0 <2.0.0, and 1.x || 2.x. If both are omitted, the latest version is used, and the highest matching published version is selected for each new session. Existing fixed integer references remain unchanged. Do not specify this parameter when Source is OFFICIAL.
        self.version_selector = version_selector

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.source is not None:
            result['Source'] = self.source

        if self.suite_id is not None:
            result['SuiteId'] = self.suite_id

        if self.version is not None:
            result['Version'] = self.version

        if self.version_selector is not None:
            result['VersionSelector'] = self.version_selector

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SuiteId') is not None:
            self.suite_id = m.get('SuiteId')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('VersionSelector') is not None:
            self.version_selector = m.get('VersionSelector')

        return self

class CreateAgentRequestCallableAgents(DaraModel):
    def __init__(
        self,
        name: str = None,
    ):
        # The name of the agent.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

