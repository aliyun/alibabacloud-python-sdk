# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTranscodeJobsRequest(DaraModel):
    def __init__(
        self,
        end_of_create_time: str = None,
        next_page_token: str = None,
        order_by: str = None,
        page_size: int = None,
        parent_job_id: str = None,
        start_of_create_time: str = None,
        status: str = None,
    ):
        # The end of the time range to filter jobs by their creation time. The time must be in UTC and formatted as `yyyy-MM-ddTHH:mm:ssZ`.
        self.end_of_create_time = end_of_create_time
        # The token for the next page of results. Not required for the first page.
        self.next_page_token = next_page_token
        # The sort order. Valid values:
        # 
        # - `CreateTimeDesc`: Sorts by creation time in descending order.
        # 
        # - `CreateTimeAsc`: Sorts by creation time in ascending order.
        self.order_by = order_by
        # The number of entries per page. Valid values: 1-100. Default: 20.
        self.page_size = page_size
        # Filters by job ID.
        self.parent_job_id = parent_job_id
        # The start of the time range to filter jobs by their creation time. The time must be in UTC and formatted as `yyyy-MM-ddTHH:mm:ssZ`.
        self.start_of_create_time = start_of_create_time
        # The job status. Valid values:
        # 
        # - `Init`: Submitted.
        # 
        # - `Success`: Succeeded.
        # 
        # - `Fail`: Failed.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_of_create_time is not None:
            result['EndOfCreateTime'] = self.end_of_create_time

        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.parent_job_id is not None:
            result['ParentJobId'] = self.parent_job_id

        if self.start_of_create_time is not None:
            result['StartOfCreateTime'] = self.start_of_create_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndOfCreateTime') is not None:
            self.end_of_create_time = m.get('EndOfCreateTime')

        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ParentJobId') is not None:
            self.parent_job_id = m.get('ParentJobId')

        if m.get('StartOfCreateTime') is not None:
            self.start_of_create_time = m.get('StartOfCreateTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

