# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class AgentServiceConfig(DaraModel):
    def __init__(
        self,
        address: str = None,
        dash_scope_config: main_models.AgentServiceConfigDashScopeConfig = None,
        dify_config: main_models.AgentServiceConfigDifyConfig = None,
        enable_health_check: bool = None,
        protocols: List[str] = None,
        provider: str = None,
    ):
        # This parameter is required.
        self.address = address
        self.dash_scope_config = dash_scope_config
        self.dify_config = dify_config
        self.enable_health_check = enable_health_check
        self.protocols = protocols
        # This parameter is required.
        self.provider = provider

    def validate(self):
        if self.dash_scope_config:
            self.dash_scope_config.validate()
        if self.dify_config:
            self.dify_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['address'] = self.address

        if self.dash_scope_config is not None:
            result['dashScopeConfig'] = self.dash_scope_config.to_map()

        if self.dify_config is not None:
            result['difyConfig'] = self.dify_config.to_map()

        if self.enable_health_check is not None:
            result['enableHealthCheck'] = self.enable_health_check

        if self.protocols is not None:
            result['protocols'] = self.protocols

        if self.provider is not None:
            result['provider'] = self.provider

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address') is not None:
            self.address = m.get('address')

        if m.get('dashScopeConfig') is not None:
            temp_model = main_models.AgentServiceConfigDashScopeConfig()
            self.dash_scope_config = temp_model.from_map(m.get('dashScopeConfig'))

        if m.get('difyConfig') is not None:
            temp_model = main_models.AgentServiceConfigDifyConfig()
            self.dify_config = temp_model.from_map(m.get('difyConfig'))

        if m.get('enableHealthCheck') is not None:
            self.enable_health_check = m.get('enableHealthCheck')

        if m.get('protocols') is not None:
            self.protocols = m.get('protocols')

        if m.get('provider') is not None:
            self.provider = m.get('provider')

        return self

class AgentServiceConfigDifyConfig(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        bot_type: str = None,
    ):
        self.api_key = api_key
        self.bot_type = bot_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['apiKey'] = self.api_key

        if self.bot_type is not None:
            result['botType'] = self.bot_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiKey') is not None:
            self.api_key = m.get('apiKey')

        if m.get('botType') is not None:
            self.bot_type = m.get('botType')

        return self

class AgentServiceConfigDashScopeConfig(DaraModel):
    def __init__(
        self,
        app_credentials: List[main_models.AgentServiceConfigDashScopeConfigAppCredentials] = None,
    ):
        self.app_credentials = app_credentials

    def validate(self):
        if self.app_credentials:
            for v1 in self.app_credentials:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['appCredentials'] = []
        if self.app_credentials is not None:
            for k1 in self.app_credentials:
                result['appCredentials'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app_credentials = []
        if m.get('appCredentials') is not None:
            for k1 in m.get('appCredentials'):
                temp_model = main_models.AgentServiceConfigDashScopeConfigAppCredentials()
                self.app_credentials.append(temp_model.from_map(k1))

        return self



class AgentServiceConfigDashScopeConfigAppCredentials(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        app_id: str = None,
    ):
        self.api_key = api_key
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['apiKey'] = self.api_key

        if self.app_id is not None:
            result['appId'] = self.app_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiKey') is not None:
            self.api_key = m.get('apiKey')

        if m.get('appId') is not None:
            self.app_id = m.get('appId')

        return self

