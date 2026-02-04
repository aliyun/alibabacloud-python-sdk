# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTransitRouterRouteTablePropagationsRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        status: str = None,
        transit_router_attachment_id: str = None,
        transit_router_attachment_resource_id: str = None,
        transit_router_attachment_resource_type: str = None,
        transit_router_route_table_id: str = None,
    ):
        # The number of entries to return on each page. Default value: **50**.
        self.max_results = max_results
        # The token that determines the start point of the query.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The status of the route learning correlation. Valid values:
        # 
        # *   **Active**: available
        # *   **Enabling**: being enabled
        # *   **Disabling**: being disabled
        self.status = status
        # The ID of the network instance connection.
        self.transit_router_attachment_id = transit_router_attachment_id
        # The ID of the network instance.
        self.transit_router_attachment_resource_id = transit_router_attachment_resource_id
        # The type of the network instance. Valid values:
        # 
        # *   **VPC**: virtual private cloud (VPC)
        # *   **VBR**: virtual border router (VBR)
        # *   **TR**: transit router
        # *   **VPN**: VPN connection
        self.transit_router_attachment_resource_type = transit_router_attachment_resource_type
        # The ID of the route table of the Enterprise Edition transit router.
        # 
        # This parameter is required.
        self.transit_router_route_table_id = transit_router_route_table_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.status is not None:
            result['Status'] = self.status

        if self.transit_router_attachment_id is not None:
            result['TransitRouterAttachmentId'] = self.transit_router_attachment_id

        if self.transit_router_attachment_resource_id is not None:
            result['TransitRouterAttachmentResourceId'] = self.transit_router_attachment_resource_id

        if self.transit_router_attachment_resource_type is not None:
            result['TransitRouterAttachmentResourceType'] = self.transit_router_attachment_resource_type

        if self.transit_router_route_table_id is not None:
            result['TransitRouterRouteTableId'] = self.transit_router_route_table_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')

        if m.get('TransitRouterAttachmentResourceId') is not None:
            self.transit_router_attachment_resource_id = m.get('TransitRouterAttachmentResourceId')

        if m.get('TransitRouterAttachmentResourceType') is not None:
            self.transit_router_attachment_resource_type = m.get('TransitRouterAttachmentResourceType')

        if m.get('TransitRouterRouteTableId') is not None:
            self.transit_router_route_table_id = m.get('TransitRouterRouteTableId')

        return self

