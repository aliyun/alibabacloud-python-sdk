# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSimulationTaskCountRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        data_source_config: str = None,
        data_source_type: str = None,
        end_time: int = None,
        event_code: str = None,
        filters_str: str = None,
        reg_id: str = None,
        start_time: int = None,
    ):
        # Sets the language type for requests and received messages, default value is **zh**. Values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Data source configuration
        self.data_source_config = data_source_config
        # Data source type
        self.data_source_type = data_source_type
        # Task end time.
        # 
        # This parameter is required.
        self.end_time = end_time
        # Event code
        # 
        # This parameter is required.
        self.event_code = event_code
        # Filter
        self.filters_str = filters_str
        # Region code
        self.reg_id = reg_id
        # Task start time.
        # 
        # This parameter is required.
        self.start_time = start_time

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

        if self.start_time is not None:
            result['startTime'] = self.start_time

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

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        return self

