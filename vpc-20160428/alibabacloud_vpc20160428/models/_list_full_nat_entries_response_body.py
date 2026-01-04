# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class ListFullNatEntriesResponseBody(DaraModel):
    def __init__(
        self,
        full_nat_entries: List[main_models.ListFullNatEntriesResponseBodyFullNatEntries] = None,
        full_nat_table_id: str = None,
        max_results: int = None,
        nat_gateway_id: str = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The information about the FULLNAT entries that are queried.
        self.full_nat_entries = full_nat_entries
        # The ID of the FULLNAT table to which the queried FULLNAT entries belong.
        self.full_nat_table_id = full_nat_table_id
        # The maximum number of entries returned.
        self.max_results = max_results
        # The ID of the VPC NAT gateway.
        self.nat_gateway_id = nat_gateway_id
        # Indicates whether the token for the next query exists. Valid values:
        # 
        # *   If the value of **NextToken** is empty, no next queries are sent.
        # *   If the value of **NextToken** is returned, the value indicates the token that is used for the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The number of FULLNAT entries returned.
        self.total_count = total_count

    def validate(self):
        if self.full_nat_entries:
            for v1 in self.full_nat_entries:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FullNatEntries'] = []
        if self.full_nat_entries is not None:
            for k1 in self.full_nat_entries:
                result['FullNatEntries'].append(k1.to_map() if k1 else None)

        if self.full_nat_table_id is not None:
            result['FullNatTableId'] = self.full_nat_table_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.full_nat_entries = []
        if m.get('FullNatEntries') is not None:
            for k1 in m.get('FullNatEntries'):
                temp_model = main_models.ListFullNatEntriesResponseBodyFullNatEntries()
                self.full_nat_entries.append(temp_model.from_map(k1))

        if m.get('FullNatTableId') is not None:
            self.full_nat_table_id = m.get('FullNatTableId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListFullNatEntriesResponseBodyFullNatEntries(DaraModel):
    def __init__(
        self,
        access_ip: str = None,
        access_port: str = None,
        creation_time: str = None,
        full_nat_entry_description: str = None,
        full_nat_entry_id: str = None,
        full_nat_entry_name: str = None,
        full_nat_entry_status: str = None,
        full_nat_table_id: str = None,
        ip_protocol: str = None,
        nat_ip: str = None,
        nat_ip_port: str = None,
        network_interface_id: str = None,
        network_interface_type: str = None,
    ):
        # The backend IP address that is used for FULLNAT address translation in FULLNAT entries.
        self.access_ip = access_ip
        # The backend port that is used for port mapping in FULLNAT entries. Valid values: **1** to **65535**.
        self.access_port = access_port
        # The time when the FULLNAT entry was created.
        self.creation_time = creation_time
        # The description of the FULLNAT entry.
        # 
        # The name must be 2 to 128 characters in length. It must start with a letter but cannot start with `http://` or `https://`.
        self.full_nat_entry_description = full_nat_entry_description
        # The ID of the FULLNAT entry.
        self.full_nat_entry_id = full_nat_entry_id
        # The name of the FULLNAT entry.
        # 
        # The name must be 2 to 128 characters in length, and can contain letters, digits, underscores (_), and hyphens (-). The name must start with a letter.
        self.full_nat_entry_name = full_nat_entry_name
        # The status of the FULLNAT entry. Valid values:
        # 
        # *   **Pending**
        # *   **Available**
        # *   **Deleting**
        # *   **Deleted**
        self.full_nat_entry_status = full_nat_entry_status
        # The ID of the FULLNAT table to which the FULLNAT entry belongs.
        self.full_nat_table_id = full_nat_table_id
        # The protocol of the packets that are forwarded. Valid values:
        # 
        # *   **TCP**
        # *   **UDP**
        self.ip_protocol = ip_protocol
        # The NAT IP address that is used for address translation in FULLNAT entries.
        self.nat_ip = nat_ip
        # The frontend port that is used for port mapping in FULLNAT entries. Valid values: **1** to **65535**.
        self.nat_ip_port = nat_ip_port
        # The ID of the elastic network interface (ENI).
        self.network_interface_id = network_interface_id
        # The type of the ENI. The value is set to **Endpoint**, which indicates a reverse endpoint.
        self.network_interface_type = network_interface_type

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

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.full_nat_entry_description is not None:
            result['FullNatEntryDescription'] = self.full_nat_entry_description

        if self.full_nat_entry_id is not None:
            result['FullNatEntryId'] = self.full_nat_entry_id

        if self.full_nat_entry_name is not None:
            result['FullNatEntryName'] = self.full_nat_entry_name

        if self.full_nat_entry_status is not None:
            result['FullNatEntryStatus'] = self.full_nat_entry_status

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

        if self.network_interface_type is not None:
            result['NetworkInterfaceType'] = self.network_interface_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessIp') is not None:
            self.access_ip = m.get('AccessIp')

        if m.get('AccessPort') is not None:
            self.access_port = m.get('AccessPort')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('FullNatEntryDescription') is not None:
            self.full_nat_entry_description = m.get('FullNatEntryDescription')

        if m.get('FullNatEntryId') is not None:
            self.full_nat_entry_id = m.get('FullNatEntryId')

        if m.get('FullNatEntryName') is not None:
            self.full_nat_entry_name = m.get('FullNatEntryName')

        if m.get('FullNatEntryStatus') is not None:
            self.full_nat_entry_status = m.get('FullNatEntryStatus')

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

        if m.get('NetworkInterfaceType') is not None:
            self.network_interface_type = m.get('NetworkInterfaceType')

        return self

