# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateFunagentInput(DaraModel):
    def __init__(
        self,
        admin_name: str = None,
        admin_secret: str = None,
        cpu: float = None,
        db_connections: int = None,
        db_host: str = None,
        db_instance_id: str = None,
        db_name: str = None,
        db_password: str = None,
        db_port: int = None,
        db_type: str = None,
        db_username: str = None,
        description: str = None,
        memory: int = None,
        replicas: int = None,
        version: str = None,
    ):
        self.admin_name = admin_name
        # 敏感字段
        self.admin_secret = admin_secret
        self.cpu = cpu
        self.db_connections = db_connections
        self.db_host = db_host
        self.db_instance_id = db_instance_id
        self.db_name = db_name
        # 敏感字段
        self.db_password = db_password
        self.db_port = db_port
        self.db_type = db_type
        self.db_username = db_username
        self.description = description
        self.memory = memory
        self.replicas = replicas
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.admin_name is not None:
            result['adminName'] = self.admin_name

        if self.admin_secret is not None:
            result['adminSecret'] = self.admin_secret

        if self.cpu is not None:
            result['cpu'] = self.cpu

        if self.db_connections is not None:
            result['dbConnections'] = self.db_connections

        if self.db_host is not None:
            result['dbHost'] = self.db_host

        if self.db_instance_id is not None:
            result['dbInstanceId'] = self.db_instance_id

        if self.db_name is not None:
            result['dbName'] = self.db_name

        if self.db_password is not None:
            result['dbPassword'] = self.db_password

        if self.db_port is not None:
            result['dbPort'] = self.db_port

        if self.db_type is not None:
            result['dbType'] = self.db_type

        if self.db_username is not None:
            result['dbUsername'] = self.db_username

        if self.description is not None:
            result['description'] = self.description

        if self.memory is not None:
            result['memory'] = self.memory

        if self.replicas is not None:
            result['replicas'] = self.replicas

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('adminName') is not None:
            self.admin_name = m.get('adminName')

        if m.get('adminSecret') is not None:
            self.admin_secret = m.get('adminSecret')

        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')

        if m.get('dbConnections') is not None:
            self.db_connections = m.get('dbConnections')

        if m.get('dbHost') is not None:
            self.db_host = m.get('dbHost')

        if m.get('dbInstanceId') is not None:
            self.db_instance_id = m.get('dbInstanceId')

        if m.get('dbName') is not None:
            self.db_name = m.get('dbName')

        if m.get('dbPassword') is not None:
            self.db_password = m.get('dbPassword')

        if m.get('dbPort') is not None:
            self.db_port = m.get('dbPort')

        if m.get('dbType') is not None:
            self.db_type = m.get('dbType')

        if m.get('dbUsername') is not None:
            self.db_username = m.get('dbUsername')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('memory') is not None:
            self.memory = m.get('memory')

        if m.get('replicas') is not None:
            self.replicas = m.get('replicas')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

