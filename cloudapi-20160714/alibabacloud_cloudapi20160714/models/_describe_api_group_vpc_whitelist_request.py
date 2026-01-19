# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeApiGroupVpcWhitelistRequest(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        security_token: str = None,
    ):
        # The ID of the API group.
        # 
        # This parameter is required.
        self.group_id = group_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

