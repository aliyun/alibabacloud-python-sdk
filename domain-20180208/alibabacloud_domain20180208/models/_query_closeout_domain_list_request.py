# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryCloseoutDomainListRequest(DaraModel):
    def __init__(
        self,
        current_id: int = None,
        page_size: int = None,
    ):
        self.current_id = current_id
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_id is not None:
            result['CurrentId'] = self.current_id

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentId') is not None:
            self.current_id = m.get('CurrentId')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

