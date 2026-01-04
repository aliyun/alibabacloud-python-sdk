# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateHaVipResponseBody(DaraModel):
    def __init__(
        self,
        ha_vip_ids: List[str] = None,
        request_id: str = None,
    ):
        # The IDs of the HAVIPs.
        self.ha_vip_ids = ha_vip_ids
        # Request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ha_vip_ids is not None:
            result['HaVipIds'] = self.ha_vip_ids

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HaVipIds') is not None:
            self.ha_vip_ids = m.get('HaVipIds')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

