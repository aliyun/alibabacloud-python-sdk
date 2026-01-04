# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifySnatEntryRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        eip_affinity: int = None,
        network_interface_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        snat_entry_id: str = None,
        snat_entry_name: str = None,
        snat_ip: str = None,
        snat_table_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        self.dry_run = dry_run
        self.eip_affinity = eip_affinity
        self.network_interface_id = network_interface_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the NAT gateway.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to obtain the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the SNAT entry that you want to modify.
        # 
        # This parameter is required.
        self.snat_entry_id = snat_entry_id
        # The name of the SNAT entry.
        # 
        # The name must be 2 to 128 characters in length. It must start with a letter but cannot start with `http://` or `https://`.
        self.snat_entry_name = snat_entry_name
        # *   The elastic IP addresses (EIPs) specified in the SNAT entry when you modify an SNAT entry of an Internet NAT gateway. Separate EIPs with commas (,).
        # 
        #     If you select multiple EIPs to create an SNAT address pool, connections are hashed to these EIPs. Network traffic may not be evenly distributed to the EIPs because the amount of traffic passes through each connection varies. We recommend that you associate these EIPs with the same EIP bandwidth plan to prevent service interruptions due to the bandwidth limit of an individual EIP.
        # 
        # *   When you modify an SNAT entry of a VPC NAT gateway, this parameter specifies the NAT IP address in the SNAT entry.
        self.snat_ip = snat_ip
        # The ID of the SNAT table to which the SNAT entry belongs.
        # 
        # This parameter is required.
        self.snat_table_id = snat_table_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.eip_affinity is not None:
            result['EipAffinity'] = self.eip_affinity

        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id

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

        if self.snat_entry_id is not None:
            result['SnatEntryId'] = self.snat_entry_id

        if self.snat_entry_name is not None:
            result['SnatEntryName'] = self.snat_entry_name

        if self.snat_ip is not None:
            result['SnatIp'] = self.snat_ip

        if self.snat_table_id is not None:
            result['SnatTableId'] = self.snat_table_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EipAffinity') is not None:
            self.eip_affinity = m.get('EipAffinity')

        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')

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

        if m.get('SnatEntryId') is not None:
            self.snat_entry_id = m.get('SnatEntryId')

        if m.get('SnatEntryName') is not None:
            self.snat_entry_name = m.get('SnatEntryName')

        if m.get('SnatIp') is not None:
            self.snat_ip = m.get('SnatIp')

        if m.get('SnatTableId') is not None:
            self.snat_table_id = m.get('SnatTableId')

        return self

