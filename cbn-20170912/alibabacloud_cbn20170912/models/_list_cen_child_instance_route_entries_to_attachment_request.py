# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class ListCenChildInstanceRouteEntriesToAttachmentRequest(DaraModel):
    def __init__(
        self,
        cen_id: str = None,
        child_instance_route_table_id: str = None,
        max_results: int = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        route_filter: List[main_models.ListCenChildInstanceRouteEntriesToAttachmentRequestRouteFilter] = None,
        service_type: str = None,
        transit_router_attachment_id: str = None,
    ):
        # The ID of the CEN instance.
        self.cen_id = cen_id
        # The ID of the route table configured on the network instance.
        # 
        # This parameter is required.
        self.child_instance_route_table_id = child_instance_route_table_id
        # The number of entries to return on each page. Default value: **20**.
        self.max_results = max_results
        # The token that determines the start point of the query. Valid values:
        # 
        # *   If this is your first query and no subsequent queries are to be sent, ignore this parameter.
        # *   If a subsequent query is to be sent, set the parameter to the value of NextToken that is returned from the last call.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The filter condition for the destination CIDR block.
        self.route_filter = route_filter
        # Specifies whether to host the route. If you leave the parameter empty, the route is not hosted. A value of TR specifies that the route is hosted on a transit router.
        self.service_type = service_type
        # The ID of the network instance connection.
        # 
        # This parameter is required.
        self.transit_router_attachment_id = transit_router_attachment_id

    def validate(self):
        if self.route_filter:
            for v1 in self.route_filter:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.child_instance_route_table_id is not None:
            result['ChildInstanceRouteTableId'] = self.child_instance_route_table_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        result['RouteFilter'] = []
        if self.route_filter is not None:
            for k1 in self.route_filter:
                result['RouteFilter'].append(k1.to_map() if k1 else None)

        if self.service_type is not None:
            result['ServiceType'] = self.service_type

        if self.transit_router_attachment_id is not None:
            result['TransitRouterAttachmentId'] = self.transit_router_attachment_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('ChildInstanceRouteTableId') is not None:
            self.child_instance_route_table_id = m.get('ChildInstanceRouteTableId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        self.route_filter = []
        if m.get('RouteFilter') is not None:
            for k1 in m.get('RouteFilter'):
                temp_model = main_models.ListCenChildInstanceRouteEntriesToAttachmentRequestRouteFilter()
                self.route_filter.append(temp_model.from_map(k1))

        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')

        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')

        return self

class ListCenChildInstanceRouteEntriesToAttachmentRequestRouteFilter(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: List[str] = None,
    ):
        # The match mode of the route.
        # 
        # *   **prefix-exact-match**: exact match.
        self.key = key
        # The destination CIDR blocks.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

