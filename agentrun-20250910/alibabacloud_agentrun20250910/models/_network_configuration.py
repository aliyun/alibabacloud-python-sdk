# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class NetworkConfiguration(DaraModel):
    def __init__(
        self,
        network_mode: str = None,
        security_group_id: str = None,
        vpc_id: str = None,
        vswitch_ids: List[str] = None,
    ):
        self.network_mode = network_mode
        self.security_group_id = security_group_id
        self.vpc_id = vpc_id
        self.vswitch_ids = vswitch_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.network_mode is not None:
            result['networkMode'] = self.network_mode

        if self.security_group_id is not None:
            result['securityGroupId'] = self.security_group_id

        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id

        if self.vswitch_ids is not None:
            result['vswitchIds'] = self.vswitch_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('networkMode') is not None:
            self.network_mode = m.get('networkMode')

        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')

        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')

        if m.get('vswitchIds') is not None:
            self.vswitch_ids = m.get('vswitchIds')

        return self

