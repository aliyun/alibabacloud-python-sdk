# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchQueryPushStatusShrinkRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        out_biz_ids_shrink: str = None,
        page_num: int = None,
        page_size: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        # This parameter is required.
        self.out_biz_ids_shrink = out_biz_ids_shrink
        self.page_num = page_num
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.out_biz_ids_shrink is not None:
            result['OutBizIds'] = self.out_biz_ids_shrink

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OutBizIds') is not None:
            self.out_biz_ids_shrink = m.get('OutBizIds')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

