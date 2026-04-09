# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDomainsRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        search: str = None,
        without_metering_data: bool = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.search = search
        self.without_metering_data = without_metering_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.search is not None:
            result['Search'] = self.search

        if self.without_metering_data is not None:
            result['WithoutMeteringData'] = self.without_metering_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Search') is not None:
            self.search = m.get('Search')

        if m.get('WithoutMeteringData') is not None:
            self.without_metering_data = m.get('WithoutMeteringData')

        return self

