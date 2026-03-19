# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20171228 import models as main_models
from darabonba.model import DaraModel

class ListLayer7CustomPortsResponseBody(DaraModel):
    def __init__(
        self,
        layer_7custom_ports: List[main_models.ListLayer7CustomPortsResponseBodyLayer7CustomPorts] = None,
        request_id: str = None,
    ):
        self.layer_7custom_ports = layer_7custom_ports
        self.request_id = request_id

    def validate(self):
        if self.layer_7custom_ports:
            for v1 in self.layer_7custom_ports:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Layer7CustomPorts'] = []
        if self.layer_7custom_ports is not None:
            for k1 in self.layer_7custom_ports:
                result['Layer7CustomPorts'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.layer_7custom_ports = []
        if m.get('Layer7CustomPorts') is not None:
            for k1 in m.get('Layer7CustomPorts'):
                temp_model = main_models.ListLayer7CustomPortsResponseBodyLayer7CustomPorts()
                self.layer_7custom_ports.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListLayer7CustomPortsResponseBodyLayer7CustomPorts(DaraModel):
    def __init__(
        self,
        flag: str = None,
        proxy_ports: List[str] = None,
        proxy_type: str = None,
    ):
        self.flag = flag
        self.proxy_ports = proxy_ports
        self.proxy_type = proxy_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.flag is not None:
            result['Flag'] = self.flag

        if self.proxy_ports is not None:
            result['ProxyPorts'] = self.proxy_ports

        if self.proxy_type is not None:
            result['ProxyType'] = self.proxy_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Flag') is not None:
            self.flag = m.get('Flag')

        if m.get('ProxyPorts') is not None:
            self.proxy_ports = m.get('ProxyPorts')

        if m.get('ProxyType') is not None:
            self.proxy_type = m.get('ProxyType')

        return self

