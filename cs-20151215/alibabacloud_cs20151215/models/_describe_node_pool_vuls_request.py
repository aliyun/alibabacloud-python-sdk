# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeNodePoolVulsRequest(DaraModel):
    def __init__(
        self,
        necessity: str = None,
    ):
        # The vulnerability fix urgency levels to query. Separate multiple levels with commas (,). Valid values:
        # 
        # - `asap`: high
        # - `later`: medium
        # - `nntf`: low.
        self.necessity = necessity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.necessity is not None:
            result['necessity'] = self.necessity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('necessity') is not None:
            self.necessity = m.get('necessity')

        return self

