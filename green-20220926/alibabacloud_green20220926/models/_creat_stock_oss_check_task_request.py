# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatStockOssCheckTaskRequest(DaraModel):
    def __init__(
        self,
        bucket_prefix_filter_config: str = None,
        buckets: str = None,
        callback_id: str = None,
        distinct_history_tasks: bool = None,
        end_time: str = None,
        execute_date: int = None,
        execute_time: str = None,
        freeze: bool = None,
        freeze_high_risk_1: bool = None,
        freeze_high_risk_2: bool = None,
        freeze_medium_risk_1: bool = None,
        freeze_medium_risk_2: bool = None,
        freeze_restore_path: str = None,
        freeze_type: str = None,
        is_inc: bool = None,
        media_type: int = None,
        prefix_filter_type: str = None,
        prefix_filters: str = None,
        priority: int = None,
        referer: str = None,
        region_id: str = None,
        scan_limit: int = None,
        scan_no_file_type: bool = None,
        scan_resource_type: str = None,
        scan_service: str = None,
        start_time: str = None,
        task_cycle: int = None,
        task_name: str = None,
        task_type: str = None,
    ):
        # The filter configuration for each bucket. The value can be parsed as a JSON map. The key is the bucket name, and the value is the filter configuration, which includes prefix/suffix filters and a list of filter strings.
        self.bucket_prefix_filter_config = bucket_prefix_filter_config
        # The storage buckets.
        self.buckets = buckets
        # The notification callback ID.
        self.callback_id = callback_id
        # Specifies whether to deduplicate against historically scanned tasks.
        self.distinct_history_tasks = distinct_history_tasks
        # The task end time. Format: `YYYY-MM-DD HH:mm:ss`.
        self.end_time = end_time
        # The execution date of the scheduled task. The value is in integer format.
        self.execute_date = execute_date
        # The expected execution time of the scheduled task. Format: `HH:mm:ss-HH:mm:ss`.
        self.execute_time = execute_time
        # Specifies whether to freeze files.
        self.freeze = freeze
        # Specifies whether to freeze high-risk images.
        self.freeze_high_risk_1 = freeze_high_risk_1
        # Specifies whether to freeze high-risk audio and text.
        self.freeze_high_risk_2 = freeze_high_risk_2
        # Specifies whether to freeze medium-risk images.
        self.freeze_medium_risk_1 = freeze_medium_risk_1
        # Specifies whether to freeze medium-risk audio and text.
        self.freeze_medium_risk_2 = freeze_medium_risk_2
        # The path to which frozen files are transferred.
        self.freeze_restore_path = freeze_restore_path
        # The freeze type.
        self.freeze_type = freeze_type
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
        # Referer。
        self.referer = referer
        # The region ID.
        self.region_id = region_id
        # The maximum number of files to scan.
        self.scan_limit = scan_limit
        # Specifies whether to scan images without file extensions.
        self.scan_no_file_type = scan_no_file_type
        # The type of files to scan.
        self.scan_resource_type = scan_resource_type
        # The scan service code.
        self.scan_service = scan_service
        # The task start time. Format: `YYYY-MM-DD HH:mm:ss`.
        self.start_time = start_time
        # The scheduling cycle.
        self.task_cycle = task_cycle
        # The task name.
        self.task_name = task_name
        # The task type.
        self.task_type = task_type

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

        if self.callback_id is not None:
            result['CallbackId'] = self.callback_id

        if self.distinct_history_tasks is not None:
            result['DistinctHistoryTasks'] = self.distinct_history_tasks

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.execute_date is not None:
            result['ExecuteDate'] = self.execute_date

        if self.execute_time is not None:
            result['ExecuteTime'] = self.execute_time

        if self.freeze is not None:
            result['Freeze'] = self.freeze

        if self.freeze_high_risk_1 is not None:
            result['FreezeHighRisk1'] = self.freeze_high_risk_1

        if self.freeze_high_risk_2 is not None:
            result['FreezeHighRisk2'] = self.freeze_high_risk_2

        if self.freeze_medium_risk_1 is not None:
            result['FreezeMediumRisk1'] = self.freeze_medium_risk_1

        if self.freeze_medium_risk_2 is not None:
            result['FreezeMediumRisk2'] = self.freeze_medium_risk_2

        if self.freeze_restore_path is not None:
            result['FreezeRestorePath'] = self.freeze_restore_path

        if self.freeze_type is not None:
            result['FreezeType'] = self.freeze_type

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

        if self.referer is not None:
            result['Referer'] = self.referer

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.scan_limit is not None:
            result['ScanLimit'] = self.scan_limit

        if self.scan_no_file_type is not None:
            result['ScanNoFileType'] = self.scan_no_file_type

        if self.scan_resource_type is not None:
            result['ScanResourceType'] = self.scan_resource_type

        if self.scan_service is not None:
            result['ScanService'] = self.scan_service

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.task_cycle is not None:
            result['TaskCycle'] = self.task_cycle

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketPrefixFilterConfig') is not None:
            self.bucket_prefix_filter_config = m.get('BucketPrefixFilterConfig')

        if m.get('Buckets') is not None:
            self.buckets = m.get('Buckets')

        if m.get('CallbackId') is not None:
            self.callback_id = m.get('CallbackId')

        if m.get('DistinctHistoryTasks') is not None:
            self.distinct_history_tasks = m.get('DistinctHistoryTasks')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ExecuteDate') is not None:
            self.execute_date = m.get('ExecuteDate')

        if m.get('ExecuteTime') is not None:
            self.execute_time = m.get('ExecuteTime')

        if m.get('Freeze') is not None:
            self.freeze = m.get('Freeze')

        if m.get('FreezeHighRisk1') is not None:
            self.freeze_high_risk_1 = m.get('FreezeHighRisk1')

        if m.get('FreezeHighRisk2') is not None:
            self.freeze_high_risk_2 = m.get('FreezeHighRisk2')

        if m.get('FreezeMediumRisk1') is not None:
            self.freeze_medium_risk_1 = m.get('FreezeMediumRisk1')

        if m.get('FreezeMediumRisk2') is not None:
            self.freeze_medium_risk_2 = m.get('FreezeMediumRisk2')

        if m.get('FreezeRestorePath') is not None:
            self.freeze_restore_path = m.get('FreezeRestorePath')

        if m.get('FreezeType') is not None:
            self.freeze_type = m.get('FreezeType')

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

        if m.get('Referer') is not None:
            self.referer = m.get('Referer')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ScanLimit') is not None:
            self.scan_limit = m.get('ScanLimit')

        if m.get('ScanNoFileType') is not None:
            self.scan_no_file_type = m.get('ScanNoFileType')

        if m.get('ScanResourceType') is not None:
            self.scan_resource_type = m.get('ScanResourceType')

        if m.get('ScanService') is not None:
            self.scan_service = m.get('ScanService')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TaskCycle') is not None:
            self.task_cycle = m.get('TaskCycle')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

