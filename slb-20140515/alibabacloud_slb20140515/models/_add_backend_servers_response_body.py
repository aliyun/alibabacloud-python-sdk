# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_slb20140515 import models as main_models
from darabonba.model import DaraModel

class AddBackendServersResponseBody(DaraModel):
    def __init__(
        self,
        backend_servers: main_models.AddBackendServersResponseBodyBackendServers = None,
        load_balancer_id: str = None,
        request_id: str = None,
    ):
        # The list of backend servers.
        self.backend_servers = backend_servers
        # The ID of the CLB instance.
        self.load_balancer_id = load_balancer_id
        # The ID of the request.
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

        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackendServers') is not None:
            temp_model = main_models.AddBackendServersResponseBodyBackendServers()
            self.backend_servers = temp_model.from_map(m.get('BackendServers'))

        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class AddBackendServersResponseBodyBackendServers(DaraModel):
    def __init__(
        self,
        backend_server: List[main_models.AddBackendServersResponseBodyBackendServersBackendServer] = None,
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
                temp_model = main_models.AddBackendServersResponseBodyBackendServersBackendServer()
                self.backend_server.append(temp_model.from_map(k1))

        return self



class AddBackendServersResponseBodyBackendServersBackendServer(DaraModel):
    def __init__(
        self,
        description: str = None,
        server_id: str = None,
        type: str = None,
        weight: str = None,
    ):
        # The description of the backend server.
        self.description = description
        # The ID of the ECS instance, ENI, or elastic container instance.
        self.server_id = server_id
        # The type of the backend server. Valid values:
        # 
        # *   **ecs** (default): an ECS instance
        # *   **eni**: an ENI
        # *   **eci**: an elastic container instance
        self.type = type
        # The weight of the backend server.
        # 
        # Valid values: **0 to 100**. Default value: **100**.
        # 
        # If the value is set to **0**, no requests are forwarded to the backend server.
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.server_id is not None:
            result['ServerId'] = self.server_id

        if self.type is not None:
            result['Type'] = self.type

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

