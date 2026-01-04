# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class AllocateEipAddressRequest(DaraModel):
    def __init__(
        self,
        activity_id: int = None,
        auto_pay: bool = None,
        bandwidth: str = None,
        client_token: str = None,
        description: str = None,
        isp: str = None,
        instance_charge_type: str = None,
        instance_id: str = None,
        internet_charge_type: str = None,
        ip_address: str = None,
        name: str = None,
        netmode: str = None,
        owner_account: str = None,
        owner_id: int = None,
        period: int = None,
        pricing_cycle: str = None,
        public_ip_address_pool_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_protection_types: List[str] = None,
        tag: List[main_models.AllocateEipAddressRequestTag] = None,
        zone: str = None,
    ):
        # The promotion code. This parameter is not required.
        self.activity_id = activity_id
        # Specifies whether to enable automatic payment. Valid values:
        # 
        # *   **false** (default): The automatic payment is disabled. If you select this option, you must go to the Order Center to complete the payment after an order is generated.
        # *   **true**: The automatic payment is enabled. Payments are automatically complete after an order is generated.
        # 
        # If **InstanceChargeType** is set to **PrePaid**, this parameter is required. If **InstanceChargeType** is set to **PostPaid**, this parameter is not required.
        self.auto_pay = auto_pay
        # The maximum bandwidth of the EIP. Unit: Mbit/s.
        # 
        # *   Valid values when **InstanceChargeType** is set to **PostPaid** and **InternetChargeType** is set to **PayByBandwidth**: **1** to **500**.****
        # *   Valid values when **InstanceChargeType** is set to **PostPaid** and **InternetChargeType** is set to **PayByTraffic**: **1** to **200**.****
        # *   Valid values when **InstanceChargeType** is set to **PrePaid**: **1** to **1000**.****
        # 
        # Default value: **5**. Unit: Mbit/s.
        self.bandwidth = bandwidth
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate a token, but you must make sure that the token is unique among different requests. The **client token** can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the value of **RequestId** as the **client token**. The value of **RequestId** is different for each API request.
        self.client_token = client_token
        # The description of the EIP.
        # 
        # The description must be 2 to 256 characters in length. The description must start with a letter but cannot start with `http://` or `https://`.
        # 
        # >  You cannot specify this parameter if you create a subscription EIP.
        self.description = description
        # The line type. Valid values:
        # 
        # *   **BGP** (default): BGP (Multi-ISP) All regions support BGP (Multi-ISP) EIPs.
        # *   **BGP_PRO**: BGP (Multi-ISP) Pro Only the following regions support BGP (Multi-ISP) Pro lines: China (Hong Kong), Singapore, Japan (Tokyo), Malaysia (Kuala Lumpur), Philippines (Manila), Indonesia (Jakarta), and Thailand (Bangkok).
        # 
        # For more information about BGP (Multi-ISP) and BGP (Multi-ISP) Pro, see the "Line types" section of [What is EIP?](https://help.aliyun.com/document_detail/32321.html)
        # 
        # *   If you are allowed to use single-ISP bandwidth, you can also choose one of the following values:
        # 
        #     *   **ChinaTelecom**
        #     *   **ChinaUnicom**
        #     *   **ChinaMobile**
        #     *   **ChinaTelecom_L2**
        #     *   **ChinaUnicom_L2**
        #     *   **ChinaMobile_L2**
        # 
        # *   If your services are deployed in China East 1 Finance, this parameter is required and you must set the value to **BGP_FinanceCloud**.
        self.isp = isp
        # The billing method of the EIP. Valid values:
        # 
        # *   **PrePaid**: subscription
        # *   **PostPaid** (default): pay-as-you-go
        # 
        # If **InstanceChargeType** is set to **PrePaid**, set **InternetChargeType** to **PayByBandwidth**. If **InstanceChargeType** is set to **PostPaid**, set **InternetChargeType** to **PayByBandwidth** or **PayByTraffic**.
        self.instance_charge_type = instance_charge_type
        # The EIP ID.
        # 
        # Specify **IpAddress** or **InstanceId**. If you leave both parameters empty, the system randomly allocates an EIP.
        self.instance_id = instance_id
        # The metering method of the EIP. Valid values:
        # 
        # *   **PayByBandwidth** (default): pay-by-bandwidth
        # *   **PayByTraffic**: pay-by-data-transfer
        # 
        # When **InstanceChargeType** is set to **PrePaid**, set **InternetChargeType** to **PayByBandwidth**.
        # 
        # When **InstanceChargeType** is set to **PostPaid**, set **InternetChargeType** to **PayByBandwidth** or **PayByTraffic**.
        self.internet_charge_type = internet_charge_type
        # The IP address of the EIP that you want to request.
        # 
        # Specify **IpAddress** or **InstanceId**. If you leave both parameters empty, the system randomly allocates an EIP.
        self.ip_address = ip_address
        # The EIP name.
        # 
        # The name must be 1 to 128 characters in length and start with a letter, and can contain letters, digits, periods (.), underscores (_), and hyphens (-).
        # 
        # >  You cannot specify this parameter if you create a subscription EIP.
        self.name = name
        # The network type. Default value: **public**.
        self.netmode = netmode
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The subscription duration of the EIP.
        # 
        # Valid values when **PricingCycle** is set to **Month**: **1** to **9**.****
        # 
        # Valid values when **PricingCycle** is set to **Year**: **1** to **5**.****
        # 
        # This parameter must be specified when **InstanceChargeType** is set to **PrePaid**. This parameter is optional when **InstanceChargeType** is set to **PostPaid**.
        self.period = period
        # The billing cycle of the subscription EIP. Valid values:
        # 
        # *   **Month** (default)
        # *   **Year**
        # 
        # If **InstanceChargeType** is set to **PrePaid**, this parameter is required. If **InstanceChargeType** is set to **PostPaid**, this parameter is not required.
        self.pricing_cycle = pricing_cycle
        # The ID of the IP address pool.
        # 
        # The EIP is allocated from the IP address pool.
        # 
        # By default, the IP address pool feature is unavailable. To use the IP address pool, apply for the privilege in the Quota Center console. For more information, see the "Request a quota increase in the Quota Center console" section in [Manage EIP quotas](https://help.aliyun.com/document_detail/108213.html).
        self.public_ip_address_pool_id = public_ip_address_pool_id
        # The ID of the region to which the EIP belongs.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The editions of Anti-DDoS.
        # 
        # *   If you do not specify this parameter, Anti-DDoS Origin Basic is used.
        # *   If you set the parameter to **AntiDDoS_Enhanced**, Anti-DDoS Pro/Premium is used.
        # 
        # You can specify up to 10 editions of Anti-DDoS.
        self.security_protection_types = security_protection_types
        self.tag = tag
        # The zone of the EIP.
        # 
        # When the service type of the IP address pool specified by **PublicIpAddressPoolId** is CloudBox, the default value is the zone of the IP address pool.
        # 
        # For more information, see [ListPublicIpAddressPools](https://help.aliyun.com/document_detail/429433.html).
        self.zone = zone

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
        if self.activity_id is not None:
            result['ActivityId'] = self.activity_id

        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.isp is not None:
            result['ISP'] = self.isp

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type

        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address

        if self.name is not None:
            result['Name'] = self.name

        if self.netmode is not None:
            result['Netmode'] = self.netmode

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.period is not None:
            result['Period'] = self.period

        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle

        if self.public_ip_address_pool_id is not None:
            result['PublicIpAddressPoolId'] = self.public_ip_address_pool_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.security_protection_types is not None:
            result['SecurityProtectionTypes'] = self.security_protection_types

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.zone is not None:
            result['Zone'] = self.zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityId') is not None:
            self.activity_id = m.get('ActivityId')

        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ISP') is not None:
            self.isp = m.get('ISP')

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')

        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Netmode') is not None:
            self.netmode = m.get('Netmode')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')

        if m.get('PublicIpAddressPoolId') is not None:
            self.public_ip_address_pool_id = m.get('PublicIpAddressPoolId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecurityProtectionTypes') is not None:
            self.security_protection_types = m.get('SecurityProtectionTypes')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.AllocateEipAddressRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('Zone') is not None:
            self.zone = m.get('Zone')

        return self



class AllocateEipAddressRequestTag(DaraModel):
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

