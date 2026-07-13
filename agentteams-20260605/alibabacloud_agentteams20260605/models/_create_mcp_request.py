# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateMcpRequest(DaraModel):
    def __init__(
        self,
        addresses: List[str] = None,
        auth_config: str = None,
        auth_enabled: bool = None,
        client_token: str = None,
        create_type: str = None,
        description: str = None,
        instance_id: str = None,
        name: str = None,
        protocol: str = None,
        swagger_config: str = None,
    ):
        # This parameter is required.
        self.addresses = addresses
        self.auth_config = auth_config
        self.auth_enabled = auth_enabled
        self.client_token = client_token
        self.create_type = create_type
        self.description = description
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.name = name
        self.protocol = protocol
        self.swagger_config = swagger_config

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

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.create_type is not None:
            result['CreateType'] = self.create_type

        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.swagger_config is not None:
            result['SwaggerConfig'] = self.swagger_config

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Addresses') is not None:
            self.addresses = m.get('Addresses')

        if m.get('AuthConfig') is not None:
            self.auth_config = m.get('AuthConfig')

        if m.get('AuthEnabled') is not None:
            self.auth_enabled = m.get('AuthEnabled')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CreateType') is not None:
            self.create_type = m.get('CreateType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('SwaggerConfig') is not None:
            self.swagger_config = m.get('SwaggerConfig')

        return self

