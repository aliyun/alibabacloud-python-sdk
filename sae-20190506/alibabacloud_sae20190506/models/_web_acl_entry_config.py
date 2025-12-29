# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class WebAclEntryConfig(DaraModel):
    def __init__(
        self,
        entry: str = None,
    ):
        # This parameter is required.
        self.entry = entry

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entry is not None:
            result['Entry'] = self.entry

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Entry') is not None:
            self.entry = m.get('Entry')

        return self

