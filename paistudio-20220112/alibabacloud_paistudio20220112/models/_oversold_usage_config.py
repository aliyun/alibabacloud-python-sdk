# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OversoldUsageConfig(DaraModel):
    def __init__(
        self,
        disabled: str = None,
        disabled_by: str = None,
    ):
        self.disabled = disabled
        self.disabled_by = disabled_by

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disabled is not None:
            result['Disabled'] = self.disabled

        if self.disabled_by is not None:
            result['DisabledBy'] = self.disabled_by

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')

        if m.get('DisabledBy') is not None:
            self.disabled_by = m.get('DisabledBy')

        return self

