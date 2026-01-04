# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class ModifyDomainResourceRequest(DaraModel):
    def __init__(
        self,
        domain: str = None,
        https_ext: str = None,
        instance_ids: List[str] = None,
        proxy_types: List[main_models.ModifyDomainResourceRequestProxyTypes] = None,
        real_servers: List[str] = None,
        rs_type: int = None,
    ):
        # The domain name that is added to the Anti-DDoS Pro or Anti-DDoS Premium instance.
        # 
        # This parameter is required.
        self.domain = domain
        # The advanced HTTPS settings. This parameter takes effect only when the value of the **ProxyType** parameter includes **https**. The value is a string that consists of a JSON struct. The JSON struct contains the following fields:
        # 
        # *   **Http2https**: specifies whether to turn on Enforce HTTPS Routing. This field is optional and must be an integer. Valid values: **0** and **1**. The value 0 indicates that Enforce HTTPS Routing is turned off. The value 1 indicates that Enforce HTTPS Routing is turned on. The default value is 0.
        # 
        #     If your website supports both HTTP and HTTPS, this feature meets your business requirements. If you enable this feature, all HTTP requests to access the website are redirected to HTTPS requests on the standard port 443.
        # 
        # *   **Https2http**: specifies whether to turn on Enable HTTP. This field is optional and must be an integer. Valid values: **0** and **1**. The value 0 indicates that Enable HTTP is turned off. The value 1 indicates that Enable HTTP is turned on. The default value is 0.
        # 
        #     If your website does not support HTTPS, this feature meets your business requirements If this feature is enabled, all HTTPS requests are redirected to HTTP requests and forwarded to origin servers. This feature can redirect WebSockets requests to WebSocket requests. Requests are redirected over the standard port 80.
        # 
        # *   **Http2**: specifies whether to turn on Enable HTTP/2. This field is optional. Data type: integer. Valid values: **0** and **1**. The value 0 indicates that Enable HTTP/2 is turned off. The value 1 indicates that Enable HTTP/2 is turned on. The default value is 0.
        # 
        #     After you turn on the switch, HTTP/2 is used.
        self.https_ext = https_ext
        # An array consisting of the IDs of instances that you want to associate.
        # 
        # This parameter is required.
        self.instance_ids = instance_ids
        # The details about the protocol type and port number.
        # 
        # This parameter is required.
        self.proxy_types = proxy_types
        # An array that consists of the addresses of origin servers.
        # 
        # This parameter is required.
        self.real_servers = real_servers
        # The address type of the origin server. Valid values:
        # 
        # *   **0**: IP address
        # 
        # *   **1**: domain name
        # 
        #     If you deploy proxies, such as a Web Application Firewall (WAF) instance, between the origin server and the Anti-DDoS Pro or Anti-DDoS Premium instance, set the value to 1. If you use the domain name, you must enter the address of the proxy, such as the CNAME of WAF.
        # 
        # This parameter is required.
        self.rs_type = rs_type

    def validate(self):
        if self.proxy_types:
            for v1 in self.proxy_types:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.https_ext is not None:
            result['HttpsExt'] = self.https_ext

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        result['ProxyTypes'] = []
        if self.proxy_types is not None:
            for k1 in self.proxy_types:
                result['ProxyTypes'].append(k1.to_map() if k1 else None)

        if self.real_servers is not None:
            result['RealServers'] = self.real_servers

        if self.rs_type is not None:
            result['RsType'] = self.rs_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('HttpsExt') is not None:
            self.https_ext = m.get('HttpsExt')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        self.proxy_types = []
        if m.get('ProxyTypes') is not None:
            for k1 in m.get('ProxyTypes'):
                temp_model = main_models.ModifyDomainResourceRequestProxyTypes()
                self.proxy_types.append(temp_model.from_map(k1))

        if m.get('RealServers') is not None:
            self.real_servers = m.get('RealServers')

        if m.get('RsType') is not None:
            self.rs_type = m.get('RsType')

        return self

class ModifyDomainResourceRequestProxyTypes(DaraModel):
    def __init__(
        self,
        proxy_ports: List[int] = None,
        proxy_type: str = None,
    ):
        # The port numbers.
        # 
        # This parameter is required.
        self.proxy_ports = proxy_ports
        # The type of the protocol. Valid values:
        # 
        # *   **http**
        # *   **https**
        # *   **websocket**
        # *   **websockets**
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

