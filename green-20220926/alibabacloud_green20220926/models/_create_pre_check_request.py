# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePreCheckRequest(DaraModel):
    def __init__(
        self,
        buckets: str = None,
        distinct_history_tasks: bool = None,
        end_time: str = None,
        is_inc: bool = None,
        media_type: int = None,
        prefix_filter_type: str = None,
        prefix_filters: str = None,
        priority: int = None,
        region_id: str = None,
        scan_limit: int = None,
        scan_no_file_type: bool = None,
        scan_service: str = None,
        start_time: str = None,
        task_name: str = None,
    ):
        # Buckets.
        self.buckets = buckets
        # Whether to deduplicate historical detected tasks.
        self.distinct_history_tasks = distinct_history_tasks
        # Task end time.
        self.end_time = end_time
        # Whether it is a scheduled scan task.
        self.is_inc = is_inc
        # Media type.
        self.media_type = media_type
        # Prefix filter type.
        self.prefix_filter_type = prefix_filter_type
        # Prefixes.
        self.prefix_filters = prefix_filters
        # Priority.
        self.priority = priority
        # Region ID.
        self.region_id = region_id
        # Scan limit count.
        self.scan_limit = scan_limit
        # Whether to scan images without file extensions.
        self.scan_no_file_type = scan_no_file_type
        # Scan service code.
        self.scan_service = scan_service
        # Task start time.
        self.start_time = start_time
        # Task name.
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.buckets is not None:
            result['Buckets'] = self.buckets

        if self.distinct_history_tasks is not None:
            result['DistinctHistoryTasks'] = self.distinct_history_tasks

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.is_inc is not None:
            result['IsInc'] = self.is_inc

        if self.media_type is not None:
            result['MediaType'] = self.media_type

        if self.prefix_filter_type is not None:
            result['PrefixFilterType'] = self.prefix_filter_type

        if self.prefix_filters is not None:
            result['PrefixFilters'] = self.prefix_filters

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.scan_limit is not None:
            result['ScanLimit'] = self.scan_limit

        if self.scan_no_file_type is not None:
            result['ScanNoFileType'] = self.scan_no_file_type

        if self.scan_service is not None:
            result['ScanService'] = self.scan_service

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Buckets') is not None:
            self.buckets = m.get('Buckets')

        if m.get('DistinctHistoryTasks') is not None:
            self.distinct_history_tasks = m.get('DistinctHistoryTasks')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('IsInc') is not None:
            self.is_inc = m.get('IsInc')

        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')

        if m.get('PrefixFilterType') is not None:
            self.prefix_filter_type = m.get('PrefixFilterType')

        if m.get('PrefixFilters') is not None:
            self.prefix_filters = m.get('PrefixFilters')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ScanLimit') is not None:
            self.scan_limit = m.get('ScanLimit')

        if m.get('ScanNoFileType') is not None:
            self.scan_no_file_type = m.get('ScanNoFileType')

        if m.get('ScanService') is not None:
            self.scan_service = m.get('ScanService')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        return self

