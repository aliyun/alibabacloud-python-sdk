# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetHistoryListByBizTypeRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_type: str = None,
        page: int = None,
        page_size: int = None,
    ):
        # This parameter is required.
        self.biz_id = biz_id
        # This parameter is required.
        self.biz_type = biz_type
        self.page = page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['bizId'] = self.biz_id

        if self.biz_type is not None:
            result['bizType'] = self.biz_type

        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizId') is not None:
            self.biz_id = m.get('bizId')

        if m.get('bizType') is not None:
            self.biz_type = m.get('bizType')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        return self

