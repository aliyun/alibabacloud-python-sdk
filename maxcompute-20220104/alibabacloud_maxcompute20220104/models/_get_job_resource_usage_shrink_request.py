# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetJobResourceUsageShrinkRequest(DaraModel):
    def __init__(
        self,
        date: str = None,
        job_owner_list_shrink: str = None,
        page_number: int = None,
        page_size: int = None,
        quota_nickname_list_shrink: str = None,
    ):
        # The date that is accurate to the day part for the query. The date must be in the yyyy-MM-dd format.
        # 
        # This parameter is required.
        self.date = date
        # The list of job executors.
        self.job_owner_list_shrink = job_owner_list_shrink
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The list of nicknames of quotas that are used by jobs.
        self.quota_nickname_list_shrink = quota_nickname_list_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date is not None:
            result['date'] = self.date

        if self.job_owner_list_shrink is not None:
            result['jobOwnerList'] = self.job_owner_list_shrink

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.quota_nickname_list_shrink is not None:
            result['quotaNicknameList'] = self.quota_nickname_list_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('date') is not None:
            self.date = m.get('date')

        if m.get('jobOwnerList') is not None:
            self.job_owner_list_shrink = m.get('jobOwnerList')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('quotaNicknameList') is not None:
            self.quota_nickname_list_shrink = m.get('quotaNicknameList')

        return self

