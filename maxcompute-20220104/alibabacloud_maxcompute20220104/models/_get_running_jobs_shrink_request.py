# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetRunningJobsShrinkRequest(DaraModel):
    def __init__(
        self,
        from_: int = None,
        job_owner_list_shrink: str = None,
        page_number: int = None,
        page_size: int = None,
        quota_nickname_list_shrink: str = None,
        to: int = None,
    ):
        # The time when the query starts. This parameter specifies the time when a job is submitted.
        # 
        # *   The time range that is specified by the **from** and **to** request parameters is a closed interval. The start time and end time are included in the range. If the value of **from** is the same as the value of **to**, the time range is invalid, and a null value is returned.
        # *   The value is a UNIX timestamp that represents the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # This parameter is required.
        self.from_ = from_
        # The list of job executors.
        self.job_owner_list_shrink = job_owner_list_shrink
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 20.
        self.page_size = page_size
        # The list of nicknames of quotas that are used by jobs.
        self.quota_nickname_list_shrink = quota_nickname_list_shrink
        # The time when the query ends. This parameter specifies the time when a job is submitted.
        # 
        # *   The time interval that is specified by the **from** and **to** request parameters is a closed interval. The start time and end time are included in the interval. If the value of **from** is the same as the value of **to**, the interval is invalid, and a null value is returned.
        # *   The value is a UNIX timestamp that represents the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # This parameter is required.
        self.to = to

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_ is not None:
            result['from'] = self.from_

        if self.job_owner_list_shrink is not None:
            result['jobOwnerList'] = self.job_owner_list_shrink

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.quota_nickname_list_shrink is not None:
            result['quotaNicknameList'] = self.quota_nickname_list_shrink

        if self.to is not None:
            result['to'] = self.to

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('from') is not None:
            self.from_ = m.get('from')

        if m.get('jobOwnerList') is not None:
            self.job_owner_list_shrink = m.get('jobOwnerList')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('quotaNicknameList') is not None:
            self.quota_nickname_list_shrink = m.get('quotaNicknameList')

        if m.get('to') is not None:
            self.to = m.get('to')

        return self

