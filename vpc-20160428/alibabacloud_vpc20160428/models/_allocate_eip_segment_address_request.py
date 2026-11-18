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
        # The peak bandwidth of the EIP. Unit: Mbit/s.
        # 
        # - If **InternetChargeType** is set to **PayByBandwidth**, the valid values for **Bandwidth** are **1** to **500**.
        # 
        # - If **InternetChargeType** is set to **PayByTraffic**, the valid values for **Bandwidth** are **1** to **200**.
        # 
        # Default value: **5** Mbit/s.
        self.bandwidth = bandwidth
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can generate a parameter value from your client to ensure that the value is unique among different requests. **ClientToken** only supports ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** of each API request is different.
        self.client_token = client_token
        # The subnet mask of the contiguous EIPs. Valid values:
        # 
        # - **28**: The system allocates 16 contiguous EIPs per call.
        # 
        # - **27**: The system allocates 32 contiguous EIPs per call.
        # 
        # - **26**: The system allocates 64 contiguous EIPs per call.
        # 
        # - **25**: The system allocates 128 contiguous EIPs per call.
        # 
        # - **24**: The system allocates 256 contiguous EIPs per call.
        # 
        # > Due to IP address reservation, the actual number of contiguous EIPs allocated may be 1, 3, or 4 fewer than expected.
        # 
        # This parameter is required.
        self.eip_mask = eip_mask
        # The billing method of the contiguous EIPs. Valid values:
        # 
        # - **PayByBandwidth** (default): pay-by-bandwidth.
        # 
        # - **PayByTraffic**: pay-by-data-transfer.
        self.internet_charge_type = internet_charge_type
        # The line type. Valid values:
        # 
        # - **BGP** (default): BGP (Multi-ISP) line. BGP (Multi-ISP) EIPs are supported in all regions.
        # - **BGP_PRO**: BGP (Multi-ISP) Pro line. BGP (Multi-ISP) Pro EIPs are supported only in the Hong Kong (China), Singapore, Japan (Tokyo), Malaysia (Kuala Lumpur), Philippines (Manila), Indonesia (Jakarta), and Thailand (Bangkok) regions.
        # 
        # For more information about BGP (Multi-ISP) and BGP (Multi-ISP) Pro lines, see [EIP line types](https://help.aliyun.com/document_detail/32321.html).
        # 
        # If you are a single-ISP bandwidth whitelist user, you can also select the following types:
        # - **ChinaTelecom**: China Telecom
        # - **ChinaUnicom**: China Unicom
        # - **ChinaMobile**: China Mobile
        # - **ChinaTelecom_L2**: China Telecom L2
        # - **ChinaUnicom_L2**: China Unicom L2
        # - **ChinaMobile_L2**: China Mobile L2
        # 
        # If you are an Alibaba Finance Cloud user in the China (Hangzhou) region, this parameter is required. Set the value to **BGP_FinanceCloud**.
        self.isp = isp
        # The network type. Set the value to **public**, which indicates the Internet.
        self.netmode = netmode
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the contiguous EIPs.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query region IDs.
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

