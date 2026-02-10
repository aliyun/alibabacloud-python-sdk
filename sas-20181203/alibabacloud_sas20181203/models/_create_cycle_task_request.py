# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCycleTaskRequest(DaraModel):
    def __init__(
        self,
        enable: int = None,
        first_date_str: int = None,
        interval_period: int = None,
        param: str = None,
        period_unit: str = None,
        source: str = None,
        target_end_time: int = None,
        target_start_time: int = None,
        task_name: str = None,
        task_type: str = None,
    ):
        # Specifies whether to enable the task. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        # 
        # This parameter is required.
        self.enable = enable
        # The first time when the task is performed.
        # 
        # This parameter is required.
        self.first_date_str = first_date_str
        # The interval of the task.
        # 
        # This parameter is required.
        self.interval_period = interval_period
        # The additional information.
        self.param = param
        # The unit of the scan interval. Valid values:
        # 
        # *   **day**: days
        # *   **hour**: hours
        # 
        # This parameter is required.
        self.period_unit = period_unit
        # The additional source for the task.
        self.source = source
        # The time when the task ends. Unit: hours.
        # 
        # This parameter is required.
        self.target_end_time = target_end_time
        # The time when the task is started. Unit: hours.
        # 
        # This parameter is required.
        self.target_start_time = target_start_time
        # The name of the task. Valid values:
        # 
        # *   **VIRUS_VUL_SCHEDULE_SCAN**: virus scan task
        # *   **IMAGE_SCAN**: image scan task
        # *   **EMG_VUL_SCHEDULE_SCAN**: urgent vulnerability scan task
        # 
        # This parameter is required.
        self.task_name = task_name
        # The type of the task. Valid values:
        # 
        # *   **VIRUS_VUL_SCHEDULE_SCAN**: virus scan task
        # *   **IMAGE_SCAN**: image scan task
        # *   **EMG_VUL_SCHEDULE_SCAN**: urgent vulnerability scan task
        # 
        # This parameter is required.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['Enable'] = self.enable

        if self.first_date_str is not None:
            result['FirstDateStr'] = self.first_date_str

        if self.interval_period is not None:
            result['IntervalPeriod'] = self.interval_period

        if self.param is not None:
            result['Param'] = self.param

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.source is not None:
            result['Source'] = self.source

        if self.target_end_time is not None:
            result['TargetEndTime'] = self.target_end_time

        if self.target_start_time is not None:
            result['TargetStartTime'] = self.target_start_time

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('FirstDateStr') is not None:
            self.first_date_str = m.get('FirstDateStr')

        if m.get('IntervalPeriod') is not None:
            self.interval_period = m.get('IntervalPeriod')

        if m.get('Param') is not None:
            self.param = m.get('Param')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('TargetEndTime') is not None:
            self.target_end_time = m.get('TargetEndTime')

        if m.get('TargetStartTime') is not None:
            self.target_start_time = m.get('TargetStartTime')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

