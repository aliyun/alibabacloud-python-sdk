# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RemoveWhiteListSettingShrinkRequest(DaraModel):
    def __init__(
        self,
        ids_shrink: str = None,
        service_code: str = None,
    ):
        # IDs of the whitelist to be deleted in bulk.
        self.ids_shrink = ids_shrink
        # ServiceCode for the real person cloud product, only value: **antcloudauth**.
        self.service_code = service_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ids_shrink is not None:
            result['Ids'] = self.ids_shrink

        if self.service_code is not None:
            result['ServiceCode'] = self.service_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids_shrink = m.get('Ids')

        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')

        return self

