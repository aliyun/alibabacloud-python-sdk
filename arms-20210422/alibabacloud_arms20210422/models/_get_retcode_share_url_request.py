# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetRetcodeShareUrlRequest(DaraModel):
    def __init__(
        self,
        pid: str = None,
    ):
        # This parameter is required.
        self.pid = pid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pid is not None:
            result['Pid'] = self.pid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')

        return self

