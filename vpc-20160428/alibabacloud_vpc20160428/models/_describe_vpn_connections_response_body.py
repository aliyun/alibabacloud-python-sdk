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
        # The number of entries returned per page.
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
        # 转发路由器实例所属的云企业网实例ID。
        self.attach_instance_id = attach_instance_id
        # IPsec连接绑定的资源类型。
        # 
        # - **CEN**：表示IPsec连接已绑定云企业网实例下的转发路由器实例。
        # - **NO_ASSOCIATED**：表示IPsec连接未绑定任何资源。
        # - **VPNGW**：表示IPsec连接绑定了VPN网关实例。
        self.attach_type = attach_type
        # 创建IPsec连接的时间戳。单位：毫秒。
        # 
        # 时间戳的格式采用Unix时间戳，表示从格林威治时间1970年01月01日00时00分00秒至创建IPsec连接时的总时长。
        self.create_time = create_time
        # IPsec连接是否绑定了跨账号的转发路由器实例。
        # 
        # - **true**：是。
        # - **false**：否。
        self.cross_account_authorized = cross_account_authorized
        # IPsec连接关联的用户网关的实例ID。
        self.customer_gateway_id = customer_gateway_id
        # IPsec连接的配置是否立即生效。
        # 
        # - **true**：是，配置变更完成后触发重连。
        # - **false**：否，有流量时触发重连。
        self.effect_immediately = effect_immediately
        # IPsec连接是否已开启DPD（对等体存活检测）功能。
        # 
        # - **true**：开启DPD功能。
        # 
        #     IPsec发起端会发送DPD报文用来检测对端的设备是否存活，如果在设定时间内未收到正确回应则认为对端已经断线，IPsec将删除ISAKMP SA和相应的IPsec SA，安全隧道同样也会被删除。
        # 
        # - **false**：不开启DPD功能，IPsec发起端不会发送DPD探测报文。
        self.enable_dpd = enable_dpd
        # IPsec连接是否已开启NAT穿越功能。
        # 
        # - **true**：开启NAT穿越功能。
        # 
        #    开启后，IKE协商过程会删除对UDP端口号的验证过程，同时实现对VPN隧道中NAT网关设备的发现功能。
        # 
        # - **false**：不开启NAT穿越功能。
        self.enable_nat_traversal = enable_nat_traversal
        # 隧道BGP的开启状态。
        # 
        # - **true**：已开启。
        # - **false**：未开启。
        self.enable_tunnels_bgp = enable_tunnels_bgp
        # 第一阶段协商的配置。
        self.ike_config = ike_config
        # IPsec连接的网关IP地址。
        # 
        # > 仅IPsec连接绑定转发路由器实例时会返回当前参数。
        self.internet_ip = internet_ip
        # 第二阶段协商的配置。
        self.ipsec_config = ipsec_config
        # IPsec连接阿里云侧的网段。
        # 
        # 在多个网段的情况下，网段之间使用半角逗号（,）分隔。
        self.local_subnet = local_subnet
        # IPsec连接的名称。
        self.name = name
        # IPsec连接的网络类型。
        # 
        # - **public**：公网，表示IPsec连接通过公网建立加密通信通道。
        # - **private**：私网，表示IPsec连接通过私网建立加密通信通道。
        self.network_type = network_type
        # 对端的CA证书。
        self.remote_ca_certificate = remote_ca_certificate
        # 本地数据中心侧的网段。
        # 
        # 在多个网段的情况下，网段之间使用半角逗号（,）分隔。
        self.remote_subnet = remote_subnet
        # IPsec连接所属的资源组ID。
        # 
        # 您可以调用[ListResourceGroups](https://help.aliyun.com/document_detail/158855.html)接口查询资源组信息。
        self.resource_group_id = resource_group_id
        # IPsec连接的带宽规格。单位：**Mbps**。
        self.spec = spec
        # IPsec连接与转发路由器实例的绑定状态。
        # 
        # - **active**：IPsec连接已与VPN网关实例绑定，状态正常。
        # - **init**：IPsec连接未绑定任何资源，IPsec连接初始化。
        # - **attaching**：IPsec连接与转发路由器实例绑定中。
        # - **attached**：IPsec连接已与转发路由器实例绑定。
        # - **detaching**：IPsec连接与转发路由器实例解绑中。
        # - **financialLocked**：欠费锁定。
        # - **provisioning**：资源准备中。
        # - **updating**：更新中。
        # - **upgrading**：升级中。
        # - **deleted**：已删除。
        self.state = state
        # IPsec连接的状态。
        # 
        # - **ike_sa_not_established**：第一阶段协商失败。
        # 
        # - **ike_sa_established**：第一阶段协商成功。
        # 
        # - **ipsec_sa_not_established**：第二阶段协商失败。
        # 
        # - **ipsec_sa_established**：第二阶段协商成功。
        self.status = status
        # IPsec连接绑定的标签列表。
        self.tag = tag
        # IPsec连接绑定的转发路由器实例ID。
        self.transit_router_id = transit_router_id
        # 转发路由器实例的名称。
        self.transit_router_name = transit_router_name
        # 用于说明VPN单条隧道的带宽规格，取值：
        # Standard（默认值）：标准型，默认带宽1Gbps
        # Large（大型）：大型，默认带宽3Gbps
        self.tunnel_bandwidth = tunnel_bandwidth
        # IPsec连接的隧道配置信息。
        # 
        # 仅查询双隧道模式的IPsec连接会返回**TunnelOptionsSpecification**数组下的参数。
        self.tunnel_options_specification = tunnel_options_specification
        # IPsec连接的健康检查配置。
        self.vco_health_check = vco_health_check
        # IPsec连接BGP路由协议的配置。
        self.vpn_bgp_config = vpn_bgp_config
        # IPsec连接的ID。
        self.vpn_connection_id = vpn_connection_id
        # VPN网关的实例ID。
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
        # BGP路由协议的认证密钥。
        self.auth_key = auth_key
        # 阿里云侧自治系统号。
        self.local_asn = local_asn
        # 阿里云侧BGP地址。
        self.local_bgp_ip = local_bgp_ip
        # 对端自治系统号。
        self.peer_asn = peer_asn
        # 对端BGP地址。
        self.peer_bgp_ip = peer_bgp_ip
        # BGP路由协议的协商状态。
        # 
        # - **success**：正常。
        # 
        # - **false**：异常。
        self.status = status
        # IPsec连接BGP网段。该网段是一个在169.254.0.0/16内的子网掩码长度为30的网段。
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
        # 目的IP地址。
        self.dip = dip
        # 健康检查的开启状态。
        # 
        # - **true**：已开启。
        # 
        # - **false**：未开启。
        self.enable = enable
        # 健康检查的时间间隔。单位：秒。
        self.interval = interval
        # 健康检查失败时是否撤销已发布的路由。
        # 
        # - **revoke_route**：撤销路由。
        # - **reserve_route**：不撤销路由。
        self.policy = policy
        # 健康检查的重试发包次数。
        self.retry = retry
        # 源IP地址。
        self.sip = sip
        # 健康检查状态。
        # 
        # - **success**：正常。
        # - **failed**：异常。
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
        # 隧道关联的用户网关ID。
        self.customer_gateway_id = customer_gateway_id
        # 隧道是否已开启DPD（对等体存活检测）功能。
        # - **false**：未开启。
        # - **true**：已开启。
        self.enable_dpd = enable_dpd
        # 隧道是否已开启NAT穿越功能。
        # 
        # - **false**：未开启。
        # - **true**：已开启。
        self.enable_nat_traversal = enable_nat_traversal
        # 隧道的IP地址。
        self.internet_ip = internet_ip
        # 隧道对端的CA证书。
        # 
        # 仅VPN网关实例的类型为国密型时才会返回当前参数。
        self.remote_ca_certificate = remote_ca_certificate
        # 隧道的角色。
        # 
        # - **master**：表示当前隧道为主隧道。
        # - **slave**：表示当前隧道为备隧道。
        self.role = role
        # 隧道的状态。
        # 
        # - **active**：状态正常。
        # - **updating**：更新中。
        # - **deleting**：删除中。
        self.state = state
        # IPsec连接的状态。
        # 
        # - **ike_sa_not_established**：第一阶段协商失败。
        # 
        # - **ike_sa_established**：第一阶段协商成功。
        # 
        # - **ipsec_sa_not_established**：第二阶段协商失败。
        # 
        # - **ipsec_sa_established**：第二阶段协商成功。
        self.status = status
        # 隧道的BGP配置信息。
        self.tunnel_bgp_config = tunnel_bgp_config
        # 隧道ID。
        self.tunnel_id = tunnel_id
        # 第一阶段协商的配置。
        self.tunnel_ike_config = tunnel_ike_config
        # 隧道的创建顺序。
        # - **1**：第一条隧道。
        # - **2**：第二条隧道。
        # 
        # > 仅IPsec连接绑定转发路由器时会返回该参数。
        self.tunnel_index = tunnel_index
        # 第二阶段协商的配置。
        self.tunnel_ipsec_config = tunnel_ipsec_config
        # 隧道部署的可用区。
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
        # IPsec阶段认证算法。
        self.ipsec_auth_alg = ipsec_auth_alg
        # IPsec阶段加密算法。
        self.ipsec_enc_alg = ipsec_enc_alg
        # IPsec阶段生存时间。单位：秒。
        self.ipsec_lifetime = ipsec_lifetime
        # IPsec阶段DH分组。
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
        # IKE阶段认证算法。
        self.ike_auth_alg = ike_auth_alg
        # IKE阶段加密算法。
        self.ike_enc_alg = ike_enc_alg
        # IKE阶段生存时间。单位：秒。
        self.ike_lifetime = ike_lifetime
        # IKE协商模式。
        # 
        # - **main**：主模式，协商过程安全性高。
        # - **aggressive**：野蛮模式，协商快速且协商成功率高。
        self.ike_mode = ike_mode
        # IKE阶段DH分组。
        self.ike_pfs = ike_pfs
        # IKE协议版本。
        self.ike_version = ike_version
        # 隧道本端（阿里云侧）的标识。
        self.local_id = local_id
        # 预共享密钥。
        self.psk = psk
        # 隧道对端的标识。
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
        # BGP的协商状态。
        # 
        # - **success**：正常。
        # - **failed**：异常。
        self.bgp_status = bgp_status
        # 隧道本端（阿里云侧）的自治系统号。
        self.local_asn = local_asn
        # 隧道本端（阿里云侧）的BGP地址。
        self.local_bgp_ip = local_bgp_ip
        # 隧道对端的自治系统号。
        self.peer_asn = peer_asn
        # 隧道对端的BGP地址。
        self.peer_bgp_ip = peer_bgp_ip
        # 隧道的BGP网段。
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
        # 标签键。
        self.key = key
        # 标签值。
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
        # IPsec阶段认证算法。
        self.ipsec_auth_alg = ipsec_auth_alg
        # IPsec阶段加密算法。
        self.ipsec_enc_alg = ipsec_enc_alg
        # IPsec阶段生存时间。单位：秒。
        self.ipsec_lifetime = ipsec_lifetime
        # IPsec阶段DH分组。
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
        # IKE阶段认证算法。
        self.ike_auth_alg = ike_auth_alg
        # IKE阶段加密算法。
        self.ike_enc_alg = ike_enc_alg
        # IKE阶段生存时间。单位：秒。
        self.ike_lifetime = ike_lifetime
        # IKE阶段协商模式。
        # 
        # - **main**：主模式，协商过程安全性高。
        # - **aggressive**：野蛮模式，协商快速且协商成功率高。
        self.ike_mode = ike_mode
        # IKE阶段DH分组。
        self.ike_pfs = ike_pfs
        # IKE协议版本。
        # 
        # - **ikev1**
        # - **ikev2**
        # 
        # 相对于IKEv1版本，IKEv2版本简化了SA的协商过程并且对于多网段的场景提供了更好的支持。
        self.ike_version = ike_version
        # IPsec连接对端本地数据中心侧的标识。
        self.local_id = local_id
        # 预共享密钥。
        self.psk = psk
        # IPsec连接阿里云侧的标识。
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

