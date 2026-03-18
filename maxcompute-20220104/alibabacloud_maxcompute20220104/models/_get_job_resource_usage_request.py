# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetJobResourceUsageRequest(DaraModel):
    def __init__(
        self,
        date: str = None,
        job_owner_list: List[str] = None,
        page_number: int = None,
        page_size: int = None,
        quota_nickname_list: List[str] = None,
    ):
        # This parameter is required.
        self.date = date
        self.job_owner_list = job_owner_list
        self.page_number = page_number
        self.page_size = page_size
        self.quota_nickname_list = quota_nickname_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date is not None:
            result['date'] = self.date

        if self.job_owner_list is not None:
            result['jobOwnerList'] = self.job_owner_list

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.quota_nickname_list is not None:
            result['quotaNicknameList'] = self.quota_nickname_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('date') is not None:
            self.date = m.get('date')

        if m.get('jobOwnerList') is not None:
            self.job_owner_list = m.get('jobOwnerList')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('quotaNicknameList') is not None:
            self.quota_nickname_list = m.get('quotaNicknameList')

        return self

