# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListIntentionNoteRequest(DaraModel):
    def __init__(
        self,
        begin_time: int = None,
        biz_type: str = None,
        end_time: int = None,
        intention_biz_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.begin_time = begin_time
        self.biz_type = biz_type
        self.end_time = end_time
        # This parameter is required.
        self.intention_biz_id = intention_biz_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.intention_biz_id is not None:
            result['IntentionBizId'] = self.intention_biz_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('IntentionBizId') is not None:
            self.intention_biz_id = m.get('IntentionBizId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

