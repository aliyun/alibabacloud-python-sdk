# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCycleTaskRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
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
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values: true: performs only a dry run without performing the actual operation. false: performs the actual request. Default value: false.
        self.dry_run = dry_run
        # Specifies whether to enable the task. Valid values:
        # - **1**: Enable.
        # - **0**: Disable.
        # 
        # This parameter is required.
        self.enable = enable
        # The time of the first execution.
        # 
        # This parameter is required.
        self.first_date_str = first_date_str
        # The interval period.
        # 
        # This parameter is required.
        self.interval_period = interval_period
        # The extended information field.
        # 
        # > Note: This parameter is required. If you do not specify this parameter, the API returns an error. The value is a JSON-formatted string that must contain at least the targetInfo array.
        self.param = param
        # The unit of the scan period. Valid values:
        # - **day**: day.
        # - **hour**: hour.
        # 
        # This parameter is required.
        self.period_unit = period_unit
        # The source from which the task is created.
        self.source = source
        # The end time of the task, in hours.
        # 
        # This parameter is required.
        self.target_end_time = target_end_time
        # The start time of the task, in hours.
        # 
        # This parameter is required.
        self.target_start_time = target_start_time
        # The task name. This is a custom string used to identify the periodic scan task.
        # 
        # This parameter is required.
        self.task_name = task_name
        # The task type. Valid values:
        # - **VIRUS_VUL_SCHEDULE_SCAN**: virus scan.
        # - **IMAGE_SCAN**: image scan.
        # - **EMG_VUL_SCHEDULE_SCAN**: emergency vulnerability scan.
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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

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
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

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

