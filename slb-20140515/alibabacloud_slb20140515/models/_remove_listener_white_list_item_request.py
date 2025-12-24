# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RemoveListenerWhiteListItemRequest(DaraModel):
    def __init__(
        self,
        listener_port: int = None,
        listener_protocol: str = None,
        load_balancer_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        source_items: str = None,
    ):
        # The listening port.
        # 
        # This parameter is required.
        self.listener_port = listener_port
        # The frontend protocol that is used by the CLB instance.
        # 
        # >  This parameter is required when listeners that use different protocols listen on the same port.
        self.listener_protocol = listener_protocol
        # The ID of the CLB instance.
        # 
        # This parameter is required.
        self.load_balancer_id = load_balancer_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region where the Classic Load Balancer (CLB) instance is created.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/27584.html) operation to query the most recent region list.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The list of IP addresses or CIDR blocks that you want to remove from the whitelist. Separate multiple IP addresses or CIDR blocks with commas (,).
        # 
        # >  If all IP addresses are removed from the whitelist, the listener does not forward requests.
        # 
        # This parameter is required.
        self.source_items = source_items

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port

        if self.listener_protocol is not None:
            result['ListenerProtocol'] = self.listener_protocol

        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.source_items is not None:
            result['SourceItems'] = self.source_items

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')

        if m.get('ListenerProtocol') is not None:
            self.listener_protocol = m.get('ListenerProtocol')

        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SourceItems') is not None:
            self.source_items = m.get('SourceItems')

        return self

