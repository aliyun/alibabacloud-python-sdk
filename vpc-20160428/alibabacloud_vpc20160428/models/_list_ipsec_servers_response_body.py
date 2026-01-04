# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class ListIpsecServersResponseBody(DaraModel):
    def __init__(
        self,
        ipsec_servers: List[main_models.ListIpsecServersResponseBodyIpsecServers] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of IPsec servers.
        self.ipsec_servers = ipsec_servers
        # The number of entries returned per page.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If no value is returned for **NextToken**, no next queries are sent.
        # *   If a value is returned for **NextToken**, the value can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.ipsec_servers:
            for v1 in self.ipsec_servers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['IpsecServers'] = []
        if self.ipsec_servers is not None:
            for k1 in self.ipsec_servers:
                result['IpsecServers'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ipsec_servers = []
        if m.get('IpsecServers') is not None:
            for k1 in m.get('IpsecServers'):
                temp_model = main_models.ListIpsecServersResponseBodyIpsecServers()
                self.ipsec_servers.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListIpsecServersResponseBodyIpsecServers(DaraModel):
    def __init__(
        self,
        client_ip_pool: str = None,
        creation_time: str = None,
        effect_immediately: bool = None,
        idaa_sinstance_id: str = None,
        ike_config: main_models.ListIpsecServersResponseBodyIpsecServersIkeConfig = None,
        internet_ip: str = None,
        ipsec_config: main_models.ListIpsecServersResponseBodyIpsecServersIpsecConfig = None,
        ipsec_server_id: str = None,
        ipsec_server_name: str = None,
        local_subnet: str = None,
        max_connections: int = None,
        multi_factor_auth_enabled: bool = None,
        online_client_count: int = None,
        psk: str = None,
        psk_enabled: bool = None,
        region_id: str = None,
        resource_group_id: str = None,
        vpn_gateway_id: str = None,
    ):
        # The client CIDR block. It refers to the CIDR block that is allocated to the virtual interface of the client.
        self.client_ip_pool = client_ip_pool
        # The time when the IPsec server was created.
        # 
        # T is used as a delimiter. Z indicates that the time is in UTC.
        self.creation_time = creation_time
        # Indicates whether the current IPsec tunnel is deleted and negotiations are reinitiated. Valid values:
        # 
        # *   **true**: immediately initiates negotiations after the configuration is completed.
        # *   **false**: initiates negotiations when inbound traffic is detected.
        self.effect_immediately = effect_immediately
        # The ID of the IDaaS instance.
        self.idaa_sinstance_id = idaa_sinstance_id
        # The configurations of Phase 1 negotiations.
        self.ike_config = ike_config
        # The public IP address of the VPN gateway.
        self.internet_ip = internet_ip
        # The configurations of Phase 2 negotiations.
        self.ipsec_config = ipsec_config
        # The IPsec server ID.
        self.ipsec_server_id = ipsec_server_id
        # The name of the IPsec server.
        self.ipsec_server_name = ipsec_server_name
        # The local CIDR blocks, which refer to the CIDR blocks on the virtual private cloud (VPC) side.
        self.local_subnet = local_subnet
        # The number of SSL-VPN connections supported by the VPN gateway.
        # 
        # >  The number of SSL-VPN connections specified in this parameter includes both SSL-VPN and IPsec-VPN connections. For example, you have five SSL-VPN connections and three SSL clients occupy three SSL-VPN connections. In this case, two clients can connect to the IPsec server.
        self.max_connections = max_connections
        # Indicates whether two-factor authentication is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**: The feature is disabled.
        self.multi_factor_auth_enabled = multi_factor_auth_enabled
        # The number of clients that are connected to the IPsec server.
        self.online_client_count = online_client_count
        # The pre-shared key.
        self.psk = psk
        # Indicates whether pre-shared key authentication is enabled. Only **true** may be returned, which indicates that pre-shared key authentication is enabled.
        self.psk_enabled = psk_enabled
        # The ID of the region where the IPsec server is created.
        self.region_id = region_id
        # The ID of the resource group to which the IPsec server belongs.
        # 
        # You can call the [ListResourceGroups](https://help.aliyun.com/document_detail/158855.html) operation to query the resource group information.
        self.resource_group_id = resource_group_id
        # The ID of the VPN gateway.
        self.vpn_gateway_id = vpn_gateway_id

    def validate(self):
        if self.ike_config:
            self.ike_config.validate()
        if self.ipsec_config:
            self.ipsec_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_ip_pool is not None:
            result['ClientIpPool'] = self.client_ip_pool

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.effect_immediately is not None:
            result['EffectImmediately'] = self.effect_immediately

        if self.idaa_sinstance_id is not None:
            result['IDaaSInstanceId'] = self.idaa_sinstance_id

        if self.ike_config is not None:
            result['IkeConfig'] = self.ike_config.to_map()

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.ipsec_config is not None:
            result['IpsecConfig'] = self.ipsec_config.to_map()

        if self.ipsec_server_id is not None:
            result['IpsecServerId'] = self.ipsec_server_id

        if self.ipsec_server_name is not None:
            result['IpsecServerName'] = self.ipsec_server_name

        if self.local_subnet is not None:
            result['LocalSubnet'] = self.local_subnet

        if self.max_connections is not None:
            result['MaxConnections'] = self.max_connections

        if self.multi_factor_auth_enabled is not None:
            result['MultiFactorAuthEnabled'] = self.multi_factor_auth_enabled

        if self.online_client_count is not None:
            result['OnlineClientCount'] = self.online_client_count

        if self.psk is not None:
            result['Psk'] = self.psk

        if self.psk_enabled is not None:
            result['PskEnabled'] = self.psk_enabled

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.vpn_gateway_id is not None:
            result['VpnGatewayId'] = self.vpn_gateway_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIpPool') is not None:
            self.client_ip_pool = m.get('ClientIpPool')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('EffectImmediately') is not None:
            self.effect_immediately = m.get('EffectImmediately')

        if m.get('IDaaSInstanceId') is not None:
            self.idaa_sinstance_id = m.get('IDaaSInstanceId')

        if m.get('IkeConfig') is not None:
            temp_model = main_models.ListIpsecServersResponseBodyIpsecServersIkeConfig()
            self.ike_config = temp_model.from_map(m.get('IkeConfig'))

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IpsecConfig') is not None:
            temp_model = main_models.ListIpsecServersResponseBodyIpsecServersIpsecConfig()
            self.ipsec_config = temp_model.from_map(m.get('IpsecConfig'))

        if m.get('IpsecServerId') is not None:
            self.ipsec_server_id = m.get('IpsecServerId')

        if m.get('IpsecServerName') is not None:
            self.ipsec_server_name = m.get('IpsecServerName')

        if m.get('LocalSubnet') is not None:
            self.local_subnet = m.get('LocalSubnet')

        if m.get('MaxConnections') is not None:
            self.max_connections = m.get('MaxConnections')

        if m.get('MultiFactorAuthEnabled') is not None:
            self.multi_factor_auth_enabled = m.get('MultiFactorAuthEnabled')

        if m.get('OnlineClientCount') is not None:
            self.online_client_count = m.get('OnlineClientCount')

        if m.get('Psk') is not None:
            self.psk = m.get('Psk')

        if m.get('PskEnabled') is not None:
            self.psk_enabled = m.get('PskEnabled')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('VpnGatewayId') is not None:
            self.vpn_gateway_id = m.get('VpnGatewayId')

        return self

class ListIpsecServersResponseBodyIpsecServersIpsecConfig(DaraModel):
    def __init__(
        self,
        ipsec_auth_alg: str = None,
        ipsec_enc_alg: str = None,
        ipsec_lifetime: int = None,
        ipsec_pfs: str = None,
    ):
        # The IPsec authentication algorithm.
        self.ipsec_auth_alg = ipsec_auth_alg
        # The IPsec encryption algorithm.
        self.ipsec_enc_alg = ipsec_enc_alg
        # The IPsec lifetime. Unit: seconds.
        self.ipsec_lifetime = ipsec_lifetime
        # The Diffie-Hellman key exchange algorithm.
        self.ipsec_pfs = ipsec_pfs

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipsec_auth_alg is not None:
            result['IpsecAuthAlg'] = self.ipsec_auth_alg

        if self.ipsec_enc_alg is not None:
            result['IpsecEncAlg'] = self.ipsec_enc_alg

        if self.ipsec_lifetime is not None:
            result['IpsecLifetime'] = self.ipsec_lifetime

        if self.ipsec_pfs is not None:
            result['IpsecPfs'] = self.ipsec_pfs

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpsecAuthAlg') is not None:
            self.ipsec_auth_alg = m.get('IpsecAuthAlg')

        if m.get('IpsecEncAlg') is not None:
            self.ipsec_enc_alg = m.get('IpsecEncAlg')

        if m.get('IpsecLifetime') is not None:
            self.ipsec_lifetime = m.get('IpsecLifetime')

        if m.get('IpsecPfs') is not None:
            self.ipsec_pfs = m.get('IpsecPfs')

        return self

class ListIpsecServersResponseBodyIpsecServersIkeConfig(DaraModel):
    def __init__(
        self,
        ike_auth_alg: str = None,
        ike_enc_alg: str = None,
        ike_lifetime: int = None,
        ike_mode: str = None,
        ike_pfs: str = None,
        ike_version: str = None,
        local_id: str = None,
        remote_id: str = None,
    ):
        # The IKE authentication algorithm.
        self.ike_auth_alg = ike_auth_alg
        # The IKE encryption algorithm.
        self.ike_enc_alg = ike_enc_alg
        # The IKE lifetime. Unit: seconds.
        self.ike_lifetime = ike_lifetime
        # The IKE negotiation mode. Valid values:
        # 
        # **main**: This mode offers higher security during negotiations.
        self.ike_mode = ike_mode
        # The Diffie-Hellman key exchange algorithm.
        self.ike_pfs = ike_pfs
        # The IKE version.
        self.ike_version = ike_version
        # The ID of the IPsec server. The default value is the public IP address of the VPN gateway. Both FQDNs and IP addresses are supported.
        self.local_id = local_id
        # The identifier of the customer gateway. Both fully qualified domain names (FQDNs) and IP addresses are supported. By default, this parameter is empty.
        self.remote_id = remote_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ike_auth_alg is not None:
            result['IkeAuthAlg'] = self.ike_auth_alg

        if self.ike_enc_alg is not None:
            result['IkeEncAlg'] = self.ike_enc_alg

        if self.ike_lifetime is not None:
            result['IkeLifetime'] = self.ike_lifetime

        if self.ike_mode is not None:
            result['IkeMode'] = self.ike_mode

        if self.ike_pfs is not None:
            result['IkePfs'] = self.ike_pfs

        if self.ike_version is not None:
            result['IkeVersion'] = self.ike_version

        if self.local_id is not None:
            result['LocalId'] = self.local_id

        if self.remote_id is not None:
            result['RemoteId'] = self.remote_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IkeAuthAlg') is not None:
            self.ike_auth_alg = m.get('IkeAuthAlg')

        if m.get('IkeEncAlg') is not None:
            self.ike_enc_alg = m.get('IkeEncAlg')

        if m.get('IkeLifetime') is not None:
            self.ike_lifetime = m.get('IkeLifetime')

        if m.get('IkeMode') is not None:
            self.ike_mode = m.get('IkeMode')

        if m.get('IkePfs') is not None:
            self.ike_pfs = m.get('IkePfs')

        if m.get('IkeVersion') is not None:
            self.ike_version = m.get('IkeVersion')

        if m.get('LocalId') is not None:
            self.local_id = m.get('LocalId')

        if m.get('RemoteId') is not None:
            self.remote_id = m.get('RemoteId')

        return self

