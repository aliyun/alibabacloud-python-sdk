# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentteams20260605 import models as main_models
from darabonba.model import DaraModel

class GetMcpResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetMcpResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            temp_model = main_models.GetMcpResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetMcpResponseBodyData(DaraModel):
    def __init__(
        self,
        addresses: List[str] = None,
        auth_config: str = None,
        auth_enabled: bool = None,
        create_type: str = None,
        deploy_status: str = None,
        description: str = None,
        id: str = None,
        mcp_server_config: str = None,
        name: str = None,
        protocol: str = None,
        swagger_config: str = None,
        url: str = None,
    ):
        self.addresses = addresses
        self.auth_config = auth_config
        self.auth_enabled = auth_enabled
        self.create_type = create_type
        self.deploy_status = deploy_status
        self.description = description
        self.id = id
        self.mcp_server_config = mcp_server_config
        self.name = name
        self.protocol = protocol
        self.swagger_config = swagger_config
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addresses is not None:
            result['Addresses'] = self.addresses

        if self.auth_config is not None:
            result['AuthConfig'] = self.auth_config

        if self.auth_enabled is not None:
            result['AuthEnabled'] = self.auth_enabled

        if self.create_type is not None:
            result['CreateType'] = self.create_type

        if self.deploy_status is not None:
            result['DeployStatus'] = self.deploy_status

        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.mcp_server_config is not None:
            result['McpServerConfig'] = self.mcp_server_config

        if self.name is not None:
            result['Name'] = self.name

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.swagger_config is not None:
            result['SwaggerConfig'] = self.swagger_config

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Addresses') is not None:
            self.addresses = m.get('Addresses')

        if m.get('AuthConfig') is not None:
            self.auth_config = m.get('AuthConfig')

        if m.get('AuthEnabled') is not None:
            self.auth_enabled = m.get('AuthEnabled')

        if m.get('CreateType') is not None:
            self.create_type = m.get('CreateType')

        if m.get('DeployStatus') is not None:
            self.deploy_status = m.get('DeployStatus')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('McpServerConfig') is not None:
            self.mcp_server_config = m.get('McpServerConfig')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('SwaggerConfig') is not None:
            self.swagger_config = m.get('SwaggerConfig')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

