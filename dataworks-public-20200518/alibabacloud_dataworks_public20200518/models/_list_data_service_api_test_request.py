# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDataServiceApiTestRequest(DaraModel):
    def __init__(
        self,
        api_id: int = None,
        page_size: int = None,
    ):
        # The ID of the DataService Studio API on which tests are performed.
        # 
        # This parameter is required.
        self.api_id = api_id
        # The number of entries to return on each page. Maximum value: 100.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_id is not None:
            result['ApiId'] = self.api_id

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

