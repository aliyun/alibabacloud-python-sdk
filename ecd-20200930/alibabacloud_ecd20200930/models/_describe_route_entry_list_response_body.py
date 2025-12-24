# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeRouteEntryListResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        route_entries: List[main_models.DescribeRouteEntryListResponseBodyRouteEntries] = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.route_entries = route_entries

    def validate(self):
        if self.route_entries:
            for v1 in self.route_entries:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['RouteEntries'] = []
        if self.route_entries is not None:
            for k1 in self.route_entries:
                result['RouteEntries'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.route_entries = []
        if m.get('RouteEntries') is not None:
            for k1 in m.get('RouteEntries'):
                temp_model = main_models.DescribeRouteEntryListResponseBodyRouteEntries()
                self.route_entries.append(temp_model.from_map(k1))

        return self

class DescribeRouteEntryListResponseBodyRouteEntries(DaraModel):
    def __init__(
        self,
        description: str = None,
        destination_cidr_block: str = None,
        ip_version: str = None,
        next_hops: List[main_models.DescribeRouteEntryListResponseBodyRouteEntriesNextHops] = None,
        route_entry_id: str = None,
        route_entry_name: str = None,
        route_table_id: str = None,
        status: str = None,
        type: str = None,
    ):
        self.description = description
        self.destination_cidr_block = destination_cidr_block
        self.ip_version = ip_version
        self.next_hops = next_hops
        self.route_entry_id = route_entry_id
        self.route_entry_name = route_entry_name
        self.route_table_id = route_table_id
        self.status = status
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
        if self.description is not None:
            result['Description'] = self.description

        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

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

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        self.next_hops = []
        if m.get('NextHops') is not None:
            for k1 in m.get('NextHops'):
                temp_model = main_models.DescribeRouteEntryListResponseBodyRouteEntriesNextHops()
                self.next_hops.append(temp_model.from_map(k1))

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

class DescribeRouteEntryListResponseBodyRouteEntriesNextHops(DaraModel):
    def __init__(
        self,
        next_hop_id: str = None,
        next_hop_type: str = None,
    ):
        self.next_hop_id = next_hop_id
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

        if self.next_hop_type is not None:
            result['NextHopType'] = self.next_hop_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextHopId') is not None:
            self.next_hop_id = m.get('NextHopId')

        if m.get('NextHopType') is not None:
            self.next_hop_type = m.get('NextHopType')

        return self

