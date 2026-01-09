# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListDomainsResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        domains: List[str] = None,
        total: int = None,
    ):
        # The number of domain names that are returned on the current page.
        self.count = count
        # The domain names.
        self.domains = domains
        # The total number of domain names that are returned.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['count'] = self.count

        if self.domains is not None:
            result['domains'] = self.domains

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')

        if m.get('domains') is not None:
            self.domains = m.get('domains')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

