# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class RemoveBackendServersResponseBody(DaraModel):
    def __init__(
        self,
        backend_servers: main_models.RemoveBackendServersResponseBodyBackendServers = None,
        request_id: str = None,
    ):
        # The list of backend servers that you want to add to the SLB instance.
        self.backend_servers = backend_servers
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.backend_servers:
            self.backend_servers.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backend_servers is not None:
            result['BackendServers'] = self.backend_servers.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackendServers') is not None:
            temp_model = main_models.RemoveBackendServersResponseBodyBackendServers()
            self.backend_servers = temp_model.from_map(m.get('BackendServers'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class RemoveBackendServersResponseBodyBackendServers(DaraModel):
    def __init__(
        self,
        backend_server: List[main_models.RemoveBackendServersResponseBodyBackendServersBackendServer] = None,
    ):
        self.backend_server = backend_server

    def validate(self):
        if self.backend_server:
            for v1 in self.backend_server:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BackendServer'] = []
        if self.backend_server is not None:
            for k1 in self.backend_server:
                result['BackendServer'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backend_server = []
        if m.get('BackendServer') is not None:
            for k1 in m.get('BackendServer'):
                temp_model = main_models.RemoveBackendServersResponseBodyBackendServersBackendServer()
                self.backend_server.append(temp_model.from_map(k1))

        return self

class RemoveBackendServersResponseBodyBackendServersBackendServer(DaraModel):
    def __init__(
        self,
        ip: str = None,
        port: int = None,
        server_id: str = None,
        type: str = None,
        weight: int = None,
    ):
        # The IP address of the backend server.
        self.ip = ip
        # The backend port that is used by the ELB instance.
        self.port = port
        # The instance ID of the backend server.
        self.server_id = server_id
        # The type of the backend server. Valid values:
        # 
        # *   **ens**: an ENS instance.
        # *   **eni**: an ENI.
        self.type = type
        # The weight of the backend server.
        # 
        # >  The value 0 indicates that requests are not forwarded to the backend server.
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip is not None:
            result['Ip'] = self.ip

        if self.port is not None:
            result['Port'] = self.port

        if self.server_id is not None:
            result['ServerId'] = self.server_id

        if self.type is not None:
            result['Type'] = self.type

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

