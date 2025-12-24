# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRulesRequest(DaraModel):
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
        rule_list: str = None,
    ):
        # The frontend listener port that is used by the SLB instance.
        # 
        # Valid values: **1 to 65535**.
        # 
        # This parameter is required.
        self.listener_port = listener_port
        # The frontend protocol that is used by the SLB instance.
        # 
        # > This parameter is required if the same port is used by listeners that use different protocols.
        self.listener_protocol = listener_protocol
        # The ID of the SLB instance.
        # 
        # This parameter is required.
        self.load_balancer_id = load_balancer_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where the Server Load Balancer (SLB) instance is deployed.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/27584.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The forwarding rules that you want to create. You can create at most 10 forwarding rules in each call. Each forwarding rule contains the following parameters:
        # 
        # *   **RuleName**: Required. The value must be of the STRING type. The name of the forwarding rule. The name must be 1 to 40 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.), and underscores (_). Forwarding rule names must be unique within the same listener.
        # *   **Domain**: Optional. The value must be a string. The domain name that is associated with the forwarding rule. You must specify this parameter or the **URL** parameter.
        # *   **Url**: Optional. The value must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.), percent signs (%), question marks (?), number signs (#), and ampersands (&). The value must be a string. The URL cannot be only a forward slash (/). However, it must start with a forward slash (/). You must specify this parameter or the **Domain** parameter.
        # *   **VServerGroupId**: Required. The value must be a string. The ID of the vServer group to be specified in the forwarding rule.
        # 
        # >  You must specify at least one between the `Domain` and `URL` parameters. You can also specify both. The combination of `Domain` and `Url` must be unique within the same listener.
        # 
        # This parameter is required.
        self.rule_list = rule_list

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

        if self.rule_list is not None:
            result['RuleList'] = self.rule_list

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

        if m.get('RuleList') is not None:
            self.rule_list = m.get('RuleList')

        return self

