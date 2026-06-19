# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateHaVipResponseBody(DaraModel):
    def __init__(
        self,
        ha_vip_id: str = None,
        request_id: str = None,
    ):
        self.ha_vip_id = ha_vip_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ha_vip_id is not None:
            result['HaVipId'] = self.ha_vip_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HaVipId') is not None:
            self.ha_vip_id = m.get('HaVipId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

