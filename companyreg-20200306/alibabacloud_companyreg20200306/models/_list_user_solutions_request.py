# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListUserSolutionsRequest(DaraModel):
    def __init__(
        self,
        biz_type: str = None,
        exist_status: List[int] = None,
        intention_biz_id: str = None,
        page_num: int = None,
        page_size: int = None,
    ):
        self.biz_type = biz_type
        self.exist_status = exist_status
        self.intention_biz_id = intention_biz_id
        self.page_num = page_num
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.exist_status is not None:
            result['ExistStatus'] = self.exist_status

        if self.intention_biz_id is not None:
            result['IntentionBizId'] = self.intention_biz_id

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('ExistStatus') is not None:
            self.exist_status = m.get('ExistStatus')

        if m.get('IntentionBizId') is not None:
            self.intention_biz_id = m.get('IntentionBizId')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

