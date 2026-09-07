# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTenantAppRequest(DaraModel):
    def __init__(
        self,
        key_name: str = None,
        page_number: int = None,
        page_size: int = None,
        source_type: str = None,
    ):
        # The application name keyword, matched by containment. If this parameter is not specified or is set to an empty string, no name-based filtering is applied. `%` can be used as a wildcard, and `_` is matched as a literal character.
        self.key_name = key_name
        # The page number, starting from 1. If this parameter is not specified or is set to a value less than or equal to 0, the value 1 is used.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 500. If this parameter is not specified, is set to a value less than or equal to 0, or is set to a value greater than 500, the value 20 is used.
        self.page_size = page_size
        # The application source. Valid values:
        # - MARKET: marketplace applications.
        # - TENANT: applications uploaded by the current tenant.
        # 
        # If this parameter is not specified, both types of visible applications are queried.
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key_name is not None:
            result['KeyName'] = self.key_name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyName') is not None:
            self.key_name = m.get('KeyName')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        return self

