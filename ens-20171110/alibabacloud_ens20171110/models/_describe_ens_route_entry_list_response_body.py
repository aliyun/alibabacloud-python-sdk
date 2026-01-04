# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeEnsRouteEntryListResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        route_entrys: List[main_models.DescribeEnsRouteEntryListResponseBodyRouteEntrys] = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The information about the routes.
        self.route_entrys = route_entrys
        # The number of returned entries.
        self.total_count = total_count

    def validate(self):
        if self.route_entrys:
            for v1 in self.route_entrys:
                 if v1:
                    v1.validate()

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

        result['RouteEntrys'] = []
        if self.route_entrys is not None:
            for k1 in self.route_entrys:
                result['RouteEntrys'].append(k1.to_map() if k1 else None)

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

        self.route_entrys = []
        if m.get('RouteEntrys') is not None:
            for k1 in m.get('RouteEntrys'):
                temp_model = main_models.DescribeEnsRouteEntryListResponseBodyRouteEntrys()
                self.route_entrys.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeEnsRouteEntryListResponseBodyRouteEntrys(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        description: str = None,
        destination_cidr_block: str = None,
        next_hops: List[main_models.DescribeEnsRouteEntryListResponseBodyRouteEntrysNextHops] = None,
        route_entry_id: str = None,
        route_entry_name: str = None,
        route_table_id: str = None,
        source_cidr_block: str = None,
        status: str = None,
        type: str = None,
    ):
        # The time when the IP address was created. The time is displayed in UTC.
        self.creation_time = creation_time
        # Enter a description for the route.
        self.description = description
        # The destination CIDR block of the route.
        self.destination_cidr_block = destination_cidr_block
        # The information about the next hop.
        self.next_hops = next_hops
        # The ID of the route.
        self.route_entry_id = route_entry_id
        # The name of the route.
        self.route_entry_name = route_entry_name
        # The ID of the route table.
        self.route_table_id = route_table_id
        # The source CIDR block. This field is used when you configure a route entry in the gateway route table. This field is not supported in the vSwitch route table.
        self.source_cidr_block = source_cidr_block
        # The status of the route entry. Valid values:
        self.status = status
        # The type of the route entry.
        self.type = type

    def validate(self):
        if self.next_hops:
            for v1 in self.next_hops:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block

        result['NextHops'] = []
        if self.next_hops is not None:
            for k1 in self.next_hops:
                result['NextHops'].append(k1.to_map() if k1 else None)

        if self.route_entry_id is not None:
            result['RouteEntryId'] = self.route_entry_id

        if self.route_entry_name is not None:
            result['RouteEntryName'] = self.route_entry_name

        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id

        if self.source_cidr_block is not None:
            result['SourceCidrBlock'] = self.source_cidr_block

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')

        self.next_hops = []
        if m.get('NextHops') is not None:
            for k1 in m.get('NextHops'):
                temp_model = main_models.DescribeEnsRouteEntryListResponseBodyRouteEntrysNextHops()
                self.next_hops.append(temp_model.from_map(k1))

        if m.get('RouteEntryId') is not None:
            self.route_entry_id = m.get('RouteEntryId')

        if m.get('RouteEntryName') is not None:
            self.route_entry_name = m.get('RouteEntryName')

        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')

        if m.get('SourceCidrBlock') is not None:
            self.source_cidr_block = m.get('SourceCidrBlock')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeEnsRouteEntryListResponseBodyRouteEntrysNextHops(DaraModel):
    def __init__(
        self,
        next_hop_id: str = None,
        next_hop_name: str = None,
        next_hop_type: str = None,
    ):
        # The ID of the next hop.
        self.next_hop_id = next_hop_id
        # The instance ID of the next hop.
        self.next_hop_name = next_hop_name
        # The type of the next hop. Valid values:
        self.next_hop_type = next_hop_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_hop_id is not None:
            result['NextHopId'] = self.next_hop_id

        if self.next_hop_name is not None:
            result['NextHopName'] = self.next_hop_name

        if self.next_hop_type is not None:
            result['NextHopType'] = self.next_hop_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextHopId') is not None:
            self.next_hop_id = m.get('NextHopId')

        if m.get('NextHopName') is not None:
            self.next_hop_name = m.get('NextHopName')

        if m.get('NextHopType') is not None:
            self.next_hop_type = m.get('NextHopType')

        return self

