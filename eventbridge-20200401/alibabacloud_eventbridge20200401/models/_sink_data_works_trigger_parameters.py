# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SinkDataWorksTriggerParameters(DaraModel):
    def __init__(
        self,
        enable: str = None,
    ):
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['Enable'] = self.enable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        return self

