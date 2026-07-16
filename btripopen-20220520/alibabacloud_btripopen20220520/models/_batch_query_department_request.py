# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchQueryDepartmentRequest(DaraModel):
    def __init__(
        self,
        modified_time_greater_or_equal_than: str = None,
        out_dept_id: str = None,
        page_size: int = None,
        page_token: str = None,
    ):
        self.modified_time_greater_or_equal_than = modified_time_greater_or_equal_than
        self.out_dept_id = out_dept_id
        self.page_size = page_size
        self.page_token = page_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.modified_time_greater_or_equal_than is not None:
            result['modified_time_greater_or_equal_than'] = self.modified_time_greater_or_equal_than

        if self.out_dept_id is not None:
            result['out_dept_id'] = self.out_dept_id

        if self.page_size is not None:
            result['page_size'] = self.page_size

        if self.page_token is not None:
            result['page_token'] = self.page_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modified_time_greater_or_equal_than') is not None:
            self.modified_time_greater_or_equal_than = m.get('modified_time_greater_or_equal_than')

        if m.get('out_dept_id') is not None:
            self.out_dept_id = m.get('out_dept_id')

        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')

        if m.get('page_token') is not None:
            self.page_token = m.get('page_token')

        return self

