# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateNetworkServiceRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        name: str = None,
        security_group_id: str = None,
        type: str = None,
        vpc_id: str = None,
        vswitch_ids: List[str] = None,
        region_id: str = None,
    ):
        self.client_token = client_token
        self.name = name
        self.security_group_id = security_group_id
        self.type = type
        # VPC id。
        self.vpc_id = vpc_id
        self.vswitch_ids = vswitch_ids
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['clientToken'] = self.client_token

        if self.name is not None:
            result['name'] = self.name

        if self.security_group_id is not None:
            result['securityGroupId'] = self.security_group_id

        if self.type is not None:
            result['type'] = self.type

        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id

        if self.vswitch_ids is not None:
            result['vswitchIds'] = self.vswitch_ids

        if self.region_id is not None:
            result['regionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')

        if m.get('vswitchIds') is not None:
            self.vswitch_ids = m.get('vswitchIds')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        return self

