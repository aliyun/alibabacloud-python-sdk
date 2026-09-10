# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDataCheckColumnResultsRequest(DaraModel):
    def __init__(
        self,
        page_index: int = None,
        page_size: int = None,
        result_id: str = None,
    ):
        # The page number, starting from 1.
        self.page_index = page_index
        # The number of entries per page.
        self.page_size = page_size
        # The validation result ID.
        # 
        # This parameter is required.
        self.result_id = result_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_index is not None:
            result['pageIndex'] = self.page_index

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.result_id is not None:
            result['resultId'] = self.result_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('resultId') is not None:
            self.result_id = m.get('resultId')

        return self

