# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class SetBackendServersRequest(DaraModel):
    def __init__(
        self,
        backend_servers: List[main_models.SetBackendServersRequestBackendServers] = None,
        load_balancer_id: str = None,
    ):
        # The list of backend servers that you added. You can modify the weights of up to 20 backend servers in each request.
        # 
        # This parameter is required.
        self.backend_servers = backend_servers
        # The ID of the Edge Load Balancer (ELB) instance.
        # 
        # This parameter is required.
        self.load_balancer_id = load_balancer_id

    def validate(self):
        if self.backend_servers:
            for v1 in self.backend_servers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BackendServers'] = []
        if self.backend_servers is not None:
            for k1 in self.backend_servers:
                result['BackendServers'].append(k1.to_map() if k1 else None)

        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backend_servers = []
        if m.get('BackendServers') is not None:
            for k1 in m.get('BackendServers'):
                temp_model = main_models.SetBackendServersRequestBackendServers()
                self.backend_servers.append(temp_model.from_map(k1))

        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        return self

class SetBackendServersRequestBackendServers(DaraModel):
    def __init__(
        self,
        server_id: str = None,
        type: str = None,
        weight: int = None,
    ):
        # The ID of the instance that you use as the backend server.
        # 
        # This parameter is required.
        self.server_id = server_id
        # The type of the backend server. Valid values:
        # 
        # *   **ens**: ENS instance
        # *   **eni**: elastic network interface (ENI)
        self.type = type
        # The weight of the backend server. Default value: 100. Valid values: **0** to **100**.
        # 
        # >  The value 0 indicates that requests are not forwarded to the backend server.
        # 
        # This parameter is required.
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.server_id is not None:
            result['ServerId'] = self.server_id

        if self.type is not None:
            result['Type'] = self.type

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

