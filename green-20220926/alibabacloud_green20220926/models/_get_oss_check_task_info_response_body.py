# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_green20220926 import models as main_models
from darabonba.model import DaraModel

class GetOssCheckTaskInfoResponseBody(DaraModel):
    def __init__(
        self,
        buckets: str = None,
        config: main_models.GetOssCheckTaskInfoResponseBodyConfig = None,
        end_time: str = None,
        finish_num: int = None,
        is_inc: bool = None,
        last_execute_date: str = None,
        media_type: int = None,
        next_execute_date: str = None,
        object_num: int = None,
        request_id: str = None,
        search_num: int = None,
        start_time: str = None,
        status: int = None,
        task_id: str = None,
        task_name: str = None,
        task_type: str = None,
    ):
        self.buckets = buckets
        self.config = config
        self.end_time = end_time
        self.finish_num = finish_num
        self.is_inc = is_inc
        self.last_execute_date = last_execute_date
        self.media_type = media_type
        self.next_execute_date = next_execute_date
        self.object_num = object_num
        self.request_id = request_id
        self.search_num = search_num
        self.start_time = start_time
        self.status = status
        self.task_id = task_id
        self.task_name = task_name
        self.task_type = task_type

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.buckets is not None:
            result['Buckets'] = self.buckets

        if self.config is not None:
            result['Config'] = self.config.to_map()

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.finish_num is not None:
            result['FinishNum'] = self.finish_num

        if self.is_inc is not None:
            result['IsInc'] = self.is_inc

        if self.last_execute_date is not None:
            result['LastExecuteDate'] = self.last_execute_date

        if self.media_type is not None:
            result['MediaType'] = self.media_type

        if self.next_execute_date is not None:
            result['NextExecuteDate'] = self.next_execute_date

        if self.object_num is not None:
            result['ObjectNum'] = self.object_num

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.search_num is not None:
            result['SearchNum'] = self.search_num

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Buckets') is not None:
            self.buckets = m.get('Buckets')

        if m.get('Config') is not None:
            temp_model = main_models.GetOssCheckTaskInfoResponseBodyConfig()
            self.config = temp_model.from_map(m.get('Config'))

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('FinishNum') is not None:
            self.finish_num = m.get('FinishNum')

        if m.get('IsInc') is not None:
            self.is_inc = m.get('IsInc')

        if m.get('LastExecuteDate') is not None:
            self.last_execute_date = m.get('LastExecuteDate')

        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')

        if m.get('NextExecuteDate') is not None:
            self.next_execute_date = m.get('NextExecuteDate')

        if m.get('ObjectNum') is not None:
            self.object_num = m.get('ObjectNum')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SearchNum') is not None:
            self.search_num = m.get('SearchNum')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

