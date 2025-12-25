# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_milvus20231012 import models as main_models
from darabonba.model import DaraModel

class MigrationSource(DaraModel):
    def __init__(
        self,
        auth_info: main_models.MigrationSourceAuthInfo = None,
        database: str = None,
        endpoint: main_models.MigrationSourceEndpoint = None,
    ):
        self.auth_info = auth_info
        self.database = database
        self.endpoint = endpoint

    def validate(self):
        if self.auth_info:
            self.auth_info.validate()
        if self.endpoint:
            self.endpoint.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_info is not None:
            result['authInfo'] = self.auth_info.to_map()

        if self.database is not None:
            result['database'] = self.database

        if self.endpoint is not None:
            result['endpoint'] = self.endpoint.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authInfo') is not None:
            temp_model = main_models.MigrationSourceAuthInfo()
            self.auth_info = temp_model.from_map(m.get('authInfo'))

        if m.get('database') is not None:
            self.database = m.get('database')

        if m.get('endpoint') is not None:
            temp_model = main_models.MigrationSourceEndpoint()
            self.endpoint = temp_model.from_map(m.get('endpoint'))

        return self

class MigrationSourceEndpoint(DaraModel):
    def __init__(
        self,
        endpoint: str = None,
        port: str = None,
    ):
        self.endpoint = endpoint
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint

        if self.port is not None:
            result['port'] = self.port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')

        if m.get('port') is not None:
            self.port = m.get('port')

        return self

class MigrationSourceAuthInfo(DaraModel):
    def __init__(
        self,
        auth_type: str = None,
        password: str = None,
        token: str = None,
        username: str = None,
    ):
        self.auth_type = auth_type
        self.password = password
        self.token = token
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_type is not None:
            result['authType'] = self.auth_type

        if self.password is not None:
            result['password'] = self.password

        if self.token is not None:
            result['token'] = self.token

        if self.username is not None:
            result['username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authType') is not None:
            self.auth_type = m.get('authType')

        if m.get('password') is not None:
            self.password = m.get('password')

        if m.get('token') is not None:
            self.token = m.get('token')

        if m.get('username') is not None:
            self.username = m.get('username')

        return self

