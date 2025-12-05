# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class ChatMessagesRequestInputs(TeaModel):
    def __init__(
        self,
        custom_agent_id: str = None,
        language: str = None,
        region_id: str = None,
        timezone: str = None,
    ):
        self.custom_agent_id = custom_agent_id
        self.language = language
        self.region_id = region_id
        self.timezone = timezone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_agent_id is not None:
            result['CustomAgentId'] = self.custom_agent_id
        if self.language is not None:
            result['Language'] = self.language
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.timezone is not None:
            result['Timezone'] = self.timezone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomAgentId') is not None:
            self.custom_agent_id = m.get('CustomAgentId')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Timezone') is not None:
            self.timezone = m.get('Timezone')
        return self


class ChatMessagesRequest(TeaModel):
    def __init__(
        self,
        conversation_id: str = None,
        inputs: ChatMessagesRequestInputs = None,
        parent_message_id: str = None,
        query: str = None,
    ):
        self.conversation_id = conversation_id
        self.inputs = inputs
        self.parent_message_id = parent_message_id
        # This parameter is required.
        self.query = query

    def validate(self):
        if self.inputs:
            self.inputs.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id
        if self.inputs is not None:
            result['Inputs'] = self.inputs.to_map()
        if self.parent_message_id is not None:
            result['ParentMessageId'] = self.parent_message_id
        if self.query is not None:
            result['Query'] = self.query
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')
        if m.get('Inputs') is not None:
            temp_model = ChatMessagesRequestInputs()
            self.inputs = temp_model.from_map(m['Inputs'])
        if m.get('ParentMessageId') is not None:
            self.parent_message_id = m.get('ParentMessageId')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        return self


class ChatMessagesShrinkRequest(TeaModel):
    def __init__(
        self,
        conversation_id: str = None,
        inputs_shrink: str = None,
        parent_message_id: str = None,
        query: str = None,
    ):
        self.conversation_id = conversation_id
        self.inputs_shrink = inputs_shrink
        self.parent_message_id = parent_message_id
        # This parameter is required.
        self.query = query

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id
        if self.inputs_shrink is not None:
            result['Inputs'] = self.inputs_shrink
        if self.parent_message_id is not None:
            result['ParentMessageId'] = self.parent_message_id
        if self.query is not None:
            result['Query'] = self.query
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')
        if m.get('Inputs') is not None:
            self.inputs_shrink = m.get('Inputs')
        if m.get('ParentMessageId') is not None:
            self.parent_message_id = m.get('ParentMessageId')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        return self


