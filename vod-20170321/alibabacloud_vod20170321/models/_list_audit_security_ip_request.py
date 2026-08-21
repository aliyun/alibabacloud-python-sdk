# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAuditSecurityIpRequest(DaraModel):
    def __init__(
        self,
        security_group_name: str = None,
    ):
        # The name of the review security IP group. By default, all groups are returned.
        self.security_group_name = security_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.security_group_name is not None:
            result['SecurityGroupName'] = self.security_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityGroupName') is not None:
            self.security_group_name = m.get('SecurityGroupName')

        return self

