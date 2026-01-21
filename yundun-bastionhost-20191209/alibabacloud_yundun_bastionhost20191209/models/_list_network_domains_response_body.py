# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yundun_bastionhost20191209 import models as main_models
from darabonba.model import DaraModel

class ListNetworkDomainsResponseBody(DaraModel):
    def __init__(
        self,
        network_domains: List[main_models.ListNetworkDomainsResponseBodyNetworkDomains] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The network domains that are returned.
        self.network_domains = network_domains
        # The request ID.
        self.request_id = request_id
        # The total number of network domains that are returned.
        self.total_count = total_count

    def validate(self):
        if self.network_domains:
            for v1 in self.network_domains:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NetworkDomains'] = []
        if self.network_domains is not None:
            for k1 in self.network_domains:
                result['NetworkDomains'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.network_domains = []
        if m.get('NetworkDomains') is not None:
            for k1 in m.get('NetworkDomains'):
                temp_model = main_models.ListNetworkDomainsResponseBodyNetworkDomains()
                self.network_domains.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListNetworkDomainsResponseBodyNetworkDomains(DaraModel):
    def __init__(
        self,
        comment: str = None,
        default: bool = None,
        network_domain_id: str = None,
        network_domain_name: str = None,
        network_domain_type: str = None,
        proxies_state: List[main_models.ListNetworkDomainsResponseBodyNetworkDomainsProxiesState] = None,
    ):
        # The remarks of the network domain.
        self.comment = comment
        # Indicates whether the network domain is built-in.
        # 
        # *   **true**
        # *   **false**
        self.default = default
        # The network domain ID.
        self.network_domain_id = network_domain_id
        # The name of the network domain.
        self.network_domain_name = network_domain_name
        # The connection mode of the network domain. Valid values:
        # 
        # *   **Direct**
        # *   **Proxy**
        self.network_domain_type = network_domain_type
        self.proxies_state = proxies_state

    def validate(self):
        if self.proxies_state:
            for v1 in self.proxies_state:
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

        result['ProxiesState'] = []
        if self.proxies_state is not None:
            for k1 in self.proxies_state:
                result['ProxiesState'].append(k1.to_map() if k1 else None)

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

        self.proxies_state = []
        if m.get('ProxiesState') is not None:
            for k1 in m.get('ProxiesState'):
                temp_model = main_models.ListNetworkDomainsResponseBodyNetworkDomainsProxiesState()
                self.proxies_state.append(temp_model.from_map(k1))

        return self

class ListNetworkDomainsResponseBodyNetworkDomainsProxiesState(DaraModel):
    def __init__(
        self,
        node_type: str = None,
        proxy_state: str = None,
    ):
        # The node type of the proxy server. Valid values:
        # 
        # *   **Master**: primary proxy server.
        # *   **Slave**: secondary proxy server.
        self.node_type = node_type
        # The status of the proxy server.
        # 
        # *   **Available**
        # *   **Unavailable**
        self.proxy_state = proxy_state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.proxy_state is not None:
            result['ProxyState'] = self.proxy_state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('ProxyState') is not None:
            self.proxy_state = m.get('ProxyState')

        return self

