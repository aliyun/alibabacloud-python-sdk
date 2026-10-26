# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetAgentResponseBody(DaraModel):
    def __init__(
        self,
        agent: main_models.GetAgentResponseBodyAgent = None,
        request_id: str = None,
    ):
        # The agent details.
        self.agent = agent
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.agent:
            self.agent.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent is not None:
            result['Agent'] = self.agent.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Agent') is not None:
            temp_model = main_models.GetAgentResponseBodyAgent()
            self.agent = temp_model.from_map(m.get('Agent'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetAgentResponseBodyAgent(DaraModel):
    def __init__(
        self,
        agent_version: int = None,
        callable_agents: List[main_models.GetAgentResponseBodyAgentCallableAgents] = None,
        creator_id: str = None,
        description: str = None,
        display_name: str = None,
        expert_suites: List[main_models.GetAgentResponseBodyAgentExpertSuites] = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        metadata: Dict[str, Any] = None,
        model: main_models.GetAgentResponseBodyAgentModel = None,
        modifier_id: str = None,
        name: str = None,
        required_runtime: List[str] = None,
        skills: List[main_models.GetAgentResponseBodyAgentSkills] = None,
        system_prompt: str = None,
        tools: List[main_models.GetAgentResponseBodyAgentTools] = None,
        visibility: str = None,
        visibility_scope: main_models.GetAgentResponseBodyAgentVisibilityScope = None,
    ):
        # 本次读取的定义版本。更新当前定义时，将该值作为 UpdateAgent 的 ExpectedVersion，可拒绝覆盖其他调用者已提交的新版本。读取历史快照的版本不代表当前版本。
        self.agent_version = agent_version
        # A list of callable sub-agents.
        self.callable_agents = callable_agents
        # The creator ID.
        self.creator_id = creator_id
        # **The description.**
        self.description = description
        # **The display name.**
        self.display_name = display_name
        # Agent 定义绑定的专家套件及固定发布版本。
        self.expert_suites = expert_suites
        # The creation time, as a Unix timestamp in milliseconds.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.gmt_create_time = gmt_create_time
        # The last modification time, as a Unix timestamp in milliseconds.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.gmt_modified_time = gmt_modified_time
        # **Additional metadata.**
        self.metadata = metadata
        # **The model configuration.**
        self.model = model
        # The ID of the last modifier.
        self.modifier_id = modifier_id
        # **The agent name.**
        self.name = name
        # The runtime dependencies.
        self.required_runtime = required_runtime
        # A list of skills.
        self.skills = skills
        # **The system prompt.**
        self.system_prompt = system_prompt
        # **A list of tools.**
        self.tools = tools
        # **The visibility level.**
        self.visibility = visibility
        # The visibility scope.
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
        if self.model:
            self.model.validate()
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
        if self.agent_version is not None:
            result['AgentVersion'] = self.agent_version

        result['CallableAgents'] = []
        if self.callable_agents is not None:
            for k1 in self.callable_agents:
                result['CallableAgents'].append(k1.to_map() if k1 else None)

        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id

        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        result['ExpertSuites'] = []
        if self.expert_suites is not None:
            for k1 in self.expert_suites:
                result['ExpertSuites'].append(k1.to_map() if k1 else None)

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        if self.model is not None:
            result['Model'] = self.model.to_map()

        if self.modifier_id is not None:
            result['ModifierId'] = self.modifier_id

        if self.name is not None:
            result['Name'] = self.name

        if self.required_runtime is not None:
            result['RequiredRuntime'] = self.required_runtime

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
        if m.get('AgentVersion') is not None:
            self.agent_version = m.get('AgentVersion')

        self.callable_agents = []
        if m.get('CallableAgents') is not None:
            for k1 in m.get('CallableAgents'):
                temp_model = main_models.GetAgentResponseBodyAgentCallableAgents()
                self.callable_agents.append(temp_model.from_map(k1))

        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        self.expert_suites = []
        if m.get('ExpertSuites') is not None:
            for k1 in m.get('ExpertSuites'):
                temp_model = main_models.GetAgentResponseBodyAgentExpertSuites()
                self.expert_suites.append(temp_model.from_map(k1))

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('Model') is not None:
            temp_model = main_models.GetAgentResponseBodyAgentModel()
            self.model = temp_model.from_map(m.get('Model'))

        if m.get('ModifierId') is not None:
            self.modifier_id = m.get('ModifierId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RequiredRuntime') is not None:
            self.required_runtime = m.get('RequiredRuntime')

        self.skills = []
        if m.get('Skills') is not None:
            for k1 in m.get('Skills'):
                temp_model = main_models.GetAgentResponseBodyAgentSkills()
                self.skills.append(temp_model.from_map(k1))

        if m.get('SystemPrompt') is not None:
            self.system_prompt = m.get('SystemPrompt')

        self.tools = []
        if m.get('Tools') is not None:
            for k1 in m.get('Tools'):
                temp_model = main_models.GetAgentResponseBodyAgentTools()
                self.tools.append(temp_model.from_map(k1))

        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')

        if m.get('VisibilityScope') is not None:
            temp_model = main_models.GetAgentResponseBodyAgentVisibilityScope()
            self.visibility_scope = temp_model.from_map(m.get('VisibilityScope'))

        return self

class GetAgentResponseBodyAgentVisibilityScope(DaraModel):
    def __init__(
        self,
        project_ids: List[str] = None,
        user_ids: List[str] = None,
    ):
        # A list of project IDs that can view the agent.
        self.project_ids = project_ids
        # A list of user IDs that can view the agent.
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

class GetAgentResponseBodyAgentTools(DaraModel):
    def __init__(
        self,
        builtin_name: str = None,
        kind: str = None,
        mcp_items: List[str] = None,
        mcp_server_name: str = None,
    ):
        # **The name of the built-in tool. This parameter applies only when `Kind` is set to `builtin`.**
        self.builtin_name = builtin_name
        # **The tool type.**
        self.kind = kind
        # **The selected MCP tool items. This parameter applies only when `Kind` is set to `mcp`.**
        self.mcp_items = mcp_items
        # **The name of the associated MCP server. This parameter applies only when `Kind` is set to `mcp`.**
        self.mcp_server_name = mcp_server_name

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

        return self

class GetAgentResponseBodyAgentSkills(DaraModel):
    def __init__(
        self,
        name: str = None,
        package_version: str = None,
        skill_id: str = None,
        source: str = None,
        version: int = None,
    ):
        # The skill name.
        self.name = name
        # 指定 AgentVersion 查询已发布快照时返回固定的官方制品版本；查询草稿或自定义 Skill 时不返回。
        self.package_version = package_version
        self.skill_id = skill_id
        # OFFICIAL 表示官方目录资源；省略或 DB 表示原有个人或企业资源。
        self.source = source
        # The skill version.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.package_version is not None:
            result['PackageVersion'] = self.package_version

        if self.skill_id is not None:
            result['SkillId'] = self.skill_id

        if self.source is not None:
            result['Source'] = self.source

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PackageVersion') is not None:
            self.package_version = m.get('PackageVersion')

        if m.get('SkillId') is not None:
            self.skill_id = m.get('SkillId')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class GetAgentResponseBodyAgentModel(DaraModel):
    def __init__(
        self,
        config: Dict[str, Any] = None,
        max_tokens: int = None,
        model_name: str = None,
        stream: bool = None,
        temperature: float = None,
        top_p: float = None,
    ):
        # Additional configuration for the model.
        self.config = config
        # The maximum number of tokens to generate in one response.
        self.max_tokens = max_tokens
        # The model name.
        self.model_name = model_name
        # Indicates whether streaming output is enabled.
        self.stream = stream
        # The temperature.
        self.temperature = temperature
        # The top-p.
        self.top_p = top_p

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.max_tokens is not None:
            result['MaxTokens'] = self.max_tokens

        if self.model_name is not None:
            result['ModelName'] = self.model_name

        if self.stream is not None:
            result['Stream'] = self.stream

        if self.temperature is not None:
            result['Temperature'] = self.temperature

        if self.top_p is not None:
            result['TopP'] = self.top_p

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('MaxTokens') is not None:
            self.max_tokens = m.get('MaxTokens')

        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        if m.get('Stream') is not None:
            self.stream = m.get('Stream')

        if m.get('Temperature') is not None:
            self.temperature = m.get('Temperature')

        if m.get('TopP') is not None:
            self.top_p = m.get('TopP')

        return self

class GetAgentResponseBodyAgentExpertSuites(DaraModel):
    def __init__(
        self,
        description: str = None,
        display_name: str = None,
        name: str = None,
        package_version: str = None,
        semantic_version: str = None,
        source: str = None,
        suite_id: str = None,
        version: int = None,
    ):
        # 套件已删除、发布快照缺失或调用者无权查看时，不返回套件摘要，仅保留 ID 和版本号。
        self.description = description
        self.display_name = display_name
        self.name = name
        # 显式查询 Agent 已发布版本时返回固定的官方制品版本；查询草稿或自定义套件时不返回。
        self.package_version = package_version
        # 可选套件摘要字段，当前新 DataAgent 应用不返回；缺省不表示版本 0。不可作为 UpdateAgent 的 Version，回写引用时必须省略。官方制品的固定版本请读取 PackageVersion。
        self.semantic_version = semantic_version
        # OFFICIAL 表示官方目录资源；省略或 DB 表示个人或企业资源。
        self.source = source
        self.suite_id = suite_id
        # 仅个人或企业套件在引用明确指定版本或读取发布快照时返回；官方套件不返回。未返回不是 0；SDK 若将缺省整数初始化为 0，回写时必须省略。官方项只回写 Source 和 SuiteId，不传 Version、SemanticVersion 或 PackageVersion。
        self.version = version

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

        if self.name is not None:
            result['Name'] = self.name

        if self.package_version is not None:
            result['PackageVersion'] = self.package_version

        if self.semantic_version is not None:
            result['SemanticVersion'] = self.semantic_version

        if self.source is not None:
            result['Source'] = self.source

        if self.suite_id is not None:
            result['SuiteId'] = self.suite_id

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PackageVersion') is not None:
            self.package_version = m.get('PackageVersion')

        if m.get('SemanticVersion') is not None:
            self.semantic_version = m.get('SemanticVersion')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SuiteId') is not None:
            self.suite_id = m.get('SuiteId')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class GetAgentResponseBodyAgentCallableAgents(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        name: str = None,
        source: str = None,
        version: int = None,
    ):
        # The sub-agent display name.
        self.display_name = display_name
        # The sub-agent name.
        self.name = name
        # The sub-agent source.
        self.source = source
        # The sub-agent version.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.name is not None:
            result['Name'] = self.name

        if self.source is not None:
            result['Source'] = self.source

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

