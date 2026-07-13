# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateMcpShrinkRequest(DaraModel):
    def __init__(
        self,
        addresses_shrink: str = None,
        auth_config: str = None,
        auth_enabled: bool = None,
        client_token: str = None,
        create_type: str = None,
        description: str = None,
        id: str = None,
        instance_id: str = None,
        swagger_config: str = None,
    ):
        # This parameter is required.
        self.addresses_shrink = addresses_shrink
        self.auth_config = auth_config
        self.auth_enabled = auth_enabled
        self.client_token = client_token
        self.create_type = create_type
        self.description = description
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.instance_id = instance_id
        self.swagger_config = swagger_config

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addresses_shrink is not None:
            result['Addresses'] = self.addresses_shrink

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

        if self.id is not None:
            result['Id'] = self.id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.swagger_config is not None:
            result['SwaggerConfig'] = self.swagger_config

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Addresses') is not None:
            self.addresses_shrink = m.get('Addresses')

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

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('SwaggerConfig') is not None:
            self.swagger_config = m.get('SwaggerConfig')

        return self

