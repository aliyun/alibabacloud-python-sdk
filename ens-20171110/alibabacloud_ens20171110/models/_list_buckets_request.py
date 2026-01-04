# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListBucketsRequest(DaraModel):
    def __init__(
        self,
        page_number: str = None,
        page_size: str = None,
        prefix: str = None,
    ):
        # The page number. Pages start from page 1.
        self.page_number = page_number
        # The maximum number of returned buckets. You can leave this parameter empty. The default value is 10. The value cannot be greater than 100.
        self.page_size = page_size
        # The prefix that returned bucket names must contain. If this parameter is not specified, prefix information will not be used as a filter.
        self.prefix = prefix

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

        if self.prefix is not None:
            result['Prefix'] = self.prefix

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')

        return self

