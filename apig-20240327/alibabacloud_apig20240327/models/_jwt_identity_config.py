# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class JwtIdentityConfig(DaraModel):
    def __init__(
        self,
        claims_to_headers_configs: List[main_models.JwtIdentityConfigClaimsToHeadersConfigs] = None,
        jwks: str = None,
        jwt_payload_config: main_models.JwtIdentityConfigJwtPayloadConfig = None,
        jwt_token_config: main_models.JwtIdentityConfigJwtTokenConfig = None,
        remote_jwks: str = None,
        secret_type: str = None,
        type: str = None,
    ):
        # The claims-to-headers configurations.
        self.claims_to_headers_configs = claims_to_headers_configs
        # The JWKS configuration.
        self.jwks = jwks
        # The JWT payload configuration.
        self.jwt_payload_config = jwt_payload_config
        # The JWT token configuration.
        self.jwt_token_config = jwt_token_config
        # The remote JWKS.
        self.remote_jwks = remote_jwks
        # The secret type.
        self.secret_type = secret_type
        # The type of authentication configuration.
        self.type = type

    def validate(self):
        if self.claims_to_headers_configs:
            for v1 in self.claims_to_headers_configs:
                 if v1:
                    v1.validate()
        if self.jwt_payload_config:
            self.jwt_payload_config.validate()
        if self.jwt_token_config:
            self.jwt_token_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['claimsToHeadersConfigs'] = []
        if self.claims_to_headers_configs is not None:
            for k1 in self.claims_to_headers_configs:
                result['claimsToHeadersConfigs'].append(k1.to_map() if k1 else None)

        if self.jwks is not None:
            result['jwks'] = self.jwks

        if self.jwt_payload_config is not None:
            result['jwtPayloadConfig'] = self.jwt_payload_config.to_map()

        if self.jwt_token_config is not None:
            result['jwtTokenConfig'] = self.jwt_token_config.to_map()

        if self.remote_jwks is not None:
            result['remoteJwks'] = self.remote_jwks

        if self.secret_type is not None:
            result['secretType'] = self.secret_type

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.claims_to_headers_configs = []
        if m.get('claimsToHeadersConfigs') is not None:
            for k1 in m.get('claimsToHeadersConfigs'):
                temp_model = main_models.JwtIdentityConfigClaimsToHeadersConfigs()
                self.claims_to_headers_configs.append(temp_model.from_map(k1))

        if m.get('jwks') is not None:
            self.jwks = m.get('jwks')

        if m.get('jwtPayloadConfig') is not None:
            temp_model = main_models.JwtIdentityConfigJwtPayloadConfig()
            self.jwt_payload_config = temp_model.from_map(m.get('jwtPayloadConfig'))

        if m.get('jwtTokenConfig') is not None:
            temp_model = main_models.JwtIdentityConfigJwtTokenConfig()
            self.jwt_token_config = temp_model.from_map(m.get('jwtTokenConfig'))

        if m.get('remoteJwks') is not None:
            self.remote_jwks = m.get('remoteJwks')

        if m.get('secretType') is not None:
            self.secret_type = m.get('secretType')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class JwtIdentityConfigJwtTokenConfig(DaraModel):
    def __init__(
        self,
        key: str = None,
        pass_: bool = None,
        position: str = None,
        prefix: str = None,
    ):
        # The JWT key configuration.
        self.key = key
        # Specifies whether to pass through.
        self.pass_ = pass_
        # The storage location of the JWT.
        self.position = position
        # The prefix configuration.
        self.prefix = prefix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['key'] = self.key

        if self.pass_ is not None:
            result['pass'] = self.pass_

        if self.position is not None:
            result['position'] = self.position

        if self.prefix is not None:
            result['prefix'] = self.prefix

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('pass') is not None:
            self.pass_ = m.get('pass')

        if m.get('position') is not None:
            self.position = m.get('position')

        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')

        return self

class JwtIdentityConfigJwtPayloadConfig(DaraModel):
    def __init__(
        self,
        payload_key_name: str = None,
        payload_key_value: str = None,
    ):
        # The JWT payload key configuration.
        self.payload_key_name = payload_key_name
        # The JWT payload value configuration.
        self.payload_key_value = payload_key_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.payload_key_name is not None:
            result['payloadKeyName'] = self.payload_key_name

        if self.payload_key_value is not None:
            result['payloadKeyValue'] = self.payload_key_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('payloadKeyName') is not None:
            self.payload_key_name = m.get('payloadKeyName')

        if m.get('payloadKeyValue') is not None:
            self.payload_key_value = m.get('payloadKeyValue')

        return self

class JwtIdentityConfigClaimsToHeadersConfigs(DaraModel):
    def __init__(
        self,
        claim: str = None,
        header: str = None,
        override: bool = None,
    ):
        # The claim.
        self.claim = claim
        # The header.
        self.header = header
        # The override.
        self.override = override

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.claim is not None:
            result['claim'] = self.claim

        if self.header is not None:
            result['header'] = self.header

        if self.override is not None:
            result['override'] = self.override

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('claim') is not None:
            self.claim = m.get('claim')

        if m.get('header') is not None:
            self.header = m.get('header')

        if m.get('override') is not None:
            self.override = m.get('override')

        return self

