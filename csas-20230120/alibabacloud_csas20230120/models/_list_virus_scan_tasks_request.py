# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListVirusScanTasksRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        end_time: int = None,
        page_size: int = None,
        performance_modes: List[str] = None,
        scan_modes: List[str] = None,
        start_time: int = None,
        status: int = None,
        task_ids: List[str] = None,
        user_group_id: str = None,
    ):
        # This parameter is required.
        self.current_page = current_page
        self.end_time = end_time
        # This parameter is required.
        self.page_size = page_size
        self.performance_modes = performance_modes
        self.scan_modes = scan_modes
        self.start_time = start_time
        self.status = status
        self.task_ids = task_ids
        self.user_group_id = user_group_id

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

        if self.performance_modes is not None:
            result['PerformanceModes'] = self.performance_modes

        if self.scan_modes is not None:
            result['ScanModes'] = self.scan_modes

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.task_ids is not None:
            result['TaskIds'] = self.task_ids

        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PerformanceModes') is not None:
            self.performance_modes = m.get('PerformanceModes')

        if m.get('ScanModes') is not None:
            self.scan_modes = m.get('ScanModes')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskIds') is not None:
            self.task_ids = m.get('TaskIds')

        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')

        return self

