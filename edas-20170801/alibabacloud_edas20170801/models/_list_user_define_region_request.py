# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListUserDefineRegionRequest(DaraModel):
    def __init__(
        self,
        debug_enable: bool = None,
    ):
        # Indicates whether remote debugging is allowed.
        self.debug_enable = debug_enable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.debug_enable is not None:
            result['DebugEnable'] = self.debug_enable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DebugEnable') is not None:
            self.debug_enable = m.get('DebugEnable')

        return self

