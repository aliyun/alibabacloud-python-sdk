# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class AllocateEipAddressProRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        bandwidth: str = None,
        client_token: str = None,
        isp: str = None,
        instance_charge_type: str = None,
        instance_id: str = None,
        internet_charge_type: str = None,
        ip_address: str = None,
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
        tag: List[main_models.AllocateEipAddressProRequestTag] = None,
    ):
        # Specifies whether to enable automatic payment. Valid values:
        # 
        # - **false**: Disables automatic payment. You must go to the Order Center to pay for the order.
        # 
        # - **true**: Enables automatic payment. The payment is completed automatically.
        # 
        # This parameter is required only when **InstanceChargeType** is set to **PrePaid**.
        self.auto_pay = auto_pay
        # The peak bandwidth of the EIP. Unit: Mbps.
        # 
        # - If **InstanceChargeType** is **PostPaid** (pay-as-you-go) and **InternetChargeType** is **PayByBandwidth**, **Bandwidth** can be from **1** to **500**.
        # 
        # - If **InstanceChargeType** is **PostPaid** (pay-as-you-go) and **InternetChargeType** is **PayByTraffic**, **Bandwidth** can be from **1** to **200**.
        # 
        # - If **InstanceChargeType** is **PrePaid** (subscription), **Bandwidth** can be from **1** to **1000**.
        # 
        # Default value: **5**.
        self.bandwidth = bandwidth
        # A token used to ensure the idempotence of the request.
        # 
        # You must ensure that this token is unique across requests. The token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the request as the **ClientToken**. The **RequestId** differs for each API request.
        self.client_token = client_token
        # The line type. Valid values:
        # 
        # - **BGP** (default): BGP (Multi-ISP) line. All regions support EIPs that use BGP (Multi-ISP) lines.
        # 
        # - **BGP_PRO**: BGP (Multi-ISP) Pro line. This line type is available only in the China (Hong Kong), Singapore, Malaysia (Kuala Lumpur), Philippines (Manila), Indonesia (Jakarta), and Thailand (Bangkok) regions.
        # 
        # For more information about BGP (Multi-ISP) and BGP (Multi-ISP) Pro lines, see [EIP line types](https://help.aliyun.com/document_detail/32321.html).
        # 
        # - If your account is on the allowlist for single-ISP bandwidth, you can also select one of the following values:
        # 
        #   - **ChinaTelecom**
        # 
        #   - **ChinaUnicom**
        # 
        #   - **ChinaMobile**
        # 
        #   - **ChinaTelecom_L2**
        # 
        #   - **ChinaUnicom_L2**
        # 
        #   - **ChinaMobile_L2**
        # 
        # - For China (Hangzhou) Finance Cloud users, this parameter is required and must be set to **BGP_FinanceCloud**.
        self.isp = isp
        # The billing method of the EIP. Valid values:
        # 
        # - **PrePaid**: subscription
        # 
        # - **PostPaid** (default): pay-as-you-go
        # 
        # If **InstanceChargeType** is set to **PrePaid**, **InternetChargeType** must be set to **PayByBandwidth**.
        # 
        # If **InstanceChargeType** is set to **PostPaid**, you can set **InternetChargeType** to **PayByBandwidth** or **PayByTraffic**.
        self.instance_charge_type = instance_charge_type
        # The ID of the EIP to be allocated.
        # 
        # You can specify either **IpAddress** or **InstanceId**. If you do not specify either parameter, the system randomly allocates an EIP.
        self.instance_id = instance_id
        # The metering method of the EIP. Valid values:
        # 
        # - **PayByBandwidth** (default): pay-by-bandwidth
        # 
        # - **PayByTraffic**: pay-by-traffic
        # 
        # If **InstanceChargeType** is set to **PrePaid**, **InternetChargeType** must be set to **PayByBandwidth**.
        # 
        # If **InstanceChargeType** is set to **PostPaid**, you can set **InternetChargeType** to **PayByBandwidth** or **PayByTraffic**.
        self.internet_charge_type = internet_charge_type
        # The IP address of the EIP to be allocated.
        # 
        # You can specify either **IpAddress** or **InstanceId**. If you do not specify either parameter, the system randomly allocates an EIP.
        self.ip_address = ip_address
        # The network type. The only valid value is **public** (default), which indicates the public network.
        self.netmode = netmode
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The subscription period.
        # 
        # - If **PricingCycle** is **Month**, **Period** can be from **1** to **9**.
        # 
        # - If **PricingCycle** is **Year**, **Period** can be from **1** to **3**.
        # 
        # This parameter is required when **InstanceChargeType** is set to **PrePaid**.
        # 
        # If `InstanceChargeType` is set to `PostPaid`, this parameter is not required.
        self.period = period
        # The billing cycle of the subscription EIP. Valid values:
        # 
        # - **Month** (default): Billed monthly.
        # 
        # - **Year**: Billed annually.
        # 
        # This parameter is required only when **InstanceChargeType** is set to **PrePaid** (subscription).
        self.pricing_cycle = pricing_cycle
        # The ID of the IP address pool from which to allocate the EIP.
        # 
        # This feature is disabled by default. To use this feature, apply for the required permissions in Quota Center. For more information, see [Increase quotas by using Quota Center](https://help.aliyun.com/document_detail/108213.html).
        self.public_ip_address_pool_id = public_ip_address_pool_id
        # The ID of the region where the EIP is to be allocated.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group for the EIP.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The security protection level.
        # 
        # - If you do not specify this parameter, DDoS Protection (Basic) is enabled by default.
        # 
        # - Set the value to **AntiDDoS_Enhanced** to enable DDoS Protection (Enhanced).
        self.security_protection_types = security_protection_types
        # The tags to add to the EIP.
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
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

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
                temp_model = main_models.AllocateEipAddressProRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class AllocateEipAddressProRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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

