# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_appflow20230904 import models as main_models
from darabonba.model import DaraModel

class GetUserAuthConfigResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        user_auth_config: main_models.GetUserAuthConfigResponseBodyUserAuthConfig = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.user_auth_config = user_auth_config

    def validate(self):
        if self.user_auth_config:
            self.user_auth_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.user_auth_config is not None:
            result['UserAuthConfig'] = self.user_auth_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UserAuthConfig') is not None:
            temp_model = main_models.GetUserAuthConfigResponseBodyUserAuthConfig()
            self.user_auth_config = temp_model.from_map(m.get('UserAuthConfig'))

        return self

class GetUserAuthConfigResponseBodyUserAuthConfig(DaraModel):
    def __init__(
        self,
        auth_config: str = None,
        auth_config_id: str = None,
        auth_config_name: str = None,
        auth_type: str = None,
        connector_id: str = None,
        connector_version: str = None,
    ):
        self.auth_config = auth_config
        self.auth_config_id = auth_config_id
        self.auth_config_name = auth_config_name
        self.auth_type = auth_type
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

        if self.auth_type is not None:
            result['AuthType'] = self.auth_type

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

        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')

        if m.get('ConnectorId') is not None:
            self.connector_id = m.get('ConnectorId')

        if m.get('ConnectorVersion') is not None:
            self.connector_version = m.get('ConnectorVersion')

        return self

