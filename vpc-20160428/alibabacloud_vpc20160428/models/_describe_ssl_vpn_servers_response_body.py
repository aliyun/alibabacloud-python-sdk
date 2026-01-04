# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribeSslVpnServersResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        ssl_vpn_servers: main_models.DescribeSslVpnServersResponseBodySslVpnServers = None,
        total_count: int = None,
    ):
        # The number of the page to return.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The detailed information about the SSL-VPN servers.
        self.ssl_vpn_servers = ssl_vpn_servers
        # The number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.ssl_vpn_servers:
            self.ssl_vpn_servers.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.ssl_vpn_servers is not None:
            result['SslVpnServers'] = self.ssl_vpn_servers.to_map()

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SslVpnServers') is not None:
            temp_model = main_models.DescribeSslVpnServersResponseBodySslVpnServers()
            self.ssl_vpn_servers = temp_model.from_map(m.get('SslVpnServers'))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeSslVpnServersResponseBodySslVpnServers(DaraModel):
    def __init__(
        self,
        ssl_vpn_server: List[main_models.DescribeSslVpnServersResponseBodySslVpnServersSslVpnServer] = None,
    ):
        self.ssl_vpn_server = ssl_vpn_server

    def validate(self):
        if self.ssl_vpn_server:
            for v1 in self.ssl_vpn_server:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SslVpnServer'] = []
        if self.ssl_vpn_server is not None:
            for k1 in self.ssl_vpn_server:
                result['SslVpnServer'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ssl_vpn_server = []
        if m.get('SslVpnServer') is not None:
            for k1 in m.get('SslVpnServer'):
                temp_model = main_models.DescribeSslVpnServersResponseBodySslVpnServersSslVpnServer()
                self.ssl_vpn_server.append(temp_model.from_map(k1))

        return self

class DescribeSslVpnServersResponseBodySslVpnServersSslVpnServer(DaraModel):
    def __init__(
        self,
        cipher: str = None,
        client_ip_pool: str = None,
        compress: bool = None,
        connections: int = None,
        create_time: int = None,
        enable_multi_factor_auth: bool = None,
        idaa_sapplication_id: str = None,
        idaa_sinstance_id: str = None,
        idaa_sinstance_version: str = None,
        idaa_sregion_id: str = None,
        internet_ip: str = None,
        local_subnet: str = None,
        max_connections: int = None,
        name: str = None,
        port: int = None,
        proto: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        ssl_vpn_server_id: str = None,
        vpn_gateway_id: str = None,
    ):
        # The encryption algorithm.
        self.cipher = cipher
        # The client CIDR block.
        self.client_ip_pool = client_ip_pool
        # Indicates whether data compression is enabled. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        self.compress = compress
        # The total number of current connections.
        self.connections = connections
        # The timestamp generated when the SSL-VPN server was created.
        self.create_time = create_time
        # Indicates whether two-factor authentication is enabled.
        # 
        # *   **true**
        # *   **false** (default)
        self.enable_multi_factor_auth = enable_multi_factor_auth
        # The ID of the IDaaS application.
        self.idaa_sapplication_id = idaa_sapplication_id
        # The ID of the IDaaS EIAM instance.
        self.idaa_sinstance_id = idaa_sinstance_id
        # The version of the IDaaS EIAM instance.
        # 
        # *   This parameter is returned only if the SSL server is associated with an IDaaS EIAM 2.0 instance. Only **EIAM 2.0** is returned.
        # *   If the SSL server is associated with an IDaaS EIAM 1.0 instance, no value is returned.
        self.idaa_sinstance_version = idaa_sinstance_version
        # The region ID of the IDaaS EIAM instance.
        self.idaa_sregion_id = idaa_sregion_id
        # The public IP address of the VPN gateway.
        self.internet_ip = internet_ip
        # The local CIDR block.
        self.local_subnet = local_subnet
        # The maximum number of connections.
        self.max_connections = max_connections
        # The name of the SSL server.
        self.name = name
        # The port that is used by the SSL-VPN server.
        self.port = port
        # The protocol that is used by the SSL server.
        self.proto = proto
        # The region ID of the SSL server.
        self.region_id = region_id
        # The resource group ID of the SSL server.
        # 
        # You can call the [ListResourceGroups](https://help.aliyun.com/document_detail/158855.html) operation to query resource groups.
        self.resource_group_id = resource_group_id
        # The ID of the SSL server.
        self.ssl_vpn_server_id = ssl_vpn_server_id
        # The ID of the VPN gateway.
        self.vpn_gateway_id = vpn_gateway_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cipher is not None:
            result['Cipher'] = self.cipher

        if self.client_ip_pool is not None:
            result['ClientIpPool'] = self.client_ip_pool

        if self.compress is not None:
            result['Compress'] = self.compress

        if self.connections is not None:
            result['Connections'] = self.connections

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.enable_multi_factor_auth is not None:
            result['EnableMultiFactorAuth'] = self.enable_multi_factor_auth

        if self.idaa_sapplication_id is not None:
            result['IDaaSApplicationId'] = self.idaa_sapplication_id

        if self.idaa_sinstance_id is not None:
            result['IDaaSInstanceId'] = self.idaa_sinstance_id

        if self.idaa_sinstance_version is not None:
            result['IDaaSInstanceVersion'] = self.idaa_sinstance_version

        if self.idaa_sregion_id is not None:
            result['IDaaSRegionId'] = self.idaa_sregion_id

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.local_subnet is not None:
            result['LocalSubnet'] = self.local_subnet

        if self.max_connections is not None:
            result['MaxConnections'] = self.max_connections

        if self.name is not None:
            result['Name'] = self.name

        if self.port is not None:
            result['Port'] = self.port

        if self.proto is not None:
            result['Proto'] = self.proto

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.ssl_vpn_server_id is not None:
            result['SslVpnServerId'] = self.ssl_vpn_server_id

        if self.vpn_gateway_id is not None:
            result['VpnGatewayId'] = self.vpn_gateway_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cipher') is not None:
            self.cipher = m.get('Cipher')

        if m.get('ClientIpPool') is not None:
            self.client_ip_pool = m.get('ClientIpPool')

        if m.get('Compress') is not None:
            self.compress = m.get('Compress')

        if m.get('Connections') is not None:
            self.connections = m.get('Connections')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EnableMultiFactorAuth') is not None:
            self.enable_multi_factor_auth = m.get('EnableMultiFactorAuth')

        if m.get('IDaaSApplicationId') is not None:
            self.idaa_sapplication_id = m.get('IDaaSApplicationId')

        if m.get('IDaaSInstanceId') is not None:
            self.idaa_sinstance_id = m.get('IDaaSInstanceId')

        if m.get('IDaaSInstanceVersion') is not None:
            self.idaa_sinstance_version = m.get('IDaaSInstanceVersion')

        if m.get('IDaaSRegionId') is not None:
            self.idaa_sregion_id = m.get('IDaaSRegionId')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('LocalSubnet') is not None:
            self.local_subnet = m.get('LocalSubnet')

        if m.get('MaxConnections') is not None:
            self.max_connections = m.get('MaxConnections')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Proto') is not None:
            self.proto = m.get('Proto')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SslVpnServerId') is not None:
            self.ssl_vpn_server_id = m.get('SslVpnServerId')

        if m.get('VpnGatewayId') is not None:
            self.vpn_gateway_id = m.get('VpnGatewayId')

        return self

