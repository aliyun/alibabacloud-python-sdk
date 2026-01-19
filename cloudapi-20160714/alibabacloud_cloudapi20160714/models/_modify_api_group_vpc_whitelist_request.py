# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyApiGroupVpcWhitelistRequest(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        security_token: str = None,
        vpc_ids: str = None,
    ):
        # The ID of the API group.
        # 
        # This parameter is required.
        self.group_id = group_id
        self.security_token = security_token
        # The ID of the VPC instance.
        # 
        # This parameter is required.
        self.vpc_ids = vpc_ids

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

        if self.vpc_ids is not None:
            result['VpcIds'] = self.vpc_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('VpcIds') is not None:
            self.vpc_ids = m.get('VpcIds')

        return self

