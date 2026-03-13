# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UserQueryRequest(DaraModel):
    def __init__(
        self,
        modified_time_greater_or_equal_than: str = None,
        page_size: int = None,
        page_token: str = None,
        third_part_job_no: str = None,
    ):
        self.modified_time_greater_or_equal_than = modified_time_greater_or_equal_than
        self.page_size = page_size
        self.page_token = page_token
        self.third_part_job_no = third_part_job_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.modified_time_greater_or_equal_than is not None:
            result['modified_time_greater_or_equal_than'] = self.modified_time_greater_or_equal_than

        if self.page_size is not None:
            result['page_size'] = self.page_size

        if self.page_token is not None:
            result['page_token'] = self.page_token

        if self.third_part_job_no is not None:
            result['third_part_job_no'] = self.third_part_job_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modified_time_greater_or_equal_than') is not None:
            self.modified_time_greater_or_equal_than = m.get('modified_time_greater_or_equal_than')

        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')

        if m.get('page_token') is not None:
            self.page_token = m.get('page_token')

        if m.get('third_part_job_no') is not None:
            self.third_part_job_no = m.get('third_part_job_no')

        return self

