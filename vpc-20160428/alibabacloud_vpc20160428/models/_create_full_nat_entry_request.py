# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateFullNatEntryRequest(DaraModel):
    def __init__(
        self,
        access_ip: str = None,
        access_port: str = None,
        client_token: str = None,
        dry_run: bool = None,
        full_nat_entry_description: str = None,
        full_nat_entry_name: str = None,
        full_nat_table_id: str = None,
        ip_protocol: str = None,
        nat_ip: str = None,
        nat_ip_port: str = None,
        network_interface_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The backend IP address to be modified in FULLNAT address translation.
        # 
        # This parameter is required.
        self.access_ip = access_ip
        # The backend port to be modified in the mapping of FULLNAT port. Valid values: **1** to **65535**.
        # 
        # This parameter is required.
        self.access_port = access_port
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate a value, and you must make sure that each request has a unique token value. The client token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the value of **RequestId** as the value of **ClientToken**. The **request ID** may be different for each request.
        self.client_token = client_token
        # Specifies whether to only precheck this request. Valid values:
        # 
        # *   **true**: prechecks the request without adding the FULLNAT entry. The system checks whether your AccessKey pair is valid, whether RAM users are granted required permissions, and whether the required parameters are set. If the request fails to pass the precheck, an error code is returned. If the request passes the precheck, the `DryRunOperation` error code is returned.
        # *   **false**: sends the API request. This is the default value. After the request passes the precheck, a 2XX HTTP status code is returned and the FULLNAT entry is added.
        self.dry_run = dry_run
        # The description of the FULLNAT entry.
        # 
        # This parameter is optional. If you enter a description, the description must be 2 to 256 characters in length, and cannot start with `http://` or `https://`.
        self.full_nat_entry_description = full_nat_entry_description
        # The FULLNAT entry name. The name must be 2 to 128 characters in length. It must start with a letter but cannot start with http:// or https://.
        self.full_nat_entry_name = full_nat_entry_name
        # The ID of the FULLNAT table to which the FULLNAT entry belongs.
        # 
        # This parameter is required.
        self.full_nat_table_id = full_nat_table_id
        # The protocol of the packets that are forwarded by the port. Valid values:
        # 
        # *   **TCP**
        # *   **UDP**
        # 
        # This parameter is required.
        self.ip_protocol = ip_protocol
        # The NAT IP address that provides address translation.
        # 
        # This parameter is required.
        self.nat_ip = nat_ip
        # The frontend port to be modified in the mapping of FULLNAT port. Valid values: **1** to **65535**.
        self.nat_ip_port = nat_ip_port
        # The elastic network interface (ENI) ID.
        # 
        # This parameter is required.
        self.network_interface_id = network_interface_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the Virtual Private Cloud (VPC) NAT gateway to which the FULLNAT entry to be added belongs.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
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
        if self.access_ip is not None:
            result['AccessIp'] = self.access_ip

        if self.access_port is not None:
            result['AccessPort'] = self.access_port

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.full_nat_entry_description is not None:
            result['FullNatEntryDescription'] = self.full_nat_entry_description

        if self.full_nat_entry_name is not None:
            result['FullNatEntryName'] = self.full_nat_entry_name

        if self.full_nat_table_id is not None:
            result['FullNatTableId'] = self.full_nat_table_id

        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol

        if self.nat_ip is not None:
            result['NatIp'] = self.nat_ip

        if self.nat_ip_port is not None:
            result['NatIpPort'] = self.nat_ip_port

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessIp') is not None:
            self.access_ip = m.get('AccessIp')

        if m.get('AccessPort') is not None:
            self.access_port = m.get('AccessPort')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('FullNatEntryDescription') is not None:
            self.full_nat_entry_description = m.get('FullNatEntryDescription')

        if m.get('FullNatEntryName') is not None:
            self.full_nat_entry_name = m.get('FullNatEntryName')

        if m.get('FullNatTableId') is not None:
            self.full_nat_table_id = m.get('FullNatTableId')

        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')

        if m.get('NatIp') is not None:
            self.nat_ip = m.get('NatIp')

        if m.get('NatIpPort') is not None:
            self.nat_ip_port = m.get('NatIpPort')

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

        return self

