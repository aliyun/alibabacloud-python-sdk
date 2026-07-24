# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePreCheckRequest(DaraModel):
    def __init__(
        self,
        bucket_prefix_filter_config: str = None,
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
        # The filter configuration for each bucket. The value can be parsed as a JSON map. The key is the bucket name, and the value is the filter configuration, which includes prefix/suffix filters and a list of filter strings.
        self.bucket_prefix_filter_config = bucket_prefix_filter_config
        # The OSS buckets.
        self.buckets = buckets
        # Specifies whether to deduplicate against historically scanned tasks.
        self.distinct_history_tasks = distinct_history_tasks
        # The task end time. Format: YYYY-MM-DD HH:mm:ss.
        self.end_time = end_time
        # Specifies whether the task is a scheduled scan task.
        self.is_inc = is_inc
        # The media asset type.
        self.media_type = media_type
        # The prefix filter type.
        self.prefix_filter_type = prefix_filter_type
        # The prefixes.
        self.prefix_filters = prefix_filters
        # The priority.
        self.priority = priority
        # The region ID.
        self.region_id = region_id
        # The maximum number of items to scan.
        self.scan_limit = scan_limit
        # Specifies whether to scan images without file extensions.
        self.scan_no_file_type = scan_no_file_type
        # The scan service code.
        self.scan_service = scan_service
        # The task start time. Format: YYYY-MM-DD HH:mm:ss.
        self.start_time = start_time
        # The task name.
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_prefix_filter_config is not None:
            result['BucketPrefixFilterConfig'] = self.bucket_prefix_filter_config

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
        if m.get('BucketPrefixFilterConfig') is not None:
            self.bucket_prefix_filter_config = m.get('BucketPrefixFilterConfig')

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

