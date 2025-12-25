# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class CreateConsumerRequest(DaraModel):
    def __init__(
        self,
        ak_sk_identity_configs: List[main_models.AkSkIdentityConfig] = None,
        apikey_identity_config: main_models.ApiKeyIdentityConfig = None,
        description: str = None,
        enable: bool = None,
        gateway_type: str = None,
        jwt_identity_config: main_models.JwtIdentityConfig = None,
        name: str = None,
    ):
        # The list of AK/SK identity configurations.
        self.ak_sk_identity_configs = ak_sk_identity_configs
        # The configuration for the API key authentication method.
        self.apikey_identity_config = apikey_identity_config
        # The description of the consumer.
        self.description = description
        # Indicates if enabled.
        self.enable = enable
        # The type of the gateway.
        self.gateway_type = gateway_type
        # The configuration of the JWT identity.
        self.jwt_identity_config = jwt_identity_config
        # The name of the consumer.
        self.name = name

    def validate(self):
        if self.ak_sk_identity_configs:
            for v1 in self.ak_sk_identity_configs:
                 if v1:
                    v1.validate()
        if self.apikey_identity_config:
            self.apikey_identity_config.validate()
        if self.jwt_identity_config:
            self.jwt_identity_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['akSkIdentityConfigs'] = []
        if self.ak_sk_identity_configs is not None:
            for k1 in self.ak_sk_identity_configs:
                result['akSkIdentityConfigs'].append(k1.to_map() if k1 else None)

        if self.apikey_identity_config is not None:
            result['apikeyIdentityConfig'] = self.apikey_identity_config.to_map()

        if self.description is not None:
            result['description'] = self.description

        if self.enable is not None:
            result['enable'] = self.enable

        if self.gateway_type is not None:
            result['gatewayType'] = self.gateway_type

        if self.jwt_identity_config is not None:
            result['jwtIdentityConfig'] = self.jwt_identity_config.to_map()

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ak_sk_identity_configs = []
        if m.get('akSkIdentityConfigs') is not None:
            for k1 in m.get('akSkIdentityConfigs'):
                temp_model = main_models.AkSkIdentityConfig()
                self.ak_sk_identity_configs.append(temp_model.from_map(k1))

        if m.get('apikeyIdentityConfig') is not None:
            temp_model = main_models.ApiKeyIdentityConfig()
            self.apikey_identity_config = temp_model.from_map(m.get('apikeyIdentityConfig'))

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('gatewayType') is not None:
            self.gateway_type = m.get('gatewayType')

        if m.get('jwtIdentityConfig') is not None:
            temp_model = main_models.JwtIdentityConfig()
            self.jwt_identity_config = temp_model.from_map(m.get('jwtIdentityConfig'))

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

