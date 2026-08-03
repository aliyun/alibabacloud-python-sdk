# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeScenesRequest(DaraModel):
    def __init__(
        self,
        search_code: str = None,
    ):
        # The search keyword. This operation performs a case-insensitive, fuzzy match.
        self.search_code = search_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.search_code is not None:
            result['SearchCode'] = self.search_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SearchCode') is not None:
            self.search_code = m.get('SearchCode')

        return self

