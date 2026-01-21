# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yundun_bastionhost20191209 import models as main_models
from darabonba.model import DaraModel

class CreateNetworkDomainRequest(DaraModel):
    def __init__(
        self,
        comment: str = None,
        instance_id: str = None,
        network_domain_name: str = None,
        network_domain_type: str = None,
        proxies: List[main_models.CreateNetworkDomainRequestProxies] = None,
        region_id: str = None,
    ):
        # The remarks of the network domain. The remarks can be up to 500 characters in length.
        self.comment = comment
        # The ID of the bastion host for which you want to create a network domain.
        # 
        # > You can call the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to query the ID of the bastion host.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the network domain that you want to create. The name can be up to 128 characters in length.
        # 
        # This parameter is required.
        self.network_domain_name = network_domain_name
        # The connection mode of the network domain to be created. Valid values:
        # 
        # *   Direct
        # *   Proxy
        # 
        # This parameter is required.
        self.network_domain_type = network_domain_type
        # The information about the proxy servers.
        self.proxies = proxies
        # The region ID of the bastion host for which you want to create a network domain.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id

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

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.network_domain_name is not None:
            result['NetworkDomainName'] = self.network_domain_name

        if self.network_domain_type is not None:
            result['NetworkDomainType'] = self.network_domain_type

        result['Proxies'] = []
        if self.proxies is not None:
            for k1 in self.proxies:
                result['Proxies'].append(k1.to_map() if k1 else None)

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NetworkDomainName') is not None:
            self.network_domain_name = m.get('NetworkDomainName')

        if m.get('NetworkDomainType') is not None:
            self.network_domain_type = m.get('NetworkDomainType')

        self.proxies = []
        if m.get('Proxies') is not None:
            for k1 in m.get('Proxies'):
                temp_model = main_models.CreateNetworkDomainRequestProxies()
                self.proxies.append(temp_model.from_map(k1))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class CreateNetworkDomainRequestProxies(DaraModel):
    def __init__(
        self,
        address: str = None,
        node_type: str = None,
        password: str = None,
        port: int = None,
        proxy_type: str = None,
        user: str = None,
    ):
        # The IP address of the proxy server.
        self.address = address
        # The node type of the proxy server. Valid values:
        # 
        # - **Master**: primary proxy server.
        # - **Slave**: secondary proxy server.
        self.node_type = node_type
        # The Base64-encoded password of the proxy server.
        self.password = password
        # The port of the proxy server.
        self.port = port
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

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.password is not None:
            result['Password'] = self.password

        if self.port is not None:
            result['Port'] = self.port

        if self.proxy_type is not None:
            result['ProxyType'] = self.proxy_type

        if self.user is not None:
            result['User'] = self.user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('ProxyType') is not None:
            self.proxy_type = m.get('ProxyType')

        if m.get('User') is not None:
            self.user = m.get('User')

        return self

