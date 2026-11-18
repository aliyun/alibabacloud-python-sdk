# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSnatEntryRequest(DaraModel):
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
        snat_entry_name: str = None,
        snat_ip: str = None,
        snat_table_id: str = None,
        source_cidr: str = None,
        source_vswitch_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among different requests. The `ClientToken` parameter can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** of each API request may be different.
        self.client_token = client_token
        # Specifies whether to perform a dry run on the request. Valid values:
        # 
        # - **true**: performs a dry run on the request without creating the SNAT entry. The system checks whether your AccessKey pair is valid, the authorization of the Resource Access Management (RAM) user, and whether the required parameters are specified. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # 
        # - **false** (default): sends a normal request. If the request passes the dry run, a 2xx HTTP status code is returned and the SNAT entry is created.
        self.dry_run = dry_run
        # Specifies whether to enable EIP affinity. Valid values:
        # 
        # - **0** (default): disables EIP affinity.
        # 
        # - **1**: enables EIP affinity.
        # 
        # > After you enable EIP affinity, if the SNAT entry is associated with multiple EIPs or NAT IP addresses, the same EIP or NAT IP address is used when the same client accesses the same destination IP address. Otherwise, the client randomly selects an EIP or NAT IP address from the associated EIPs or NAT IP addresses.
        self.eip_affinity = eip_affinity
        # The ID of the network interface controller (NIC).
        # 
        # > The IPv4 addresses of the network interface controller (NIC) are used as the SNAT addresses.
        self.network_interface_id = network_interface_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where the NAT gateway is deployed. 
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query region IDs.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The name of the SNAT entry.
        # 
        # The name must be 2 to 128 characters in length, and must start with a letter or a Chinese character. It cannot start with `http://` or `https://`.
        self.snat_entry_name = snat_entry_name
        # When you add an SNAT entry to an Internet NAT gateway:
        # * The SnatIp parameter is required.
        # 
        # * This parameter specifies the EIPs in the SNAT entry. Separate multiple EIPs with commas (,).
        # 
        # * If SnatIp specifies only one public IP address, the ECS instance uses the specified public IP address to access the Internet.
        # 
        # * If SnatIp specifies multiple public IP addresses, the ECS instance randomly uses one of the public IP addresses in SnatIp to access the Internet.
        # 
        # > When you specify multiple EIPs to configure an SNAT IP address pool, service connections are allocated to the multiple EIPs through a hash algorithm. Because service traffic of each connection is different, service traffic of the multiple EIPs may be uneven. Add all EIPs to the same Internet Shared Bandwidth to prevent service interruptions caused by the bandwidth limit of a single EIP.
        # 
        # When you add an SNAT entry to a VPC NAT gateway:
        # 
        # * This parameter specifies the NAT IP addresses in the SNAT entry. Separate multiple NAT IP addresses with commas (,).
        # 
        # * You must specify either SnatIp or NetworkInterfaceId.
        self.snat_ip = snat_ip
        # The ID of the SNAT table.
        # 
        # This parameter is required.
        self.snat_table_id = snat_table_id
        # The CIDR block of the VPC, vSwitch, or ECS instance. You can also specify a custom CIDR block.
        # 
        # SNAT entries support the following granularities: 
        # 
        # - VPC granularity: the CIDR block of the VPC where the NAT gateway is deployed. All ECS instances in the VPC can access the Internet or external networks through SNAT rules.
        # 
        # - vSwitch granularity: the CIDR block of a specified vSwitch, such as 192.168.1.0/24. All ECS instances in the vSwitch can access the Internet or external networks through SNAT rules.
        # 
        # - ECS instance granularity: the IP address of a specified ECS instance, such as 192.168.1.1/32. The ECS instance can access the Internet or external networks through SNAT rules.
        # 
        # - Custom CIDR block: all ECS instances within the specified CIDR block can access the Internet or external networks through SNAT rules.
        # 
        # > You must specify either the **SourceCIDR** parameter or the **SourceVSwtichId** parameter.
        self.source_cidr = source_cidr
        # The ID of the vSwitch.
        # 
        # * When you add an SNAT entry to an Internet NAT gateway, this parameter specifies that all ECS instances in the vSwitch can access the Internet through SNAT rules. When you specify multiple EIPs to configure an SNAT IP address pool, service connections are allocated to the multiple EIPs through a hash algorithm. Because service traffic of each connection is different, service traffic of the multiple EIPs may be uneven. Add all EIPs to the same Internet Shared Bandwidth to prevent service interruptions caused by the bandwidth limit of a single EIP.
        # 
        # * When you add an SNAT entry to a VPC NAT gateway, this parameter specifies that all ECS instances in the vSwitch can access external networks through SNAT rules.
        # 
        # > You must specify either the **SourceCIDR** parameter or the **SourceVSwtichId** parameter.
        self.source_vswitch_id = source_vswitch_id

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

        if self.snat_entry_name is not None:
            result['SnatEntryName'] = self.snat_entry_name

        if self.snat_ip is not None:
            result['SnatIp'] = self.snat_ip

        if self.snat_table_id is not None:
            result['SnatTableId'] = self.snat_table_id

        if self.source_cidr is not None:
            result['SourceCIDR'] = self.source_cidr

        if self.source_vswitch_id is not None:
            result['SourceVSwitchId'] = self.source_vswitch_id

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

        if m.get('SnatEntryName') is not None:
            self.snat_entry_name = m.get('SnatEntryName')

        if m.get('SnatIp') is not None:
            self.snat_ip = m.get('SnatIp')

        if m.get('SnatTableId') is not None:
            self.snat_table_id = m.get('SnatTableId')

        if m.get('SourceCIDR') is not None:
            self.source_cidr = m.get('SourceCIDR')

        if m.get('SourceVSwitchId') is not None:
            self.source_vswitch_id = m.get('SourceVSwitchId')

        return self

