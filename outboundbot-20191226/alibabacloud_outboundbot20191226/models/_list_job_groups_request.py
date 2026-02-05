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
        self.async_query = async_query
        self.end_time = end_time
        # This parameter is required.
        self.instance_id = instance_id
        self.job_group_status_filter = job_group_status_filter
        self.only_min_concurrency_enabled = only_min_concurrency_enabled
        # This parameter is required.
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size
        self.search_text = search_text
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

