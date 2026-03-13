# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_slb20130221 import models as main_models
from darabonba.model import DaraModel

class DescribeBackendServersResponseBody(DaraModel):
    def __init__(
        self,
        listeners: main_models.DescribeBackendServersResponseBodyListeners = None,
        request_id: str = None,
    ):
        self.listeners = listeners
        self.request_id = request_id

    def validate(self):
        if self.listeners:
            self.listeners.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.listeners is not None:
            result['Listeners'] = self.listeners.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Listeners') is not None:
            temp_model = main_models.DescribeBackendServersResponseBodyListeners()
            self.listeners = temp_model.from_map(m.get('Listeners'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeBackendServersResponseBodyListeners(DaraModel):
    def __init__(
        self,
        listener: List[main_models.DescribeBackendServersResponseBodyListenersListener] = None,
    ):
        self.listener = listener

    def validate(self):
        if self.listener:
            for v1 in self.listener:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Listener'] = []
        if self.listener is not None:
            for k1 in self.listener:
                result['Listener'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.listener = []
        if m.get('Listener') is not None:
            for k1 in m.get('Listener'):
                temp_model = main_models.DescribeBackendServersResponseBodyListenersListener()
                self.listener.append(temp_model.from_map(k1))

        return self

class DescribeBackendServersResponseBodyListenersListener(DaraModel):
    def __init__(
        self,
        backend_servers: main_models.DescribeBackendServersResponseBodyListenersListenerBackendServers = None,
        listener_port: int = None,
    ):
        self.backend_servers = backend_servers
        self.listener_port = listener_port

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

        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackendServers') is not None:
            temp_model = main_models.DescribeBackendServersResponseBodyListenersListenerBackendServers()
            self.backend_servers = temp_model.from_map(m.get('BackendServers'))

        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')

        return self

class DescribeBackendServersResponseBodyListenersListenerBackendServers(DaraModel):
    def __init__(
        self,
        backend_server: List[main_models.DescribeBackendServersResponseBodyListenersListenerBackendServersBackendServer] = None,
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
                temp_model = main_models.DescribeBackendServersResponseBodyListenersListenerBackendServersBackendServer()
                self.backend_server.append(temp_model.from_map(k1))

        return self

class DescribeBackendServersResponseBodyListenersListenerBackendServersBackendServer(DaraModel):
    def __init__(
        self,
        server_health_status: str = None,
        server_id: str = None,
    ):
        self.server_health_status = server_health_status
        self.server_id = server_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.server_health_status is not None:
            result['ServerHealthStatus'] = self.server_health_status

        if self.server_id is not None:
            result['ServerId'] = self.server_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServerHealthStatus') is not None:
            self.server_health_status = m.get('ServerHealthStatus')

        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')

        return self

