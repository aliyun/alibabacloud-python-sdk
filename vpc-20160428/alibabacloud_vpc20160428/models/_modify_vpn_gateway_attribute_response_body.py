# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyVpnGatewayAttributeResponseBody(DaraModel):
    def __init__(
        self,
        auto_propagate: bool = None,
        business_status: str = None,
        create_time: int = None,
        description: str = None,
        disaster_recovery_internet_ip: str = None,
        disaster_recovery_vswitch_id: str = None,
        enable_bgp: bool = None,
        end_time: int = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        name: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        spec: str = None,
        ssl_vpn_internet_ip: str = None,
        status: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        vpn_gateway_id: str = None,
    ):
        # Indicates whether BGP routes are automatically advertised to the VPC. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.auto_propagate = auto_propagate
        # The payment status of the VPN gateway. Valid values:
        # 
        # *   **Normal**
        # *   **FinancialLocked**
        self.business_status = business_status
        # The time when the VPN gateway was created. Unit: milliseconds.
        # 
        # This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_time = create_time
        # The description of the VPN gateway.
        self.description = description
        # The second IP address assigned by the system to create an IPsec-VPN connection.
        # 
        # This parameter is returned only when the VPN gateway supports the dual-tunnel mode.
        self.disaster_recovery_internet_ip = disaster_recovery_internet_ip
        # The ID of the second vSwitch associated with the VPN gateway.
        # 
        # This parameter is returned only when the VPN gateway supports the dual-tunnel mode.
        self.disaster_recovery_vswitch_id = disaster_recovery_vswitch_id
        # Indicates whether BGP is enabled for the VPN gateway. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.enable_bgp = enable_bgp
        # The time when the VPN gateway expires. Unit: milliseconds.
        # 
        # This value is a UNIX timestamp representing the number of milliseconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC.
        self.end_time = end_time
        # *   If the VPN gateway supports IPsec-VPN connections in single-tunnel mode, the address is the IP address of the VPN gateway and can be used to create an IPsec-VPN connection or an SSL-VPN connection.
        # 
        # *   If the VPN gateway supports IPsec-VPN connections in dual-tunnel mode, the address is the first IP address used to create an IPsec-VPN connection. The address cannot be used to create an SSL-VPN connection.
        # 
        #     If the VPN gateway supports IPsec-VPN connections in dual-tunnel mode, the system assigns two IP addresses to the VPN gateway to create two encrypted tunnels.
        self.internet_ip = internet_ip
        # The private IP address of the vSwitch that is used by the system when the VPN gateway is deployed.
        # 
        # The parameter is returned only for VPN gateways that support single-tunnel IPsec-VPN connections. The IPsec-VPN feature must be enabled.
        self.intranet_ip = intranet_ip
        # The name of the VPN gateway.
        self.name = name
        # The request ID.
        self.request_id = request_id
        # The ID of the resource group to which the VPN gateway belongs.
        # 
        # You can call the [ListResourceGroups](https://help.aliyun.com/document_detail/158855.html) operation to query resource groups.
        self.resource_group_id = resource_group_id
        # The maximum bandwidth of the VPN gateway. Unit: Mbit/s.
        self.spec = spec
        # The IP address of the SSL-VPN connection.
        # 
        # This parameter is returned only when the VPN gateway is a public VPN gateway and supports only the single-tunnel mode. In addition, the VPN gateway must have the SSL-VPN feature enabled.
        self.ssl_vpn_internet_ip = ssl_vpn_internet_ip
        # The status of the VPN gateway. Valid values:
        # 
        # *   **init**
        # *   **provisioning**
        # *   **active**
        # *   **updating**
        # *   **deleting**
        self.status = status
        # The ID of the vSwitch associated with the VPN gateway.
        self.v_switch_id = v_switch_id
        # The ID of the VPC to which the VPN gateway belongs.
        self.vpc_id = vpc_id
        # The ID of the VPN gateway.
        self.vpn_gateway_id = vpn_gateway_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_propagate is not None:
            result['AutoPropagate'] = self.auto_propagate

        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.disaster_recovery_internet_ip is not None:
            result['DisasterRecoveryInternetIp'] = self.disaster_recovery_internet_ip

        if self.disaster_recovery_vswitch_id is not None:
            result['DisasterRecoveryVSwitchId'] = self.disaster_recovery_vswitch_id

        if self.enable_bgp is not None:
            result['EnableBgp'] = self.enable_bgp

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip

        if self.name is not None:
            result['Name'] = self.name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.spec is not None:
            result['Spec'] = self.spec

        if self.ssl_vpn_internet_ip is not None:
            result['SslVpnInternetIp'] = self.ssl_vpn_internet_ip

        if self.status is not None:
            result['Status'] = self.status

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpn_gateway_id is not None:
            result['VpnGatewayId'] = self.vpn_gateway_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPropagate') is not None:
            self.auto_propagate = m.get('AutoPropagate')

        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisasterRecoveryInternetIp') is not None:
            self.disaster_recovery_internet_ip = m.get('DisasterRecoveryInternetIp')

        if m.get('DisasterRecoveryVSwitchId') is not None:
            self.disaster_recovery_vswitch_id = m.get('DisasterRecoveryVSwitchId')

        if m.get('EnableBgp') is not None:
            self.enable_bgp = m.get('EnableBgp')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        if m.get('SslVpnInternetIp') is not None:
            self.ssl_vpn_internet_ip = m.get('SslVpnInternetIp')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpnGatewayId') is not None:
            self.vpn_gateway_id = m.get('VpnGatewayId')

        return self

