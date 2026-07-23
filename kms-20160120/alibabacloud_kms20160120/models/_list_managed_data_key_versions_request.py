# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListManagedDataKeyVersionsRequest(DaraModel):
    def __init__(
        self,
        data_key_name: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The name of the managed data key (DK) to query. This parameter is required.
        self.data_key_name = data_key_name
        # The page number. The value must be an integer greater than 0. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_key_name is not None:
            result['DataKeyName'] = self.data_key_name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataKeyName') is not None:
            self.data_key_name = m.get('DataKeyName')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

