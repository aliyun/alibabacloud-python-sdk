# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class UpdateAgentRequest(DaraModel):
    def __init__(
        self,
        callable_agents: List[main_models.UpdateAgentRequestCallableAgents] = None,
        description: str = None,
        display_name: str = None,
        expected_version: int = None,
        expert_suites: List[main_models.UpdateAgentRequestExpertSuites] = None,
        metadata: Dict[str, Any] = None,
        model: Dict[str, Any] = None,
        name: str = None,
        publish_immediately: bool = None,
        skills: List[main_models.UpdateAgentRequestSkills] = None,
        system_prompt: str = None,
        tools: List[main_models.UpdateAgentRequestTools] = None,
        visibility: str = None,
        visibility_scope: main_models.UpdateAgentRequestVisibilityScope = None,
    ):
        # The list of callable sub-agent references. For non-empty references, the referenced sub-agents must be visible. The agent cannot reference itself or form a call loop. Omit this parameter if no modification is required. Do not use an empty array to express general retention or clearing semantics.
        self.callable_agents = callable_agents
        # The description of the agent.
        self.description = description
        # The display name of the agent.
        self.display_name = display_name
        # The agent definition version used for concurrency control. We recommend that you explicitly specify the AgentVersion just obtained from GetAgent for each call. The update is rejected if the version does not match the current version on the server. To ensure compatibility with different deployment versions, do not rely on the server-side processing when this parameter is omitted.
        self.expected_version = expected_version
        # The list of expert suite references. If omitted, existing references are retained. An explicit empty array clears the references. For official suites, specify only Source=OFFICIAL and SuiteId. Version, VersionSelector, or client artifact fields are not accepted. For custom suites, use SuiteId, and you can explicitly specify an existing integer Version.
        self.expert_suites = expert_suites
        # The extended metadata. If omitted, existing metadata is retained. If passed, business metadata is updated, and the server retains protected system metadata.
        self.metadata = metadata
        # The model configuration.
        self.model = model
        # The name of the agent to be updated. Use the Name returned by GetAgent. This field is used to locate the target agent and cannot be used to rename the agent.
        # 
        # This parameter is required.
        self.name = name
        # Specifies whether to publish the agent immediately after the update. Valid values: true: saves a new draft version first and then requests publishing. false or omitted: saves only the definition. Saving and publishing are not atomic operations. If the operation fails, call GetAgent to read the current version back before retrying, to avoid blindly repeating the update.
        self.publish_immediately = publish_immediately
        # The list of skill references. Omit this parameter if no modification is required. Do not use an empty array to indicate retention or clearing. For official skills, specify only Source=OFFICIAL and SkillId. Name, Version, VersionSelector, or client artifact fields are not accepted. For custom skills, specify Name, and you can explicitly specify an existing integer Version.
        self.skills = skills
        # The system prompt.
        self.system_prompt = system_prompt
        # The list of tool references. Omit this parameter if no modification is required. The current new backend retains existing tools even if an empty array is passed. A non-empty array replaces the references. Each item must include Kind and the corresponding configuration, and cannot include only Name. Replace the MCP service and tool names in the example with actual values available to the current identity.
        self.tools = tools
        # The visibility level. Valid values: <br>`TENANT`: visible within the account. <br>`PROJECT`: visible to specified projects. <br>`USER`: visible to specified users.
        self.visibility = visibility
        # The visibility scope. The corresponding field is used based on the Visibility parameter.
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

        if self.expected_version is not None:
            result['ExpectedVersion'] = self.expected_version

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
                temp_model = main_models.UpdateAgentRequestCallableAgents()
                self.callable_agents.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('ExpectedVersion') is not None:
            self.expected_version = m.get('ExpectedVersion')

        self.expert_suites = []
        if m.get('ExpertSuites') is not None:
            for k1 in m.get('ExpertSuites'):
                temp_model = main_models.UpdateAgentRequestExpertSuites()
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
                temp_model = main_models.UpdateAgentRequestSkills()
                self.skills.append(temp_model.from_map(k1))

        if m.get('SystemPrompt') is not None:
            self.system_prompt = m.get('SystemPrompt')

        self.tools = []
        if m.get('Tools') is not None:
            for k1 in m.get('Tools'):
                temp_model = main_models.UpdateAgentRequestTools()
                self.tools.append(temp_model.from_map(k1))

        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')

        if m.get('VisibilityScope') is not None:
            temp_model = main_models.UpdateAgentRequestVisibilityScope()
            self.visibility_scope = temp_model.from_map(m.get('VisibilityScope'))

        return self

