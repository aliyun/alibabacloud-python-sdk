# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AddGatewaySecurityGroupRuleRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        port_ranges: List[str] = None,
        security_group_id: str = None,
    ):
        # Description of the security group rule.
        self.description = description
        # Port ranges.
        self.port_ranges = port_ranges
        # Security group ID.
        self.security_group_id = security_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.port_ranges is not None:
            result['portRanges'] = self.port_ranges

        if self.security_group_id is not None:
            result['securityGroupId'] = self.security_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('portRanges') is not None:
            self.port_ranges = m.get('portRanges')

        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')

        return self

