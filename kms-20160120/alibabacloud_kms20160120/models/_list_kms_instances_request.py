# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListKmsInstancesRequest(DaraModel):
    def __init__(
        self,
        filters: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.filters = filters
        # The number of the page to return. The default value is 1.
        self.page_number = page_number
        # The number of entries to return on each page. Valid values: 1 to 100. Default value: 20.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filters is not None:
            result['Filters'] = self.filters

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Filters') is not None:
            self.filters = m.get('Filters')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

