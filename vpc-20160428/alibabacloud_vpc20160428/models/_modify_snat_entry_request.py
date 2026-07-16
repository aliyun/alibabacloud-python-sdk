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
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The ClientToken value can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** may differ for each API request.
        self.client_token = client_token
        # Specifies whether to perform a dry run. Valid values:
        # 
        # - **true**: performs a dry run without modifying the SNAT entry. The system checks the required parameters, request format, and service limits. If the check fails, the corresponding error is returned. If the check succeeds, the `DryRunOperation` error code is returned.
        # 
        # - **false** (default): performs a dry run and sends the request. After the check succeeds, a 2xx HTTP status code is returned and the SNAT entry is modified.
        self.dry_run = dry_run
        # Specifies whether to enable EIP affinity. Valid values:
        # 
        # - **0**: disables EIP affinity.
        # 
        # - **1**: enables EIP affinity.
        # 
        # > After you enable EIP affinity, if the SNAT entry is associated with multiple EIPs or NAT IP addresses, the same client uses the same EIP or NAT IP address for access. Otherwise, the client randomly selects an EIP or NAT IP address from the associated ones for access.
        self.eip_affinity = eip_affinity
        # The ID of the elastic network interfaces (ENIs).
        # 
        # > The IPv4 addresses of the network interface controller (NIC) are used as the SNAT addresses.
        self.network_interface_id = network_interface_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the NAT gateway.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the region ID.
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
        # The name must be 2 to 128 characters in length and must start with a letter or a Chinese character. It cannot start with `http://` or `https://`.
        self.snat_entry_name = snat_entry_name
        # - When you modify an SNAT entry for an Internet NAT gateway, this parameter specifies the EIPs in the SNAT entry. Separate multiple EIPs with commas (,).
        #  
        # > When you specify multiple EIPs to allocate an SNAT IP IPAM pool, service traffic is distributed across the EIPs by using a hash algorithm. Because traffic varies across connections, service traffic may be unevenly distributed across the EIPs. Add all EIPs to the same Internet Shared Bandwidth instance to prevent service interruptions caused by bandwidth throttling on a single EIP.
        # 
        # - When you modify an SNAT entry for a VPC NAT gateway, this parameter specifies the NAT IP addresses in the SNAT entry. Separate multiple NAT IP addresses with commas (,).
        # 
        # - The SnatIp and NetworkInterfaceId parameters cannot be specified at the same time.
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

