# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyHaVipAttributeRequest(DaraModel):
    def __init__(
        self,
        ha_vip_id: str = None,
        name: str = None,
    ):
        # The ID of the HAVIP that you want to modify.
        # 
        # This parameter is required.
        self.ha_vip_id = ha_vip_id
        # The name of the HAVIP. The name must be 1 to 128 characters in length and cannot start with http:// or https://.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ha_vip_id is not None:
            result['HaVipId'] = self.ha_vip_id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HaVipId') is not None:
            self.ha_vip_id = m.get('HaVipId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