class ChatMessagesResponseBody(TeaModel):
    def __init__(
        self,
        answer: str = None,
        conversation_id: str = None,
        created_at: int = None,
        event: str = None,
        id: str = None,
        message_id: str = None,
        mode: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        self.answer = answer
        self.conversation_id = conversation_id
        self.created_at = created_at
        self.event = event
        self.id = id
        self.message_id = message_id
        self.mode = mode
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer is not None:
            result['Answer'] = self.answer
        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.event is not None:
            result['Event'] = self.event
        if self.id is not None:
            result['Id'] = self.id
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Answer') is not None:
            self.answer = m.get('Answer')
        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Event') is not None:
            self.event = m.get('Event')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ChatMessagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChatMessagesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ChatMessagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChatMessagesTaskStopRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ChatMessagesTaskStopResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: str = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class ChatMessagesTaskStopResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChatMessagesTaskStopResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ChatMessagesTaskStopResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppInstanceRequestDBInstanceConfig(TeaModel):
    def __init__(
        self,
        dbinstance_class: str = None,
        dbinstance_storage: int = None,
        pay_type: str = None,
    ):
        self.dbinstance_class = dbinstance_class
        self.dbinstance_storage = dbinstance_storage
        self.pay_type = pay_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class
        if self.dbinstance_storage is not None:
            result['DBInstanceStorage'] = self.dbinstance_storage
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')
        if m.get('DBInstanceStorage') is not None:
            self.dbinstance_storage = m.get('DBInstanceStorage')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        return self


class CreateAppInstanceRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        app_type: str = None,
        client_token: str = None,
        dbinstance_config: CreateAppInstanceRequestDBInstanceConfig = None,
        dbinstance_name: str = None,
        dashboard_password: str = None,
        dashboard_username: str = None,
        database_password: str = None,
        instance_class: str = None,
        public_endpoint_enabled: bool = None,
        public_network_access_enabled: bool = None,
        ragenabled: bool = None,
        region_id: str = None,
        v_switch_id: str = None,
    ):
        self.app_name = app_name
        self.app_type = app_type
        self.client_token = client_token
        self.dbinstance_config = dbinstance_config
        self.dbinstance_name = dbinstance_name
        self.dashboard_password = dashboard_password
        self.dashboard_username = dashboard_username
        self.database_password = database_password
        self.instance_class = instance_class
        self.public_endpoint_enabled = public_endpoint_enabled
        self.public_network_access_enabled = public_network_access_enabled
        self.ragenabled = ragenabled
        self.region_id = region_id
        self.v_switch_id = v_switch_id

    def validate(self):
        if self.dbinstance_config:
            self.dbinstance_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dbinstance_config is not None:
            result['DBInstanceConfig'] = self.dbinstance_config.to_map()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.dashboard_password is not None:
            result['DashboardPassword'] = self.dashboard_password
        if self.dashboard_username is not None:
            result['DashboardUsername'] = self.dashboard_username
        if self.database_password is not None:
            result['DatabasePassword'] = self.database_password
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.public_endpoint_enabled is not None:
            result['PublicEndpointEnabled'] = self.public_endpoint_enabled
        if self.public_network_access_enabled is not None:
            result['PublicNetworkAccessEnabled'] = self.public_network_access_enabled
        if self.ragenabled is not None:
            result['RAGEnabled'] = self.ragenabled
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DBInstanceConfig') is not None:
            temp_model = CreateAppInstanceRequestDBInstanceConfig()
            self.dbinstance_config = temp_model.from_map(m['DBInstanceConfig'])
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('DashboardPassword') is not None:
            self.dashboard_password = m.get('DashboardPassword')
        if m.get('DashboardUsername') is not None:
            self.dashboard_username = m.get('DashboardUsername')
        if m.get('DatabasePassword') is not None:
            self.database_password = m.get('DatabasePassword')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('PublicEndpointEnabled') is not None:
            self.public_endpoint_enabled = m.get('PublicEndpointEnabled')
        if m.get('PublicNetworkAccessEnabled') is not None:
            self.public_network_access_enabled = m.get('PublicNetworkAccessEnabled')
        if m.get('RAGEnabled') is not None:
            self.ragenabled = m.get('RAGEnabled')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class CreateAppInstanceShrinkRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        app_type: str = None,
        client_token: str = None,
        dbinstance_config_shrink: str = None,
        dbinstance_name: str = None,
        dashboard_password: str = None,
        dashboard_username: str = None,
        database_password: str = None,
        instance_class: str = None,
        public_endpoint_enabled: bool = None,
        public_network_access_enabled: bool = None,
        ragenabled: bool = None,
        region_id: str = None,
        v_switch_id: str = None,
    ):
        self.app_name = app_name
        self.app_type = app_type
        self.client_token = client_token
        self.dbinstance_config_shrink = dbinstance_config_shrink
        self.dbinstance_name = dbinstance_name
        self.dashboard_password = dashboard_password
        self.dashboard_username = dashboard_username
        self.database_password = database_password
        self.instance_class = instance_class
        self.public_endpoint_enabled = public_endpoint_enabled
        self.public_network_access_enabled = public_network_access_enabled
        self.ragenabled = ragenabled
        self.region_id = region_id
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dbinstance_config_shrink is not None:
            result['DBInstanceConfig'] = self.dbinstance_config_shrink
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.dashboard_password is not None:
            result['DashboardPassword'] = self.dashboard_password
        if self.dashboard_username is not None:
            result['DashboardUsername'] = self.dashboard_username
        if self.database_password is not None:
            result['DatabasePassword'] = self.database_password
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.public_endpoint_enabled is not None:
            result['PublicEndpointEnabled'] = self.public_endpoint_enabled
        if self.public_network_access_enabled is not None:
            result['PublicNetworkAccessEnabled'] = self.public_network_access_enabled
        if self.ragenabled is not None:
            result['RAGEnabled'] = self.ragenabled
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DBInstanceConfig') is not None:
            self.dbinstance_config_shrink = m.get('DBInstanceConfig')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('DashboardPassword') is not None:
            self.dashboard_password = m.get('DashboardPassword')
        if m.get('DashboardUsername') is not None:
            self.dashboard_username = m.get('DashboardUsername')
        if m.get('DatabasePassword') is not None:
            self.database_password = m.get('DatabasePassword')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('PublicEndpointEnabled') is not None:
            self.public_endpoint_enabled = m.get('PublicEndpointEnabled')
        if m.get('PublicNetworkAccessEnabled') is not None:
            self.public_network_access_enabled = m.get('PublicNetworkAccessEnabled')
        if m.get('RAGEnabled') is not None:
            self.ragenabled = m.get('RAGEnabled')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class CreateAppInstanceResponseBody(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        request_id: str = None,
    ):
        self.instance_name = instance_name
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAppInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAppInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAppInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCustomAgentRequest(TeaModel):
    def __init__(
        self,
        enable_tools: bool = None,
        name: str = None,
        system_prompt: str = None,
        tools: List[str] = None,
    ):
        self.enable_tools = enable_tools
        self.name = name
        # This parameter is required.
        self.system_prompt = system_prompt
        self.tools = tools

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_tools is not None:
            result['EnableTools'] = self.enable_tools
        if self.name is not None:
            result['Name'] = self.name
        if self.system_prompt is not None:
            result['SystemPrompt'] = self.system_prompt
        if self.tools is not None:
            result['Tools'] = self.tools
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableTools') is not None:
            self.enable_tools = m.get('EnableTools')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SystemPrompt') is not None:
            self.system_prompt = m.get('SystemPrompt')
        if m.get('Tools') is not None:
            self.tools = m.get('Tools')
        return self


class CreateCustomAgentShrinkRequest(TeaModel):
    def __init__(
        self,
        enable_tools: bool = None,
        name: str = None,
        system_prompt: str = None,
        tools_shrink: str = None,
    ):
        self.enable_tools = enable_tools
        self.name = name
        # This parameter is required.
        self.system_prompt = system_prompt
        self.tools_shrink = tools_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_tools is not None:
            result['EnableTools'] = self.enable_tools
        if self.name is not None:
            result['Name'] = self.name
        if self.system_prompt is not None:
            result['SystemPrompt'] = self.system_prompt
        if self.tools_shrink is not None:
            result['Tools'] = self.tools_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableTools') is not None:
            self.enable_tools = m.get('EnableTools')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SystemPrompt') is not None:
            self.system_prompt = m.get('SystemPrompt')
        if m.get('Tools') is not None:
            self.tools_shrink = m.get('Tools')
        return self


class CreateCustomAgentResponseBody(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        enable_tools: bool = None,
        id: str = None,
        name: str = None,
        request_id: str = None,
        system_prompt: str = None,
        tools: List[str] = None,
    ):
        self.created_at = created_at
        self.enable_tools = enable_tools
        # AgentId
        self.id = id
        self.name = name
        self.request_id = request_id
        self.system_prompt = system_prompt
        self.tools = tools

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.enable_tools is not None:
            result['EnableTools'] = self.enable_tools
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.system_prompt is not None:
            result['SystemPrompt'] = self.system_prompt
        if self.tools is not None:
            result['Tools'] = self.tools
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('EnableTools') is not None:
            self.enable_tools = m.get('EnableTools')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SystemPrompt') is not None:
            self.system_prompt = m.get('SystemPrompt')
        if m.get('Tools') is not None:
            self.tools = m.get('Tools')
        return self


class CreateCustomAgentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCustomAgentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateCustomAgentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAppInstanceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_name: str = None,
        region_id: str = None,
    ):
        self.client_token = client_token
        self.instance_name = instance_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteAppInstanceResponseBody(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        request_id: str = None,
    ):
        self.instance_name = instance_name
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAppInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAppInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteAppInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCustomAgentRequest(TeaModel):
    def __init__(
        self,
        custom_agent_id: str = None,
    ):
        # AgentId。
        self.custom_agent_id = custom_agent_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_agent_id is not None:
            result['CustomAgentId'] = self.custom_agent_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomAgentId') is not None:
            self.custom_agent_id = m.get('CustomAgentId')
        return self


class DeleteCustomAgentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: str = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class DeleteCustomAgentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCustomAgentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteCustomAgentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppInstanceAttributeRequest(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        region_id: str = None,
    ):
        self.instance_name = instance_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeAppInstanceAttributeResponseBody(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        app_type: str = None,
        dbinstance_name: str = None,
        eip_status: str = None,
        instance_class: str = None,
        instance_minor_version: str = None,
        instance_name: str = None,
        nat_status: str = None,
        public_connection_string: str = None,
        region_id: str = None,
        request_id: str = None,
        status: str = None,
        v_switch_id: str = None,
        vpc_connection_string: str = None,
        zone_id: str = None,
    ):
        self.app_name = app_name
        self.app_type = app_type
        self.dbinstance_name = dbinstance_name
        self.eip_status = eip_status
        self.instance_class = instance_class
        self.instance_minor_version = instance_minor_version
        self.instance_name = instance_name
        self.nat_status = nat_status
        self.public_connection_string = public_connection_string
        self.region_id = region_id
        self.request_id = request_id
        self.status = status
        self.v_switch_id = v_switch_id
        self.vpc_connection_string = vpc_connection_string
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.eip_status is not None:
            result['EipStatus'] = self.eip_status
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.instance_minor_version is not None:
            result['InstanceMinorVersion'] = self.instance_minor_version
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.nat_status is not None:
            result['NatStatus'] = self.nat_status
        if self.public_connection_string is not None:
            result['PublicConnectionString'] = self.public_connection_string
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_connection_string is not None:
            result['VpcConnectionString'] = self.vpc_connection_string
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('EipStatus') is not None:
            self.eip_status = m.get('EipStatus')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('InstanceMinorVersion') is not None:
            self.instance_minor_version = m.get('InstanceMinorVersion')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('NatStatus') is not None:
            self.nat_status = m.get('NatStatus')
        if m.get('PublicConnectionString') is not None:
            self.public_connection_string = m.get('PublicConnectionString')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcConnectionString') is not None:
            self.vpc_connection_string = m.get('VpcConnectionString')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeAppInstanceAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAppInstanceAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAppInstanceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppInstancesRequest(TeaModel):
    def __init__(
        self,
        app_type: str = None,
        dbinstance_name: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
    ):
        self.app_type = app_type
        self.dbinstance_name = dbinstance_name
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeAppInstancesResponseBodyInstances(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        app_type: str = None,
        dbinstance_name: str = None,
        instance_class: str = None,
        instance_minor_version: str = None,
        instance_name: str = None,
        public_connection_string: str = None,
        region_id: str = None,
        status: str = None,
        v_switch_id: str = None,
        vpc_connection_string: str = None,
    ):
        self.app_name = app_name
        self.app_type = app_type
        self.dbinstance_name = dbinstance_name
        self.instance_class = instance_class
        self.instance_minor_version = instance_minor_version
        self.instance_name = instance_name
        self.public_connection_string = public_connection_string
        self.region_id = region_id
        self.status = status
        self.v_switch_id = v_switch_id
        self.vpc_connection_string = vpc_connection_string

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.instance_minor_version is not None:
            result['InstanceMinorVersion'] = self.instance_minor_version
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.public_connection_string is not None:
            result['PublicConnectionString'] = self.public_connection_string
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_connection_string is not None:
            result['VpcConnectionString'] = self.vpc_connection_string
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('InstanceMinorVersion') is not None:
            self.instance_minor_version = m.get('InstanceMinorVersion')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('PublicConnectionString') is not None:
            self.public_connection_string = m.get('PublicConnectionString')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcConnectionString') is not None:
            self.vpc_connection_string = m.get('VpcConnectionString')
        return self


