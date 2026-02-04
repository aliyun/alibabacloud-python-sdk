# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class ListTransitRouterRouteTableAssociationsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
        transit_router_associations: List[main_models.ListTransitRouterRouteTableAssociationsResponseBodyTransitRouterAssociations] = None,
    ):
        # The number of entries returned per page.
        self.max_results = max_results
        # The token that determines the start point of the query. Valid values:
        # 
        # *   If **NextToken** was not returned, it indicates that no additional results exist.
        # *   If **NextToken** was returned in the previous query, specify the value to obtain the next set of results.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count
        # A list of associated forwarding correlations.
        self.transit_router_associations = transit_router_associations

    def validate(self):
        if self.transit_router_associations:
            for v1 in self.transit_router_associations:
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

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['TransitRouterAssociations'] = []
        if self.transit_router_associations is not None:
            for k1 in self.transit_router_associations:
                result['TransitRouterAssociations'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.transit_router_associations = []
        if m.get('TransitRouterAssociations') is not None:
            for k1 in m.get('TransitRouterAssociations'):
                temp_model = main_models.ListTransitRouterRouteTableAssociationsResponseBodyTransitRouterAssociations()
                self.transit_router_associations.append(temp_model.from_map(k1))

        return self

class ListTransitRouterRouteTableAssociationsResponseBodyTransitRouterAssociations(DaraModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        status: str = None,
        transit_router_attachment_id: str = None,
        transit_router_route_table_id: str = None,
    ):
        # The ID of the next hop.
        self.resource_id = resource_id
        # The type of next hop. Valid values:
        # 
        # *   **VPC**: VPC
        # *   **VBR**: VBR
        # *   **TR**: transit router
        # *   **VPN** :VPN attachment
        self.resource_type = resource_type
        # The status of the associated forwarding correlation. Valid values:
        # 
        # *   **Active**: The associated forwarding correlation is available.
        # *   **Associating**: The associated forwarding correlation is being created.
        # *   **Dissociating**: The associated forwarding correlation is being deleted.
        # *   **Deleted**: The associated forwarding correlation is deleted.
        self.status = status
        # The ID of the network instance connection.
        self.transit_router_attachment_id = transit_router_attachment_id
        # The ID of the route table of the Enterprise Edition transit router.
        self.transit_router_route_table_id = transit_router_route_table_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.status is not None:
            result['Status'] = self.status

        if self.transit_router_attachment_id is not None:
            result['TransitRouterAttachmentId'] = self.transit_router_attachment_id

        if self.transit_router_route_table_id is not None:
            result['TransitRouterRouteTableId'] = self.transit_router_route_table_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')

        if m.get('TransitRouterRouteTableId') is not None:
            self.transit_router_route_table_id = m.get('TransitRouterRouteTableId')

        return self

