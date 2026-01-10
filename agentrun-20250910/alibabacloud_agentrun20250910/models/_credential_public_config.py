# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class CredentialPublicConfig(DaraModel):
    def __init__(
        self,
        auth_config: Dict[str, str] = None,
        auth_type: str = None,
        header_key: str = None,
        provider: str = None,
        remote_config: main_models.CredentialPublicConfigRemoteConfig = None,
        users: List[main_models.CredentialPublicConfigUsers] = None,
    ):
        self.auth_config = auth_config
        self.auth_type = auth_type
        self.header_key = header_key
        self.provider = provider
        self.remote_config = remote_config
        self.users = users

    def validate(self):
        if self.remote_config:
            self.remote_config.validate()
        if self.users:
            for v1 in self.users:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_config is not None:
            result['authConfig'] = self.auth_config

        if self.auth_type is not None:
            result['authType'] = self.auth_type

        if self.header_key is not None:
            result['headerKey'] = self.header_key

        if self.provider is not None:
            result['provider'] = self.provider

        if self.remote_config is not None:
            result['remoteConfig'] = self.remote_config.to_map()

        result['users'] = []
        if self.users is not None:
            for k1 in self.users:
                result['users'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authConfig') is not None:
            self.auth_config = m.get('authConfig')

        if m.get('authType') is not None:
            self.auth_type = m.get('authType')

        if m.get('headerKey') is not None:
            self.header_key = m.get('headerKey')

        if m.get('provider') is not None:
            self.provider = m.get('provider')

        if m.get('remoteConfig') is not None:
            temp_model = main_models.CredentialPublicConfigRemoteConfig()
            self.remote_config = temp_model.from_map(m.get('remoteConfig'))

        self.users = []
        if m.get('users') is not None:
            for k1 in m.get('users'):
                temp_model = main_models.CredentialPublicConfigUsers()
                self.users.append(temp_model.from_map(k1))

        return self

class CredentialPublicConfigUsers(DaraModel):
    def __init__(
        self,
        password: str = None,
        username: str = None,
    ):
        self.password = password
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.password is not None:
            result['password'] = self.password

        if self.username is not None:
            result['username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('password') is not None:
            self.password = m.get('password')

        if m.get('username') is not None:
            self.username = m.get('username')

        return self



class CredentialPublicConfigRemoteConfig(DaraModel):
    def __init__(
        self,
        timeout: int = None,
        ttl: int = None,
        uri: str = None,
    ):
        self.timeout = timeout
        self.ttl = ttl
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.timeout is not None:
            result['timeout'] = self.timeout

        if self.ttl is not None:
            result['ttl'] = self.ttl

        if self.uri is not None:
            result['uri'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')

        if m.get('ttl') is not None:
            self.ttl = m.get('ttl')

        if m.get('uri') is not None:
            self.uri = m.get('uri')

        return self

