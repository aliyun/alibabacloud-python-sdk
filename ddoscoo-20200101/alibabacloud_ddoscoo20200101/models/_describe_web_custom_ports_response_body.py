# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeWebCustomPortsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        web_custom_ports: List[main_models.DescribeWebCustomPortsResponseBodyWebCustomPorts] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # An array consisting of information about supported custom ports that are used by a website.
        self.web_custom_ports = web_custom_ports

    def validate(self):
        if self.web_custom_ports:
            for v1 in self.web_custom_ports:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['WebCustomPorts'] = []
        if self.web_custom_ports is not None:
            for k1 in self.web_custom_ports:
                result['WebCustomPorts'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.web_custom_ports = []
        if m.get('WebCustomPorts') is not None:
            for k1 in m.get('WebCustomPorts'):
                temp_model = main_models.DescribeWebCustomPortsResponseBodyWebCustomPorts()
                self.web_custom_ports.append(temp_model.from_map(k1))

        return self

class DescribeWebCustomPortsResponseBodyWebCustomPorts(DaraModel):
    def __init__(
        self,
        proxy_ports: List[str] = None,
        proxy_type: str = None,
    ):
        # An array that consists of supported custom ports.
        self.proxy_ports = proxy_ports
        # The type of the protocol. Valid values:
        # 
        # *   **http**
        # *   **https**
        self.proxy_type = proxy_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.proxy_ports is not None:
            result['ProxyPorts'] = self.proxy_ports

        if self.proxy_type is not None:
            result['ProxyType'] = self.proxy_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProxyPorts') is not None:
            self.proxy_ports = m.get('ProxyPorts')

        if m.get('ProxyType') is not None:
            self.proxy_type = m.get('ProxyType')

        return self

