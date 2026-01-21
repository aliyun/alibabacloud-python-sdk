# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yundun_bastionhost20191209 import models as main_models
from darabonba.model import DaraModel

class GetNetworkDomainResponseBody(DaraModel):
    def __init__(
        self,
        network_domain: main_models.GetNetworkDomainResponseBodyNetworkDomain = None,
        request_id: str = None,
    ):
        # The detailed information about the network domain.
        self.network_domain = network_domain
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.network_domain:
            self.network_domain.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.network_domain is not None:
            result['NetworkDomain'] = self.network_domain.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkDomain') is not None:
            temp_model = main_models.GetNetworkDomainResponseBodyNetworkDomain()
            self.network_domain = temp_model.from_map(m.get('NetworkDomain'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetNetworkDomainResponseBodyNetworkDomain(DaraModel):
    def __init__(
        self,
        comment: str = None,
        default: bool = None,
        network_domain_id: str = None,
        network_domain_name: str = None,
        network_domain_type: str = None,
        proxies: List[main_models.GetNetworkDomainResponseBodyNetworkDomainProxies] = None,
    ):
        # The remarks of the network domain.
        self.comment = comment
        # Indicates whether the network domain is a built-in network domain.
        # 
        # * **true**
        # * **false**
        self.default = default
        # The network domain ID.
        self.network_domain_id = network_domain_id
        # The name of the network domain.
        self.network_domain_name = network_domain_name
        # The connection mode of the network domain. Valid values:
        # 
        # * Direct
        # * Proxy
        self.network_domain_type = network_domain_type
        # The information about the proxy servers.
        self.proxies = proxies

    def validate(self):
        if self.proxies:
            for v1 in self.proxies:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.default is not None:
            result['Default'] = self.default

        if self.network_domain_id is not None:
            result['NetworkDomainId'] = self.network_domain_id

        if self.network_domain_name is not None:
            result['NetworkDomainName'] = self.network_domain_name

        if self.network_domain_type is not None:
            result['NetworkDomainType'] = self.network_domain_type

        result['Proxies'] = []
        if self.proxies is not None:
            for k1 in self.proxies:
                result['Proxies'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('Default') is not None:
            self.default = m.get('Default')

        if m.get('NetworkDomainId') is not None:
            self.network_domain_id = m.get('NetworkDomainId')

        if m.get('NetworkDomainName') is not None:
            self.network_domain_name = m.get('NetworkDomainName')

        if m.get('NetworkDomainType') is not None:
            self.network_domain_type = m.get('NetworkDomainType')

        self.proxies = []
        if m.get('Proxies') is not None:
            for k1 in m.get('Proxies'):
                temp_model = main_models.GetNetworkDomainResponseBodyNetworkDomainProxies()
                self.proxies.append(temp_model.from_map(k1))

        return self

class GetNetworkDomainResponseBodyNetworkDomainProxies(DaraModel):
    def __init__(
        self,
        address: str = None,
        has_password: bool = None,
        node_type: str = None,
        port: int = None,
        proxy_state: str = None,
        proxy_state_error_code: str = None,
        proxy_type: str = None,
        user: str = None,
    ):
        # The IP address of the proxy server.
        self.address = address
        # Indicates whether the proxy server has a password. Valid values:
        # 
        # - **true**
        # - **false**
        self.has_password = has_password
        # The node type of the proxy server. Valid values:
        # - **Master**: primary proxy server.
        # - **Slave**: secondary proxy server.
        self.node_type = node_type
        # The port of the proxy server.
        self.port = port
        # The status of the proxy server.
        # 
        # - **Available**
        # - **Unavailable**
        self.proxy_state = proxy_state
        # The error code that indicates the status of the proxy server.
        # 
        # - **CHECK_PWD_FAILED**: The password is invalid.
        # - **CHECK_PWD_TIMEOUT**: The password verification session timed out.
        # - **CHECK_PWD_NETWORK_ERR**: A network error occurred.
        # - **UNEXPECTED**: An unknown error occurred.
        self.proxy_state_error_code = proxy_state_error_code
        # The proxy type. Valid values:
        # 
        # - **SSHProxy**
        # - **HTTPProxy**
        # - **Socks5Proxy**
        self.proxy_type = proxy_type
        # The username of the proxy server.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address

        if self.has_password is not None:
            result['HasPassword'] = self.has_password

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.port is not None:
            result['Port'] = self.port

        if self.proxy_state is not None:
            result['ProxyState'] = self.proxy_state

        if self.proxy_state_error_code is not None:
            result['ProxyStateErrorCode'] = self.proxy_state_error_code

        if self.proxy_type is not None:
            result['ProxyType'] = self.proxy_type

        if self.user is not None:
            result['User'] = self.user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('HasPassword') is not None:
            self.has_password = m.get('HasPassword')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('ProxyState') is not None:
            self.proxy_state = m.get('ProxyState')

        if m.get('ProxyStateErrorCode') is not None:
            self.proxy_state_error_code = m.get('ProxyStateErrorCode')

        if m.get('ProxyType') is not None:
            self.proxy_type = m.get('ProxyType')

        if m.get('User') is not None:
            self.user = m.get('User')

        return self

