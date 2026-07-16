# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDataMaskingRunHistoryRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        dst_type: int = None,
        end_time: int = None,
        lang: str = None,
        main_process_id: int = None,
        page_size: int = None,
        src_table_name: str = None,
        src_type: int = None,
        start_time: int = None,
        status: int = None,
        task_id: str = None,
    ):
        # The page number to return.
        self.current_page = current_page
        # The type of service to which the masked data is destined. Valid values: **1** for MaxCompute, **2** for OSS, **3** for ADS, **4** for OTS, and **5** for RDS.
        self.dst_type = dst_type
        # The end time to query for task executions. This is a UNIX timestamp in milliseconds.
        self.end_time = end_time
        # The language of the request and response. Default value: **zh_cn**. Valid values:
        # 
        # - **zh_cn**: Chinese.
        # 
        # - **en_us**: English.
        self.lang = lang
        # The ID of the main task.
        # 
        # > If a task has subtasks, this parameter specifies the ID of the main task. Otherwise, this parameter is empty.
        self.main_process_id = main_process_id
        # The number of entries to return on each page.
        self.page_size = page_size
        # The name of the source table.
        self.src_table_name = src_table_name
        # The type of service to which the source data belongs. Valid values: **1** for MaxCompute, **2** for OSS, **3** for ADS, **4** for OTS, and **5** for RDS.
        self.src_type = src_type
        # The start time to query for task executions. This is a UNIX timestamp in milliseconds.
        self.start_time = start_time
        # The execution status of the task. Valid values:
        # 
        # - **-1**: pending.
        # 
        # - **0**: running.
        # 
        # - **1**: successful.
        # 
        # - **2**: failed.
        # 
        # - **3**: stopped by user.
        # 
        # - **4**: partially failed.
        self.status = status
        # The ID of the data masking task.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.dst_type is not None:
            result['DstType'] = self.dst_type

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.main_process_id is not None:
            result['MainProcessId'] = self.main_process_id

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.src_table_name is not None:
            result['SrcTableName'] = self.src_table_name

        if self.src_type is not None:
            result['SrcType'] = self.src_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('DstType') is not None:
            self.dst_type = m.get('DstType')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MainProcessId') is not None:
            self.main_process_id = m.get('MainProcessId')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SrcTableName') is not None:
            self.src_table_name = m.get('SrcTableName')

        if m.get('SrcType') is not None:
            self.src_type = m.get('SrcType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

