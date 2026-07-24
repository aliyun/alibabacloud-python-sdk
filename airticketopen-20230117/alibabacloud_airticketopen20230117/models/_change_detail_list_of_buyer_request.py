# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChangeDetailListOfBuyerRequest(DaraModel):
    def __init__(
        self,
        page_index: int = None,
        page_size: int = None,
        utc_create_begin: int = None,
        utc_create_end: int = None,
    ):
        # The page index.
        self.page_index = page_index
        # The page size.
        self.page_size = page_size
        # The start time for change order creation. The value is a 13-digit UTC timestamp.
        self.utc_create_begin = utc_create_begin
        # The end time for change order creation. The value is a 13-digit UTC timestamp.
        self.utc_create_end = utc_create_end

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_index is not None:
            result['page_index'] = self.page_index

        if self.page_size is not None:
            result['page_size'] = self.page_size

        if self.utc_create_begin is not None:
            result['utc_create_begin'] = self.utc_create_begin

        if self.utc_create_end is not None:
            result['utc_create_end'] = self.utc_create_end

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page_index') is not None:
            self.page_index = m.get('page_index')

        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')

        if m.get('utc_create_begin') is not None:
            self.utc_create_begin = m.get('utc_create_begin')

        if m.get('utc_create_end') is not None:
            self.utc_create_end = m.get('utc_create_end')

        return self

