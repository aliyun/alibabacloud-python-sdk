# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribeVpnConnectionsResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        vpn_connections: main_models.DescribeVpnConnectionsResponseBodyVpnConnections = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page for paging queries.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count
        self.vpn_connections = vpn_connections

    def validate(self):
        if self.vpn_connections:
            self.vpn_connections.validate()

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

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.vpn_connections is not None:
            result['VpnConnections'] = self.vpn_connections.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('VpnConnections') is not None:
            temp_model = main_models.DescribeVpnConnectionsResponseBodyVpnConnections()
            self.vpn_connections = temp_model.from_map(m.get('VpnConnections'))

        return self

class DescribeVpnConnectionsResponseBodyVpnConnections(DaraModel):
    def __init__(
        self,
        vpn_connection: List[main_models.DescribeVpnConnectionsResponseBodyVpnConnectionsVpnConnection] = None,
    ):
        self.vpn_connection = vpn_connection

    def validate(self):
        if self.vpn_connection:
            for v1 in self.vpn_connection:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['VpnConnection'] = []
        if self.vpn_connection is not None:
            for k1 in self.vpn_connection:
                result['VpnConnection'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.vpn_connection = []
        if m.get('VpnConnection') is not None:
            for k1 in m.get('VpnConnection'):
                temp_model = main_models.DescribeVpnConnectionsResponseBodyVpnConnectionsVpnConnection()
                self.vpn_connection.append(temp_model.from_map(k1))

        return self

class DescribeVpnConnectionsResponseBodyVpnConnectionsVpnConnection(DaraModel):
    def __init__(
        self,
        attach_instance_id: str = None,
        attach_type: str = None,
        create_time: int = None,
        cross_account_authorized: bool = None,
        customer_gateway_id: str = None,
        effect_immediately: bool = None,
        enable_dpd: bool = None,
        enable_nat_traversal: bool = None,
        enable_tunnels_bgp: bool = None,
        ike_config: main_models.DescribeVpnConnectionsResponseBodyVpnConnectionsVpnConnectionIkeConfig = None,
        internet_ip: str = None,
        ipsec_config: main_models.DescribeVpnConnectionsResponseBodyVpnConnectionsVpnConnectionIpsecConfig = None,
        local_subnet: str = None,
        name: str = None,
        network_type: str = None,
        remote_ca_certificate: str = None,
        remote_subnet: str = None,
        resource_group_id: str = None,
        spec: str = None,
        state: str = None,
        status: str = None,
        tag: main_models.DescribeVpnConnectionsResponseBodyVpnConnectionsVpnConnectionTag = None,
        transit_router_id: str = None,
        transit_router_name: str = None,
        tunnel_bandwidth: str = None,
        tunnel_options_specification: main_models.DescribeVpnConnectionsResponseBodyVpnConnectionsVpnConnectionTunnelOptionsSpecification = None,
        vco_health_check: main_models.DescribeVpnConnectionsResponseBodyVpnConnectionsVpnConnectionVcoHealthCheck = None,
        vpn_bgp_config: main_models.DescribeVpnConnectionsResponseBodyVpnConnectionsVpnConnectionVpnBgpConfig = None,
        vpn_connection_id: str = None,
        vpn_gateway_id: str = None,
    ):
        self.attach_instance_id = attach_instance_id
        self.attach_type = attach_type
        self.create_time = create_time
        self.cross_account_authorized = cross_account_authorized
        self.customer_gateway_id = customer_gateway_id
        self.effect_immediately = effect_immediately
        self.enable_dpd = enable_dpd
        self.enable_nat_traversal = enable_nat_traversal
        self.enable_tunnels_bgp = enable_tunnels_bgp
        self.ike_config = ike_config
        self.internet_ip = internet_ip
        self.ipsec_config = ipsec_config
        self.local_subnet = local_subnet
        self.name = name
        self.network_type = network_type
        self.remote_ca_certificate = remote_ca_certificate
        self.remote_subnet = remote_subnet
        self.resource_group_id = resource_group_id
        self.spec = spec
        self.state = state
        self.status = status
        self.tag = tag
        self.transit_router_id = transit_router_id
        self.transit_router_name = transit_router_name
        self.tunnel_bandwidth = tunnel_bandwidth
        self.tunnel_options_specification = tunnel_options_specification
        self.vco_health_check = vco_health_check
        self.vpn_bgp_config = vpn_bgp_config
        self.vpn_connection_id = vpn_connection_id
        self.vpn_gateway_id = vpn_gateway_id

    def validate(self):
        if self.ike_config:
            self.ike_config.validate()
        if self.ipsec_config:
            self.ipsec_config.validate()
        if self.tag:
            self.tag.validate()
        if self.tunnel_options_specification:
            self.tunnel_options_specification.validate()
        if self.vco_health_check:
            self.vco_health_check.validate()
        if self.vpn_bgp_config:
            self.vpn_bgp_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attach_instance_id is not None:
            result['AttachInstanceId'] = self.attach_instance_id

        if self.attach_type is not None:
            result['AttachType'] = self.attach_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.cross_account_authorized is not None:
            result['CrossAccountAuthorized'] = self.cross_account_authorized

        if self.customer_gateway_id is not None:
            result['CustomerGatewayId'] = self.customer_gateway_id

        if self.effect_immediately is not None:
            result['EffectImmediately'] = self.effect_immediately

        if self.enable_dpd is not None:
            result['EnableDpd'] = self.enable_dpd

        if self.enable_nat_traversal is not None:
            result['EnableNatTraversal'] = self.enable_nat_traversal

        if self.enable_tunnels_bgp is not None:
            result['EnableTunnelsBgp'] = self.enable_tunnels_bgp

        if self.ike_config is not None:
            result['IkeConfig'] = self.ike_config.to_map()

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.ipsec_config is not None:
            result['IpsecConfig'] = self.ipsec_config.to_map()

        if self.local_subnet is not None:
            result['LocalSubnet'] = self.local_subnet

        if self.name is not None:
            result['Name'] = self.name

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.remote_ca_certificate is not None:
            result['RemoteCaCertificate'] = self.remote_ca_certificate

        if self.remote_subnet is not None:
            result['RemoteSubnet'] = self.remote_subnet

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.spec is not None:
            result['Spec'] = self.spec

        if self.state is not None:
            result['State'] = self.state

        if self.status is not None:
            result['Status'] = self.status

        if self.tag is not None:
            result['Tag'] = self.tag.to_map()

        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id

        if self.transit_router_name is not None:
            result['TransitRouterName'] = self.transit_router_name

        if self.tunnel_bandwidth is not None:
            result['TunnelBandwidth'] = self.tunnel_bandwidth

        if self.tunnel_options_specification is not None:
            result['TunnelOptionsSpecification'] = self.tunnel_options_specification.to_map()

        if self.vco_health_check is not None:
            result['VcoHealthCheck'] = self.vco_health_check.to_map()

        if self.vpn_bgp_config is not None:
            result['VpnBgpConfig'] = self.vpn_bgp_config.to_map()

        if self.vpn_connection_id is not None:
            result['VpnConnectionId'] = self.vpn_connection_id

        if self.vpn_gateway_id is not None:
            result['VpnGatewayId'] = self.vpn_gateway_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachInstanceId') is not None:
            self.attach_instance_id = m.get('AttachInstanceId')

        if m.get('AttachType') is not None:
            self.attach_type = m.get('AttachType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CrossAccountAuthorized') is not None:
            self.cross_account_authorized = m.get('CrossAccountAuthorized')

        if m.get('CustomerGatewayId') is not None:
            self.customer_gateway_id = m.get('CustomerGatewayId')

        if m.get('EffectImmediately') is not None:
            self.effect_immediately = m.get('EffectImmediately')

        if m.get('EnableDpd') is not None:
            self.enable_dpd = m.get('EnableDpd')

        if m.get('EnableNatTraversal') is not None:
            self.enable_nat_traversal = m.get('EnableNatTraversal')

        if m.get('EnableTunnelsBgp') is not None:
            self.enable_tunnels_bgp = m.get('EnableTunnelsBgp')

        if m.get('IkeConfig') is not None:
            temp_model = main_models.DescribeVpnConnectionsResponseBodyVpnConnectionsVpnConnectionIkeConfig()
            self.ike_config = temp_model.from_map(m.get('IkeConfig'))

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IpsecConfig') is not None:
            temp_model = main_models.DescribeVpnConnectionsResponseBodyVpnConnectionsVpnConnectionIpsecConfig()
            self.ipsec_config = temp_model.from_map(m.get('IpsecConfig'))

        if m.get('LocalSubnet') is not None:
            self.local_subnet = m.get('LocalSubnet')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('RemoteCaCertificate') is not None:
            self.remote_ca_certificate = m.get('RemoteCaCertificate')

        if m.get('RemoteSubnet') is not None:
            self.remote_subnet = m.get('RemoteSubnet')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tag') is not None:
            temp_model = main_models.DescribeVpnConnectionsResponseBodyVpnConnectionsVpnConnectionTag()
            self.tag = temp_model.from_map(m.get('Tag'))

        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')

        if m.get('TransitRouterName') is not None:
            self.transit_router_name = m.get('TransitRouterName')

        if m.get('TunnelBandwidth') is not None:
            self.tunnel_bandwidth = m.get('TunnelBandwidth')

        if m.get('TunnelOptionsSpecification') is not None:
            temp_model = main_models.DescribeVpnConnectionsResponseBodyVpnConnectionsVpnConnectionTunnelOptionsSpecification()
            self.tunnel_options_specification = temp_model.from_map(m.get('TunnelOptionsSpecification'))

        if m.get('VcoHealthCheck') is not None:
            temp_model = main_models.DescribeVpnConnectionsResponseBodyVpnConnectionsVpnConnectionVcoHealthCheck()
            self.vco_health_check = temp_model.from_map(m.get('VcoHealthCheck'))

        if m.get('VpnBgpConfig') is not None:
            temp_model = main_models.DescribeVpnConnectionsResponseBodyVpnConnectionsVpnConnectionVpnBgpConfig()
            self.vpn_bgp_config = temp_model.from_map(m.get('VpnBgpConfig'))

        if m.get('VpnConnectionId') is not None:
            self.vpn_connection_id = m.get('VpnConnectionId')

        if m.get('VpnGatewayId') is not None:
            self.vpn_gateway_id = m.get('VpnGatewayId')

        return self

class DescribeVpnConnectionsResponseBodyVpnConnectionsVpnConnectionVpnBgpConfig(DaraModel):
    def __init__(
        self,
        auth_key: str = None,
        local_asn: int = None,
        local_bgp_ip: str = None,
        peer_asn: int = None,
        peer_bgp_ip: str = None,
        status: str = None,
        tunnel_cidr: str = None,
    ):
        self.auth_key = auth_key
        self.local_asn = local_asn
        self.local_bgp_ip = local_bgp_ip
        self.peer_asn = peer_asn
        self.peer_bgp_ip = peer_bgp_ip
        self.status = status
        self.tunnel_cidr = tunnel_cidr

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key

        if self.local_asn is not None:
            result['LocalAsn'] = self.local_asn

        if self.local_bgp_ip is not None:
            result['LocalBgpIp'] = self.local_bgp_ip

        if self.peer_asn is not None:
            result['PeerAsn'] = self.peer_asn

        if self.peer_bgp_ip is not None:
            result['PeerBgpIp'] = self.peer_bgp_ip

        if self.status is not None:
            result['Status'] = self.status

        if self.tunnel_cidr is not None:
            result['TunnelCidr'] = self.tunnel_cidr

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')

        if m.get('LocalAsn') is not None:
            self.local_asn = m.get('LocalAsn')

        if m.get('LocalBgpIp') is not None:
            self.local_bgp_ip = m.get('LocalBgpIp')

        if m.get('PeerAsn') is not None:
            self.peer_asn = m.get('PeerAsn')

        if m.get('PeerBgpIp') is not None:
            self.peer_bgp_ip = m.get('PeerBgpIp')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TunnelCidr') is not None:
            self.tunnel_cidr = m.get('TunnelCidr')

        return self

class DescribeVpnConnectionsResponseBodyVpnConnectionsVpnConnectionVcoHealthCheck(DaraModel):
    def __init__(
        self,
        dip: str = None,
        enable: str = None,
        interval: int = None,
        policy: str = None,
        retry: int = None,
        sip: str = None,
        status: str = None,
    ):
        self.dip = dip
        self.enable = enable
        self.interval = interval
        self.policy = policy
        self.retry = retry
        self.sip = sip
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dip is not None:
            result['Dip'] = self.dip

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.retry is not None:
            result['Retry'] = self.retry

        if self.sip is not None:
            result['Sip'] = self.sip

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dip') is not None:
            self.dip = m.get('Dip')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('Retry') is not None:
            self.retry = m.get('Retry')

        if m.get('Sip') is not None:
            self.sip = m.get('Sip')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeVpnConnectionsResponseBodyVpnConnectionsVpnConnectionTunnelOptionsSpecification(DaraModel):
    def __init__(
        self,
        tunnel_options: List[main_models.DescribeVpnConnectionsResponseBodyVpnConnectionsVpnConnectionTunnelOptionsSpecificationTunnelOptions] = None,
    ):
        self.tunnel_options = tunnel_options

    def validate(self):
        if self.tunnel_options:
            for v1 in self.tunnel_options:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TunnelOptions'] = []
        if self.tunnel_options is not None:
            for k1 in self.tunnel_options:
                result['TunnelOptions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tunnel_options = []
        if m.get('TunnelOptions') is not None:
            for k1 in m.get('TunnelOptions'):
                temp_model = main_models.DescribeVpnConnectionsResponseBodyVpnConnectionsVpnConnectionTunnelOptionsSpecificationTunnelOptions()
                self.tunnel_options.append(temp_model.from_map(k1))

        return self

class DescribeVpnConnectionsResponseBodyVpnConnectionsVpnConnectionTunnelOptionsSpecificationTunnelOptions(DaraModel):
    def __init__(
        self,
        customer_gateway_id: str = None,
        enable_dpd: str = None,
        enable_nat_traversal: str = None,
        internet_ip: str = None,
        remote_ca_certificate: str = None,
        role: str = None,
        state: str = None,
        status: str = None,
        tunnel_bgp_config: main_models.DescribeVpnConnectionsResponseBodyVpnConnectionsVpnConnectionTunnelOptionsSpecificationTunnelOptionsTunnelBgpConfig = None,
        tunnel_id: str = None,
        tunnel_ike_config: main_models.DescribeVpnConnectionsResponseBodyVpnConnectionsVpnConnectionTunnelOptionsSpecificationTunnelOptionsTunnelIkeConfig = None,
        tunnel_index: int = None,
        tunnel_ipsec_config: main_models.DescribeVpnConnectionsResponseBodyVpnConnectionsVpnConnectionTunnelOptionsSpecificationTunnelOptionsTunnelIpsecConfig = None,
        zone_no: str = None,
    ):
        self.customer_gateway_id = customer_gateway_id
        self.enable_dpd = enable_dpd
        self.enable_nat_traversal = enable_nat_traversal
        self.internet_ip = internet_ip
        self.remote_ca_certificate = remote_ca_certificate
        self.role = role
        self.state = state
        self.status = status
        self.tunnel_bgp_config = tunnel_bgp_config
        self.tunnel_id = tunnel_id
        self.tunnel_ike_config = tunnel_ike_config
        self.tunnel_index = tunnel_index
        self.tunnel_ipsec_config = tunnel_ipsec_config
        self.zone_no = zone_no

    def validate(self):
        if self.tunnel_bgp_config:
            self.tunnel_bgp_config.validate()
        if self.tunnel_ike_config:
            self.tunnel_ike_config.validate()
        if self.tunnel_ipsec_config:
            self.tunnel_ipsec_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.customer_gateway_id is not None:
            result['CustomerGatewayId'] = self.customer_gateway_id

        if self.enable_dpd is not None:
            result['EnableDpd'] = self.enable_dpd

        if self.enable_nat_traversal is not None:
            result['EnableNatTraversal'] = self.enable_nat_traversal

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.remote_ca_certificate is not None:
            result['RemoteCaCertificate'] = self.remote_ca_certificate

        if self.role is not None:
            result['Role'] = self.role

        if self.state is not None:
            result['State'] = self.state

        if self.status is not None:
            result['Status'] = self.status

        if self.tunnel_bgp_config is not None:
            result['TunnelBgpConfig'] = self.tunnel_bgp_config.to_map()

        if self.tunnel_id is not None:
            result['TunnelId'] = self.tunnel_id

        if self.tunnel_ike_config is not None:
            result['TunnelIkeConfig'] = self.tunnel_ike_config.to_map()

        if self.tunnel_index is not None:
            result['TunnelIndex'] = self.tunnel_index

        if self.tunnel_ipsec_config is not None:
            result['TunnelIpsecConfig'] = self.tunnel_ipsec_config.to_map()

        if self.zone_no is not None:
            result['ZoneNo'] = self.zone_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomerGatewayId') is not None:
            self.customer_gateway_id = m.get('CustomerGatewayId')

        if m.get('EnableDpd') is not None:
            self.enable_dpd = m.get('EnableDpd')

        if m.get('EnableNatTraversal') is not None:
            self.enable_nat_traversal = m.get('EnableNatTraversal')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('RemoteCaCertificate') is not None:
            self.remote_ca_certificate = m.get('RemoteCaCertificate')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TunnelBgpConfig') is not None:
            temp_model = main_models.DescribeVpnConnectionsResponseBodyVpnConnectionsVpnConnectionTunnelOptionsSpecificationTunnelOptionsTunnelBgpConfig()
            self.tunnel_bgp_config = temp_model.from_map(m.get('TunnelBgpConfig'))

        if m.get('TunnelId') is not None:
            self.tunnel_id = m.get('TunnelId')

        if m.get('TunnelIkeConfig') is not None:
            temp_model = main_models.DescribeVpnConnectionsResponseBodyVpnConnectionsVpnConnectionTunnelOptionsSpecificationTunnelOptionsTunnelIkeConfig()
            self.tunnel_ike_config = temp_model.from_map(m.get('TunnelIkeConfig'))

        if m.get('TunnelIndex') is not None:
            self.tunnel_index = m.get('TunnelIndex')

        if m.get('TunnelIpsecConfig') is not None:
            temp_model = main_models.DescribeVpnConnectionsResponseBodyVpnConnectionsVpnConnectionTunnelOptionsSpecificationTunnelOptionsTunnelIpsecConfig()
            self.tunnel_ipsec_config = temp_model.from_map(m.get('TunnelIpsecConfig'))

        if m.get('ZoneNo') is not None:
            self.zone_no = m.get('ZoneNo')

        return self

class DescribeVpnConnectionsResponseBodyVpnConnectionsVpnConnectionTunnelOptionsSpecificationTunnelOptionsTunnelIpsecConfig(DaraModel):
    def __init__(
        self,
        ipsec_auth_alg: str = None,
        ipsec_enc_alg: str = None,
        ipsec_lifetime: str = None,
        ipsec_pfs: str = None,
    ):
        self.ipsec_auth_alg = ipsec_auth_alg
        self.ipsec_enc_alg = ipsec_enc_alg
        self.ipsec_lifetime = ipsec_lifetime
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

class DescribeVpnConnectionsResponseBodyVpnConnectionsVpnConnectionTunnelOptionsSpecificationTunnelOptionsTunnelIkeConfig(DaraModel):
    def __init__(
        self,
        ike_auth_alg: str = None,
        ike_enc_alg: str = None,
        ike_lifetime: str = None,
        ike_mode: str = None,
        ike_pfs: str = None,
        ike_version: str = None,
        local_id: str = None,
        psk: str = None,
        remote_id: str = None,
    ):
        self.ike_auth_alg = ike_auth_alg
        self.ike_enc_alg = ike_enc_alg
        self.ike_lifetime = ike_lifetime
        self.ike_mode = ike_mode
        self.ike_pfs = ike_pfs
        self.ike_version = ike_version
        self.local_id = local_id
        self.psk = psk
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

        if self.psk is not None:
            result['Psk'] = self.psk

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

        if m.get('Psk') is not None:
            self.psk = m.get('Psk')

        if m.get('RemoteId') is not None:
            self.remote_id = m.get('RemoteId')

        return self

class DescribeVpnConnectionsResponseBodyVpnConnectionsVpnConnectionTunnelOptionsSpecificationTunnelOptionsTunnelBgpConfig(DaraModel):
    def __init__(
        self,
        bgp_status: str = None,
        local_asn: str = None,
        local_bgp_ip: str = None,
        peer_asn: str = None,
        peer_bgp_ip: str = None,
        tunnel_cidr: str = None,
    ):
        self.bgp_status = bgp_status
        self.local_asn = local_asn
        self.local_bgp_ip = local_bgp_ip
        self.peer_asn = peer_asn
        self.peer_bgp_ip = peer_bgp_ip
        self.tunnel_cidr = tunnel_cidr

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bgp_status is not None:
            result['BgpStatus'] = self.bgp_status

        if self.local_asn is not None:
            result['LocalAsn'] = self.local_asn

        if self.local_bgp_ip is not None:
            result['LocalBgpIp'] = self.local_bgp_ip

        if self.peer_asn is not None:
            result['PeerAsn'] = self.peer_asn

        if self.peer_bgp_ip is not None:
            result['PeerBgpIp'] = self.peer_bgp_ip

        if self.tunnel_cidr is not None:
            result['TunnelCidr'] = self.tunnel_cidr

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BgpStatus') is not None:
            self.bgp_status = m.get('BgpStatus')

        if m.get('LocalAsn') is not None:
            self.local_asn = m.get('LocalAsn')

        if m.get('LocalBgpIp') is not None:
            self.local_bgp_ip = m.get('LocalBgpIp')

        if m.get('PeerAsn') is not None:
            self.peer_asn = m.get('PeerAsn')

        if m.get('PeerBgpIp') is not None:
            self.peer_bgp_ip = m.get('PeerBgpIp')

        if m.get('TunnelCidr') is not None:
            self.tunnel_cidr = m.get('TunnelCidr')

        return self

class DescribeVpnConnectionsResponseBodyVpnConnectionsVpnConnectionTag(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeVpnConnectionsResponseBodyVpnConnectionsVpnConnectionTagTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeVpnConnectionsResponseBodyVpnConnectionsVpnConnectionTagTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeVpnConnectionsResponseBodyVpnConnectionsVpnConnectionTagTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeVpnConnectionsResponseBodyVpnConnectionsVpnConnectionIpsecConfig(DaraModel):
    def __init__(
        self,
        ipsec_auth_alg: str = None,
        ipsec_enc_alg: str = None,
        ipsec_lifetime: int = None,
        ipsec_pfs: str = None,
    ):
        self.ipsec_auth_alg = ipsec_auth_alg
        self.ipsec_enc_alg = ipsec_enc_alg
        self.ipsec_lifetime = ipsec_lifetime
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

class DescribeVpnConnectionsResponseBodyVpnConnectionsVpnConnectionIkeConfig(DaraModel):
    def __init__(
        self,
        ike_auth_alg: str = None,
        ike_enc_alg: str = None,
        ike_lifetime: int = None,
        ike_mode: str = None,
        ike_pfs: str = None,
        ike_version: str = None,
        local_id: str = None,
        psk: str = None,
        remote_id: str = None,
    ):
        self.ike_auth_alg = ike_auth_alg
        self.ike_enc_alg = ike_enc_alg
        self.ike_lifetime = ike_lifetime
        self.ike_mode = ike_mode
        self.ike_pfs = ike_pfs
        self.ike_version = ike_version
        self.local_id = local_id
        self.psk = psk
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

        if self.psk is not None:
            result['Psk'] = self.psk

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

        if m.get('Psk') is not None:
            self.psk = m.get('Psk')

        if m.get('RemoteId') is not None:
            self.remote_id = m.get('RemoteId')

        return self

