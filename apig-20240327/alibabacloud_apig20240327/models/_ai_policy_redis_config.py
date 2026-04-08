# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AiPolicyRedisConfig(DaraModel):
    def __init__(
        self,
        database_number: int = None,
        host: str = None,
        password: str = None,
        port: int = None,
        timeout: int = None,
        username: str = None,
    ):
        self.database_number = database_number
        self.host = host
        self.password = password
        self.port = port
        self.timeout = timeout
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.database_number is not None:
            result['databaseNumber'] = self.database_number

        if self.host is not None:
            result['host'] = self.host

        if self.password is not None:
            result['password'] = self.password

        if self.port is not None:
            result['port'] = self.port

        if self.timeout is not None:
            result['timeout'] = self.timeout

        if self.username is not None:
            result['username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('databaseNumber') is not None:
            self.database_number = m.get('databaseNumber')

        if m.get('host') is not None:
            self.host = m.get('host')

        if m.get('password') is not None:
            self.password = m.get('password')

        if m.get('port') is not None:
            self.port = m.get('port')

        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')

        if m.get('username') is not None:
            self.username = m.get('username')

        return self

