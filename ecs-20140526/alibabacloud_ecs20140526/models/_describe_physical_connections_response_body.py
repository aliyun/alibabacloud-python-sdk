# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribePhysicalConnectionsResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        physical_connection_set: main_models.DescribePhysicalConnectionsResponseBodyPhysicalConnectionSet = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.physical_connection_set = physical_connection_set
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.physical_connection_set:
            self.physical_connection_set.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.physical_connection_set is not None:
            result['PhysicalConnectionSet'] = self.physical_connection_set.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PhysicalConnectionSet') is not None:
            temp_model = main_models.DescribePhysicalConnectionsResponseBodyPhysicalConnectionSet()
            self.physical_connection_set = temp_model.from_map(m.get('PhysicalConnectionSet'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribePhysicalConnectionsResponseBodyPhysicalConnectionSet(DaraModel):
    def __init__(
        self,
        physical_connection_type: List[main_models.DescribePhysicalConnectionsResponseBodyPhysicalConnectionSetPhysicalConnectionType] = None,
    ):
        self.physical_connection_type = physical_connection_type

    def validate(self):
        if self.physical_connection_type:
            for v1 in self.physical_connection_type:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PhysicalConnectionType'] = []
        if self.physical_connection_type is not None:
            for k1 in self.physical_connection_type:
                result['PhysicalConnectionType'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.physical_connection_type = []
        if m.get('PhysicalConnectionType') is not None:
            for k1 in m.get('PhysicalConnectionType'):
                temp_model = main_models.DescribePhysicalConnectionsResponseBodyPhysicalConnectionSetPhysicalConnectionType()
                self.physical_connection_type.append(temp_model.from_map(k1))

        return self

class DescribePhysicalConnectionsResponseBodyPhysicalConnectionSetPhysicalConnectionType(DaraModel):
    def __init__(
        self,
        access_point_id: str = None,
        ad_location: str = None,
        bandwidth: int = None,
        business_status: str = None,
        circuit_code: str = None,
        creation_time: str = None,
        description: str = None,
        enabled_time: str = None,
        line_operator: str = None,
        name: str = None,
        peer_location: str = None,
        physical_connection_id: str = None,
        port_number: str = None,
        port_type: str = None,
        redundant_physical_connection_id: str = None,
        spec: str = None,
        status: str = None,
        type: str = None,
    ):
        self.access_point_id = access_point_id
        self.ad_location = ad_location
        self.bandwidth = bandwidth
        self.business_status = business_status
        self.circuit_code = circuit_code
        self.creation_time = creation_time
        self.description = description
        self.enabled_time = enabled_time
        self.line_operator = line_operator
        self.name = name
        self.peer_location = peer_location
        self.physical_connection_id = physical_connection_id
        self.port_number = port_number
        self.port_type = port_type
        self.redundant_physical_connection_id = redundant_physical_connection_id
        self.spec = spec
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_point_id is not None:
            result['AccessPointId'] = self.access_point_id

        if self.ad_location is not None:
            result['AdLocation'] = self.ad_location

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status

        if self.circuit_code is not None:
            result['CircuitCode'] = self.circuit_code

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.enabled_time is not None:
            result['EnabledTime'] = self.enabled_time

        if self.line_operator is not None:
            result['LineOperator'] = self.line_operator

        if self.name is not None:
            result['Name'] = self.name

        if self.peer_location is not None:
            result['PeerLocation'] = self.peer_location

        if self.physical_connection_id is not None:
            result['PhysicalConnectionId'] = self.physical_connection_id

        if self.port_number is not None:
            result['PortNumber'] = self.port_number

        if self.port_type is not None:
            result['PortType'] = self.port_type

        if self.redundant_physical_connection_id is not None:
            result['RedundantPhysicalConnectionId'] = self.redundant_physical_connection_id

        if self.spec is not None:
            result['Spec'] = self.spec

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessPointId') is not None:
            self.access_point_id = m.get('AccessPointId')

        if m.get('AdLocation') is not None:
            self.ad_location = m.get('AdLocation')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')

        if m.get('CircuitCode') is not None:
            self.circuit_code = m.get('CircuitCode')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnabledTime') is not None:
            self.enabled_time = m.get('EnabledTime')

        if m.get('LineOperator') is not None:
            self.line_operator = m.get('LineOperator')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PeerLocation') is not None:
            self.peer_location = m.get('PeerLocation')

        if m.get('PhysicalConnectionId') is not None:
            self.physical_connection_id = m.get('PhysicalConnectionId')

        if m.get('PortNumber') is not None:
            self.port_number = m.get('PortNumber')

        if m.get('PortType') is not None:
            self.port_type = m.get('PortType')

        if m.get('RedundantPhysicalConnectionId') is not None:
            self.redundant_physical_connection_id = m.get('RedundantPhysicalConnectionId')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

