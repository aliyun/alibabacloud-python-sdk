# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class DescribePublishedRouteEntriesResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        published_route_entries: main_models.DescribePublishedRouteEntriesResponseBodyPublishedRouteEntries = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # A list of routes.
        self.published_route_entries = published_route_entries
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.published_route_entries:
            self.published_route_entries.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.published_route_entries is not None:
            result['PublishedRouteEntries'] = self.published_route_entries.to_map()

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

        if m.get('PublishedRouteEntries') is not None:
            temp_model = main_models.DescribePublishedRouteEntriesResponseBodyPublishedRouteEntries()
            self.published_route_entries = temp_model.from_map(m.get('PublishedRouteEntries'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribePublishedRouteEntriesResponseBodyPublishedRouteEntries(DaraModel):
    def __init__(
        self,
        published_route_entry: List[main_models.DescribePublishedRouteEntriesResponseBodyPublishedRouteEntriesPublishedRouteEntry] = None,
    ):
        self.published_route_entry = published_route_entry

    def validate(self):
        if self.published_route_entry:
            for v1 in self.published_route_entry:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PublishedRouteEntry'] = []
        if self.published_route_entry is not None:
            for k1 in self.published_route_entry:
                result['PublishedRouteEntry'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.published_route_entry = []
        if m.get('PublishedRouteEntry') is not None:
            for k1 in m.get('PublishedRouteEntry'):
                temp_model = main_models.DescribePublishedRouteEntriesResponseBodyPublishedRouteEntriesPublishedRouteEntry()
                self.published_route_entry.append(temp_model.from_map(k1))

        return self

class DescribePublishedRouteEntriesResponseBodyPublishedRouteEntriesPublishedRouteEntry(DaraModel):
    def __init__(
        self,
        child_instance_route_table_id: str = None,
        conflicts: main_models.DescribePublishedRouteEntriesResponseBodyPublishedRouteEntriesPublishedRouteEntryConflicts = None,
        destination_cidr_block: str = None,
        next_hop_id: str = None,
        next_hop_type: str = None,
        operational_mode: bool = None,
        publish_status: str = None,
        route_type: str = None,
    ):
        # The ID of the route table configured on the network instance.
        self.child_instance_route_table_id = child_instance_route_table_id
        # A list of conflicting routes.
        self.conflicts = conflicts
        # The destination CIDR block of the route.
        self.destination_cidr_block = destination_cidr_block
        # The ID of the instance specified as the next hop in the route.
        self.next_hop_id = next_hop_id
        # The type of the instance specified as the next hop in the route.
        # 
        # *   **Instance**: ECS instance
        # *   **HaVip**: high-availability virtual IP address (HAVIP).
        # *   **RouterInterface**: router interface.
        # *   **NetworkInterface**: elastic network interface (ENI).
        # *   **VpnGateway**: VPN gateway.
        # *   **IPv6Gateway**: IPv6 gateway.
        # *   **NatGateway**: NAT gateway.
        # *   **Attachment**: network instance connection
        # *   **service**: cloud service
        # *   **VBR**: VBR
        # *   **CCN**: CCN instance
        # *   **VPC**: VPC
        # *   **local**: system route. No next hop is specified.
        # *   **TR**: transit router
        # *   **BlackHole**: blackhole route. No next hop is specified.
        # *   **EcRouterInterface**: router interface for Express Connect
        # *   **HealthCheck**: health check
        # *   **AS**: access gateway for CCN
        # *   **classicLink**: classic network-type instance
        # *   **GatewayEndpoint**: gateway endpoint
        # *   **CPE**: data center connected to the VBR
        self.next_hop_type = next_hop_type
        # Indicates whether the route is allowed to be advertised to or withdrawn from the CEN instance. Valid values:
        # 
        # *   **true**: The route is allowed to be advertised to or withdrawn from the CEN instance.
        # *   **false**: The route is not allowed to be advertised to or withdrawn from the CEN instance.
        self.operational_mode = operational_mode
        # Indicates whether the route is advertised to the CEN instance. Valid values:
        # 
        # *   **Published**: The route is advertised to the CEN instance.
        # *   **NonPublished**: The route is not advertised to the CEN instance.
        self.publish_status = publish_status
        # The type of the route. Valid values:
        # 
        # *   **CEN**: route that is advertised through CEN
        # *   **System**: system route
        # *   **Custom**: custom route
        self.route_type = route_type

    def validate(self):
        if self.conflicts:
            self.conflicts.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.child_instance_route_table_id is not None:
            result['ChildInstanceRouteTableId'] = self.child_instance_route_table_id

        if self.conflicts is not None:
            result['Conflicts'] = self.conflicts.to_map()

        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block

        if self.next_hop_id is not None:
            result['NextHopId'] = self.next_hop_id

        if self.next_hop_type is not None:
            result['NextHopType'] = self.next_hop_type

        if self.operational_mode is not None:
            result['OperationalMode'] = self.operational_mode

        if self.publish_status is not None:
            result['PublishStatus'] = self.publish_status

        if self.route_type is not None:
            result['RouteType'] = self.route_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChildInstanceRouteTableId') is not None:
            self.child_instance_route_table_id = m.get('ChildInstanceRouteTableId')

        if m.get('Conflicts') is not None:
            temp_model = main_models.DescribePublishedRouteEntriesResponseBodyPublishedRouteEntriesPublishedRouteEntryConflicts()
            self.conflicts = temp_model.from_map(m.get('Conflicts'))

        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')

        if m.get('NextHopId') is not None:
            self.next_hop_id = m.get('NextHopId')

        if m.get('NextHopType') is not None:
            self.next_hop_type = m.get('NextHopType')

        if m.get('OperationalMode') is not None:
            self.operational_mode = m.get('OperationalMode')

        if m.get('PublishStatus') is not None:
            self.publish_status = m.get('PublishStatus')

        if m.get('RouteType') is not None:
            self.route_type = m.get('RouteType')

        return self

class DescribePublishedRouteEntriesResponseBodyPublishedRouteEntriesPublishedRouteEntryConflicts(DaraModel):
    def __init__(
        self,
        conflict: List[main_models.DescribePublishedRouteEntriesResponseBodyPublishedRouteEntriesPublishedRouteEntryConflictsConflict] = None,
    ):
        self.conflict = conflict

    def validate(self):
        if self.conflict:
            for v1 in self.conflict:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Conflict'] = []
        if self.conflict is not None:
            for k1 in self.conflict:
                result['Conflict'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conflict = []
        if m.get('Conflict') is not None:
            for k1 in m.get('Conflict'):
                temp_model = main_models.DescribePublishedRouteEntriesResponseBodyPublishedRouteEntriesPublishedRouteEntryConflictsConflict()
                self.conflict.append(temp_model.from_map(k1))

        return self

class DescribePublishedRouteEntriesResponseBodyPublishedRouteEntriesPublishedRouteEntryConflictsConflict(DaraModel):
    def __init__(
        self,
        destination_cidr_block: str = None,
        instance_id: str = None,
        instance_type: str = None,
        region_id: str = None,
        status: str = None,
    ):
        # The destination CIDR block of the conflicting route.
        self.destination_cidr_block = destination_cidr_block
        # The ID of the peer network instance on which conflicting routes are found.
        self.instance_id = instance_id
        # The type of the peer network instance on which the conflicting routes are found. Valid values:
        # 
        # *   **VPC**: VPC
        # *   **VBR**: VBR
        # *   **CCN**: CCN instance
        self.instance_type = instance_type
        # The ID of the region where the peer network instance on which the conflicting routes are found is deployed.
        self.region_id = region_id
        # The cause of the route confliction. Valid values:
        # 
        # *   **conflict**: The routes have the same destination CIDR block.
        # *   **overflow**: The number of routes in the route table configured on another network instance has reached the upper limit.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

