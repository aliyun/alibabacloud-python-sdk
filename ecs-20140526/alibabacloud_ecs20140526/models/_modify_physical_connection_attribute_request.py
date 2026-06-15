# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyPhysicalConnectionAttributeRequest(DaraModel):
    def __init__(
        self,
        circuit_code: str = None,
        client_token: str = None,
        description: str = None,
        line_operator: str = None,
        name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        peer_location: str = None,
        physical_connection_id: str = None,
        port_type: str = None,
        redundant_physical_connection_id: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        user_cidr: str = None,
        bandwidth: int = None,
    ):
        # The circuit code of the physical connection, provided by the line operator.
        self.circuit_code = circuit_code
        # A client-generated token to ensure the idempotency of the request.
        # 
        # The token must be unique across requests. The client token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The new description of the physical connection.
        self.description = description
        # The line operator that provides the physical connection.
        self.line_operator = line_operator
        # The new name of the physical connection.
        self.name = name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The peer location of the physical connection.
        self.peer_location = peer_location
        # The ID of the physical connection.
        # 
        # This parameter is required.
        self.physical_connection_id = physical_connection_id
        # The port type of the physical connection.
        self.port_type = port_type
        # The ID of the redundant physical connection.
        self.redundant_physical_connection_id = redundant_physical_connection_id
        # The ID of the region where the physical connection is located.
        # 
        # To get the latest list of regions, call the `DescribeRegions` operation.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The client-side IP address or CIDR block in your data center.
        # 
        # This parameter is used only for outbound traffic shaping.
        self.user_cidr = user_cidr
        # The bandwidth of the physical connection.
        # 
        # Unit: Mbit/s.
        self.bandwidth = bandwidth

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.physical_connection_id is not None:
            result['PhysicalConnectionId'] = self.physical_connection_id

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

        if self.user_cidr is not None:
            result['UserCidr'] = self.user_cidr

        if self.bandwidth is not None:
            result['bandwidth'] = self.bandwidth

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('PhysicalConnectionId') is not None:
            self.physical_connection_id = m.get('PhysicalConnectionId')

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

        if m.get('UserCidr') is not None:
            self.user_cidr = m.get('UserCidr')

        if m.get('bandwidth') is not None:
            self.bandwidth = m.get('bandwidth')

        return self

