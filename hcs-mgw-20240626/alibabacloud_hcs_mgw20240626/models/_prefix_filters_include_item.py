# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class PrefixFiltersIncludeItem(DaraModel):
    def __init__(
        self,
        prefix: List[str] = None,
    ):
        # The full object key prefix. A maximum of 10,000 prefixes are supported by default, and each prefix can be up to 1,024 bytes in length.
        self.prefix = prefix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.prefix is not None:
            result['Prefix'] = self.prefix

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')

        return self

