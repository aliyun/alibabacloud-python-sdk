# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetModuleConfigStatusRequest(DaraModel):
    def __init__(
        self,
        module_names: List[str] = None,
    ):
        # The service modules that you want to query.
        # 
        # This parameter is required.
        self.module_names = module_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.module_names is not None:
            result['ModuleNames'] = self.module_names

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModuleNames') is not None:
            self.module_names = m.get('ModuleNames')

        return self

