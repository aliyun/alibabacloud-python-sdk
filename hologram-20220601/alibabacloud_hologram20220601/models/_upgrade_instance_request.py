# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpgradeInstanceRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        type: str = None,
        upgrade_time: str = None,
    ):
        self.region_id = region_id
        self.type = type
        self.upgrade_time = upgrade_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.type is not None:
            result['type'] = self.type

        if self.upgrade_time is not None:
            result['upgradeTime'] = self.upgrade_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('upgradeTime') is not None:
            self.upgrade_time = m.get('upgradeTime')

        return self

