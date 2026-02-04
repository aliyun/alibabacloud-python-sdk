# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListTransitRouterMulticastGroupsRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        group_ip_address: str = None,
        is_group_member: bool = None,
        is_group_source: bool = None,
        max_results: int = None,
        network_interface_ids: List[str] = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        peer_transit_router_multicast_domains: List[str] = None,
        resource_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
        transit_router_attachment_id: str = None,
        transit_router_multicast_domain_id: str = None,
        v_switch_ids: List[str] = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must make sure that it is unique among all requests. The token can contain only ASCII characters.
        self.client_token = client_token
        # The IP address of the multicast group.
        # 
        # Each multicast group is identified by its IP address.
        self.group_ip_address = group_ip_address
        # Specified whether to query the multicast members. Valid values:
        # 
        # *   **false**
        # *   **true**
        # 
        # >- This parameter must be specified together with the IsGroupMember parameter.
        # >- If you do not set IsGroupMember or IsGroupSource, both the multicast sources and members are queried.
        # >- If you set only one of them or both of them, the specified values prevail.
        self.is_group_member = is_group_member
        # Specifies whether to query the multicast sources. Valid values:
        # 
        # *   **false**
        # *   **true**
        # 
        # > - This parameter must be specified together with the IsGroupMember parameter.
        # > *   If you do not specify IsGroupMember or IsGroupSource, both the multicast sources and members are queried.
        # > *   If you specify only one of them or both of them, the specified values prevail.
        self.is_group_source = is_group_source
        # The number of entries to return on each page. Default value: **20**.
        self.max_results = max_results
        # The IDs of ENIs.
        self.network_interface_ids = network_interface_ids
        # The token that determines the start point of the query. Valid values:
        # 
        # *   If this is your first query and no next queries are to be sent, ignore this parameter.
        # *   If a subsequent query is to be sent, set the parameter to the value of NextToken that is returned from the last call.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the inter-region multicast domain.
        self.peer_transit_router_multicast_domains = peer_transit_router_multicast_domains
        # The ID of the resource associated with the multicast resource.
        self.resource_id = resource_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The type of the multicast resource. Valid values:
        # 
        # *   **VPC**: queries multicast resources by VPC.
        # *   **TR**: queries multicast resources that are also deployed in a different region.
        self.resource_type = resource_type
        # The ID of the network instance connection
        # 
        # You must configure one of the TransitRouterMulticastDomainId and TransitRouterAttachmentId parameters.
        self.transit_router_attachment_id = transit_router_attachment_id
        # The ID of the multicast domain.
        # 
        # You must configure one of the TransitRouterMulticastDomainId and TransitRouterAttachmentId parameters.
        self.transit_router_multicast_domain_id = transit_router_multicast_domain_id
        # The vSwitch IDs.
        self.v_switch_ids = v_switch_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.group_ip_address is not None:
            result['GroupIpAddress'] = self.group_ip_address

        if self.is_group_member is not None:
            result['IsGroupMember'] = self.is_group_member

        if self.is_group_source is not None:
            result['IsGroupSource'] = self.is_group_source

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.network_interface_ids is not None:
            result['NetworkInterfaceIds'] = self.network_interface_ids

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.peer_transit_router_multicast_domains is not None:
            result['PeerTransitRouterMulticastDomains'] = self.peer_transit_router_multicast_domains

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.transit_router_attachment_id is not None:
            result['TransitRouterAttachmentId'] = self.transit_router_attachment_id

        if self.transit_router_multicast_domain_id is not None:
            result['TransitRouterMulticastDomainId'] = self.transit_router_multicast_domain_id

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('GroupIpAddress') is not None:
            self.group_ip_address = m.get('GroupIpAddress')

        if m.get('IsGroupMember') is not None:
            self.is_group_member = m.get('IsGroupMember')

        if m.get('IsGroupSource') is not None:
            self.is_group_source = m.get('IsGroupSource')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NetworkInterfaceIds') is not None:
            self.network_interface_ids = m.get('NetworkInterfaceIds')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PeerTransitRouterMulticastDomains') is not None:
            self.peer_transit_router_multicast_domains = m.get('PeerTransitRouterMulticastDomains')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('TransitRouterAttachmentId') is not None:
            self.transit_router_attachment_id = m.get('TransitRouterAttachmentId')

        if m.get('TransitRouterMulticastDomainId') is not None:
            self.transit_router_multicast_domain_id = m.get('TransitRouterMulticastDomainId')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        return self

