# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteSecurityIPGroupRequest(DaraModel):
    def __init__(
        self,
        global_security_group_id: str = None,
        region_name: str = None,
    ):
        # This parameter is required.
        self.global_security_group_id = global_security_group_id
        # This parameter is required.
        self.region_name = region_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.global_security_group_id is not None:
            result['GlobalSecurityGroupId'] = self.global_security_group_id

        if self.region_name is not None:
            result['RegionName'] = self.region_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GlobalSecurityGroupId') is not None:
            self.global_security_group_id = m.get('GlobalSecurityGroupId')

        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')

        return self

