# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckUpgradeItemRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        region_id: str = None,
        role_for: str = None,
        upgrade_item_id: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # - **zh** (default): Chinese.
        # 
        # - **en**: English.
        self.lang = lang
        # The region of the Data Management center. Select a region based on the location of your assets. Valid values:
        # 
        # - cn-hangzhou: The assets are in the Chinese mainland.
        # 
        # - ap-southeast-1: The assets are in a region outside the Chinese mainland.
        self.region_id = region_id
        # The user ID of a member. An administrator can use this parameter to switch to the member\\"s perspective.
        self.role_for = role_for
        # The ID of the upgrade item.
        self.upgrade_item_id = upgrade_item_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        if self.upgrade_item_id is not None:
            result['UpgradeItemId'] = self.upgrade_item_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('UpgradeItemId') is not None:
            self.upgrade_item_id = m.get('UpgradeItemId')

        return self

