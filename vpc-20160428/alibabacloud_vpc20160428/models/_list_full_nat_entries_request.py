# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListFullNatEntriesRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        full_nat_entry_id: str = None,
        full_nat_entry_names: List[str] = None,
        full_nat_table_id: str = None,
        ip_protocol: str = None,
        max_results: int = None,
        nat_gateway_id: str = None,
        nat_ip: str = None,
        nat_ip_port: str = None,
        network_interface_ids: List[str] = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # The ID of the FULLNAT entry that you want to query.
        self.full_nat_entry_id = full_nat_entry_id
        # The name of the FULLNAT entry that you want to query. You can specify at most 20 names.
        # 
        # The name must be 2 to 128 characters in length, and can contain letters, digits, underscores (_), and hyphens (-). The name must start with a letter.
        self.full_nat_entry_names = full_nat_entry_names
        # The ID of the FULLNAT table to which the FULLNAT entries to be queried belong.
        # 
        # >  You must specify at least one of **FullNatTableId** and **NatGatewayId**.
        self.full_nat_table_id = full_nat_table_id
        # The protocol of the packets that are forwarded by the port. Valid values:
        # 
        # *   **TCP**
        # *   **UDP**
        self.ip_protocol = ip_protocol
        # The number of entries per page. Valid values: **1** to **100**. Default value: **20**.
        self.max_results = max_results
        # The ID of the NAT gateway.
        # 
        # >  You must specify at least one of **FullNatTableId** and **NatGatewayId**.
        self.nat_gateway_id = nat_gateway_id
        # The NAT IP address that provides address translation in FULLNAT entries.
        self.nat_ip = nat_ip
        # The frontend port to be modified in the mapping of FULLNAT port. Valid values: **1** to **65535**.
        self.nat_ip_port = nat_ip_port
        # The ID of the elastic network interface (ENI) that you want to query.
        self.network_interface_ids = network_interface_ids
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   You do not need to specify this parameter for the first request.
        # *   You must specify the token that is obtained from the previous query as the value of the **NextToken** parameter.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the virtual private cloud (VPC) NAT gateway to which the FULLNAT entries to be queried belong.
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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.full_nat_entry_id is not None:
            result['FullNatEntryId'] = self.full_nat_entry_id

        if self.full_nat_entry_names is not None:
            result['FullNatEntryNames'] = self.full_nat_entry_names

        if self.full_nat_table_id is not None:
            result['FullNatTableId'] = self.full_nat_table_id

        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        if self.nat_ip is not None:
            result['NatIp'] = self.nat_ip

        if self.nat_ip_port is not None:
            result['NatIpPort'] = self.nat_ip_port

        if self.network_interface_ids is not None:
            result['NetworkInterfaceIds'] = self.network_interface_ids

        if self.next_token is not None:
            result['NextToken'] = self.next_token

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
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('FullNatEntryId') is not None:
            self.full_nat_entry_id = m.get('FullNatEntryId')

        if m.get('FullNatEntryNames') is not None:
            self.full_nat_entry_names = m.get('FullNatEntryNames')

        if m.get('FullNatTableId') is not None:
            self.full_nat_table_id = m.get('FullNatTableId')

        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        if m.get('NatIp') is not None:
            self.nat_ip = m.get('NatIp')

        if m.get('NatIpPort') is not None:
            self.nat_ip_port = m.get('NatIpPort')

        if m.get('NetworkInterfaceIds') is not None:
            self.network_interface_ids = m.get('NetworkInterfaceIds')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

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

