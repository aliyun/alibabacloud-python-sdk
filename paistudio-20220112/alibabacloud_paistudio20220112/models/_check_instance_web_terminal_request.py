# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckInstanceWebTerminalRequest(DaraModel):
    def __init__(
        self,
        check_info: str = None,
    ):
        self.check_info = check_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_info is not None:
            result['CheckInfo'] = self.check_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckInfo') is not None:
            self.check_info = m.get('CheckInfo')

        return self

