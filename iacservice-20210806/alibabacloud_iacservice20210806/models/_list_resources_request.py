# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListResourcesRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        source_type: str = None,
        source_value: str = None,
        spec_type: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        # This parameter is required.
        self.source_type = source_type
        # This parameter is required.
        self.source_value = source_value
        # This parameter is required.
        self.spec_type = spec_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.source_value is not None:
            result['sourceValue'] = self.source_value

        if self.spec_type is not None:
            result['specType'] = self.spec_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('sourceValue') is not None:
            self.source_value = m.get('sourceValue')

        if m.get('specType') is not None:
            self.spec_type = m.get('specType')

        return self

