# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConfigSetDeleteRequest(DaraModel):
    def __init__(
        self,
        ids: str = None,
        is_force: bool = None,
    ):
        self.ids = ids
        self.is_force = is_force

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ids is not None:
            result['Ids'] = self.ids

        if self.is_force is not None:
            result['IsForce'] = self.is_force

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')

        if m.get('IsForce') is not None:
            self.is_force = m.get('IsForce')

        return self

