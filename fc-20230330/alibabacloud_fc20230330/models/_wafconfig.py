# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class WAFConfig(DaraModel):
    def __init__(
        self,
        enable_waf: bool = None,
    ):
        self.enable_waf = enable_waf

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_waf is not None:
            result['enableWAF'] = self.enable_waf

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enableWAF') is not None:
            self.enable_waf = m.get('enableWAF')

        return self

