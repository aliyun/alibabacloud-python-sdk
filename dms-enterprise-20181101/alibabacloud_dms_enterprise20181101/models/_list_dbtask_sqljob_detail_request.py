# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDBTaskSQLJobDetailRequest(DaraModel):
    def __init__(
        self,
        job_id: int = None,
        page_number: int = None,
        page_size: int = None,
        tid: int = None,
    ):
        # The ID of the SQL task. You can call the [ListDBTaskSQLJob](https://help.aliyun.com/document_detail/207049.html) operation to query the SQL task ID.
        # 
        # This parameter is required.
        self.job_id = job_id
        # The number of the page to return.
        self.page_number = page_number
        # The number of entries to return on each page.
        self.page_size = page_size
        # The ID of the tenant. You can call the [GetUserActiveTenant](https://help.aliyun.com/document_detail/198073.html) operation to query the tenant ID.
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

