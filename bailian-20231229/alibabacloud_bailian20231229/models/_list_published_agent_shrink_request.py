# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPublishedAgentShrinkRequest(DaraModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        sub_types_shrink: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.sub_types_shrink = sub_types_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_no is not None:
            result['pageNo'] = self.page_no

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.sub_types_shrink is not None:
            result['subTypes'] = self.sub_types_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('subTypes') is not None:
            self.sub_types_shrink = m.get('subTypes')

        return self

