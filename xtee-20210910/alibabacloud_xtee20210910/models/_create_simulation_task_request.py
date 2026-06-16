# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSimulationTaskRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        data_source_config: str = None,
        data_source_type: str = None,
        end_time: int = None,
        event_code: str = None,
        filters_str: str = None,
        reg_id: str = None,
        rules_str: str = None,
        run_task: bool = None,
        start_time: int = None,
        task_name: str = None,
    ):
        # The language type for the request and response. Default value: **zh**. Valid values:
        # - **zh**: Chinese
        # - **en**: English.
        self.lang = lang
        # The datasource config.
        self.data_source_config = data_source_config
        # The data source type.
        self.data_source_type = data_source_type
        # The end time, in milliseconds (ms).
        # 
        # This parameter is required.
        self.end_time = end_time
        # The event code.
        # 
        # This parameter is required.
        self.event_code = event_code
        # The filter.
        self.filters_str = filters_str
        # The region code.
        self.reg_id = reg_id
        # The list of policies.
        # 
        # This parameter is required.
        self.rules_str = rules_str
        # Specifies whether to run the task immediately.
        # 
        # This parameter is required.
        self.run_task = run_task
        # The start time, in milliseconds (ms).
        # 
        # This parameter is required.
        self.start_time = start_time
        # The task name.
        # 
        # This parameter is required.
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.data_source_config is not None:
            result['dataSourceConfig'] = self.data_source_config

        if self.data_source_type is not None:
            result['dataSourceType'] = self.data_source_type

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.event_code is not None:
            result['eventCode'] = self.event_code

        if self.filters_str is not None:
            result['filtersStr'] = self.filters_str

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.rules_str is not None:
            result['rulesStr'] = self.rules_str

        if self.run_task is not None:
            result['runTask'] = self.run_task

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.task_name is not None:
            result['taskName'] = self.task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('dataSourceConfig') is not None:
            self.data_source_config = m.get('dataSourceConfig')

        if m.get('dataSourceType') is not None:
            self.data_source_type = m.get('dataSourceType')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('eventCode') is not None:
            self.event_code = m.get('eventCode')

        if m.get('filtersStr') is not None:
            self.filters_str = m.get('filtersStr')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('rulesStr') is not None:
            self.rules_str = m.get('rulesStr')

        if m.get('runTask') is not None:
            self.run_task = m.get('runTask')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('taskName') is not None:
            self.task_name = m.get('taskName')

        return self

