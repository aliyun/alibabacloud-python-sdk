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
        # Specifies whether to automatically pay the bill for the VPN gateway. Valid values:
        # 
        # - **true**: automatically pays the bill for the VPN gateway.
        # 
        # - **false** (default): does not automatically pay the bill for the VPN gateway.
        # 
        # > To successfully create a VPN gateway instance, enable automatic payment. If you disable automatic payment, you must manually pay the bill to create the VPN gateway instance.
        self.auto_pay = auto_pay
        # The bandwidth specification of the VPN gateway. Unit: Mbit/s.
        # 
        # <props="china">- If you want to create a public VPN gateway, valid values are **5**, **10**, **20**, **50**, **100**, **200**, **500**, and **1000**.
        # <props="china">- If you want to create a private VPN gateway, valid values are **200** and **1000**.
        # <props="intl">- If you want to create a public VPN gateway, valid values are **10**, **100**, **200**, **500**, and **1000**.
        # <props="intl">- If you want to create a private VPN gateway, valid values are **200** and **1000**.
        # 
        # >The maximum bandwidth specification supported by VPN gateways in some regions is 500 Mbit/s. For more information, see [VPN gateway limits](https://help.aliyun.com/document_detail/65290.html).
        # 
        # This parameter is required.
        self.bandwidth = bandwidth
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** may be different for each API request.
        self.client_token = client_token
        # The second vSwitch associated with the VPN VPC-connected instance.
        # 
        # - If the current region supports dual-tunnel IPsec-VPN connections, this parameter is required.
        # - You must specify two vSwitches in different zones within the VPC associated with the VPN VPC-connected instance to implement zone-level disaster recovery for IPsec-VPN connections.
        # - For regions that support only one zone, zone-level disaster recovery is not supported. Specify two different vSwitches in the same zone to achieve high availability for IPsec-VPN connections. You can also specify the same vSwitch.
        # 
        # For information about the regions and zones that support dual-tunnel IPsec-VPN connections, see [Upgrade an IPsec-VPN connection to dual-tunnel mode](https://help.aliyun.com/document_detail/2358946.html).
        self.disaster_recovery_vswitch_id = disaster_recovery_vswitch_id
        # Specifies whether to enable the IPsec-VPN feature. Valid values:
        # 
        # - **true** (default): enables the IPsec-VPN feature.
        # 
        # - **false**: disables the IPsec-VPN feature.
        self.enable_ipsec = enable_ipsec
        # Specifies whether to enable the SSL-VPN feature. Valid values:
        # 
        # - **true**: enables the SSL-VPN feature.
        # 
        # - **false** (default): disables the SSL-VPN feature.
        self.enable_ssl = enable_ssl
        # <props="china">The billing method of the VPN gateway. Set the value to **PREPAY**, which specifies the subscription billing method.
        # <props="intl">The billing method of the VPN gateway. Set the value to **POSTPAY**, which specifies the pay-as-you-go billing method.
        # <props="partner">The billing method of the VPN gateway. Set the value to **POSTPAY**, which specifies the pay-as-you-go billing method.
        # 
        # <props="china">This parameter is required when you create a VPN gateway.
        self.instance_charge_type = instance_charge_type
        # The name of the VPN gateway. The default value is the ID of the VPN gateway.
        # 
        # The name must be 2 to 100 characters in length. It cannot start with `http://` or `https://`. It must start with an uppercase or lowercase letter and can contain uppercase and lowercase letters, digits, underscores (_), hyphens (-), and periods (.). Other special characters are not supported.
        self.name = name
        # The network type of the VPN gateway. Valid values:
        # 
        # - **public** (default): public VPN gateway.
        # - **private**: private VPN gateway.
        self.network_type = network_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The subscription duration. Unit: months. Valid values: **1** to **9**, **12**, **24**, and **36**.
        # 
        # <props="china">
        # > This parameter is required if **InstanceChargeType** is set to **PREPAY**..
        self.period = period
        # The region ID of the VPN gateway. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the VPN gateway belongs.
        # 
        # - You can call the [ListResourceGroups](https://help.aliyun.com/document_detail/158855.html) operation to query resource group IDs.
        # - If you do not specify a resource group ID, the VPN gateway belongs to the default resource group after it is created.
        # - After the VPN gateway is created, if you create SSL servers, SSL client certificates, IPsec servers, or IPsec-VPN connections (when the IPsec-VPN connection is associated with the VPN gateway) under the VPN gateway, these resources belong to the same resource group as the VPN gateway. The resource group of these resources cannot be modified.
        # 
        #   If you change the resource group of the VPN gateway, the resource group of the preceding resources is also changed.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The maximum number of clients that can be simultaneously connected. Valid values: **5** (default), **10**, **20**, **50**, **100**, **200**, **500**, and **1000**.
        self.ssl_connections = ssl_connections
        # The vSwitch associated with the VPN gateway instance. 
        # 
        # - In regions that support dual-tunnel IPsec-VPN connections, this parameter is required. You must specify a vSwitch and also specify the **DisasterRecoveryVSwitchId** parameter.
        # - In regions that support only single-tunnel IPsec-VPN connections, if you do not specify a vSwitch, the system automatically selects a vSwitch from the VPC.
        self.v_switch_id = v_switch_id
        # The ID of the VPC-connected instance to which the VPN gateway belongs.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id
        # The type of the VPN gateway. Valid values:
        # - **Normal** (default): standard.
        # <props="china">- **NationalStandard**: Chinese SM-based..
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

