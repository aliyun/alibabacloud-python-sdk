# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AllocateEipSegmentAddressRequest(DaraModel):
    def __init__(
        self,
        bandwidth: str = None,
        client_token: str = None,
        eip_mask: str = None,
        internet_charge_type: str = None,
        isp: str = None,
        netmode: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        zone: str = None,
    ):
        # The maximum bandwidth of the contiguous EIP group. Unit: Mbit/s.
        # 
        # *   Valid values when **InstanceChargeType** is set to **PostPaid** and **InternetChargeType** is set to **PayByBandwidth**: **1** to **500**.****
        # *   Valid values when **InstanceChargeType** is set to **PostPaid** and **InternetChargeType** is set to **PayByTraffic**: **1** to **200**.****
        # *   Valid values when **InstanceChargeType** is set to **PrePaid**: **1** to **1000**.****
        # 
        # Default value: **5**. Unit: Mbit/s.
        self.bandwidth = bandwidth
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate a token, but you must make sure that the token is unique among different requests. **ClientToken** can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # The subnet mask of the contiguous EIP group. Valid values:
        # 
        # *   **28**: applies for 16 contiguous EIPs in each call.
        # *   **27**: applies for 32 contiguous EIPs in each call.
        # *   **26**: applies for 64 contiguous EIPs in each call.
        # *   **25**: applies for 128 contiguous EIPs in each call.
        # *   **24**: applies for 256 contiguous EIPs in each call.
        # 
        # >  Some IP address are reserved for specific purposes. Therefore, the actual number of the contiguous EIPs may be one, three, or four less than the expected number.
        # 
        # This parameter is required.
        self.eip_mask = eip_mask
        # The metering method of contiguous EIPs. Valid values:
        # 
        # *   **PayByBandwidth** (default)
        # *   **PayByTraffic**
        self.internet_charge_type = internet_charge_type
        # The line type. Valid values:
        # 
        # *   **BGP** (default): BGP (Multi-ISP) line The BGP (Multi-ISP) line is supported in all regions.
        # *   **BGP_PRO**: BGP (Multi-ISP) Pro line BGP (Multi-ISP) Pro line is supported only in the China (Hong Kong), Singapore, Japan (Tokyo), Malaysia (Kuala Lumpur), Philippines (Manila), Indonesia (Jakarta), and Thailand (Bangkok) regions.
        # 
        # For more information about the BGP (Multi-ISP) line and BGP (Multi-ISP) Pro line, see [EIP line types](https://help.aliyun.com/document_detail/32321.html).
        # 
        # If you are allowed to use single-ISP bandwidth, you can also use one of the following values:
        # 
        # *   **ChinaTelecom**
        # *   **ChinaUnicom**
        # *   **ChinaMobile**
        # *   **ChinaTelecom_L2**
        # *   **ChinaUnicom_L2**
        # *   **ChinaMobile_L2**
        # 
        # If your services are deployed in China East 1 Finance, this parameter is required and you must set the parameter to **BGP_FinanceCloud**.
        self.isp = isp
        # The network type. Set the value to **public**, which specifies the public network type.
        self.netmode = netmode
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region in which the contiguous EIP group resides.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The zone of the contiguous EIP group.
        self.zone = zone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.eip_mask is not None:
            result['EipMask'] = self.eip_mask

        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type

        if self.isp is not None:
            result['Isp'] = self.isp

        if self.netmode is not None:
            result['Netmode'] = self.netmode

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.zone is not None:
            result['Zone'] = self.zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('EipMask') is not None:
            self.eip_mask = m.get('EipMask')

        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')

        if m.get('Isp') is not None:
            self.isp = m.get('Isp')

        if m.get('Netmode') is not None:
            self.netmode = m.get('Netmode')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Zone') is not None:
            self.zone = m.get('Zone')

        return self

