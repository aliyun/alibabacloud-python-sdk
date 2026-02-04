# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class ListTransitRouterMulticastGroupsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
        transit_router_multicast_groups: List[main_models.ListTransitRouterMulticastGroupsResponseBodyTransitRouterMulticastGroups] = None,
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
        # A list of multicast groups.
        self.transit_router_multicast_groups = transit_router_multicast_groups

    def validate(self):
        if self.transit_router_multicast_groups:
            for v1 in self.transit_router_multicast_groups:
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

        result['TransitRouterMulticastGroups'] = []
        if self.transit_router_multicast_groups is not None:
            for k1 in self.transit_router_multicast_groups:
                result['TransitRouterMulticastGroups'].append(k1.to_map() if k1 else None)

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

        self.transit_router_multicast_groups = []
        if m.get('TransitRouterMulticastGroups') is not None:
            for k1 in m.get('TransitRouterMulticastGroups'):
                temp_model = main_models.ListTransitRouterMulticastGroupsResponseBodyTransitRouterMulticastGroups()
                self.transit_router_multicast_groups.append(temp_model.from_map(k1))

        return self

class ListTransitRouterMulticastGroupsResponseBodyTransitRouterMulticastGroups(DaraModel):
    def __init__(
        self,
        group_ip_address: str = None,
        group_member: bool = None,
        group_source: bool = None,
        member_type: str = None,
        network_interface_id: str = None,
        peer_transit_router_multicast_domain_id: str = None,
        resource_id: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
        source_type: str = None,
        status: str = None,
        transit_router_attachment_id: str = None,
        transit_router_multicast_domain_id: str = None,
        v_switch_id: str = None,
    ):
        # The IP address of the multicast group to which the multicast resource belongs.
        self.group_ip_address = group_ip_address
        # Indicates whether the multicast resource is a multicast member. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.group_member = group_member
        # Indicates whether the multicast resource is a multicast source. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.group_source = group_source
        # The type of the multicast source.
        # 
        # If the value is **Static**, the multicast source is manually specified.
        self.member_type = member_type
        # The ID of the ENI, which is a multicast resource.
        self.network_interface_id = network_interface_id
        # The ID of the multicast domain associated with the multicast resource that is deployed across regions.
        self.peer_transit_router_multicast_domain_id = peer_transit_router_multicast_domain_id
        # The ID of the resource associated with the multicast resource.
        self.resource_id = resource_id
        # The ID of the Alibaba Cloud account to which the multicast resource belongs.
        self.resource_owner_id = resource_owner_id
        # The type of the multicast resource. Valid values:
        # 
        # *   **VPC**: The multicast resource is in a VPC.
        # *   **TR**: The multicast resource is deployed across regions.
        self.resource_type = resource_type
        # The type of the multicast member.
        # 
        # If the value is **Static**, the multicast member is manually specified.
        self.source_type = source_type
        # The status of the multicast resource. Valid values:
        # 
        # *   **Registering**: being created
        # *   **Registered**: available
        # *   **Deregistering**: being deleted
        self.status = status
        # The ID of the network instance connection.
        self.transit_router_attachment_id = transit_router_attachment_id
        # The ID of the multicast domain.
        self.transit_router_multicast_domain_id = transit_router_multicast_domain_id
        # The ID of the vSwitch to which the multicast resource belongs.
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_ip_address is not None:
            result['GroupIpAddress'] = self.group_ip_address

        if self.group_member is not None:
            result['GroupMember'] = self.group_member

        if self.group_source is not None:
            result['GroupSource'] = self.group_source

        if self.member_type is not None:
            result['MemberType'] = self.member_type

        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id

        if self.peer_transit_router_multicast_domain_id is not None:
            result['PeerTransitRouterMulticastDomainId'] = self.peer_transit_router_multicast_domain_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.source_type is not None:
            result['SourceType'] = self.source_type

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
        if m.get('GroupIpAddress') is not None:
            self.group_ip_address = m.get('GroupIpAddress')

        if m.get('GroupMember') is not None:
            self.group_member = m.get('GroupMember')

        if m.get('GroupSource') is not None:
            self.group_source = m.get('GroupSource')

        if m.get('MemberType') is not None:
            self.member_type = m.get('MemberType')

        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')

        if m.get('PeerTransitRouterMulticastDomainId') is not None:
            self.peer_transit_router_multicast_domain_id = m.get('PeerTransitRouterMulticastDomainId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')

        if m.get('TransitRouterMulticastDomainId') is not None:
            self.transit_router_multicast_domain_id = m.get('TransitRouterMulticastDomainId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

