# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UserAPICountInfo(DaraModel):
    def __init__(
        self,
        api_type: str = None,
        scope: str = None,
        used_count: int = None,
    ):
        self.api_type = api_type
        self.scope = scope
        self.used_count = used_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_type is not None:
            result['apiType'] = self.api_type

        if self.scope is not None:
            result['scope'] = self.scope

        if self.used_count is not None:
            result['usedCount'] = self.used_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiType') is not None:
            self.api_type = m.get('apiType')

        if m.get('scope') is not None:
            self.scope = m.get('scope')

        if m.get('usedCount') is not None:
            self.used_count = m.get('usedCount')

        return self

