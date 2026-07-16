# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListJobGroupsRequest(DaraModel):
    def __init__(
        self,
        async_query: bool = None,
        end_time: int = None,
        instance_id: str = None,
        job_group_status_filter: str = None,
        only_min_concurrency_enabled: bool = None,
        page_number: int = None,
        page_size: int = None,
        search_text: str = None,
        start_time: int = None,
    ):
        # Specifies whether to retrieve the query results asynchronously.
        self.async_query = async_query
        # The end of the time range for the query, based on the creation time of the job group. Specify the time as a UNIX timestamp in milliseconds.
        self.end_time = end_time
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Filters results by job status. To specify multiple statuses, separate them with commas. The statuses are combined with a logical OR. Valid values:
        # 
        # - **Draft**: The job group is a draft.
        # 
        # - **Scheduling**: The job group is being scheduled.
        # 
        # - **Executing**: The job group is executing.
        # 
        # - **Completed**: The job group has completed.
        # 
        # - **Paused**: The job group is paused.
        # 
        # - **Failed**: The job group has failed.
        # 
        # - **Cancelled**: The job group is canceled.
        # 
        # - **Initializing**: The job group is initializing.
        self.job_group_status_filter = job_group_status_filter
        # Specifies whether to return only job groups with minimum concurrency enabled.
        self.only_min_concurrency_enabled = only_min_concurrency_enabled
        # The page number.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries to return per page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The search text.
        self.search_text = search_text
        # The start of the time range for the query, based on the creation time of the job group. Specify the time as a UNIX timestamp in milliseconds.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.async_query is not None:
            result['AsyncQuery'] = self.async_query

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.job_group_status_filter is not None:
            result['JobGroupStatusFilter'] = self.job_group_status_filter

        if self.only_min_concurrency_enabled is not None:
            result['OnlyMinConcurrencyEnabled'] = self.only_min_concurrency_enabled

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.search_text is not None:
            result['SearchText'] = self.search_text

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsyncQuery') is not None:
            self.async_query = m.get('AsyncQuery')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('JobGroupStatusFilter') is not None:
            self.job_group_status_filter = m.get('JobGroupStatusFilter')

        if m.get('OnlyMinConcurrencyEnabled') is not None:
            self.only_min_concurrency_enabled = m.get('OnlyMinConcurrencyEnabled')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SearchText') is not None:
            self.search_text = m.get('SearchText')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

