# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListComputeTask2Request(DaraModel):
    def __init__(
        self,
        client_id: int = None,
        page_num: int = None,
        page_size: int = None,
    ):
        self.client_id = client_id
        self.page_num = page_num
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id is not None:
            result['clientId'] = self.client_id

        if self.page_num is not None:
            result['pageNum'] = self.page_num

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientId') is not None:
            self.client_id = m.get('clientId')

        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        return self

