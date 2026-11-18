# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class UpdateConsumerRequest(DaraModel):
    def __init__(
        self,
        ak_sk_identity_configs: List[main_models.AkSkIdentityConfig] = None,
        apikey_identity_config: main_models.ApiKeyIdentityConfig = None,
        clear_expire_at: bool = None,
        description: str = None,
        enable: bool = None,
        enable_after_renewal: bool = None,
        expire_at: int = None,
        jwt_identity_config: main_models.JwtIdentityConfig = None,
        renew: bool = None,
    ):
        # The list of AK/SK identity authentication configurations.
        self.ak_sk_identity_configs = ak_sk_identity_configs
        # The API key identity authentication configuration.
        self.apikey_identity_config = apikey_identity_config
        # Specifies whether to clear the expiration time and restore permanent validity. If this parameter is set to true, expireAt cannot be specified at the same time. The default value is false, which indicates that the expiration time is not cleared.
        self.clear_expire_at = clear_expire_at
        # The description.
        self.description = description
        # Specifies whether to enable the consumer.
        self.enable = enable
        # Specifies whether to enable the consumer after renewal. This parameter can be set to true only when renew=true. The default value is false, which retains the current enabled or disabled state and does not implicitly enable a manually disabled consumer.
        self.enable_after_renewal = enable_after_renewal
        # The expiration time of the consumer, in UTC UNIX seconds. It must be a positive integer and later than the current time. If this parameter is not specified, the original value is retained. This parameter cannot be set at the same time as clearExpireAt=true. If renew=true, the value must be later than the original unexpired expiration time. If the configuration is saved but fails to be delivered, a retry with the original expiration time is allowed, but shortening the expiration time is still prohibited.
        self.expire_at = expire_at
        # The JWT identity authentication configuration.
        self.jwt_identity_config = jwt_identity_config
        # Specifies whether to only renew the consumer. If this parameter is set to true, only the validity period is updated and the consumer is explicitly enabled at the same time. The latest credentials, description, and authorizations on the server are retained. You must set expireAt or clearExpireAt=true, and you cannot specify identity configurations or description. The default value is false, which retains the original consumer update semantics.
        self.renew = renew

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

        if self.clear_expire_at is not None:
            result['clearExpireAt'] = self.clear_expire_at

        if self.description is not None:
            result['description'] = self.description

        if self.enable is not None:
            result['enable'] = self.enable

        if self.enable_after_renewal is not None:
            result['enableAfterRenewal'] = self.enable_after_renewal

        if self.expire_at is not None:
            result['expireAt'] = self.expire_at

        if self.jwt_identity_config is not None:
            result['jwtIdentityConfig'] = self.jwt_identity_config.to_map()

        if self.renew is not None:
            result['renew'] = self.renew

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

        if m.get('clearExpireAt') is not None:
            self.clear_expire_at = m.get('clearExpireAt')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('enableAfterRenewal') is not None:
            self.enable_after_renewal = m.get('enableAfterRenewal')

        if m.get('expireAt') is not None:
            self.expire_at = m.get('expireAt')

        if m.get('jwtIdentityConfig') is not None:
            temp_model = main_models.JwtIdentityConfig()
            self.jwt_identity_config = temp_model.from_map(m.get('jwtIdentityConfig'))

        if m.get('renew') is not None:
            self.renew = m.get('renew')

        return self

