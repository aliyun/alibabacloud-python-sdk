# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListUserIntentionsRequest(DaraModel):
    def __init__(
        self,
        area: str = None,
        biz_type: str = None,
        biz_types: str = None,
        intention_biz_id: str = None,
        page_num: int = None,
        page_size: int = None,
        sort_filed: str = None,
        sort_order: str = None,
        status: int = None,
        with_ext_info: bool = None,
    ):
        self.area = area
        self.biz_type = biz_type
        self.biz_types = biz_types
        self.intention_biz_id = intention_biz_id
        self.page_num = page_num
        self.page_size = page_size
        self.sort_filed = sort_filed
        self.sort_order = sort_order
        self.status = status
        self.with_ext_info = with_ext_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.area is not None:
            result['Area'] = self.area

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.biz_types is not None:
            result['BizTypes'] = self.biz_types

        if self.intention_biz_id is not None:
            result['IntentionBizId'] = self.intention_biz_id

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sort_filed is not None:
            result['SortFiled'] = self.sort_filed

        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order

        if self.status is not None:
            result['Status'] = self.status

        if self.with_ext_info is not None:
            result['WithExtInfo'] = self.with_ext_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('BizTypes') is not None:
            self.biz_types = m.get('BizTypes')

        if m.get('IntentionBizId') is not None:
            self.intention_biz_id = m.get('IntentionBizId')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SortFiled') is not None:
            self.sort_filed = m.get('SortFiled')

        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('WithExtInfo') is not None:
            self.with_ext_info = m.get('WithExtInfo')

        return self

