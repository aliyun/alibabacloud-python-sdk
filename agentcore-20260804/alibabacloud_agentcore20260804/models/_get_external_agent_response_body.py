# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class GetExternalAgentResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetExternalAgentResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business status code. The value is SUCCESS when the request succeeds.
        self.code = code
        # The details of the external agent.
        self.data = data
        # The HTTP status code. The value is 200 when the request succeeds.
        self.http_status_code = http_status_code
        # The request processing result message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetExternalAgentResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class GetExternalAgentResponseBodyData(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        create_mode: str = None,
        created_at: str = None,
        deploy_type: str = None,
        description: str = None,
        external_agent_status: main_models.GetExternalAgentResponseBodyDataExternalAgentStatus = None,
        instruction: str = None,
        latest_spec_version: int = None,
        latest_version_status: str = None,
        model: main_models.GetExternalAgentResponseBodyDataModel = None,
        model_source: str = None,
        name: str = None,
        region_id: str = None,
        runtime: str = None,
        skills: List[main_models.GetExternalAgentResponseBodyDataSkills] = None,
        status: str = None,
        template: main_models.GetExternalAgentResponseBodyDataTemplate = None,
        tools: List[main_models.GetExternalAgentResponseBodyDataTools] = None,
        updated_at: str = None,
        workspace_id: str = None,
    ):
        # The external agent ID.
        self.agent_id = agent_id
        # The creation mode.
        self.create_mode = create_mode
        # The creation time in RFC 3339 format.
        self.created_at = created_at
        # The deployment type.
        self.deploy_type = deploy_type
        # The description of the external agent.
        self.description = description
        # The runtime status information reported by the external agent.
        self.external_agent_status = external_agent_status
        # The agent instruction that guides the behavior of the agent.
        self.instruction = instruction
        # The latest specification version number.
        self.latest_spec_version = latest_spec_version
        # The processing status of the latest specification version. Valid values:
        # - pending: Pending.
        # - processing: Processing.
        # - waiting_retry: Waiting for retry.
        # - succeeded: Succeeded.
        # - failed: Failed.
        # - superseded: Superseded by a newer version.
        self.latest_version_status = latest_version_status
        # The model configuration. This parameter is available only when modelSource is set to PLATFORM.
        self.model = model
        # The model configuration source. PLATFORM indicates that the model configuration is parsed and distributed by the platform. RUNTIME indicates that the model is managed by the external runtime, and the model parameter cannot be specified at the same time. Valid values:
        # - PLATFORM: Platform model.
        # - RUNTIME: Runtime model.
        self.model_source = model_source
        # The name of the external agent.
        self.name = name
        # The region ID.
        self.region_id = region_id
        # The runtime type reported by the external agent.
        self.runtime = runtime
        # The list of skill configurations.
        self.skills = skills
        # The status of the external agent. Valid values:
        # - Creating: Being created.
        # - Running: Running.
        # - Failed: Failed.
        # - Updating: Being updated.
        # - Deleting: Being deleted.
        # - Deleted: Deleted.
        self.status = status
        # The agent template configuration.
        self.template = template
        # The list of tool configurations.
        self.tools = tools
        # The update time in RFC 3339 format.
        self.updated_at = updated_at
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        if self.external_agent_status:
            self.external_agent_status.validate()
        if self.model:
            self.model.validate()
        if self.skills:
            for v1 in self.skills:
                 if v1:
                    v1.validate()
        if self.template:
            self.template.validate()
        if self.tools:
            for v1 in self.tools:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['agentId'] = self.agent_id

        if self.create_mode is not None:
            result['createMode'] = self.create_mode

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.deploy_type is not None:
            result['deployType'] = self.deploy_type

        if self.description is not None:
            result['description'] = self.description

        if self.external_agent_status is not None:
            result['externalAgentStatus'] = self.external_agent_status.to_map()

        if self.instruction is not None:
            result['instruction'] = self.instruction

        if self.latest_spec_version is not None:
            result['latestSpecVersion'] = self.latest_spec_version

        if self.latest_version_status is not None:
            result['latestVersionStatus'] = self.latest_version_status

        if self.model is not None:
            result['model'] = self.model.to_map()

        if self.model_source is not None:
            result['modelSource'] = self.model_source

        if self.name is not None:
            result['name'] = self.name

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.runtime is not None:
            result['runtime'] = self.runtime

        result['skills'] = []
        if self.skills is not None:
            for k1 in self.skills:
                result['skills'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['status'] = self.status

        if self.template is not None:
            result['template'] = self.template.to_map()

        result['tools'] = []
        if self.tools is not None:
            for k1 in self.tools:
                result['tools'].append(k1.to_map() if k1 else None)

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')

        if m.get('createMode') is not None:
            self.create_mode = m.get('createMode')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('deployType') is not None:
            self.deploy_type = m.get('deployType')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('externalAgentStatus') is not None:
            temp_model = main_models.GetExternalAgentResponseBodyDataExternalAgentStatus()
            self.external_agent_status = temp_model.from_map(m.get('externalAgentStatus'))

        if m.get('instruction') is not None:
            self.instruction = m.get('instruction')

        if m.get('latestSpecVersion') is not None:
            self.latest_spec_version = m.get('latestSpecVersion')

        if m.get('latestVersionStatus') is not None:
            self.latest_version_status = m.get('latestVersionStatus')

        if m.get('model') is not None:
            temp_model = main_models.GetExternalAgentResponseBodyDataModel()
            self.model = temp_model.from_map(m.get('model'))

        if m.get('modelSource') is not None:
            self.model_source = m.get('modelSource')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('runtime') is not None:
            self.runtime = m.get('runtime')

        self.skills = []
        if m.get('skills') is not None:
            for k1 in m.get('skills'):
                temp_model = main_models.GetExternalAgentResponseBodyDataSkills()
                self.skills.append(temp_model.from_map(k1))

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('template') is not None:
            temp_model = main_models.GetExternalAgentResponseBodyDataTemplate()
            self.template = temp_model.from_map(m.get('template'))

        self.tools = []
        if m.get('tools') is not None:
            for k1 in m.get('tools'):
                temp_model = main_models.GetExternalAgentResponseBodyDataTools()
                self.tools.append(temp_model.from_map(k1))

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

class GetExternalAgentResponseBodyDataTools(DaraModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
    ):
        # The tool name.
        # 
        # This parameter is required.
        self.name = name
        # The tool type. Valid values:
        # - MCP: MCP tool.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class GetExternalAgentResponseBodyDataTemplate(DaraModel):
    def __init__(
        self,
        ai_registry: main_models.GetExternalAgentResponseBodyDataTemplateAiRegistry = None,
    ):
        # The AI Registry template configuration.
        self.ai_registry = ai_registry

    def validate(self):
        if self.ai_registry:
            self.ai_registry.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ai_registry is not None:
            result['aiRegistry'] = self.ai_registry.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aiRegistry') is not None:
            temp_model = main_models.GetExternalAgentResponseBodyDataTemplateAiRegistry()
            self.ai_registry = temp_model.from_map(m.get('aiRegistry'))

        return self

class GetExternalAgentResponseBodyDataTemplateAiRegistry(DaraModel):
    def __init__(
        self,
        name: str = None,
        version: str = None,
    ):
        # The name of the template in AI Registry.
        # 
        # This parameter is required.
        self.name = name
        # The version of the template in AI Registry.
        # 
        # This parameter is required.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

class GetExternalAgentResponseBodyDataSkills(DaraModel):
    def __init__(
        self,
        name: str = None,
        version: str = None,
    ):
        # The skill name.
        # 
        # This parameter is required.
        self.name = name
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
            result['name'] = self.name

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

class GetExternalAgentResponseBodyDataModel(DaraModel):
    def __init__(
        self,
        model_connection_id: str = None,
        model_name: str = None,
        quota: main_models.GetExternalAgentResponseBodyDataModelQuota = None,
    ):
        # The model connection ID.
        self.model_connection_id = model_connection_id
        # The upstream model name.
        self.model_name = model_name
        # The model token quota configuration and the quota usage status in the current cycle. This parameter is empty if no quota is configured.
        self.quota = quota

    def validate(self):
        if self.quota:
            self.quota.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_connection_id is not None:
            result['modelConnectionId'] = self.model_connection_id

        if self.model_name is not None:
            result['modelName'] = self.model_name

        if self.quota is not None:
            result['quota'] = self.quota.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modelConnectionId') is not None:
            self.model_connection_id = m.get('modelConnectionId')

        if m.get('modelName') is not None:
            self.model_name = m.get('modelName')

        if m.get('quota') is not None:
            temp_model = main_models.GetExternalAgentResponseBodyDataModelQuota()
            self.quota = temp_model.from_map(m.get('quota'))

        return self

class GetExternalAgentResponseBodyDataModelQuota(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        limit_type: str = None,
        over_limit: bool = None,
        period_type: str = None,
        rule_status: str = None,
        usage_limit: int = None,
        used_amount: int = None,
    ):
        # Indicates whether the quota is enabled. This parameter is not returned if no quota is configured.
        self.enabled = enabled
        # The quota limit type. Currently, only token is supported.
        self.limit_type = limit_type
        # Indicates whether the quota has been exceeded in the current cycle. This is a read-only field returned by the backend.
        self.over_limit = over_limit
        # The quota statistical period. day indicates daily and month indicates monthly.
        self.period_type = period_type
        # The gateway quota rule status. This is a read-only field returned by the backend.
        self.rule_status = rule_status
        # The maximum number of tokens that can be consumed within a single cycle.
        self.usage_limit = usage_limit
        # The number of tokens consumed in the current cycle. This is a read-only field returned by the backend.
        self.used_amount = used_amount

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.limit_type is not None:
            result['limitType'] = self.limit_type

        if self.over_limit is not None:
            result['overLimit'] = self.over_limit

        if self.period_type is not None:
            result['periodType'] = self.period_type

        if self.rule_status is not None:
            result['ruleStatus'] = self.rule_status

        if self.usage_limit is not None:
            result['usageLimit'] = self.usage_limit

        if self.used_amount is not None:
            result['usedAmount'] = self.used_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('limitType') is not None:
            self.limit_type = m.get('limitType')

        if m.get('overLimit') is not None:
            self.over_limit = m.get('overLimit')

        if m.get('periodType') is not None:
            self.period_type = m.get('periodType')

        if m.get('ruleStatus') is not None:
            self.rule_status = m.get('ruleStatus')

        if m.get('usageLimit') is not None:
            self.usage_limit = m.get('usageLimit')

        if m.get('usedAmount') is not None:
            self.used_amount = m.get('usedAmount')

        return self

class GetExternalAgentResponseBodyDataExternalAgentStatus(DaraModel):
    def __init__(
        self,
        heartbeat_status: str = None,
        last_active_at: str = None,
        last_heartbeat: str = None,
        local_ip: str = None,
        runtime: str = None,
    ):
        # The heartbeat status. ONLINE indicates that the most recent heartbeat has not exceeded the configured timeout threshold. STALE indicates that the heartbeat has timed out. UNKNOWN indicates that the heartbeat is missing or has an invalid format. Valid values:
        # - ONLINE: Online.
        # - STALE: Heartbeat expired.
        # - UNKNOWN: Unknown.
        self.heartbeat_status = heartbeat_status
        # The most recent active time of the external agent in RFC 3339 format.
        self.last_active_at = last_active_at
        # The most recent heartbeat time of the external agent in RFC 3339 format.
        self.last_heartbeat = last_heartbeat
        # The local IP address reported by the external agent.
        self.local_ip = local_ip
        # The runtime type reported by the external agent.
        self.runtime = runtime

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.heartbeat_status is not None:
            result['heartbeatStatus'] = self.heartbeat_status

        if self.last_active_at is not None:
            result['lastActiveAt'] = self.last_active_at

        if self.last_heartbeat is not None:
            result['lastHeartbeat'] = self.last_heartbeat

        if self.local_ip is not None:
            result['localIP'] = self.local_ip

        if self.runtime is not None:
            result['runtime'] = self.runtime

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('heartbeatStatus') is not None:
            self.heartbeat_status = m.get('heartbeatStatus')

        if m.get('lastActiveAt') is not None:
            self.last_active_at = m.get('lastActiveAt')

        if m.get('lastHeartbeat') is not None:
            self.last_heartbeat = m.get('lastHeartbeat')

        if m.get('localIP') is not None:
            self.local_ip = m.get('localIP')

        if m.get('runtime') is not None:
            self.runtime = m.get('runtime')

        return self