class DescribeAppInstancesResponseBody(TeaModel):
    def __init__(
        self,
        instances: List[DescribeAppInstancesResponseBodyInstances] = None,
        max_results: int = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.instances = instances
        self.max_results = max_results
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = DescribeAppInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAppInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAppInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAppInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEventsListRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        instance_id_list: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.instance_id_list = instance_id_list
        self.page_number = page_number
        self.page_size = page_size
        # This parameter is required.
        self.region_id = region_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id_list is not None:
            result['InstanceIdList'] = self.instance_id_list
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceIdList') is not None:
            self.instance_id_list = m.get('InstanceIdList')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeEventsListResponseBodyEvents(TeaModel):
    def __init__(
        self,
        event_code: str = None,
        event_status: str = None,
        event_time_list: List[str] = None,
        instance_description: str = None,
        instance_id: str = None,
        recovery_time: str = None,
    ):
        self.event_code = event_code
        self.event_status = event_status
        self.event_time_list = event_time_list
        self.instance_description = instance_description
        self.instance_id = instance_id
        self.recovery_time = recovery_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_code is not None:
            result['EventCode'] = self.event_code
        if self.event_status is not None:
            result['EventStatus'] = self.event_status
        if self.event_time_list is not None:
            result['EventTimeList'] = self.event_time_list
        if self.instance_description is not None:
            result['InstanceDescription'] = self.instance_description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.recovery_time is not None:
            result['RecoveryTime'] = self.recovery_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventCode') is not None:
            self.event_code = m.get('EventCode')
        if m.get('EventStatus') is not None:
            self.event_status = m.get('EventStatus')
        if m.get('EventTimeList') is not None:
            self.event_time_list = m.get('EventTimeList')
        if m.get('InstanceDescription') is not None:
            self.instance_description = m.get('InstanceDescription')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RecoveryTime') is not None:
            self.recovery_time = m.get('RecoveryTime')
        return self


class DescribeEventsListResponseBody(TeaModel):
    def __init__(
        self,
        event_code_counts: str = None,
        events: List[DescribeEventsListResponseBodyEvents] = None,
        page_count: int = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        total_pages: int = None,
    ):
        self.event_code_counts = event_code_counts
        self.events = events
        self.page_count = page_count
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.total_pages = total_pages

    def validate(self):
        if self.events:
            for k in self.events:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_code_counts is not None:
            result['EventCodeCounts'] = self.event_code_counts
        result['Events'] = []
        if self.events is not None:
            for k in self.events:
                result['Events'].append(k.to_map() if k else None)
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventCodeCounts') is not None:
            self.event_code_counts = m.get('EventCodeCounts')
        self.events = []
        if m.get('Events') is not None:
            for k in m.get('Events'):
                temp_model = DescribeEventsListResponseBodyEvents()
                self.events.append(temp_model.from_map(k))
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        return self


class DescribeEventsListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeEventsListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeEventsListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceAuthInfoRequest(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        region_id: str = None,
    ):
        self.instance_name = instance_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeInstanceAuthInfoResponseBodyApiKeys(TeaModel):
    def __init__(
        self,
        anon_key: str = None,
        service_key: str = None,
    ):
        # Supabase ANON_KEY
        self.anon_key = anon_key
        # Supabase SERVICE_ROLE_KEY
        self.service_key = service_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anon_key is not None:
            result['AnonKey'] = self.anon_key
        if self.service_key is not None:
            result['ServiceKey'] = self.service_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnonKey') is not None:
            self.anon_key = m.get('AnonKey')
        if m.get('ServiceKey') is not None:
            self.service_key = m.get('ServiceKey')
        return self


class DescribeInstanceAuthInfoResponseBodyConfigList(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeInstanceAuthInfoResponseBody(TeaModel):
    def __init__(
        self,
        api_keys: DescribeInstanceAuthInfoResponseBodyApiKeys = None,
        config_list: List[DescribeInstanceAuthInfoResponseBodyConfigList] = None,
        instance_name: str = None,
        jwt_secret: str = None,
        request_id: str = None,
    ):
        # API Keys
        self.api_keys = api_keys
        self.config_list = config_list
        self.instance_name = instance_name
        self.jwt_secret = jwt_secret
        self.request_id = request_id

    def validate(self):
        if self.api_keys:
            self.api_keys.validate()
        if self.config_list:
            for k in self.config_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_keys is not None:
            result['ApiKeys'] = self.api_keys.to_map()
        result['ConfigList'] = []
        if self.config_list is not None:
            for k in self.config_list:
                result['ConfigList'].append(k.to_map() if k else None)
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.jwt_secret is not None:
            result['JwtSecret'] = self.jwt_secret
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKeys') is not None:
            temp_model = DescribeInstanceAuthInfoResponseBodyApiKeys()
            self.api_keys = temp_model.from_map(m['ApiKeys'])
        self.config_list = []
        if m.get('ConfigList') is not None:
            for k in m.get('ConfigList'):
                temp_model = DescribeInstanceAuthInfoResponseBodyConfigList()
                self.config_list.append(temp_model.from_map(k))
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('JwtSecret') is not None:
            self.jwt_secret = m.get('JwtSecret')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInstanceAuthInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInstanceAuthInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeInstanceAuthInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceEndpointsRequest(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        region_id: str = None,
    ):
        self.instance_name = instance_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeInstanceEndpointsResponseBodyInstanceEndpoints(TeaModel):
    def __init__(
        self,
        connection_string: str = None,
        ip: str = None,
        ip_type: str = None,
        port: str = None,
    ):
        self.connection_string = connection_string
        self.ip = ip
        self.ip_type = ip_type
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.ip is not None:
            result['IP'] = self.ip
        if self.ip_type is not None:
            result['IpType'] = self.ip_type
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('IpType') is not None:
            self.ip_type = m.get('IpType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class DescribeInstanceEndpointsResponseBody(TeaModel):
    def __init__(
        self,
        instance_endpoints: List[DescribeInstanceEndpointsResponseBodyInstanceEndpoints] = None,
        instance_name: str = None,
        request_id: str = None,
    ):
        self.instance_endpoints = instance_endpoints
        self.instance_name = instance_name
        self.request_id = request_id

    def validate(self):
        if self.instance_endpoints:
            for k in self.instance_endpoints:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceEndpoints'] = []
        if self.instance_endpoints is not None:
            for k in self.instance_endpoints:
                result['InstanceEndpoints'].append(k.to_map() if k else None)
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_endpoints = []
        if m.get('InstanceEndpoints') is not None:
            for k in m.get('InstanceEndpoints'):
                temp_model = DescribeInstanceEndpointsResponseBodyInstanceEndpoints()
                self.instance_endpoints.append(temp_model.from_map(k))
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInstanceEndpointsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInstanceEndpointsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeInstanceEndpointsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceIpWhitelistRequest(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        region_id: str = None,
    ):
        self.instance_name = instance_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeInstanceIpWhitelistResponseBodyIpWhiteListGroups(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        ip_whitelist: str = None,
    ):
        self.group_name = group_name
        self.ip_whitelist = ip_whitelist

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.ip_whitelist is not None:
            result['IpWhitelist'] = self.ip_whitelist
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('IpWhitelist') is not None:
            self.ip_whitelist = m.get('IpWhitelist')
        return self


class DescribeInstanceIpWhitelistResponseBody(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        ip_white_list_groups: List[DescribeInstanceIpWhitelistResponseBodyIpWhiteListGroups] = None,
        request_id: str = None,
    ):
        self.instance_name = instance_name
        self.ip_white_list_groups = ip_white_list_groups
        self.request_id = request_id

    def validate(self):
        if self.ip_white_list_groups:
            for k in self.ip_white_list_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        result['IpWhiteListGroups'] = []
        if self.ip_white_list_groups is not None:
            for k in self.ip_white_list_groups:
                result['IpWhiteListGroups'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        self.ip_white_list_groups = []
        if m.get('IpWhiteListGroups') is not None:
            for k in m.get('IpWhiteListGroups'):
                temp_model = DescribeInstanceIpWhitelistResponseBodyIpWhiteListGroups()
                self.ip_white_list_groups.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInstanceIpWhitelistResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInstanceIpWhitelistResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeInstanceIpWhitelistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceRAGConfigRequest(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.instance_name = instance_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeInstanceRAGConfigResponseBodyConfigList(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeInstanceRAGConfigResponseBody(TeaModel):
    def __init__(
        self,
        config_list: List[DescribeInstanceRAGConfigResponseBodyConfigList] = None,
        instance_name: str = None,
        request_id: str = None,
        status: bool = None,
    ):
        self.config_list = config_list
        self.instance_name = instance_name
        self.request_id = request_id
        self.status = status

    def validate(self):
        if self.config_list:
            for k in self.config_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConfigList'] = []
        if self.config_list is not None:
            for k in self.config_list:
                result['ConfigList'].append(k.to_map() if k else None)
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_list = []
        if m.get('ConfigList') is not None:
            for k in m.get('ConfigList'):
                temp_model = DescribeInstanceRAGConfigResponseBodyConfigList()
                self.config_list.append(temp_model.from_map(k))
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeInstanceRAGConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInstanceRAGConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeInstanceRAGConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceSSLRequest(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.instance_name = instance_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeInstanceSSLResponseBody(TeaModel):
    def __init__(
        self,
        catype: str = None,
        instance_name: str = None,
        request_id: str = None,
        sslenabled: str = None,
        server_cert: str = None,
        server_key: str = None,
    ):
        self.catype = catype
        self.instance_name = instance_name
        self.request_id = request_id
        self.sslenabled = sslenabled
        self.server_cert = server_cert
        self.server_key = server_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catype is not None:
            result['CAType'] = self.catype
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sslenabled is not None:
            result['SSLEnabled'] = self.sslenabled
        if self.server_cert is not None:
            result['ServerCert'] = self.server_cert
        if self.server_key is not None:
            result['ServerKey'] = self.server_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CAType') is not None:
            self.catype = m.get('CAType')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SSLEnabled') is not None:
            self.sslenabled = m.get('SSLEnabled')
        if m.get('ServerCert') is not None:
            self.server_cert = m.get('ServerCert')
        if m.get('ServerKey') is not None:
            self.server_key = m.get('ServerKey')
        return self


class DescribeInstanceSSLResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInstanceSSLResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeInstanceSSLResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceStorageConfigRequest(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.instance_name = instance_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeInstanceStorageConfigResponseBodyConfigList(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeInstanceStorageConfigResponseBody(TeaModel):
    def __init__(
        self,
        config_list: List[DescribeInstanceStorageConfigResponseBodyConfigList] = None,
        instance_name: str = None,
        request_id: str = None,
    ):
        self.config_list = config_list
        self.instance_name = instance_name
        self.request_id = request_id

    def validate(self):
        if self.config_list:
            for k in self.config_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConfigList'] = []
        if self.config_list is not None:
            for k in self.config_list:
                result['ConfigList'].append(k.to_map() if k else None)
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_list = []
        if m.get('ConfigList') is not None:
            for k in m.get('ConfigList'):
                temp_model = DescribeInstanceStorageConfigResponseBodyConfigList()
                self.config_list.append(temp_model.from_map(k))
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInstanceStorageConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInstanceStorageConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeInstanceStorageConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetConversationsRequest(TeaModel):
    def __init__(
        self,
        last_id: str = None,
        limit: str = None,
        pinned: str = None,
        sort_by: str = None,
    ):
        self.last_id = last_id
        self.limit = limit
        self.pinned = pinned
        self.sort_by = sort_by

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.last_id is not None:
            result['LastId'] = self.last_id
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.pinned is not None:
            result['Pinned'] = self.pinned
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LastId') is not None:
            self.last_id = m.get('LastId')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('Pinned') is not None:
            self.pinned = m.get('Pinned')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        return self


class GetConversationsResponseBodyData(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        id: str = None,
        introduction: str = None,
        name: str = None,
    ):
        self.created_at = created_at
        self.id = id
        self.introduction = introduction
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.id is not None:
            result['Id'] = self.id
        if self.introduction is not None:
            result['Introduction'] = self.introduction
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Introduction') is not None:
            self.introduction = m.get('Introduction')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetConversationsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[GetConversationsResponseBodyData] = None,
        has_more: str = None,
        limit: int = None,
        request_id: str = None,
    ):
        self.data = data
        self.has_more = has_more
        self.limit = limit
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.has_more is not None:
            result['HasMore'] = self.has_more
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetConversationsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetConversationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetConversationsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetConversationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCustomAgentRequest(TeaModel):
    def __init__(
        self,
        custom_agent_id: str = None,
    ):
        self.custom_agent_id = custom_agent_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_agent_id is not None:
            result['CustomAgentId'] = self.custom_agent_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomAgentId') is not None:
            self.custom_agent_id = m.get('CustomAgentId')
        return self


class GetCustomAgentResponseBody(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        enable_tools: bool = None,
        id: str = None,
        name: str = None,
        request_id: str = None,
        system_prompt: str = None,
        tools: List[str] = None,
        updated_at: str = None,
    ):
        self.created_at = created_at
        self.enable_tools = enable_tools
        self.id = id
        self.name = name
        self.request_id = request_id
        self.system_prompt = system_prompt
        self.tools = tools
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.enable_tools is not None:
            result['EnableTools'] = self.enable_tools
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.system_prompt is not None:
            result['SystemPrompt'] = self.system_prompt
        if self.tools is not None:
            result['Tools'] = self.tools
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('EnableTools') is not None:
            self.enable_tools = m.get('EnableTools')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SystemPrompt') is not None:
            self.system_prompt = m.get('SystemPrompt')
        if m.get('Tools') is not None:
            self.tools = m.get('Tools')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        return self


class GetCustomAgentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCustomAgentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetCustomAgentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMessagesRequest(TeaModel):
    def __init__(
        self,
        conversation_id: str = None,
        first_id: str = None,
        limit: int = None,
    ):
        self.conversation_id = conversation_id
        self.first_id = first_id
        self.limit = limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id
        if self.first_id is not None:
            result['FirstId'] = self.first_id
        if self.limit is not None:
            result['Limit'] = self.limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')
        if m.get('FirstId') is not None:
            self.first_id = m.get('FirstId')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        return self


class GetMessagesResponseBodyData(TeaModel):
    def __init__(
        self,
        answer: str = None,
        conversation_id: str = None,
        created_at: str = None,
        feedback: str = None,
        id: str = None,
        query: str = None,
        retriever_resources: List[Any] = None,
    ):
        self.answer = answer
        self.conversation_id = conversation_id
        self.created_at = created_at
        self.feedback = feedback
        self.id = id
        self.query = query
        self.retriever_resources = retriever_resources

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer is not None:
            result['Answer'] = self.answer
        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.feedback is not None:
            result['Feedback'] = self.feedback
        if self.id is not None:
            result['Id'] = self.id
        if self.query is not None:
            result['Query'] = self.query
        if self.retriever_resources is not None:
            result['RetrieverResources'] = self.retriever_resources
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Answer') is not None:
            self.answer = m.get('Answer')
        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Feedback') is not None:
            self.feedback = m.get('Feedback')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('RetrieverResources') is not None:
            self.retriever_resources = m.get('RetrieverResources')
        return self


class GetMessagesResponseBody(TeaModel):
    def __init__(
        self,
        data: List[GetMessagesResponseBodyData] = None,
        has_more: bool = None,
        limit: int = None,
        request_id: str = None,
    ):
        self.data = data
        self.has_more = has_more
        self.limit = limit
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.has_more is not None:
            result['HasMore'] = self.has_more
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetMessagesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetMessagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMessagesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetMessagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCustomAgentRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListCustomAgentResponseBodyData(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        enable_tools: bool = None,
        id: str = None,
        name: str = None,
        system_prompt: str = None,
        tools: List[str] = None,
        updated_at: str = None,
    ):
        self.created_at = created_at
        self.enable_tools = enable_tools
        # AgentId。
        self.id = id
        self.name = name
        self.system_prompt = system_prompt
        self.tools = tools
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.enable_tools is not None:
            result['EnableTools'] = self.enable_tools
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.system_prompt is not None:
            result['SystemPrompt'] = self.system_prompt
        if self.tools is not None:
            result['Tools'] = self.tools
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('EnableTools') is not None:
            self.enable_tools = m.get('EnableTools')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SystemPrompt') is not None:
            self.system_prompt = m.get('SystemPrompt')
        if m.get('Tools') is not None:
            self.tools = m.get('Tools')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        return self


class ListCustomAgentResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListCustomAgentResponseBodyData] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.data = data
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListCustomAgentResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListCustomAgentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCustomAgentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListCustomAgentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCustomAgentToolsResponseBodyData(TeaModel):
    def __init__(
        self,
        en: str = None,
        ja: str = None,
        name: str = None,
        tc: str = None,
        type: str = None,
        zh: str = None,
    ):
        self.en = en
        self.ja = ja
        self.name = name
        self.tc = tc
        self.type = type
        self.zh = zh

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.en is not None:
            result['En'] = self.en
        if self.ja is not None:
            result['Ja'] = self.ja
        if self.name is not None:
            result['Name'] = self.name
        if self.tc is not None:
            result['Tc'] = self.tc
        if self.type is not None:
            result['Type'] = self.type
        if self.zh is not None:
            result['Zh'] = self.zh
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('En') is not None:
            self.en = m.get('En')
        if m.get('Ja') is not None:
            self.ja = m.get('Ja')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Tc') is not None:
            self.tc = m.get('Tc')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Zh') is not None:
            self.zh = m.get('Zh')
        return self


class ListCustomAgentToolsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListCustomAgentToolsResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListCustomAgentToolsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListCustomAgentToolsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCustomAgentToolsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListCustomAgentToolsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceAuthConfigRequestConfigList(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ModifyInstanceAuthConfigRequest(TeaModel):
    def __init__(
        self,
        config_list: List[ModifyInstanceAuthConfigRequestConfigList] = None,
        instance_name: str = None,
        region_id: str = None,
    ):
        self.config_list = config_list
        self.instance_name = instance_name
        self.region_id = region_id

    def validate(self):
        if self.config_list:
            for k in self.config_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConfigList'] = []
        if self.config_list is not None:
            for k in self.config_list:
                result['ConfigList'].append(k.to_map() if k else None)
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_list = []
        if m.get('ConfigList') is not None:
            for k in m.get('ConfigList'):
                temp_model = ModifyInstanceAuthConfigRequestConfigList()
                self.config_list.append(temp_model.from_map(k))
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyInstanceAuthConfigShrinkRequest(TeaModel):
    def __init__(
        self,
        config_list_shrink: str = None,
        instance_name: str = None,
        region_id: str = None,
    ):
        self.config_list_shrink = config_list_shrink
        self.instance_name = instance_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_list_shrink is not None:
            result['ConfigList'] = self.config_list_shrink
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigList') is not None:
            self.config_list_shrink = m.get('ConfigList')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyInstanceAuthConfigResponseBody(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        request_id: str = None,
    ):
        self.instance_name = instance_name
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyInstanceAuthConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyInstanceAuthConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyInstanceAuthConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceConfigRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        config_name: str = None,
        config_value: str = None,
        instance_name: str = None,
        region_id: str = None,
    ):
        self.client_token = client_token
        self.config_name = config_name
        self.config_value = config_value
        # This parameter is required.
        self.instance_name = instance_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.config_name is not None:
            result['ConfigName'] = self.config_name
        if self.config_value is not None:
            result['ConfigValue'] = self.config_value
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConfigName') is not None:
            self.config_name = m.get('ConfigName')
        if m.get('ConfigValue') is not None:
            self.config_value = m.get('ConfigValue')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyInstanceConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyInstanceConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyInstanceConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyInstanceConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceIpWhitelistRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        group_name: str = None,
        instance_name: str = None,
        ip_whitelist: str = None,
        modify_mode: str = None,
        region_id: str = None,
    ):
        self.client_token = client_token
        self.group_name = group_name
        self.instance_name = instance_name
        self.ip_whitelist = ip_whitelist
        self.modify_mode = modify_mode
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.ip_whitelist is not None:
            result['IpWhitelist'] = self.ip_whitelist
        if self.modify_mode is not None:
            result['ModifyMode'] = self.modify_mode
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('IpWhitelist') is not None:
            self.ip_whitelist = m.get('IpWhitelist')
        if m.get('ModifyMode') is not None:
            self.modify_mode = m.get('ModifyMode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyInstanceIpWhitelistResponseBody(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        request_id: str = None,
    ):
        self.instance_name = instance_name
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyInstanceIpWhitelistResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyInstanceIpWhitelistResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyInstanceIpWhitelistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceRAGConfigRequestConfigList(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ModifyInstanceRAGConfigRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        config_list: List[ModifyInstanceRAGConfigRequestConfigList] = None,
        instance_name: str = None,
        region_id: str = None,
        status: bool = None,
    ):
        self.client_token = client_token
        self.config_list = config_list
        # This parameter is required.
        self.instance_name = instance_name
        self.region_id = region_id
        self.status = status

    def validate(self):
        if self.config_list:
            for k in self.config_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        result['ConfigList'] = []
        if self.config_list is not None:
            for k in self.config_list:
                result['ConfigList'].append(k.to_map() if k else None)
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        self.config_list = []
        if m.get('ConfigList') is not None:
            for k in m.get('ConfigList'):
                temp_model = ModifyInstanceRAGConfigRequestConfigList()
                self.config_list.append(temp_model.from_map(k))
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ModifyInstanceRAGConfigShrinkRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        config_list_shrink: str = None,
        instance_name: str = None,
        region_id: str = None,
        status: bool = None,
    ):
        self.client_token = client_token
        self.config_list_shrink = config_list_shrink
        # This parameter is required.
        self.instance_name = instance_name
        self.region_id = region_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.config_list_shrink is not None:
            result['ConfigList'] = self.config_list_shrink
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConfigList') is not None:
            self.config_list_shrink = m.get('ConfigList')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ModifyInstanceRAGConfigResponseBody(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        request_id: str = None,
        status: str = None,
    ):
        self.instance_name = instance_name
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ModifyInstanceRAGConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyInstanceRAGConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyInstanceRAGConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceSSLRequest(TeaModel):
    def __init__(
        self,
        catype: str = None,
        instance_name: str = None,
        region_id: str = None,
        sslenabled: int = None,
        server_cert: str = None,
        server_key: str = None,
    ):
        self.catype = catype
        # This parameter is required.
        self.instance_name = instance_name
        self.region_id = region_id
        # This parameter is required.
        self.sslenabled = sslenabled
        self.server_cert = server_cert
        self.server_key = server_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catype is not None:
            result['CAType'] = self.catype
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sslenabled is not None:
            result['SSLEnabled'] = self.sslenabled
        if self.server_cert is not None:
            result['ServerCert'] = self.server_cert
        if self.server_key is not None:
            result['ServerKey'] = self.server_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CAType') is not None:
            self.catype = m.get('CAType')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SSLEnabled') is not None:
            self.sslenabled = m.get('SSLEnabled')
        if m.get('ServerCert') is not None:
            self.server_cert = m.get('ServerCert')
        if m.get('ServerKey') is not None:
            self.server_key = m.get('ServerKey')
        return self


class ModifyInstanceSSLResponseBody(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        request_id: str = None,
    ):
        self.instance_name = instance_name
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyInstanceSSLResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyInstanceSSLResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyInstanceSSLResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceStorageConfigRequestConfigList(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ModifyInstanceStorageConfigRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        config_list: List[ModifyInstanceStorageConfigRequestConfigList] = None,
        instance_name: str = None,
        region_id: str = None,
    ):
        self.client_token = client_token
        self.config_list = config_list
        # This parameter is required.
        self.instance_name = instance_name
        self.region_id = region_id

    def validate(self):
        if self.config_list:
            for k in self.config_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        result['ConfigList'] = []
        if self.config_list is not None:
            for k in self.config_list:
                result['ConfigList'].append(k.to_map() if k else None)
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        self.config_list = []
        if m.get('ConfigList') is not None:
            for k in m.get('ConfigList'):
                temp_model = ModifyInstanceStorageConfigRequestConfigList()
                self.config_list.append(temp_model.from_map(k))
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyInstanceStorageConfigShrinkRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        config_list_shrink: str = None,
        instance_name: str = None,
        region_id: str = None,
    ):
        self.client_token = client_token
        self.config_list_shrink = config_list_shrink
        # This parameter is required.
        self.instance_name = instance_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.config_list_shrink is not None:
            result['ConfigList'] = self.config_list_shrink
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConfigList') is not None:
            self.config_list_shrink = m.get('ConfigList')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyInstanceStorageConfigResponseBody(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        request_id: str = None,
    ):
        self.instance_name = instance_name
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyInstanceStorageConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyInstanceStorageConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyInstanceStorageConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyMessagesFeedbacksRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        message_id: str = None,
        rating: str = None,
    ):
        self.content = content
        self.message_id = message_id
        self.rating = rating

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.rating is not None:
            result['Rating'] = self.rating
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('Rating') is not None:
            self.rating = m.get('Rating')
        return self


class ModifyMessagesFeedbacksResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: str = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class ModifyMessagesFeedbacksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyMessagesFeedbacksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyMessagesFeedbacksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetInstancePasswordRequest(TeaModel):
    def __init__(
        self,
        dashboard_password: str = None,
        database_password: str = None,
        instance_name: str = None,
        region_id: str = None,
    ):
        self.dashboard_password = dashboard_password
        self.database_password = database_password
        # This parameter is required.
        self.instance_name = instance_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dashboard_password is not None:
            result['DashboardPassword'] = self.dashboard_password
        if self.database_password is not None:
            result['DatabasePassword'] = self.database_password
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DashboardPassword') is not None:
            self.dashboard_password = m.get('DashboardPassword')
        if m.get('DatabasePassword') is not None:
            self.database_password = m.get('DatabasePassword')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ResetInstancePasswordResponseBody(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        request_id: str = None,
    ):
        self.instance_name = instance_name
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ResetInstancePasswordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResetInstancePasswordResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ResetInstancePasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.instance_name = instance_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class RestartInstanceResponseBody(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        request_id: str = None,
    ):
        self.instance_name = instance_name
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RestartInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RestartInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RestartInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        region_id: str = None,
    ):
        self.instance_name = instance_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class StartInstanceResponseBody(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        request_id: str = None,
    ):
        self.instance_name = instance_name
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StartInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.instance_name = instance_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class StopInstanceResponseBody(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        request_id: str = None,
    ):
        self.instance_name = instance_name
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StopInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCustomAgentRequest(TeaModel):
    def __init__(
        self,
        custom_agent_id: str = None,
        enable_tools: bool = None,
        name: str = None,
        system_prompt: str = None,
        tools: List[str] = None,
    ):
        # AgentId。
        # 
        # This parameter is required.
        self.custom_agent_id = custom_agent_id
        self.enable_tools = enable_tools
        self.name = name
        self.system_prompt = system_prompt
        self.tools = tools

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_agent_id is not None:
            result['CustomAgentId'] = self.custom_agent_id
        if self.enable_tools is not None:
            result['EnableTools'] = self.enable_tools
        if self.name is not None:
            result['Name'] = self.name
        if self.system_prompt is not None:
            result['SystemPrompt'] = self.system_prompt
        if self.tools is not None:
            result['Tools'] = self.tools
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomAgentId') is not None:
            self.custom_agent_id = m.get('CustomAgentId')
        if m.get('EnableTools') is not None:
            self.enable_tools = m.get('EnableTools')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SystemPrompt') is not None:
            self.system_prompt = m.get('SystemPrompt')
        if m.get('Tools') is not None:
            self.tools = m.get('Tools')
        return self


class UpdateCustomAgentShrinkRequest(TeaModel):
    def __init__(
        self,
        custom_agent_id: str = None,
        enable_tools: bool = None,
        name: str = None,
        system_prompt: str = None,
        tools_shrink: str = None,
    ):
        # AgentId。
        # 
        # This parameter is required.
        self.custom_agent_id = custom_agent_id
        self.enable_tools = enable_tools
        self.name = name
        self.system_prompt = system_prompt
        self.tools_shrink = tools_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_agent_id is not None:
            result['CustomAgentId'] = self.custom_agent_id
        if self.enable_tools is not None:
            result['EnableTools'] = self.enable_tools
        if self.name is not None:
            result['Name'] = self.name
        if self.system_prompt is not None:
            result['SystemPrompt'] = self.system_prompt
        if self.tools_shrink is not None:
            result['Tools'] = self.tools_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomAgentId') is not None:
            self.custom_agent_id = m.get('CustomAgentId')
        if m.get('EnableTools') is not None:
            self.enable_tools = m.get('EnableTools')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SystemPrompt') is not None:
            self.system_prompt = m.get('SystemPrompt')
        if m.get('Tools') is not None:
            self.tools_shrink = m.get('Tools')
        return self


class UpdateCustomAgentResponseBody(TeaModel):
    def __init__(
        self,
        enable_tools: str = None,
        id: str = None,
        name: str = None,
        request_id: str = None,
        system_prompt: str = None,
        tools: List[str] = None,
    ):
        self.enable_tools = enable_tools
        # AgentId。
        self.id = id
        self.name = name
        self.request_id = request_id
        self.system_prompt = system_prompt
        self.tools = tools

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_tools is not None:
            result['EnableTools'] = self.enable_tools
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.system_prompt is not None:
            result['SystemPrompt'] = self.system_prompt
        if self.tools is not None:
            result['Tools'] = self.tools
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableTools') is not None:
            self.enable_tools = m.get('EnableTools')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SystemPrompt') is not None:
            self.system_prompt = m.get('SystemPrompt')
        if m.get('Tools') is not None:
            self.tools = m.get('Tools')
        return self


class UpdateCustomAgentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateCustomAgentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateCustomAgentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


