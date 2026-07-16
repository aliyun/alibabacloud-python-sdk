# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sddp20190103 import models as main_models
from darabonba.model import DaraModel

class DescribeDataMaskingRunHistoryResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        items: List[main_models.DescribeDataMaskingRunHistoryResponseBodyItems] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.current_page = current_page
        # A list of data masking task details.
        self.items = items
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeDataMaskingRunHistoryResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDataMaskingRunHistoryResponseBodyItems(DaraModel):
    def __init__(
        self,
        conflict_count: int = None,
        dst_type: int = None,
        dst_type_code: str = None,
        end_time: int = None,
        fail_code: str = None,
        fail_msg: str = None,
        has_download_file: int = None,
        has_sub_process: int = None,
        id: int = None,
        masking_count: int = None,
        percentage: int = None,
        run_index: int = None,
        src_table_name: str = None,
        src_type: int = None,
        src_type_code: str = None,
        start_time: int = None,
        status: int = None,
        task_id: str = None,
        type: int = None,
    ):
        # The number of data conflicts. This is the number of rows to be inserted into the destination table that conflict with existing data.
        self.conflict_count = conflict_count
        # The type of service to which the masked data is destined. Valid values: **1** for MaxCompute, **2** for OSS, **3** for ADS, **4** for OTS, and **5** for RDS.
        self.dst_type = dst_type
        # The type of the destination service. Valid values include **MaxCompute, OSS, ADS, OTS, and RDS**.
        self.dst_type_code = dst_type_code
        # The time when the execution ended. This is a UNIX timestamp in milliseconds.
        self.end_time = end_time
        # The error code returned when the task fails. This parameter has a value only if the task fails.
        self.fail_code = fail_code
        # The reason the task failed.
        self.fail_msg = fail_msg
        # Indicates whether a download file is available.
        # 
        # - **1**: Yes.
        # 
        # - **0**: No.
        self.has_download_file = has_download_file
        # The number of created subtasks.
        self.has_sub_process = has_sub_process
        # The ID of the execution record.
        self.id = id
        # The number of masked rows.
        self.masking_count = masking_count
        # The execution progress.
        self.percentage = percentage
        # The number of times the task has been executed.
        self.run_index = run_index
        # The name of the source table.
        self.src_table_name = src_table_name
        # The type of service to which the source data belongs. Valid values: **1** for MaxCompute, **2** for OSS, **3** for ADS, **4** for OTS, and **5** for RDS.
        self.src_type = src_type
        # The type of the source service. Valid values include **MaxCompute, OSS, ADS, OTS, and RDS**.
        self.src_type_code = src_type_code
        # The time when the execution started. This is a UNIX timestamp in milliseconds.
        self.start_time = start_time
        # The execution status of the task. Valid values:
        # 
        # - -**1**: pending.
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
        # The ID of the task.
        self.task_id = task_id
        # The execution method. Valid values:
        # 
        # - **1**: manual.
        # 
        # - **2**: scheduled.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conflict_count is not None:
            result['ConflictCount'] = self.conflict_count

        if self.dst_type is not None:
            result['DstType'] = self.dst_type

        if self.dst_type_code is not None:
            result['DstTypeCode'] = self.dst_type_code

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.fail_code is not None:
            result['FailCode'] = self.fail_code

        if self.fail_msg is not None:
            result['FailMsg'] = self.fail_msg

        if self.has_download_file is not None:
            result['HasDownloadFile'] = self.has_download_file

        if self.has_sub_process is not None:
            result['HasSubProcess'] = self.has_sub_process

        if self.id is not None:
            result['Id'] = self.id

        if self.masking_count is not None:
            result['MaskingCount'] = self.masking_count

        if self.percentage is not None:
            result['Percentage'] = self.percentage

        if self.run_index is not None:
            result['RunIndex'] = self.run_index

        if self.src_table_name is not None:
            result['SrcTableName'] = self.src_table_name

        if self.src_type is not None:
            result['SrcType'] = self.src_type

        if self.src_type_code is not None:
            result['SrcTypeCode'] = self.src_type_code

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConflictCount') is not None:
            self.conflict_count = m.get('ConflictCount')

        if m.get('DstType') is not None:
            self.dst_type = m.get('DstType')

        if m.get('DstTypeCode') is not None:
            self.dst_type_code = m.get('DstTypeCode')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('FailCode') is not None:
            self.fail_code = m.get('FailCode')

        if m.get('FailMsg') is not None:
            self.fail_msg = m.get('FailMsg')

        if m.get('HasDownloadFile') is not None:
            self.has_download_file = m.get('HasDownloadFile')

        if m.get('HasSubProcess') is not None:
            self.has_sub_process = m.get('HasSubProcess')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MaskingCount') is not None:
            self.masking_count = m.get('MaskingCount')

        if m.get('Percentage') is not None:
            self.percentage = m.get('Percentage')

        if m.get('RunIndex') is not None:
            self.run_index = m.get('RunIndex')

        if m.get('SrcTableName') is not None:
            self.src_table_name = m.get('SrcTableName')

        if m.get('SrcType') is not None:
            self.src_type = m.get('SrcType')

        if m.get('SrcTypeCode') is not None:
            self.src_type_code = m.get('SrcTypeCode')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

