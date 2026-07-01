# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListMediaConvertJobsRequest(DaraModel):
    def __init__(
        self,
        end_of_create_time: str = None,
        job_id: str = None,
        next_page_token: str = None,
        order_by: str = None,
        page_size: int = None,
        start_of_create_time: str = None,
        status: str = None,
    ):
        # The end of the time range to filter jobs by creation time. The time must be in the `yyyy-MM-ddTHH:mm:ssZ` ISO 8601 format.
        self.end_of_create_time = end_of_create_time
        # Filters the results by job ID.
        self.job_id = job_id
        # The token for the next page of results. Leave this empty for the first request. To retrieve the next page, pass the `NextPageToken` value from the previous response.
        self.next_page_token = next_page_token
        # The sort order for the results. Valid values: `CreateTimeDesc` (descending by creation time) and `CreateTimeAsc` (ascending by creation time).
        self.order_by = order_by
        # The page size. Valid values: 1 to 100. Default value: 20.
        self.page_size = page_size
        # The start of the time range to filter jobs by creation time. The time must be in the `yyyy-MM-ddTHH:mm:ssZ` ISO 8601 format.
        self.start_of_create_time = start_of_create_time
        # The status of the job. Valid values:
        # 
        # - `Inited`: The job has been submitted.
        # 
        # - `Running`: The job is running.
        # 
        # - `Complete`: The job is complete.
        # 
        # - `Error`: The job failed due to an error.
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

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_of_create_time is not None:
            result['StartOfCreateTime'] = self.start_of_create_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndOfCreateTime') is not None:
            self.end_of_create_time = m.get('EndOfCreateTime')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartOfCreateTime') is not None:
            self.start_of_create_time = m.get('StartOfCreateTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