class GetOssCheckTaskInfoResponseBodyConfig(DaraModel):
    def __init__(
        self,
        callback_id: int = None,
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
        prefix_filter_type: str = None,
        prefix_filters: List[str] = None,
        priority: int = None,
        referer: str = None,
        scan_limit: int = None,
        scan_no_file_type: bool = None,
        scan_resource_type: int = None,
        scan_service: List[str] = None,
        scan_service_infos: List[main_models.GetOssCheckTaskInfoResponseBodyConfigScanServiceInfos] = None,
        start_time: str = None,
        task_cycle: int = None,
        user_freeze_config: main_models.GetOssCheckTaskInfoResponseBodyConfigUserFreezeConfig = None,
    ):
        self.callback_id = callback_id
        self.distinct_history_tasks = distinct_history_tasks
        self.end_time = end_time
        self.execute_date = execute_date
        self.execute_time = execute_time
        self.freeze = freeze
        self.freeze_high_risk_1 = freeze_high_risk_1
        self.freeze_high_risk_2 = freeze_high_risk_2
        self.freeze_medium_risk_1 = freeze_medium_risk_1
        self.freeze_medium_risk_2 = freeze_medium_risk_2
        self.freeze_restore_path = freeze_restore_path
        self.freeze_type = freeze_type
        self.prefix_filter_type = prefix_filter_type
        self.prefix_filters = prefix_filters
        self.priority = priority
        # Referer。
        self.referer = referer
        self.scan_limit = scan_limit
        self.scan_no_file_type = scan_no_file_type
        self.scan_resource_type = scan_resource_type
        self.scan_service = scan_service
        self.scan_service_infos = scan_service_infos
        self.start_time = start_time
        self.task_cycle = task_cycle
        self.user_freeze_config = user_freeze_config

    def validate(self):
        if self.scan_service_infos:
            for v1 in self.scan_service_infos:
                 if v1:
                    v1.validate()
        if self.user_freeze_config:
            self.user_freeze_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.prefix_filter_type is not None:
            result['PrefixFilterType'] = self.prefix_filter_type

        if self.prefix_filters is not None:
            result['PrefixFilters'] = self.prefix_filters

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.referer is not None:
            result['Referer'] = self.referer

        if self.scan_limit is not None:
            result['ScanLimit'] = self.scan_limit

        if self.scan_no_file_type is not None:
            result['ScanNoFileType'] = self.scan_no_file_type

        if self.scan_resource_type is not None:
            result['ScanResourceType'] = self.scan_resource_type

        if self.scan_service is not None:
            result['ScanService'] = self.scan_service

        result['ScanServiceInfos'] = []
        if self.scan_service_infos is not None:
            for k1 in self.scan_service_infos:
                result['ScanServiceInfos'].append(k1.to_map() if k1 else None)

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.task_cycle is not None:
            result['TaskCycle'] = self.task_cycle

        if self.user_freeze_config is not None:
            result['UserFreezeConfig'] = self.user_freeze_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('PrefixFilterType') is not None:
            self.prefix_filter_type = m.get('PrefixFilterType')

        if m.get('PrefixFilters') is not None:
            self.prefix_filters = m.get('PrefixFilters')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('Referer') is not None:
            self.referer = m.get('Referer')

        if m.get('ScanLimit') is not None:
            self.scan_limit = m.get('ScanLimit')

        if m.get('ScanNoFileType') is not None:
            self.scan_no_file_type = m.get('ScanNoFileType')

        if m.get('ScanResourceType') is not None:
            self.scan_resource_type = m.get('ScanResourceType')

        if m.get('ScanService') is not None:
            self.scan_service = m.get('ScanService')

        self.scan_service_infos = []
        if m.get('ScanServiceInfos') is not None:
            for k1 in m.get('ScanServiceInfos'):
                temp_model = main_models.GetOssCheckTaskInfoResponseBodyConfigScanServiceInfos()
                self.scan_service_infos.append(temp_model.from_map(k1))

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TaskCycle') is not None:
            self.task_cycle = m.get('TaskCycle')

        if m.get('UserFreezeConfig') is not None:
            temp_model = main_models.GetOssCheckTaskInfoResponseBodyConfigUserFreezeConfig()
            self.user_freeze_config = temp_model.from_map(m.get('UserFreezeConfig'))

        return self

class GetOssCheckTaskInfoResponseBodyConfigUserFreezeConfig(DaraModel):
    def __init__(
        self,
        freeze_restore_path: str = None,
        freeze_type: str = None,
    ):
        self.freeze_restore_path = freeze_restore_path
        self.freeze_type = freeze_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.freeze_restore_path is not None:
            result['FreezeRestorePath'] = self.freeze_restore_path

        if self.freeze_type is not None:
            result['FreezeType'] = self.freeze_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FreezeRestorePath') is not None:
            self.freeze_restore_path = m.get('FreezeRestorePath')

        if m.get('FreezeType') is not None:
            self.freeze_type = m.get('FreezeType')

        return self

class GetOssCheckTaskInfoResponseBodyConfigScanServiceInfos(DaraModel):
    def __init__(
        self,
        copy_from: str = None,
        is_copy: bool = None,
        service_code: str = None,
        service_name: str = None,
    ):
        self.copy_from = copy_from
        self.is_copy = is_copy
        self.service_code = service_code
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.copy_from is not None:
            result['CopyFrom'] = self.copy_from

        if self.is_copy is not None:
            result['IsCopy'] = self.is_copy

        if self.service_code is not None:
            result['ServiceCode'] = self.service_code

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CopyFrom') is not None:
            self.copy_from = m.get('CopyFrom')

        if m.get('IsCopy') is not None:
            self.is_copy = m.get('IsCopy')

        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        return self

