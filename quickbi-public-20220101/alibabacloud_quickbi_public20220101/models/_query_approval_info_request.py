# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryApprovalInfoRequest(DaraModel):
    def __init__(
        self,
        page: int = None,
        page_size: int = None,
        status: int = None,
        user_id: str = None,
    ):
        # Page number, default is 1.
        self.page = page
        # Number of rows per page, default is 1000.
        self.page_size = page_size
        # Approval status:
        # - 0: Pending
        # - 1: Processed
        # 
        # This parameter is required.
        self.status = status
        # Current approver user ID, qbi user ID.
        # 
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.status is not None:
            result['Status'] = self.status

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

