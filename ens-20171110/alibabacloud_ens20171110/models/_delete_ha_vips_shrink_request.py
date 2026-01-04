# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteHaVipsShrinkRequest(DaraModel):
    def __init__(
        self,
        ha_vip_ids_shrink: str = None,
    ):
        # The IDs of high-availability virtual IP addresses (HAVIPs).
        # 
        # This parameter is required.
        self.ha_vip_ids_shrink = ha_vip_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ha_vip_ids_shrink is not None:
            result['HaVipIds'] = self.ha_vip_ids_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HaVipIds') is not None:
            self.ha_vip_ids_shrink = m.get('HaVipIds')

        return self

