# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateVpnGatewayRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        bandwidth: int = None,
        client_token: str = None,
        disaster_recovery_vswitch_id: str = None,
        enable_ipsec: bool = None,
        enable_ssl: bool = None,
        instance_charge_type: str = None,
        name: str = None,
        network_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        period: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        ssl_connections: int = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        vpn_type: str = None,
    ):
        # Specifies whether to enable automatic payment. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        # 
        # > To create a VPN gateway, we recommend that you enable automatic payment. If you disable automatic payment, you must manually pay the bill to create the VPN gateway.
        self.auto_pay = auto_pay
        # The maximum bandwidth of the VPN gateway. Unit: Mbit/s.
        # 
        # *   If you want to create a public VPN gateway, valid values are **10**, **100**, **200**, **500**, and **1000**.
        # *   If you want to create a private VPN gateway, valid values are **200** and **1000**.
        # 
        # >  The maximum bandwidth supported by VPN gateways in some regions is 500 Mbit/s. For more information, see [VPN gateway limits](https://help.aliyun.com/document_detail/65290.html).
        # 
        # This parameter is required.
        self.bandwidth = bandwidth
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate a value, and you must make sure that each request has a unique token value. The client token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the value of **RequestId** as the value of **ClientToken**. The value of **RequestId** for each API request is different.
        self.client_token = client_token
        # The second vSwitch with which you want to associate the VPN gateway.
        # 
        # *   If you call this operation in a region that supports the IPsec-VPN connections in dual-tunnel mode, this parameter is required.
        # *   You need to specify two vSwitches in different zones in the virtual private cloud (VPC) that is associated with the VPN gateway to implement disaster recovery across zones.
        # *   For a region that supports only one zone, disaster recovery across zones is not supported. We recommend that you specify two vSwitches in the zone to implement high availability. You can specify the same vSwitch.
        # 
        # For more information about the regions and zones that support the IPsec-VPN connections in dual-tunnel mode, see [IPsec-VPN connections support the dual-tunnel mode](https://help.aliyun.com/document_detail/2358946.html).
        self.disaster_recovery_vswitch_id = disaster_recovery_vswitch_id
        # Specifies whether to enable IPsec-VPN for the VPN gateway. Valid values:
        # 
        # *   **true** (default)
        # *   **false**
        self.enable_ipsec = enable_ipsec
        # Specifies whether to enable SSL-VPN. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        self.enable_ssl = enable_ssl
        # The billing method of the VPN gateway. Set the value to **POSTPAY**, which specifies the pay-as-you-go billing method.
        self.instance_charge_type = instance_charge_type
        # The name of the VPN gateway. The default value is the ID of the VPN gateway.
        # 
        # The name must be 2 to 100 characters in length and cannot start with `http://` or `https://`. It must start with a letter and can contain letters, digits, underscores (_), hyphens (-), and periods (.). Other special characters are not supported.
        self.name = name
        # The network type of the VPN gateway. Valid values:
        # 
        # *   **public** (default)
        # *   **private**
        self.network_type = network_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The subscription duration. Unit: month. Valid values: **1** to **9**, **12**, **24**, and **36**.
        self.period = period
        # The region ID of the VPN gateway. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the VPN gateway belongs.
        # 
        # *   You can call the [ListResourceGroups](https://help.aliyun.com/document_detail/158855.html) operation to query resource group IDs.
        # 
        # *   If you do not specify a resource group ID, the VPN gateway belongs to the default resource group.
        # 
        # *   After the VPN gateway is created, the following resources also belong to the resource group and you cannot change the resource group: SSL servers, SSL client certificates, IPsec servers, and IPsec-VPN connections.
        # 
        #     If you move the VPN gateway to a new resource group, the preceding resources are also moved to the new resource group.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The maximum number of clients that can be connected at the same time. Valid values: **5** (default), **10**, **20**, **50**, **100**, **200**, **500**, and **1000**.
        self.ssl_connections = ssl_connections
        # The vSwitch with which you want to associate the VPN gateway.
        # 
        # *   If you call this operation in a region that supports the IPsec-VPN connections in dual-tunnel mode, this parameter is required. You must specify a vSwitch and specify **DisasterRecoveryVSwitchId**.
        # *   If you call this operation in a region that supports the IPsec-VPN connections in single-tunnel mode and do not specify a vSwitch, the system automatically specifies a vSwitch.
        self.v_switch_id = v_switch_id
        # The ID of the virtual private cloud (VPC) where you want to create the VPN gateway.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id
        # The type of the VPN gateway. Valid values:
        # 
        # Set the value to **Normal** (default), which specifies a standard NAT gateway.
        self.vpn_type = vpn_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.disaster_recovery_vswitch_id is not None:
            result['DisasterRecoveryVSwitchId'] = self.disaster_recovery_vswitch_id

        if self.enable_ipsec is not None:
            result['EnableIpsec'] = self.enable_ipsec

        if self.enable_ssl is not None:
            result['EnableSsl'] = self.enable_ssl

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.name is not None:
            result['Name'] = self.name

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.period is not None:
            result['Period'] = self.period

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.ssl_connections is not None:
            result['SslConnections'] = self.ssl_connections

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpn_type is not None:
            result['VpnType'] = self.vpn_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DisasterRecoveryVSwitchId') is not None:
            self.disaster_recovery_vswitch_id = m.get('DisasterRecoveryVSwitchId')

        if m.get('EnableIpsec') is not None:
            self.enable_ipsec = m.get('EnableIpsec')

        if m.get('EnableSsl') is not None:
            self.enable_ssl = m.get('EnableSsl')

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SslConnections') is not None:
            self.ssl_connections = m.get('SslConnections')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpnType') is not None:
            self.vpn_type = m.get('VpnType')

        return self

