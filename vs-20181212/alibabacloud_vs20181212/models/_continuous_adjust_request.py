# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ContinuousAdjustRequest(DaraModel):
    def __init__(
        self,
        focus: str = None,
        id: str = None,
        iris: str = None,
        owner_id: int = None,
    ):
        self.focus = focus
        # This parameter is required.
        self.id = id
        self.iris = iris
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.focus is not None:
            result['Focus'] = self.focus

        if self.id is not None:
            result['Id'] = self.id

        if self.iris is not None:
            result['Iris'] = self.iris

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Focus') is not None:
            self.focus = m.get('Focus')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Iris') is not None:
            self.iris = m.get('Iris')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        return self

