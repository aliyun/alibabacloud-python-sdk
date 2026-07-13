# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentteams20260605 import models as main_models
from darabonba.model import DaraModel

class UpdateWorkerResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.UpdateWorkerResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
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
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.UpdateWorkerResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class UpdateWorkerResponseBodyData(DaraModel):
    def __init__(
        self,
        agent_type: str = None,
        agents: str = None,
        channels: List[main_models.UpdateWorkerResponseBodyDataChannels] = None,
        credentials: List[main_models.UpdateWorkerResponseBodyDataCredentials] = None,
        deploy_type: str = None,
        groups: List[main_models.UpdateWorkerResponseBodyDataGroups] = None,
        instance_id: str = None,
        limit_config: main_models.UpdateWorkerResponseBodyDataLimitConfig = None,
        mcp_servers: List[main_models.UpdateWorkerResponseBodyDataMcpServers] = None,
        model: main_models.UpdateWorkerResponseBodyDataModel = None,
        name: str = None,
        region_id: str = None,
        skills: List[main_models.UpdateWorkerResponseBodyDataSkills] = None,
        soul: str = None,
        start_time: str = None,
        status: str = None,
        template: main_models.UpdateWorkerResponseBodyDataTemplate = None,
        version_code: str = None,
    ):
        self.agent_type = agent_type
        self.agents = agents
        self.channels = channels
        self.credentials = credentials
        self.deploy_type = deploy_type
        self.groups = groups
        self.instance_id = instance_id
        self.limit_config = limit_config
        self.mcp_servers = mcp_servers
        self.model = model
        self.name = name
        self.region_id = region_id
        self.skills = skills
        self.soul = soul
        self.start_time = start_time
        self.status = status
        self.template = template
        self.version_code = version_code

    def validate(self):
        if self.channels:
            for v1 in self.channels:
                 if v1:
                    v1.validate()
        if self.credentials:
            for v1 in self.credentials:
                 if v1:
                    v1.validate()
        if self.groups:
            for v1 in self.groups:
                 if v1:
                    v1.validate()
        if self.limit_config:
            self.limit_config.validate()
        if self.mcp_servers:
            for v1 in self.mcp_servers:
                 if v1:
                    v1.validate()
        if self.model:
            self.model.validate()
        if self.skills:
            for v1 in self.skills:
                 if v1:
                    v1.validate()
        if self.template:
            self.template.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_type is not None:
            result['AgentType'] = self.agent_type

        if self.agents is not None:
            result['Agents'] = self.agents

        result['Channels'] = []
        if self.channels is not None:
            for k1 in self.channels:
                result['Channels'].append(k1.to_map() if k1 else None)

        result['Credentials'] = []
        if self.credentials is not None:
            for k1 in self.credentials:
                result['Credentials'].append(k1.to_map() if k1 else None)

        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type

        result['Groups'] = []
        if self.groups is not None:
            for k1 in self.groups:
                result['Groups'].append(k1.to_map() if k1 else None)

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.limit_config is not None:
            result['LimitConfig'] = self.limit_config.to_map()

        result['McpServers'] = []
        if self.mcp_servers is not None:
            for k1 in self.mcp_servers:
                result['McpServers'].append(k1.to_map() if k1 else None)

        if self.model is not None:
            result['Model'] = self.model.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        result['Skills'] = []
        if self.skills is not None:
            for k1 in self.skills:
                result['Skills'].append(k1.to_map() if k1 else None)

        if self.soul is not None:
            result['Soul'] = self.soul

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.template is not None:
            result['Template'] = self.template.to_map()

        if self.version_code is not None:
            result['VersionCode'] = self.version_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentType') is not None:
            self.agent_type = m.get('AgentType')

        if m.get('Agents') is not None:
            self.agents = m.get('Agents')

        self.channels = []
        if m.get('Channels') is not None:
            for k1 in m.get('Channels'):
                temp_model = main_models.UpdateWorkerResponseBodyDataChannels()
                self.channels.append(temp_model.from_map(k1))

        self.credentials = []
        if m.get('Credentials') is not None:
            for k1 in m.get('Credentials'):
                temp_model = main_models.UpdateWorkerResponseBodyDataCredentials()
                self.credentials.append(temp_model.from_map(k1))

        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')

        self.groups = []
        if m.get('Groups') is not None:
            for k1 in m.get('Groups'):
                temp_model = main_models.UpdateWorkerResponseBodyDataGroups()
                self.groups.append(temp_model.from_map(k1))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LimitConfig') is not None:
            temp_model = main_models.UpdateWorkerResponseBodyDataLimitConfig()
            self.limit_config = temp_model.from_map(m.get('LimitConfig'))

        self.mcp_servers = []
        if m.get('McpServers') is not None:
            for k1 in m.get('McpServers'):
                temp_model = main_models.UpdateWorkerResponseBodyDataMcpServers()
                self.mcp_servers.append(temp_model.from_map(k1))

        if m.get('Model') is not None:
            temp_model = main_models.UpdateWorkerResponseBodyDataModel()
            self.model = temp_model.from_map(m.get('Model'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        self.skills = []
        if m.get('Skills') is not None:
            for k1 in m.get('Skills'):
                temp_model = main_models.UpdateWorkerResponseBodyDataSkills()
                self.skills.append(temp_model.from_map(k1))

        if m.get('Soul') is not None:
            self.soul = m.get('Soul')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Template') is not None:
            temp_model = main_models.UpdateWorkerResponseBodyDataTemplate()
            self.template = temp_model.from_map(m.get('Template'))

        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')

        return self

class UpdateWorkerResponseBodyDataTemplate(DaraModel):
    def __init__(
        self,
        label: str = None,
        name: str = None,
        version: str = None,
    ):
        self.label = label
        self.name = name
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label is not None:
            result['Label'] = self.label

        if self.name is not None:
            result['Name'] = self.name

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class UpdateWorkerResponseBodyDataSkills(DaraModel):
    def __init__(
        self,
        label: str = None,
        name: str = None,
        version: str = None,
    ):
        self.label = label
        self.name = name
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label is not None:
            result['Label'] = self.label

        if self.name is not None:
            result['Name'] = self.name

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class UpdateWorkerResponseBodyDataModel(DaraModel):
    def __init__(
        self,
        model_name: str = None,
        model_provider: str = None,
    ):
        self.model_name = model_name
        self.model_provider = model_provider

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_name is not None:
            result['ModelName'] = self.model_name

        if self.model_provider is not None:
            result['ModelProvider'] = self.model_provider

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        if m.get('ModelProvider') is not None:
            self.model_provider = m.get('ModelProvider')

        return self

class UpdateWorkerResponseBodyDataMcpServers(DaraModel):
    def __init__(
        self,
        name: str = None,
        transport: str = None,
        url: str = None,
    ):
        self.name = name
        self.transport = transport
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.transport is not None:
            result['Transport'] = self.transport

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Transport') is not None:
            self.transport = m.get('Transport')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class UpdateWorkerResponseBodyDataLimitConfig(DaraModel):
    def __init__(
        self,
        limit_type: str = None,
        period_type: str = None,
        usage_limit: int = None,
    ):
        self.limit_type = limit_type
        self.period_type = period_type
        self.usage_limit = usage_limit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.limit_type is not None:
            result['LimitType'] = self.limit_type

        if self.period_type is not None:
            result['PeriodType'] = self.period_type

        if self.usage_limit is not None:
            result['UsageLimit'] = self.usage_limit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LimitType') is not None:
            self.limit_type = m.get('LimitType')

        if m.get('PeriodType') is not None:
            self.period_type = m.get('PeriodType')

        if m.get('UsageLimit') is not None:
            self.usage_limit = m.get('UsageLimit')

        return self

class UpdateWorkerResponseBodyDataGroups(DaraModel):
    def __init__(
        self,
        name: str = None,
        role: str = None,
        type: str = None,
    ):
        self.name = name
        self.role = role
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.role is not None:
            result['Role'] = self.role

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class UpdateWorkerResponseBodyDataCredentials(DaraModel):
    def __init__(
        self,
        name: str = None,
    ):
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

class UpdateWorkerResponseBodyDataChannels(DaraModel):
    def __init__(
        self,
        config: main_models.UpdateWorkerResponseBodyDataChannelsConfig = None,
        enabled: bool = None,
        secret_status: main_models.UpdateWorkerResponseBodyDataChannelsSecretStatus = None,
        type: str = None,
    ):
        self.config = config
        self.enabled = enabled
        self.secret_status = secret_status
        self.type = type

    def validate(self):
        if self.config:
            self.config.validate()
        if self.secret_status:
            self.secret_status.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config.to_map()

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.secret_status is not None:
            result['SecretStatus'] = self.secret_status.to_map()

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            temp_model = main_models.UpdateWorkerResponseBodyDataChannelsConfig()
            self.config = temp_model.from_map(m.get('Config'))

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('SecretStatus') is not None:
            temp_model = main_models.UpdateWorkerResponseBodyDataChannelsSecretStatus()
            self.secret_status = temp_model.from_map(m.get('SecretStatus'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class UpdateWorkerResponseBodyDataChannelsSecretStatus(DaraModel):
    def __init__(
        self,
        client_secret: bool = None,
    ):
        self.client_secret = client_secret

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_secret is not None:
            result['ClientSecret'] = self.client_secret

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientSecret') is not None:
            self.client_secret = m.get('ClientSecret')

        return self

class UpdateWorkerResponseBodyDataChannelsConfig(DaraModel):
    def __init__(
        self,
        card_template_id: str = None,
        client_id: str = None,
        extension: str = None,
        message_type: str = None,
        robot_code: str = None,
        show_thinking: bool = None,
        show_tool_calls: bool = None,
        streaming_enabled: bool = None,
    ):
        self.card_template_id = card_template_id
        self.client_id = client_id
        self.extension = extension
        self.message_type = message_type
        self.robot_code = robot_code
        self.show_thinking = show_thinking
        self.show_tool_calls = show_tool_calls
        self.streaming_enabled = streaming_enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.card_template_id is not None:
            result['CardTemplateId'] = self.card_template_id

        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.extension is not None:
            result['Extension'] = self.extension

        if self.message_type is not None:
            result['MessageType'] = self.message_type

        if self.robot_code is not None:
            result['RobotCode'] = self.robot_code

        if self.show_thinking is not None:
            result['ShowThinking'] = self.show_thinking

        if self.show_tool_calls is not None:
            result['ShowToolCalls'] = self.show_tool_calls

        if self.streaming_enabled is not None:
            result['StreamingEnabled'] = self.streaming_enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CardTemplateId') is not None:
            self.card_template_id = m.get('CardTemplateId')

        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('Extension') is not None:
            self.extension = m.get('Extension')

        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')

        if m.get('RobotCode') is not None:
            self.robot_code = m.get('RobotCode')

        if m.get('ShowThinking') is not None:
            self.show_thinking = m.get('ShowThinking')

        if m.get('ShowToolCalls') is not None:
            self.show_tool_calls = m.get('ShowToolCalls')

        if m.get('StreamingEnabled') is not None:
            self.streaming_enabled = m.get('StreamingEnabled')

        return self

