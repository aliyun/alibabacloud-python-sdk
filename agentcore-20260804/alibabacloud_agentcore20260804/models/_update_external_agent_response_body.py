# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class UpdateExternalAgentResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.UpdateExternalAgentResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business status code. A value of SUCCESS indicates success.
        self.code = code
        # The details of the updated external agent.
        self.data = data
        # The HTTP status code. A value of 200 indicates success.
        self.http_status_code = http_status_code
        # The message that indicates the result of the request.
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
            temp_model = main_models.UpdateExternalAgentResponseBodyData()
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

class UpdateExternalAgentResponseBodyData(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        create_mode: str = None,
        created_at: str = None,
        deploy_type: str = None,
        description: str = None,
        effective_result: main_models.UpdateExternalAgentResponseBodyDataEffectiveResult = None,
        effective_spec_version: int = None,
        external_agent_status: main_models.UpdateExternalAgentResponseBodyDataExternalAgentStatus = None,
        instruction: str = None,
        latest_spec_version: int = None,
        latest_version_status: str = None,
        model: main_models.UpdateExternalAgentResponseBodyDataModel = None,
        model_source: str = None,
        name: str = None,
        region_id: str = None,
        runtime: str = None,
        skills: List[main_models.UpdateExternalAgentResponseBodyDataSkills] = None,
        status: str = None,
        template: main_models.UpdateExternalAgentResponseBodyDataTemplate = None,
        tools: List[main_models.UpdateExternalAgentResponseBodyDataTools] = None,
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
        # The runtime result corresponding to the currently effective specification.
        self.effective_result = effective_result
        # The currently effective specification version number.
        self.effective_spec_version = effective_spec_version
        # The runtime status information reported by the external agent.
        self.external_agent_status = external_agent_status
        # The agent instruction that guides the behavior of the agent.
        self.instruction = instruction
        # The latest specification version number.
        self.latest_spec_version = latest_spec_version
        # The processing status of the latest specification version. Valid values:
        # - pending: Pending processing.
        # - processing: Being processed.
        # - waiting_retry: Waiting for retry.
        # - succeeded: Succeeded.
        # - failed: Failed.
        # - superseded: Superseded by a newer version.
        self.latest_version_status = latest_version_status
        # The model configuration. This parameter is available only when modelSource is set to PLATFORM.
        self.model = model
        # The source of the model configuration. Valid values:
        # 
        # - PLATFORM: The model configuration is parsed and distributed by the platform. You can specify the model parameter.
        # - RUNTIME: The model is managed by the external runtime. You cannot specify the model parameter at the same time.
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
        # - Creating: The agent is being created.
        # - Running: The agent is running.
        # - Failed: The agent has failed.
        # - Updating: The agent is being updated.
        # - Deleting: The agent is being deleted.
        # - Deleted: The agent has been deleted.
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
        if self.effective_result:
            self.effective_result.validate()
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

        if self.effective_result is not None:
            result['effectiveResult'] = self.effective_result.to_map()

        if self.effective_spec_version is not None:
            result['effectiveSpecVersion'] = self.effective_spec_version

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

        if m.get('effectiveResult') is not None:
            temp_model = main_models.UpdateExternalAgentResponseBodyDataEffectiveResult()
            self.effective_result = temp_model.from_map(m.get('effectiveResult'))

        if m.get('effectiveSpecVersion') is not None:
            self.effective_spec_version = m.get('effectiveSpecVersion')

        if m.get('externalAgentStatus') is not None:
            temp_model = main_models.UpdateExternalAgentResponseBodyDataExternalAgentStatus()
            self.external_agent_status = temp_model.from_map(m.get('externalAgentStatus'))

        if m.get('instruction') is not None:
            self.instruction = m.get('instruction')

        if m.get('latestSpecVersion') is not None:
            self.latest_spec_version = m.get('latestSpecVersion')

        if m.get('latestVersionStatus') is not None:
            self.latest_version_status = m.get('latestVersionStatus')

        if m.get('model') is not None:
            temp_model = main_models.UpdateExternalAgentResponseBodyDataModel()
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
                temp_model = main_models.UpdateExternalAgentResponseBodyDataSkills()
                self.skills.append(temp_model.from_map(k1))

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('template') is not None:
            temp_model = main_models.UpdateExternalAgentResponseBodyDataTemplate()
            self.template = temp_model.from_map(m.get('template'))

        self.tools = []
        if m.get('tools') is not None:
            for k1 in m.get('tools'):
                temp_model = main_models.UpdateExternalAgentResponseBodyDataTools()
                self.tools.append(temp_model.from_map(k1))

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

class UpdateExternalAgentResponseBodyDataTools(DaraModel):
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
        # 
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

class UpdateExternalAgentResponseBodyDataTemplate(DaraModel):
    def __init__(
        self,
        ai_registry: main_models.UpdateExternalAgentResponseBodyDataTemplateAiRegistry = None,
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
            temp_model = main_models.UpdateExternalAgentResponseBodyDataTemplateAiRegistry()
            self.ai_registry = temp_model.from_map(m.get('aiRegistry'))

        return self

class UpdateExternalAgentResponseBodyDataTemplateAiRegistry(DaraModel):
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

class UpdateExternalAgentResponseBodyDataSkills(DaraModel):
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

class UpdateExternalAgentResponseBodyDataModel(DaraModel):
    def __init__(
        self,
        model_connection_id: str = None,
        model_name: str = None,
    ):
        # The model connection ID.
        # 
        # This parameter is required.
        self.model_connection_id = model_connection_id
        # The upstream model name.
        # 
        # This parameter is required.
        self.model_name = model_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_connection_id is not None:
            result['modelConnectionId'] = self.model_connection_id

        if self.model_name is not None:
            result['modelName'] = self.model_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modelConnectionId') is not None:
            self.model_connection_id = m.get('modelConnectionId')

        if m.get('modelName') is not None:
            self.model_name = m.get('modelName')

        return self

class UpdateExternalAgentResponseBodyDataExternalAgentStatus(DaraModel):
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
        # The time when the external agent was last active in RFC 3339 format.
        self.last_active_at = last_active_at
        # The time of the most recent heartbeat from the external agent in RFC 3339 format.
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

class UpdateExternalAgentResponseBodyDataEffectiveResult(DaraModel):
    def __init__(
        self,
        matrix_user_id: str = None,
        personal_room_id: str = None,
        runtime_accept_status: str = None,
        runtime_id: str = None,
        runtime_request_version: int = None,
        workspace_prefix: str = None,
    ):
        # The user ID of the agent in Matrix.
        self.matrix_user_id = matrix_user_id
        # The Matrix personal room ID of the agent.
        self.personal_room_id = personal_room_id
        # The acceptance status of the runtime for the current request version.
        self.runtime_accept_status = runtime_accept_status
        # The runtime instance ID.
        self.runtime_id = runtime_id
        # The runtime request version number.
        self.runtime_request_version = runtime_request_version
        # The storage prefix of the agent in the workspace.
        self.workspace_prefix = workspace_prefix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.matrix_user_id is not None:
            result['matrixUserId'] = self.matrix_user_id

        if self.personal_room_id is not None:
            result['personalRoomId'] = self.personal_room_id

        if self.runtime_accept_status is not None:
            result['runtimeAcceptStatus'] = self.runtime_accept_status

        if self.runtime_id is not None:
            result['runtimeId'] = self.runtime_id

        if self.runtime_request_version is not None:
            result['runtimeRequestVersion'] = self.runtime_request_version

        if self.workspace_prefix is not None:
            result['workspacePrefix'] = self.workspace_prefix

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matrixUserId') is not None:
            self.matrix_user_id = m.get('matrixUserId')

        if m.get('personalRoomId') is not None:
            self.personal_room_id = m.get('personalRoomId')

        if m.get('runtimeAcceptStatus') is not None:
            self.runtime_accept_status = m.get('runtimeAcceptStatus')

        if m.get('runtimeId') is not None:
            self.runtime_id = m.get('runtimeId')

        if m.get('runtimeRequestVersion') is not None:
            self.runtime_request_version = m.get('runtimeRequestVersion')

        if m.get('workspacePrefix') is not None:
            self.workspace_prefix = m.get('workspacePrefix')

        return self

