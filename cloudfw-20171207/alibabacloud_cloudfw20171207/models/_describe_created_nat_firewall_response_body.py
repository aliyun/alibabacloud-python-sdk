# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeCreatedNatFirewallResponseBody(DaraModel):
    def __init__(
        self,
        created_nat_firewalls: List[main_models.DescribeCreatedNatFirewallResponseBodyCreatedNatFirewalls] = None,
        request_id: str = None,
    ):
        self.created_nat_firewalls = created_nat_firewalls
        self.request_id = request_id

    def validate(self):
        if self.created_nat_firewalls:
            for v1 in self.created_nat_firewalls:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CreatedNatFirewalls'] = []
        if self.created_nat_firewalls is not None:
            for k1 in self.created_nat_firewalls:
                result['CreatedNatFirewalls'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.created_nat_firewalls = []
        if m.get('CreatedNatFirewalls') is not None:
            for k1 in m.get('CreatedNatFirewalls'):
                temp_model = main_models.DescribeCreatedNatFirewallResponseBodyCreatedNatFirewalls()
                self.created_nat_firewalls.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeCreatedNatFirewallResponseBodyCreatedNatFirewalls(DaraModel):
    def __init__(
        self,
        nat_firewall_id: str = None,
        nat_gateway_id: str = None,
        nat_gateway_name: str = None,
    ):
        self.nat_firewall_id = nat_firewall_id
        self.nat_gateway_id = nat_gateway_id
        self.nat_gateway_name = nat_gateway_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.nat_firewall_id is not None:
            result['NatFirewallId'] = self.nat_firewall_id

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        if self.nat_gateway_name is not None:
            result['NatGatewayName'] = self.nat_gateway_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NatFirewallId') is not None:
            self.nat_firewall_id = m.get('NatFirewallId')

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        if m.get('NatGatewayName') is not None:
            self.nat_gateway_name = m.get('NatGatewayName')

        return self

