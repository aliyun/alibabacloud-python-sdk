# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AllocateIpv6InternetBandwidthRequest(DaraModel):
    def __init__(
        self,
        bandwidth: int = None,
        client_token: str = None,
        dry_run: bool = None,
        internet_charge_type: str = None,
        ipv_6address_id: str = None,
        ipv_6gateway_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The Internet bandwidth of the IPv6 address. Unit: Mbit/s.
        # 
        # <props="china">
        # 
        # - If **InternetChargeType** is set to **PayByTraffic**, the valid values are **1** to **1000**.
        # - If **InternetChargeType** is set to **PayByBandwidth**, the valid values are **1** to **2000**.
        # - If **InternetChargeType** is set to **PayByOld95**, the valid values are **1** to **2000**.
        # 
        # 
        # <props="intl">
        #  
        # - If **InternetChargeType** is set to **PayByTraffic**, the valid values are **1** to **1000**.
        # - If **InternetChargeType** is set to **PayByBandwidth**, the valid values are **1** to **2000**.
        # 
        # This parameter is required.
        self.bandwidth = bandwidth
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The ClientToken value can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** may be different for each API request.
        self.client_token = client_token
        # Specifies whether to perform a dry run. Valid values:
        # 
        # - **true**: performs a dry run without associating a prefix list with a route table. The system checks the AccessKey pair, the authorization of the Resource Access Management (RAM) user, and the required parameters. If the check fails, the corresponding error is returned. If the check succeeds, the error code `DryRunOperation` is returned.
        # 
        # - **false** (default): sends a normal request. If the check succeeds, a 2xx HTTP status code is returned and the prefix list is associated with the route table.
        self.dry_run = dry_run
        # The billing method for IPv6 Internet bandwidth. Valid values:
        # 
        # <props="china">
        # 
        # - **PayByTraffic**: pay-by-data-transfer.
        # - **PayByBandwidth** (default): pay-by-bandwidth.
        # - **PayByOld95**: traditional 95th percentile billing. IPv6 Internet bandwidth does not support traditional 95th percentile billing by default. To use this billing method, contact your account manager.
        # 
        # 
        # <props="intl">
        # 
        # - **PayByTraffic**: pay-by-data-transfer.
        # - **PayByBandwidth** (default): pay-by-bandwidth.
        self.internet_charge_type = internet_charge_type
        # The ID of the IPv6 address.
        # 
        # This parameter is required.
        self.ipv_6address_id = ipv_6address_id
        # The ID of the IPv6 gateway.
        self.ipv_6gateway_id = ipv_6gateway_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the IPv6 gateway. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

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

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type

        if self.ipv_6address_id is not None:
            result['Ipv6AddressId'] = self.ipv_6address_id

        if self.ipv_6gateway_id is not None:
            result['Ipv6GatewayId'] = self.ipv_6gateway_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')

        if m.get('Ipv6AddressId') is not None:
            self.ipv_6address_id = m.get('Ipv6AddressId')

        if m.get('Ipv6GatewayId') is not None:
            self.ipv_6gateway_id = m.get('Ipv6GatewayId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

