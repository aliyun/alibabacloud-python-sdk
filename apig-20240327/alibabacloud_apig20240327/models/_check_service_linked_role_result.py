# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckServiceLinkedRoleResult(DaraModel):
    def __init__(
        self,
        existed: bool = None,
    ):
        self.existed = existed

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.existed is not None:
            result['existed'] = self.existed

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('existed') is not None:
            self.existed = m.get('existed')

        return self

