# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListOperationProcessRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        end_time: int = None,
        page_size: int = None,
        start_time: int = None,
        status_codes: List[int] = None,
        task_ids: List[str] = None,
        task_sources: List[str] = None,
        task_types: List[str] = None,
    ):
        # The page number of the current page to display in a paged query. This parameter is used for paging.
        self.current_page = current_page
        # The end time of the query based on the task completion time. Unit: milliseconds.
        self.end_time = end_time
        # The number of entries per page.
        self.page_size = page_size
        # The start time of the query based on the task creation time. Unit: milliseconds.
        self.start_time = start_time
        # The list of task status codes.
        self.status_codes = status_codes
        # The list of task IDs.
        self.task_ids = task_ids
        # The list of task sources.
        self.task_sources = task_sources
        # The task type. Valid values:
        # - CHECK_ALL: full check.
        # - CHECK_POLICY: check performed based on check items in the configured policy.
        # - CHECK_SCHEDULE: scheduled check.
        # - CHECK_ITEM: check performed based on specified check items.
        # - CHECK_INSTANCE: check performed based on specified check items and instances.
        self.task_types = task_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status_codes is not None:
            result['StatusCodes'] = self.status_codes

        if self.task_ids is not None:
            result['TaskIds'] = self.task_ids

        if self.task_sources is not None:
            result['TaskSources'] = self.task_sources

        if self.task_types is not None:
            result['TaskTypes'] = self.task_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StatusCodes') is not None:
            self.status_codes = m.get('StatusCodes')

        if m.get('TaskIds') is not None:
            self.task_ids = m.get('TaskIds')

        if m.get('TaskSources') is not None:
            self.task_sources = m.get('TaskSources')

        if m.get('TaskTypes') is not None:
            self.task_types = m.get('TaskTypes')

        return self

