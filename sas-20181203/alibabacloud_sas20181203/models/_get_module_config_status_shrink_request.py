# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetModuleConfigStatusShrinkRequest(DaraModel):
    def __init__(
        self,
        module_names_shrink: str = None,
    ):
        # The service modules that you want to query.
        # 
        # This parameter is required.
        self.module_names_shrink = module_names_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.module_names_shrink is not None:
            result['ModuleNames'] = self.module_names_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModuleNames') is not None:
            self.module_names_shrink = m.get('ModuleNames')

        return self

