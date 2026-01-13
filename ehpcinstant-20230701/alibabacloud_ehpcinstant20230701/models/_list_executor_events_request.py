# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ehpcinstant20230701 import models as main_models
from darabonba.model import DaraModel

class ListExecutorEventsRequest(DaraModel):
    def __init__(
        self,
        filter: main_models.ListExecutorEventsRequestFilter = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # Queries the Executor filter conditions.
        self.filter = filter
        # The current page number.\\
        # Starting value: 1\\
        # Default value: 1
        self.page_number = page_number
        # The number of entries on the current page. Default value: 50. Maximum value: 100.
        self.page_size = page_size

    def validate(self):
        if self.filter:
            self.filter.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter is not None:
            result['Filter'] = self.filter.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Filter') is not None:
            temp_model = main_models.ListExecutorEventsRequestFilter()
            self.filter = temp_model.from_map(m.get('Filter'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

class ListExecutorEventsRequestFilter(DaraModel):
    def __init__(
        self,
        executor_ids: List[str] = None,
        job_id: str = None,
        level: str = None,
        time_after: int = None,
        time_before: int = None,
    ):
        # The list of executor IDs. A maximum of 100 IDs are supported.
        self.executor_ids = executor_ids
        # The job ID.
        self.job_id = job_id
        # The level of the running event. Valid value:
        # 
        # *   Normal
        # *   Warning
        # *   Error
        self.level = level
        # For jobs submitted after this time, the time in the region is converted into a Unix timestamp (UI8 regionfor Aliyun sites).
        self.time_after = time_after
        # For jobs submitted before this time, the time in the region is converted into a Unix timestamp (UI8 regionfor Aliyun sites).
        self.time_before = time_before

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.executor_ids is not None:
            result['ExecutorIds'] = self.executor_ids

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.level is not None:
            result['Level'] = self.level

        if self.time_after is not None:
            result['TimeAfter'] = self.time_after

        if self.time_before is not None:
            result['TimeBefore'] = self.time_before

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutorIds') is not None:
            self.executor_ids = m.get('ExecutorIds')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('TimeAfter') is not None:
            self.time_after = m.get('TimeAfter')

        if m.get('TimeBefore') is not None:
            self.time_before = m.get('TimeBefore')

        return self

