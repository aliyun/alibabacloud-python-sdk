# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteHaVipsRequest(DaraModel):
    def __init__(
        self,
        ha_vip_ids: List[str] = None,
    ):
        # The IDs of high-availability virtual IP addresses (HAVIPs).
        # 
        # This parameter is required.
        self.ha_vip_ids = ha_vip_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ha_vip_ids is not None:
            result['HaVipIds'] = self.ha_vip_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HaVipIds') is not None:
            self.ha_vip_ids = m.get('HaVipIds')

        return self

