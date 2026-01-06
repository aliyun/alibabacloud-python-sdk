# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class QueryRobotUnsubscriptionResponseBody(DaraModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        unsubscribed_staff_ids: List[str] = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        # requestId
        self.request_id = request_id
        self.total_count = total_count
        self.unsubscribed_staff_ids = unsubscribed_staff_ids

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

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        if self.unsubscribed_staff_ids is not None:
            result['unsubscribedStaffIds'] = self.unsubscribed_staff_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        if m.get('unsubscribedStaffIds') is not None:
            self.unsubscribed_staff_ids = m.get('unsubscribedStaffIds')

        return self

