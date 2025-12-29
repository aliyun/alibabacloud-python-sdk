# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListUserKubeConfigStatesRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        # The page number.
        # 
        # *   Valid values: ≥ 1.
        # *   Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # *   Value values: 1 to 100.
        # *   Default value: 50.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['page_number'] = self.page_number

        if self.page_size is not None:
            result['page_size'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page_number') is not None:
            self.page_number = m.get('page_number')

        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')

        return self

