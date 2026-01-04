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
        # Specifies whether to enable automatic payment. Default value: true. Valid values:
        # 
        # *   **false**: Automatic payment is disabled. After an order is generated, you must go to the Order Center to complete the payment.
        # *   **true**: Automatic payment is enabled. After an order is generated, the payment is automatically completed.
        # 
        # This parameter is required if **InstanceChargeType** is set to **PrePaid**. This parameter is optional if **InstanceChargeType** is set to **PostPaid**.
        self.auto_pay = auto_pay
        # The maximum bandwidth of the specified EIP. Unit: Mbit/s.
        # 
        # *   When **InstanceChargeType** is set to **PostPaid** and **InternetChargeType** is set to **PayByBandwidth**, valid values for **Bandwidth** are **1** to **500**.
        # *   When **InstanceChargeType** is set to **PostPaid** and **InternetChargeType** is set to **PayByTraffic**, valid values for **Bandwidth** are **1** to **200**.
        # *   When **InstanceChargeType** is set to **PrePaid**, valid values for **Bandwidth** are **1** to **1000**.
        # 
        # Default value: **5** Mbit /s.
        self.bandwidth = bandwidth
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate a token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # The line type. Valid values:
        # 
        # *   **BGP** (default): BGP (Multi-ISP) line The BGP (Multi-ISP) line is supported in all regions.
        # *   **BGP_PRO**: BGP (Multi-ISP) Pro line The BGP (Multi-ISP) Pro line is supported in the China (Hong Kong), Singapore, Malaysia (Kuala Lumpur), Philippines (Manila), Indonesia (Jakarta), and Thailand (Bangkok) regions.
        # 
        # For more information about the BGP (Multi-ISP) line and BGP (Multi-ISP) Pro line, see the "Line types" section of [What is EIP?](https://help.aliyun.com/document_detail/32321.html)
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
        # *   If your services are deployed in China East 1 Finance, this parameter is required and you must set the parameter to **BGP_FinanceCloud**.
        self.isp = isp
        # The billing method of the EIP. Valid values:
        # 
        # *   **PrePaid**: subscription
        # *   **PostPaid** (default): pay-as-you-go
        # 
        # Set the value of **InternetChargeType** to **PayByBandwidth** if **InstanceChargeType** is set to **PrePaid**.
        # 
        # Valid values when **InstanceChargeType** is set to **PostPaid**: **PayByBandwidth** or **PayByTraffic**.
        self.instance_charge_type = instance_charge_type
        # The EIP ID.
        # 
        # Specify **IpAddress** or **InstanceId**. If you leave both parameters empty, the system randomly allocates an EIP.
        self.instance_id = instance_id
        # The metering method of the EIP. Valid values:
        # 
        # *   **PayByBandwidth** (default): pay-by-bandwidth.
        # *   **PayByTraffic**: pay-by-data-transfer.
        # 
        # When **InstanceChargeType** is set to **PrePaid**, you must set **InternetChargeType** to **PayByBandwidth**.
        # 
        # When **InstanceChargeType** is set to **PostPaid**, set **InternetChargeType** to **PayByBandwidth** or **PayByTraffic**.
        self.internet_charge_type = internet_charge_type
        # The IP address of the EIP.
        # 
        # Specify **IpAddress** or **InstanceId**. If you leave both parameters empty, the system randomly allocates an EIP.
        self.ip_address = ip_address
        # The network type. By default, this value is set to **public**, which specifies the public network type.
        self.netmode = netmode
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The subscription duration.
        # 
        # *   Valid values when **PricingCycle** is set to **Month**: **1 to 9**.****
        # *   Valid values when **PricingCycle** is set to **Year**: **1 to 3**.****
        # 
        # This parameter is required if **InstanceChargeType** is set to **PrePaid**.
        # 
        # Leave this parameter empty if **InstanceChargeType** is set to **PostPaid**.
        self.period = period
        # The billing cycle of the subscription EIP. Valid values:
        # 
        # *   **Month** (default)
        # *   **Year**
        # 
        # This parameter is required if **InstanceChargeType** is set to **PrePaid**. This parameter is optional if **InstanceChargeType** is set to **PostPaid**.
        self.pricing_cycle = pricing_cycle
        # The ID of the IP address pool.
        # 
        # The EIP is allocated from the IP address pool.
        # 
        # By default, you cannot use the IP address pool. To use this feature, apply for the privilege in the Quota Center console. For more information, see the "Request a quota increase in the Quota Center console" section of [Manage EIP quotas](https://help.aliyun.com/document_detail/108213.html).
        self.public_ip_address_pool_id = public_ip_address_pool_id
        # The ID of the region to which the EIP belongs.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the EIP belongs.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The editions of Anti-DDoS.
        # 
        # *   If you do not specify this parameter, Anti-DDoS Origin Basic is used.
        # *   If you set the parameter to **AntiDDoS_Enhanced**, Anti-DDoS Pro/Premium is used.
        # 
        # You can configure Anti-DDoS editions for up to 10 EIPs.
        self.security_protection_types = security_protection_types
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

