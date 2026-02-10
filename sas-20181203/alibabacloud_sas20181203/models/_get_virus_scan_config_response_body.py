# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetVirusScanConfigResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetVirusScanConfigResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned if the request was successful.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetVirusScanConfigResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetVirusScanConfigResponseBodyData(DaraModel):
    def __init__(
        self,
        addition_type: List[str] = None,
        config_id: str = None,
        enable: int = None,
        interval_period: int = None,
        period_unit: str = None,
        scan_path: List[str] = None,
        scan_type: str = None,
        selection_key: str = None,
        target_end_time: int = None,
        target_start_time: int = None,
        task_type: str = None,
    ):
        # Extended scan types.
        self.addition_type = addition_type
        # The ID of the task configuration.
        # 
        # > You can call the [DescribeCycleTaskList](~~DescribeCycleTaskList~~) operation to query the IDs of task configurations.
        self.config_id = config_id
        # Indicates whether the periodic scan feature is enabled. Valid value:
        # 
        # *   **1**: The feature is enabled
        # *   **0**: The feature is disabled.
        self.enable = enable
        # The interval at which virus scan tasks are run.
        self.interval_period = interval_period
        # The unit of the interval at which virus scan tasks are run.
        # 
        # *   The value is fixed as **day**.
        self.period_unit = period_unit
        # The file paths.
        self.scan_path = scan_path
        # The type of the virus scan task. Valid values:
        # 
        # *   **system**: automatic scan.
        # *   **user**: custom scan.
        self.scan_type = scan_type
        # The key that stores the asset information.
        # 
        # > You can call the [GetAssetSelectionConfig](~~GetAssetSelectionConfig~~) operation to obtain the key value.
        self.selection_key = selection_key
        # The end time of the virus scan task. The time is a time frame.
        self.target_end_time = target_end_time
        # The start time of the virus scan task. The time is a time frame.
        self.target_start_time = target_start_time
        # The type of the task. Valid value:
        # 
        # *   **VIRUS_VUL_SCHEDULE_SCAN**: a virus scan task.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addition_type is not None:
            result['AdditionType'] = self.addition_type

        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.interval_period is not None:
            result['IntervalPeriod'] = self.interval_period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.scan_path is not None:
            result['ScanPath'] = self.scan_path

        if self.scan_type is not None:
            result['ScanType'] = self.scan_type

        if self.selection_key is not None:
            result['SelectionKey'] = self.selection_key

        if self.target_end_time is not None:
            result['TargetEndTime'] = self.target_end_time

        if self.target_start_time is not None:
            result['TargetStartTime'] = self.target_start_time

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdditionType') is not None:
            self.addition_type = m.get('AdditionType')

        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('IntervalPeriod') is not None:
            self.interval_period = m.get('IntervalPeriod')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('ScanPath') is not None:
            self.scan_path = m.get('ScanPath')

        if m.get('ScanType') is not None:
            self.scan_type = m.get('ScanType')

        if m.get('SelectionKey') is not None:
            self.selection_key = m.get('SelectionKey')

        if m.get('TargetEndTime') is not None:
            self.target_end_time = m.get('TargetEndTime')

        if m.get('TargetStartTime') is not None:
            self.target_start_time = m.get('TargetStartTime')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

