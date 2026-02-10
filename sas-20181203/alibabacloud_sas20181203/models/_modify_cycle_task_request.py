# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyCycleTaskRequest(DaraModel):
    def __init__(
        self,
        config_id: str = None,
        enable: int = None,
        first_date_str: int = None,
        interval_period: int = None,
        param: str = None,
        period_unit: str = None,
        target_end_time: int = None,
        target_start_time: int = None,
        task_name: str = None,
        task_type: str = None,
    ):
        # The ID of the task configuration.
        # 
        # >  You can call the [DescribeCycleTaskList](~~DescribeCycleTaskList~~) operation to query the IDs of task configurations.
        # 
        # This parameter is required.
        self.config_id = config_id
        # Specifies whether to enable the task. Valid values:
        # 
        # *   **1**: enables the task.
        # *   **0**: disables the task.
        self.enable = enable
        # The time when the task first started.
        self.first_date_str = first_date_str
        # The interval at which the task is run.
        self.interval_period = interval_period
        # The additional information.
        self.param = param
        # The unit of the scan interval. Valid values:
        # 
        # *   **day**
        # *   **hour**
        self.period_unit = period_unit
        # The end time of the task. The time must be a time frame.
        self.target_end_time = target_end_time
        # The start time of the task. The start time must be a time frame.
        self.target_start_time = target_start_time
        # The name of the task. Valid values:
        # 
        # *   **VIRUS_VUL_SCHEDULE_SCAN**: virus detection task
        # *   **IMAGE_SCAN**: image scan task
        # *   **EMG_VUL_SCHEDULE_SCAN**: urgent vulnerability scan task
        # 
        # Valid values:
        # 
        # *   VIRUS_VUL_SCHEDULE_SCAN
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     virus detection task
        # 
        #     <!-- -->
        # 
        # *   IMAGE_SCAN
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     image scan task
        # 
        #     <!-- -->
        # 
        # *   EMG_VUL_SCHEDULE_SCAN
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     urgent vulnerability scan task
        # 
        #     <!-- -->
        self.task_name = task_name
        # The type of the task. Valid values:
        # 
        # *   **VIRUS_VUL_SCHEDULE_SCAN**: virus detection task
        # *   **IMAGE_SCAN**: image scan task
        # *   **EMG_VUL_SCHEDULE_SCAN**: urgent vulnerability scan task
        # 
        # Valid values:
        # 
        # *   VIRUS_VUL_SCHEDULE_SCAN
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     virus detection task
        # 
        #     <!-- -->
        # 
        # *   IMAGE_SCAN
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     image scan task
        # 
        #     <!-- -->
        # 
        # *   EMG_VUL_SCHEDULE_SCAN
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     urgent vulnerability scan task
        # 
        #     <!-- -->
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_id is not None:
            result['ConfigId'] = self.config_id

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
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

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

        if m.get('TargetEndTime') is not None:
            self.target_end_time = m.get('TargetEndTime')

        if m.get('TargetStartTime') is not None:
            self.target_start_time = m.get('TargetStartTime')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

