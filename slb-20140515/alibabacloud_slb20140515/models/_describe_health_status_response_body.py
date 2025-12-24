# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_slb20140515 import models as main_models
from darabonba.model import DaraModel

class DescribeHealthStatusResponseBody(DaraModel):
    def __init__(
        self,
        backend_servers: main_models.DescribeHealthStatusResponseBodyBackendServers = None,
        request_id: str = None,
    ):
        # The backend servers.
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
            temp_model = main_models.DescribeHealthStatusResponseBodyBackendServers()
            self.backend_servers = temp_model.from_map(m.get('BackendServers'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeHealthStatusResponseBodyBackendServers(DaraModel):
    def __init__(
        self,
        backend_server: List[main_models.DescribeHealthStatusResponseBodyBackendServersBackendServer] = None,
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
                temp_model = main_models.DescribeHealthStatusResponseBodyBackendServersBackendServer()
                self.backend_server.append(temp_model.from_map(k1))

        return self

class DescribeHealthStatusResponseBodyBackendServersBackendServer(DaraModel):
    def __init__(
        self,
        listener_port: int = None,
        port: int = None,
        protocol: str = None,
        server_health_status: str = None,
        server_id: str = None,
        server_ip: str = None,
    ):
        # The frontend port that is used by the SLB instance.
        self.listener_port = listener_port
        # The backend port that is used by the SLB instance.
        self.port = port
        # The frontend protocol that is used by the SLB instance.
        self.protocol = protocol
        # The health status of the backend server. Valid values:
        # 
        # *   normal: The backend server is healthy.
        # *   abnormal: The backend server is unhealthy.
        # *   unavailable: The health check is not completed.
        self.server_health_status = server_health_status
        # The ID of the backend server.
        self.server_id = server_id
        # The IP address of the backend server.
        self.server_ip = server_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port

        if self.port is not None:
            result['Port'] = self.port

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.server_health_status is not None:
            result['ServerHealthStatus'] = self.server_health_status

        if self.server_id is not None:
            result['ServerId'] = self.server_id

        if self.server_ip is not None:
            result['ServerIp'] = self.server_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('ServerHealthStatus') is not None:
            self.server_health_status = m.get('ServerHealthStatus')

        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')

        if m.get('ServerIp') is not None:
            self.server_ip = m.get('ServerIp')

        return self

