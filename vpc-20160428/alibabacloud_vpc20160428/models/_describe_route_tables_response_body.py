# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribeRouteTablesResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        route_tables: main_models.DescribeRouteTablesResponseBodyRouteTables = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The detailed information about the route tables.
        self.route_tables = route_tables
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.route_tables:
            self.route_tables.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.route_tables is not None:
            result['RouteTables'] = self.route_tables.to_map()

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RouteTables') is not None:
            temp_model = main_models.DescribeRouteTablesResponseBodyRouteTables()
            self.route_tables = temp_model.from_map(m.get('RouteTables'))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeRouteTablesResponseBodyRouteTables(DaraModel):
    def __init__(
        self,
        route_table: List[main_models.DescribeRouteTablesResponseBodyRouteTablesRouteTable] = None,
    ):
        self.route_table = route_table

    def validate(self):
        if self.route_table:
            for v1 in self.route_table:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RouteTable'] = []
        if self.route_table is not None:
            for k1 in self.route_table:
                result['RouteTable'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.route_table = []
        if m.get('RouteTable') is not None:
            for k1 in m.get('RouteTable'):
                temp_model = main_models.DescribeRouteTablesResponseBodyRouteTablesRouteTable()
                self.route_table.append(temp_model.from_map(k1))

        return self

class DescribeRouteTablesResponseBodyRouteTablesRouteTable(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        resource_group_id: str = None,
        route_entrys: main_models.DescribeRouteTablesResponseBodyRouteTablesRouteTableRouteEntrys = None,
        route_table_id: str = None,
        route_table_type: str = None,
        status: str = None,
        vrouter_id: str = None,
        v_switch_ids: main_models.DescribeRouteTablesResponseBodyRouteTablesRouteTableVSwitchIds = None,
    ):
        # The time when the route table was created.
        # 
        # The time is displayed in the `YYYY-MM-DDThh:mm:ssZ` format in UTC.
        self.creation_time = creation_time
        # The ID of the resource group to which the route table belongs.
        self.resource_group_id = resource_group_id
        # The information about the route.
        self.route_entrys = route_entrys
        # The ID of the route table.
        self.route_table_id = route_table_id
        # The type of the route table. Valid values:
        # 
        # *   **Custom**
        # *   **System**
        self.route_table_type = route_table_type
        # The status of the route table. Valid values:
        # 
        # *   **Pending**
        # *   **Available**
        self.status = status
        # The vRouter ID.
        self.vrouter_id = vrouter_id
        # The vSwitch ID.
        self.v_switch_ids = v_switch_ids

    def validate(self):
        if self.route_entrys:
            self.route_entrys.validate()
        if self.v_switch_ids:
            self.v_switch_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.route_entrys is not None:
            result['RouteEntrys'] = self.route_entrys.to_map()

        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id

        if self.route_table_type is not None:
            result['RouteTableType'] = self.route_table_type

        if self.status is not None:
            result['Status'] = self.status

        if self.vrouter_id is not None:
            result['VRouterId'] = self.vrouter_id

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('RouteEntrys') is not None:
            temp_model = main_models.DescribeRouteTablesResponseBodyRouteTablesRouteTableRouteEntrys()
            self.route_entrys = temp_model.from_map(m.get('RouteEntrys'))

        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')

        if m.get('RouteTableType') is not None:
            self.route_table_type = m.get('RouteTableType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VRouterId') is not None:
            self.vrouter_id = m.get('VRouterId')

        if m.get('VSwitchIds') is not None:
            temp_model = main_models.DescribeRouteTablesResponseBodyRouteTablesRouteTableVSwitchIds()
            self.v_switch_ids = temp_model.from_map(m.get('VSwitchIds'))

        return self

class DescribeRouteTablesResponseBodyRouteTablesRouteTableVSwitchIds(DaraModel):
    def __init__(
        self,
        v_switch_id: List[str] = None,
    ):
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

class DescribeRouteTablesResponseBodyRouteTablesRouteTableRouteEntrys(DaraModel):
    def __init__(
        self,
        route_entry: List[main_models.DescribeRouteTablesResponseBodyRouteTablesRouteTableRouteEntrysRouteEntry] = None,
    ):
        self.route_entry = route_entry

    def validate(self):
        if self.route_entry:
            for v1 in self.route_entry:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RouteEntry'] = []
        if self.route_entry is not None:
            for k1 in self.route_entry:
                result['RouteEntry'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.route_entry = []
        if m.get('RouteEntry') is not None:
            for k1 in m.get('RouteEntry'):
                temp_model = main_models.DescribeRouteTablesResponseBodyRouteTablesRouteTableRouteEntrysRouteEntry()
                self.route_entry.append(temp_model.from_map(k1))

        return self

class DescribeRouteTablesResponseBodyRouteTablesRouteTableRouteEntrysRouteEntry(DaraModel):
    def __init__(
        self,
        description: str = None,
        destination_cidr_block: str = None,
        instance_id: str = None,
        next_hop_type: str = None,
        next_hops: main_models.DescribeRouteTablesResponseBodyRouteTablesRouteTableRouteEntrysRouteEntryNextHops = None,
        route_entry_id: str = None,
        route_entry_name: str = None,
        route_table_id: str = None,
        status: str = None,
        type: str = None,
    ):
        # The description of the route. The description must be 2 to 256 characters in length. It must start with a letter but cannot start with `http://` or `https://`.
        self.description = description
        # The destination CIDR block of the route. The destination CIDR block supports IPv4 and IPv6. Make sure that the destination CIDR block meets the following requirements:
        # 
        # *   The destination CIDR block is not 100.64.0.0/10 or a subset of 100.64.0.0/10.
        # *   The destination CIDR block of each route in the route table is unique.
        self.destination_cidr_block = destination_cidr_block
        # The ID of the instance associated with the next hop.
        self.instance_id = instance_id
        # The type of the next hop. Valid values:
        # 
        # *   **Instance** (default): an Elastic Compute Service (ECS) instance
        # *   **HaVip**: a high-availability virtual IP address (HaVip).
        # *   **VpnGateway**: a VPN gateway
        # *   **NatGateway**: a NAT gateway
        # *   **NetworkInterface**: a secondary elastic network interface (ENI)
        # *   **RouterInterface**: a router interface
        # *   **IPv6Gateway**: an IPv6 gateway
        # *   **Attachment**: a transit router
        self.next_hop_type = next_hop_type
        # The information about the next hop.
        self.next_hops = next_hops
        # The ID of the route.
        self.route_entry_id = route_entry_id
        # The route name.
        # 
        # The name must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores (_), and hyphens (-).
        self.route_entry_name = route_entry_name
        # The route table ID.
        self.route_table_id = route_table_id
        # The route status. Valid values:
        # 
        # *   **Pending**
        # *   **Available**
        # *   **Modifying**
        self.status = status
        # The route type. Valid values:
        # 
        # *   **Custom**
        # *   **System**
        # *   **BGP**
        # *   **CEN**
        self.type = type

    def validate(self):
        if self.next_hops:
            self.next_hops.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.next_hop_type is not None:
            result['NextHopType'] = self.next_hop_type

        if self.next_hops is not None:
            result['NextHops'] = self.next_hops.to_map()

        if self.route_entry_id is not None:
            result['RouteEntryId'] = self.route_entry_id

        if self.route_entry_name is not None:
            result['RouteEntryName'] = self.route_entry_name

        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NextHopType') is not None:
            self.next_hop_type = m.get('NextHopType')

        if m.get('NextHops') is not None:
            temp_model = main_models.DescribeRouteTablesResponseBodyRouteTablesRouteTableRouteEntrysRouteEntryNextHops()
            self.next_hops = temp_model.from_map(m.get('NextHops'))

        if m.get('RouteEntryId') is not None:
            self.route_entry_id = m.get('RouteEntryId')

        if m.get('RouteEntryName') is not None:
            self.route_entry_name = m.get('RouteEntryName')

        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeRouteTablesResponseBodyRouteTablesRouteTableRouteEntrysRouteEntryNextHops(DaraModel):
    def __init__(
        self,
        next_hop: List[main_models.DescribeRouteTablesResponseBodyRouteTablesRouteTableRouteEntrysRouteEntryNextHopsNextHop] = None,
    ):
        self.next_hop = next_hop

    def validate(self):
        if self.next_hop:
            for v1 in self.next_hop:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NextHop'] = []
        if self.next_hop is not None:
            for k1 in self.next_hop:
                result['NextHop'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.next_hop = []
        if m.get('NextHop') is not None:
            for k1 in m.get('NextHop'):
                temp_model = main_models.DescribeRouteTablesResponseBodyRouteTablesRouteTableRouteEntrysRouteEntryNextHopsNextHop()
                self.next_hop.append(temp_model.from_map(k1))

        return self

class DescribeRouteTablesResponseBodyRouteTablesRouteTableRouteEntrysRouteEntryNextHopsNextHop(DaraModel):
    def __init__(
        self,
        enabled: int = None,
        next_hop_id: str = None,
        next_hop_type: str = None,
        weight: int = None,
    ):
        # Indicates whether the route is available. Valid values:
        # 
        # *   **0**: unavailable
        # *   **1**: available
        self.enabled = enabled
        # The ID of the next hop.
        self.next_hop_id = next_hop_id
        # The type of the next hop. Valid values:
        # 
        # *   **Instance**: an ECS instance
        # *   **HaVip**: an HaVip
        # *   **VpnGateway**: a VPN gateway
        # *   **NatGateway**: a NAT gateway
        # *   **NetworkInterface**: a secondary ENI
        # *   **RouterInterface**: a router interface
        # *   **IPv6Gateway**: an IPv6 gateway
        # *   **Attachment**: a transit router
        self.next_hop_type = next_hop_type
        # The weight of the route.
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.next_hop_id is not None:
            result['NextHopId'] = self.next_hop_id

        if self.next_hop_type is not None:
            result['NextHopType'] = self.next_hop_type

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('NextHopId') is not None:
            self.next_hop_id = m.get('NextHopId')

        if m.get('NextHopType') is not None:
            self.next_hop_type = m.get('NextHopType')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