class UpdateAgentRequestVisibilityScope(DaraModel):
    def __init__(
        self,
        project_ids: List[str] = None,
        user_ids: List[str] = None,
    ):
        # The list of visible project IDs. This parameter takes effect when Visibility is set to `PROJECT`.
        self.project_ids = project_ids
        # The list of visible user IDs. This parameter is used when Visibility is set to USER.
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

class UpdateAgentRequestTools(DaraModel):
    def __init__(
        self,
        builtin_name: str = None,
        kind: str = None,
        mcp_items: List[str] = None,
        mcp_server_name: str = None,
        name: str = None,
    ):
        # The name of the built-in toolset. This parameter is required when Kind is set to BUILTIN_TOOLSET. Use a name supported by the target server. Omit this parameter when Kind is set to MCP_TOOLSET.
        self.builtin_name = builtin_name
        # The tool type. A valid tool reference must specify BUILTIN_TOOLSET or MCP_TOOLSET. For BUILTIN_TOOLSET, BuiltinName must also be specified. For MCP_TOOLSET, McpServerName must also be specified. The target server validates the reference based on the tool type.
        self.kind = kind
        # The list of selected MCP tool names. If this parameter is omitted or an empty array is passed, tools are not filtered by name. Each item must be the name of a tool that actually exists in the target service.
        self.mcp_items = mcp_items
        # The MCP service name. This parameter is required when Kind is set to MCP_TOOLSET. The service must be one that the current invoker has permissions to reference and that has an active published version.
        self.mcp_server_name = mcp_server_name
        # A field retained from the legacy model. Specifying only Name does not constitute a valid tool configuration and cannot replace Kind, BuiltinName, or McpServerName.
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

class UpdateAgentRequestSkills(DaraModel):
    def __init__(
        self,
        name: str = None,
        skill_id: str = None,
        source: str = None,
        version: int = None,
        version_selector: str = None,
    ):
        # The name of the custom skill. Use the Name of a visible custom skill. For official skills, use SkillId.
        self.name = name
        # The resource ID of the official skill. This parameter is used when Source is set to OFFICIAL.
        self.skill_id = skill_id
        # The source of the skill. OFFICIAL: official skill, used with SkillId. DB or omitted: custom skill, used with Name.
        self.source = source
        # The published integer version number of the custom skill, used to explicitly select an existing version. Do not pass this field when Source is set to OFFICIAL. This parameter is mutually exclusive with VersionSelector.
        self.version = version
        # The semantic version selection expression of the custom skill, such as ^1.2.3. Use this parameter only when the custom resource version selection capability is deployed on the target server. This parameter is mutually exclusive with Version. This field is not accepted when Source is set to OFFICIAL. To ensure compatibility with servers whose version capabilities are unconfirmed, use an existing integer Version.
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

class UpdateAgentRequestExpertSuites(DaraModel):
    def __init__(
        self,
        source: str = None,
        suite_id: str = None,
        version: int = None,
        version_selector: str = None,
    ):
        # The source of the expert suite. OFFICIAL: official suite. DB or omitted: custom suite. Both types of references use SuiteId. Version fields apply only to custom resources.
        self.source = source
        # The ID of the target expert suite. The suite must be one that the current caller has permissions to reference.
        self.suite_id = suite_id
        # The published integer version number of the custom expert suite, used to explicitly select an existing version. Do not pass this field when Source is set to OFFICIAL. This parameter is mutually exclusive with VersionSelector. To obtain explicit and reproducible references, do not rely on the default selection when the version is omitted.
        self.version = version
        # The semantic version selection expression of the custom expert suite, such as ^1.2.3. Use this parameter only when the custom resource version selection capability is deployed on the target server. This parameter is mutually exclusive with Version. This field is not accepted when Source is set to OFFICIAL. To ensure compatibility with servers whose version capabilities are unconfirmed, use an existing integer Version.
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

class UpdateAgentRequestCallableAgents(DaraModel):
    def __init__(
        self,
        name: str = None,
    ):
        # The name of the called sub-agent. The agent must be one that the current caller has permissions to use.
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

