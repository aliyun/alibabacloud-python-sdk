# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListVpcEndpointsRequest(DaraModel):
    def __init__(
        self,
        page: int = None,
        size: int = None,
    ):
        # The number of the page to return.
        # 
        # Pages start from page 1. Default value: 1.
        self.page = page
        # The number of entries to return on each page. Default value: 20.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page is not None:
            result['page'] = self.page

        if self.size is not None:
            result['size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('size') is not None:
            self.size = m.get('size')

        return self

