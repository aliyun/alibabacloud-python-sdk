# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePhysicalConnectionRequest(DaraModel):
    def __init__(
        self,
        access_point_id: str = None,
        circuit_code: str = None,
        client_token: str = None,
        description: str = None,
        line_operator: str = None,
        name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        peer_location: str = None,
        port_type: str = None,
        redundant_physical_connection_id: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        type: str = None,
        user_cidr: str = None,
        bandwidth: int = None,
    ):
        # The access point ID. You can call the `DescribeAccessPoints` operation to obtain a list of available access points.
        # 
        # This parameter is required.
        self.access_point_id = access_point_id
        # The circuit code provided by the carrier.
        self.circuit_code = circuit_code
        # A client-generated token that you can use to ensure the idempotency of the request. This token must be unique across requests, contain only ASCII characters, and be no more than 64 characters long.
        self.client_token = client_token
        # The description of the physical connection. The description must be 2 to 256 characters long and cannot start with `http://` or `https://`.
        self.description = description
        # The carrier that provides the physical connection. Valid values: `CT` (China Telecom), `CU` (China Unicom), `CM` (China Mobile), `CO` (other Chinese carriers), and `AL` (Alibaba Cloud).
        # 
        # This parameter is required.
        self.line_operator = line_operator
        # The name of the physical connection. The name must be 2 to 128 characters long. It must start with a letter and can contain letters, digits, underscores (`_`), and hyphens (`-`).
        self.name = name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The physical location of your on-premises data center.
        # 
        # This parameter is required.
        self.peer_location = peer_location
        # The port type of the physical connection. You cannot change this parameter after the physical connection is created. Valid values: `1000Base-LX` (1 Gbit/s), `10GBase-LR` (10 Gbit/s), and `40GBase-LR` (40 Gbit/s).
        self.port_type = port_type
        # The ID of the redundant physical connection. The redundant physical connection must be in the `Allocated`, `Confirmed`, or `Enabled` state.
        self.redundant_physical_connection_id = redundant_physical_connection_id
        # The ID of the region for the physical connection. You can call the `DescribeRegions` operation to obtain the latest list of regions.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The type of the physical connection. Valid values: `VPC` and `VBR`. The default value is `VPC`. This parameter is available only to whitelisted users.
        self.type = type
        # The user CIDR block. This parameter is required when `Type` is set to `VPC`. The CIDR block must be a private IPv4 block. Valid CIDR blocks include the following blocks and their subnets: `10.0.0.0/8`, `172.16.0.0/12`, and `192.168.0.0/16`.
        self.user_cidr = user_cidr
        # The bandwidth of the physical connection in Mbit/s. The value must be an integer that ranges from 1 to 10,240.
        self.bandwidth = bandwidth

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_point_id is not None:
            result['AccessPointId'] = self.access_point_id

        if self.circuit_code is not None:
            result['CircuitCode'] = self.circuit_code

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.line_operator is not None:
            result['LineOperator'] = self.line_operator

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.peer_location is not None:
            result['PeerLocation'] = self.peer_location

        if self.port_type is not None:
            result['PortType'] = self.port_type

        if self.redundant_physical_connection_id is not None:
            result['RedundantPhysicalConnectionId'] = self.redundant_physical_connection_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.type is not None:
            result['Type'] = self.type

        if self.user_cidr is not None:
            result['UserCidr'] = self.user_cidr

        if self.bandwidth is not None:
            result['bandwidth'] = self.bandwidth

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessPointId') is not None:
            self.access_point_id = m.get('AccessPointId')

        if m.get('CircuitCode') is not None:
            self.circuit_code = m.get('CircuitCode')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('LineOperator') is not None:
            self.line_operator = m.get('LineOperator')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PeerLocation') is not None:
            self.peer_location = m.get('PeerLocation')

        if m.get('PortType') is not None:
            self.port_type = m.get('PortType')

        if m.get('RedundantPhysicalConnectionId') is not None:
            self.redundant_physical_connection_id = m.get('RedundantPhysicalConnectionId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UserCidr') is not None:
            self.user_cidr = m.get('UserCidr')

        if m.get('bandwidth') is not None:
            self.bandwidth = m.get('bandwidth')

        return self

