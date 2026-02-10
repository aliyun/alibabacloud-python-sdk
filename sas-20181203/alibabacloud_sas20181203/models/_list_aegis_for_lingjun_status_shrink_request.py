# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAegisForLingjunStatusShrinkRequest(DaraModel):
    def __init__(
        self,
        uuids_shrink: str = None,
    ):
        # List of unique UUIDs for Lingjun bare metal.
        self.uuids_shrink = uuids_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.uuids_shrink is not None:
            result['Uuids'] = self.uuids_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Uuids') is not None:
            self.uuids_shrink = m.get('Uuids')

        return self

