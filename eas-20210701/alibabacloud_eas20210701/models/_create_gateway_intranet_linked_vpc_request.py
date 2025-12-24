# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateGatewayIntranetLinkedVpcRequest(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        enable_authoritative_dns: bool = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        self.account_id = account_id
        self.enable_authoritative_dns = enable_authoritative_dns
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The virtual private cloud (VPC) ID.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.enable_authoritative_dns is not None:
            result['EnableAuthoritativeDns'] = self.enable_authoritative_dns

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('EnableAuthoritativeDns') is not None:
            self.enable_authoritative_dns = m.get('EnableAuthoritativeDns')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

