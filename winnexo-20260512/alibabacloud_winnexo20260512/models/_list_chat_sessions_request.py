# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListChatSessionsRequest(DaraModel):
    def __init__(
        self,
        digital_employee_name: str = None,
        keyword: str = None,
        page: int = None,
        page_size: int = None,
        tenant_id: str = None,
    ):
        # The list of digital employee names. A single string can be passed for backward compatibility with the legacy format.
        self.digital_employee_name = digital_employee_name
        # The rule name keyword for fuzzy match.
        self.keyword = keyword
        # The page number. Default value: 1. Pages start from page 1.
        self.page = page
        # The maximum number of data records to read in this request.
        self.page_size = page_size
        # The tenant ID to which the task belongs.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.digital_employee_name is not None:
            result['digitalEmployeeName'] = self.digital_employee_name

        if self.keyword is not None:
            result['keyword'] = self.keyword

        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('digitalEmployeeName') is not None:
            self.digital_employee_name = m.get('digitalEmployeeName')

        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

