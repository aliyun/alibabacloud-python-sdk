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
        # The IDs of the automated response rules, formatted as a JSON array.
        self.ids = ids
        # The enabling status of the rule. Valid values:
        # - true: Enabled.
        # - false: Disabled.
        self.in_use = in_use
        # The region where the data management center of Threat Analysis is located. Select the region of the management center based on the region where your assets are located. Valid values:
        # - cn-hangzhou: Assets are located in the Chinese mainland and Hong Kong (China).
        # - ap-southeast-1: Assets are located outside the Chinese mainland.
        self.region_id = region_id
        # The ID of the user whose perspective the administrator switches to.
        self.role_for = role_for
        # The view type. Valid values:
        # - 0: the view of the current Alibaba Cloud account.
        # - 1: the view of all accounts in the enterprise.
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

