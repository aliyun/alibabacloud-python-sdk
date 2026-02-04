# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class ListTransitRouterMulticastDomainAssociationsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
        transit_router_multicast_associations: List[main_models.ListTransitRouterMulticastDomainAssociationsResponseBodyTransitRouterMulticastAssociations] = None,
    ):
        # The number of entries returned on each page.
        self.max_results = max_results
        # The token that determines the start point of the query. Valid values:
        # 
        # *   If **NextToken** is empty, it indicates that no subsequent query is to be sent.
        # *   If **NextToken** was returned in the previous query, specify the value to obtain the next set of results.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count
        # The information about the resource associated with the multicast domain.
        self.transit_router_multicast_associations = transit_router_multicast_associations

    def validate(self):
        if self.transit_router_multicast_associations:
            for v1 in self.transit_router_multicast_associations:
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

        result['TransitRouterMulticastAssociations'] = []
        if self.transit_router_multicast_associations is not None:
            for k1 in self.transit_router_multicast_associations:
                result['TransitRouterMulticastAssociations'].append(k1.to_map() if k1 else None)

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

        self.transit_router_multicast_associations = []
        if m.get('TransitRouterMulticastAssociations') is not None:
            for k1 in m.get('TransitRouterMulticastAssociations'):
                temp_model = main_models.ListTransitRouterMulticastDomainAssociationsResponseBodyTransitRouterMulticastAssociations()
                self.transit_router_multicast_associations.append(temp_model.from_map(k1))

        return self

class ListTransitRouterMulticastDomainAssociationsResponseBodyTransitRouterMulticastAssociations(DaraModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
        status: str = None,
        transit_router_attachment_id: str = None,
        transit_router_multicast_domain_id: str = None,
        v_switch_id: str = None,
    ):
        # The ID of the resource associated with the multicast domain.
        self.resource_id = resource_id
        # The ID of the Alibaba Cloud account to which the resource associated with the multicast domain belongs.
        self.resource_owner_id = resource_owner_id
        # The type of resource associated with the multicast domain.
        # 
        # Valid value: **VPC**.
        self.resource_type = resource_type
        # The association status. Valid values:
        # 
        # *   **Associated**: The resource is associated with the multicast domain.
        # *   **Associating**: The resource is being associated with the multicast domain.
        # *   **Dissociating**: The resource is being disassociated from the multicast domain.
        self.status = status
        # The ID of the network instance connection.
        self.transit_router_attachment_id = transit_router_attachment_id
        # The ID of the multicast domain.
        self.transit_router_multicast_domain_id = transit_router_multicast_domain_id
        # The ID of the vSwitch.
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.status is not None:
            result['Status'] = self.status

        if self.transit_router_attachment_id is not None:
            result['TransitRouterAttachmentId'] = self.transit_router_attachment_id

        if self.transit_router_multicast_domain_id is not None:
            result['TransitRouterMulticastDomainId'] = self.transit_router_multicast_domain_id

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')

        if m.get('TransitRouterMulticastDomainId') is not None:
            self.transit_router_multicast_domain_id = m.get('TransitRouterMulticastDomainId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

