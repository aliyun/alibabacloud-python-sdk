# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateSessionNetworkConfig(DaraModel):
    def __init__(
        self,
        allow_out: List[str] = None,
        deny_out: List[str] = None,
    ):
        self.allow_out = allow_out
        self.deny_out = deny_out

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_out is not None:
            result['allowOut'] = self.allow_out

        if self.deny_out is not None:
            result['denyOut'] = self.deny_out

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allowOut') is not None:
            self.allow_out = m.get('allowOut')

        if m.get('denyOut') is not None:
            self.deny_out = m.get('denyOut')

        return self

