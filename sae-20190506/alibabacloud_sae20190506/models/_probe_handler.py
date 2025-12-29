# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class ProbeHandler(DaraModel):
    def __init__(
        self,
        http_get: main_models.HTTPGetAction = None,
        tcp_socket: main_models.TCPSocketAction = None,
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
            result['HttpGet'] = self.http_get.to_map()

        if self.tcp_socket is not None:
            result['TcpSocket'] = self.tcp_socket.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpGet') is not None:
            temp_model = main_models.HTTPGetAction()
            self.http_get = temp_model.from_map(m.get('HttpGet'))

        if m.get('TcpSocket') is not None:
            temp_model = main_models.TCPSocketAction()
            self.tcp_socket = temp_model.from_map(m.get('TcpSocket'))

        return self

