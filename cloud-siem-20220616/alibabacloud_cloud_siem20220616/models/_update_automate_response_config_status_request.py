# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAutomateResponseConfigStatusRequest(DaraModel):
    def __init__(
        self,
        ids: str = None,
        in_use: bool = None,
        region_id: str = None,
        role_for: int = None,
        role_type: int = None,
    ):
        # The IDs of the automatic response rules. The value is a JSON array.
        self.ids = ids
        # Specifies whether the rule is enabled. Valid values:
        # 
        # *   true
        # *   false
        self.in_use = in_use
        # The data management center of the threat analysis feature. Specify this parameter based on the region in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions inside China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id
        # The ID of the account that you switch from the management account.
        self.role_for = role_for
        # The type of the view. Valid values:
        # - 0: the current Alibaba Cloud account
        # - 1: the global account
        self.role_type = role_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ids is not None:
            result['Ids'] = self.ids

        if self.in_use is not None:
            result['InUse'] = self.in_use

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        if self.role_type is not None:
            result['RoleType'] = self.role_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')

        if m.get('InUse') is not None:
            self.in_use = m.get('InUse')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        return self

