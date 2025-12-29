# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class VPCConfig(DaraModel):
    def __init__(
        self,
        anytunnel_via_eni: bool = None,
        role: str = None,
        security_group_id: str = None,
        v_switch_ids: List[str] = None,
        vpc_id: str = None,
    ):
        self.anytunnel_via_eni = anytunnel_via_eni
        self.role = role
        self.security_group_id = security_group_id
        self.v_switch_ids = v_switch_ids
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.anytunnel_via_eni is not None:
            result['anytunnelViaENI'] = self.anytunnel_via_eni

        if self.role is not None:
            result['role'] = self.role

        if self.security_group_id is not None:
            result['securityGroupId'] = self.security_group_id

        if self.v_switch_ids is not None:
            result['vSwitchIds'] = self.v_switch_ids

        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('anytunnelViaENI') is not None:
            self.anytunnel_via_eni = m.get('anytunnelViaENI')

        if m.get('role') is not None:
            self.role = m.get('role')

        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')

        if m.get('vSwitchIds') is not None:
            self.v_switch_ids = m.get('vSwitchIds')

        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')

        return self

