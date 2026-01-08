# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeNatFirewallAclGroupListResponseBody(DaraModel):
    def __init__(
        self,
        nat_firewalls: List[main_models.DescribeNatFirewallAclGroupListResponseBodyNatFirewalls] = None,
        request_id: str = None,
    ):
        self.nat_firewalls = nat_firewalls
        self.request_id = request_id

    def validate(self):
        if self.nat_firewalls:
            for v1 in self.nat_firewalls:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NatFirewalls'] = []
        if self.nat_firewalls is not None:
            for k1 in self.nat_firewalls:
                result['NatFirewalls'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nat_firewalls = []
        if m.get('NatFirewalls') is not None:
            for k1 in m.get('NatFirewalls'):
                temp_model = main_models.DescribeNatFirewallAclGroupListResponseBodyNatFirewalls()
                self.nat_firewalls.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeNatFirewallAclGroupListResponseBodyNatFirewalls(DaraModel):
    def __init__(
        self,
        acl_rule_count: int = None,
        is_default: bool = None,
        nat_gateway_id: str = None,
        nat_gateway_name: str = None,
        region_no: str = None,
    ):
        self.acl_rule_count = acl_rule_count
        self.is_default = is_default
        self.nat_gateway_id = nat_gateway_id
        self.nat_gateway_name = nat_gateway_name
        self.region_no = region_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_rule_count is not None:
            result['AclRuleCount'] = self.acl_rule_count

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        if self.nat_gateway_name is not None:
            result['NatGatewayName'] = self.nat_gateway_name

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclRuleCount') is not None:
            self.acl_rule_count = m.get('AclRuleCount')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        if m.get('NatGatewayName') is not None:
            self.nat_gateway_name = m.get('NatGatewayName')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        return self

