# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class ListCenChildInstanceRouteEntriesToAttachmentResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        route_entry: List[main_models.ListCenChildInstanceRouteEntriesToAttachmentResponseBodyRouteEntry] = None,
    ):
        # The token that determines the start point of the next query. Valid values:
        # 
        # *   If **NextToken** is not returned, it indicates that no additional results exist.
        # *   If **NextToken** was returned in the previous query, specify the value to obtain the next set of results.
        self.next_token = next_token
        # The ID of the region.
        self.request_id = request_id
        # The detailed information about the route.
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
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['RouteEntry'] = []
        if self.route_entry is not None:
            for k1 in self.route_entry:
                result['RouteEntry'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.route_entry = []
        if m.get('RouteEntry') is not None:
            for k1 in m.get('RouteEntry'):
                temp_model = main_models.ListCenChildInstanceRouteEntriesToAttachmentResponseBodyRouteEntry()
                self.route_entry.append(temp_model.from_map(k1))

        return self

class ListCenChildInstanceRouteEntriesToAttachmentResponseBodyRouteEntry(DaraModel):
    def __init__(
        self,
        cen_id: str = None,
        child_instance_route_table_id: str = None,
        destination_cidr_block: str = None,
        service_type: str = None,
        status: str = None,
        transit_router_attachment_id: str = None,
    ):
        # The ID of the CEN instance.
        self.cen_id = cen_id
        # The ID of the route table configured on the network instance.
        self.child_instance_route_table_id = child_instance_route_table_id
        # The destination CIDR block of the route.
        self.destination_cidr_block = destination_cidr_block
        # Indicates whether the route is hosted. If the parameter is empty, the route is not hosted. A value of TR indicates that the route is hosted on a transit router.
        self.service_type = service_type
        # The status of the route. Valid values:
        # 
        # *   **Available**: The route is available.
        # *   **Pending**: The route is being configured.
        # *   **Modifying**: the route is being modified.
        self.status = status
        # The ID of the network instance connection.
        self.transit_router_attachment_id = transit_router_attachment_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.child_instance_route_table_id is not None:
            result['ChildInstanceRouteTableId'] = self.child_instance_route_table_id

        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block

        if self.service_type is not None:
            result['ServiceType'] = self.service_type

        if self.status is not None:
            result['Status'] = self.status

        if self.transit_router_attachment_id is not None:
            result['TransitRouterAttachmentId'] = self.transit_router_attachment_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('ChildInstanceRouteTableId') is not None:
            self.child_instance_route_table_id = m.get('ChildInstanceRouteTableId')

        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')

        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')

        return self

