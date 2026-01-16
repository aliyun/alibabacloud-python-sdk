# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateResidentResourcePoolInput(DaraModel):
    def __init__(
        self,
        name: str = None,
        use_scaling: bool = None,
    ):
        self.name = name
        self.use_scaling = use_scaling

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.use_scaling is not None:
            result['useScaling'] = self.use_scaling

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('useScaling') is not None:
            self.use_scaling = m.get('useScaling')

        return self

