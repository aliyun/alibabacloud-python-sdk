# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyConcernNecessityRequest(DaraModel):
    def __init__(
        self,
        concern_necessity: str = None,
    ):
        # The priorities to fix the vulnerabilities. Valid values:
        # 
        # *   asap: high
        # *   later: medium
        # *   nntf: low
        self.concern_necessity = concern_necessity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.concern_necessity is not None:
            result['ConcernNecessity'] = self.concern_necessity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConcernNecessity') is not None:
            self.concern_necessity = m.get('ConcernNecessity')

        return self

