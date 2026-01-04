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
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The `client token` can contain only ASCII characters.
        # 
        # **
        # 
        # **Description** If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        self.dry_run = dry_run
        # Specifies whether to enable EIP affinity. Valid values:
        # 
        # *   **0**: no
        # *   **1**: yes
        # 
        # **
        # 
        # **Description** After you enable EIP affinity, if multiple EIPs are associated with an SNAT entry, each client uses one EIP to access the Internet. If EIP affinity is disabled, each client uses a random EIP to access the Internet.
        self.eip_affinity = eip_affinity
        self.network_interface_id = network_interface_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the NAT gateway.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # Valid values:
        # 
        # *   ap-northeast-2-pop
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     ap-northeast-2-pop
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The name of the SNAT entry.
        # 
        # The name must be 2 to 128 characters in length. It must start with a letter but cannot start with `http://` or `https://`.
        self.snat_entry_name = snat_entry_name
        # *   The EIPs in the SNAT entry when you add an SNAT entry to an Internet NAT gateway. Separate EIPs with commas (,).
        # 
        # >  If you specify multiple EIPs in the SNAT IP address pool, the service connection is allocated to multiple EIPs by using the hashing algorithm. The traffic of each EIP may be different. Therefore, we recommend that you associate the EIPs with an Internet Shared Bandwidth instance to prevent service interruptions caused by bandwidth exhaustion.
        # 
        # *   When you add SNAT entries for a VPC NAT gateway, this parameter specifies the NAT IP addresses in the SNAT entry. Separate multiple NAT IP addresses with commas (,).
        self.snat_ip = snat_ip
        # The ID of the SNAT table.
        # 
        # This parameter is required.
        self.snat_table_id = snat_table_id
        # You can specify the CIDR block of a VPC, a vSwitch, or an ECS instance or enter a custom CIDR block.
        # 
        # You can specify an SNAT entry in the following ways:
        # 
        # *   You can specify the CIDR block of the VPC where the NAT gateway is deployed. Then, all ECS instances in the VPC can access the Internet or external networks by using SNAT.
        # *   You can specify the CIDR block of a vSwitch, for example, 192.168.1.0/24. Then, the ECS instances in the vSwitch can access the Internet or external networks by using SNAT.
        # *   You can specify the IP address of an ECS instance, for example, 192.168.1.1/32. Then, the ECS instance can access the Internet or external networks by using SNAT.
        # *   You can specify a custom CIDR block. Then, all ECS instances within the specified CIDR block can access the Internet or external networks by using SNAT.
        # 
        # When you add an SNAT entry to an Internet NAT gateway, if **SnatIp** is set to an EIP, the ECS instance uses the specified EIP to access the Internet.
        # 
        # If **SnatIp** is set to multiple EIPs, the ECS instance randomly selects an EIP specified in the **SnatIp** parameter to access the Internet.
        # 
        # You cannot specify this parameter and **SourceVSwtichId** at the same time. If **SourceVSwitchId** is specified, you cannot specify **SourceCIDR**. If **SourceCIDR** is specified, you cannot specify **SourceVSwitchId**.
        self.source_cidr = source_cidr
        # The ID of the vSwitch.
        # 
        # *   When you add an SNAT entry to an Internet NAT gateway, this parameter specifies that ECS instances in the vSwitch can use the SNAT entry to access the Internet. If you select multiple elastic IP addresses (EIPs) to create an SNAT address pool, connections are hashed to these EIPs. Network traffic may not be evenly distributed to the EIPs because the amount of traffic that passes through each connection varies. We recommend that you associate these EIPs with the same EIP bandwidth plan to prevent service interruptions due to the bandwidth limits on individual EIPs.
        # *   When you add an SNAT entry to a VPC NAT gateway, this parameter specifies that ECS instances in the vSwitch can use the SNAT entry to access external networks.
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

