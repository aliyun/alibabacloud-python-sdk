# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class Probe(DaraModel):
    def __init__(
        self,
        failure_threshold: int = None,
        initial_delay_seconds: int = None,
        period_seconds: int = None,
        probe_handler: main_models.ProbeProbeHandler = None,
        timeout_seconds: int = None,
    ):
        self.failure_threshold = failure_threshold
        self.initial_delay_seconds = initial_delay_seconds
        self.period_seconds = period_seconds
        self.probe_handler = probe_handler
        self.timeout_seconds = timeout_seconds

    def validate(self):
        if self.probe_handler:
            self.probe_handler.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failure_threshold is not None:
            result['failureThreshold'] = self.failure_threshold

        if self.initial_delay_seconds is not None:
            result['initialDelaySeconds'] = self.initial_delay_seconds

        if self.period_seconds is not None:
            result['periodSeconds'] = self.period_seconds

        if self.probe_handler is not None:
            result['probeHandler'] = self.probe_handler.to_map()

        if self.timeout_seconds is not None:
            result['timeoutSeconds'] = self.timeout_seconds

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('failureThreshold') is not None:
            self.failure_threshold = m.get('failureThreshold')

        if m.get('initialDelaySeconds') is not None:
            self.initial_delay_seconds = m.get('initialDelaySeconds')

        if m.get('periodSeconds') is not None:
            self.period_seconds = m.get('periodSeconds')

        if m.get('probeHandler') is not None:
            temp_model = main_models.ProbeProbeHandler()
            self.probe_handler = temp_model.from_map(m.get('probeHandler'))

        if m.get('timeoutSeconds') is not None:
            self.timeout_seconds = m.get('timeoutSeconds')

        return self

class ProbeProbeHandler(DaraModel):
    def __init__(
        self,
        http_get: main_models.ProbeProbeHandlerHttpGet = None,
        tcp_socket: main_models.ProbeProbeHandlerTcpSocket = None,
    ):
        self.http_get = http_get
        self.tcp_socket = tcp_socket

    def validate(self):
        if self.http_get:
            self.http_get.validate()
        if self.tcp_socket:
            self.tcp_socket.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.http_get is not None:
            result['httpGet'] = self.http_get.to_map()

        if self.tcp_socket is not None:
            result['tcpSocket'] = self.tcp_socket.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('httpGet') is not None:
            temp_model = main_models.ProbeProbeHandlerHttpGet()
            self.http_get = temp_model.from_map(m.get('httpGet'))

        if m.get('tcpSocket') is not None:
            temp_model = main_models.ProbeProbeHandlerTcpSocket()
            self.tcp_socket = temp_model.from_map(m.get('tcpSocket'))

        return self

class ProbeProbeHandlerTcpSocket(DaraModel):
    def __init__(
        self,
        port: int = None,
    ):
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.port is not None:
            result['port'] = self.port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('port') is not None:
            self.port = m.get('port')

        return self

class ProbeProbeHandlerHttpGet(DaraModel):
    def __init__(
        self,
        http_headers: List[main_models.ProbeProbeHandlerHttpGetHttpHeaders] = None,
        path: str = None,
        port: int = None,
    ):
        self.http_headers = http_headers
        self.path = path
        self.port = port

    def validate(self):
        if self.http_headers:
            for v1 in self.http_headers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['httpHeaders'] = []
        if self.http_headers is not None:
            for k1 in self.http_headers:
                result['httpHeaders'].append(k1.to_map() if k1 else None)

        if self.path is not None:
            result['path'] = self.path

        if self.port is not None:
            result['port'] = self.port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.http_headers = []
        if m.get('httpHeaders') is not None:
            for k1 in m.get('httpHeaders'):
                temp_model = main_models.ProbeProbeHandlerHttpGetHttpHeaders()
                self.http_headers.append(temp_model.from_map(k1))

        if m.get('path') is not None:
            self.path = m.get('path')

        if m.get('port') is not None:
            self.port = m.get('port')

        return self

class ProbeProbeHandlerHttpGetHttpHeaders(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

