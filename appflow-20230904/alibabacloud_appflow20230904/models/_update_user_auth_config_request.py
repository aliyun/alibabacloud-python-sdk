# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateUserAuthConfigRequest(DaraModel):
    def __init__(
        self,
        auth_config: str = None,
        auth_config_id: str = None,
        auth_config_name: str = None,
        connector_id: str = None,
        connector_version: str = None,
    ):
        self.auth_config = auth_config
        # This parameter is required.
        self.auth_config_id = auth_config_id
        self.auth_config_name = auth_config_name
        # This parameter is required.
        self.connector_id = connector_id
        self.connector_version = connector_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_config is not None:
            result['AuthConfig'] = self.auth_config

        if self.auth_config_id is not None:
            result['AuthConfigId'] = self.auth_config_id

        if self.auth_config_name is not None:
            result['AuthConfigName'] = self.auth_config_name

        if self.connector_id is not None:
            result['ConnectorId'] = self.connector_id

        if self.connector_version is not None:
            result['ConnectorVersion'] = self.connector_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthConfig') is not None:
            self.auth_config = m.get('AuthConfig')

        if m.get('AuthConfigId') is not None:
            self.auth_config_id = m.get('AuthConfigId')

        if m.get('AuthConfigName') is not None:
            self.auth_config_name = m.get('AuthConfigName')

        if m.get('ConnectorId') is not None:
            self.connector_id = m.get('ConnectorId')

        if m.get('ConnectorVersion') is not None:
            self.connector_version = m.get('ConnectorVersion')

        return self

