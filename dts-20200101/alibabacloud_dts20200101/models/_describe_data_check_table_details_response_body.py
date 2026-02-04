# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dts20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeDataCheckTableDetailsResponseBody(DaraModel):
    def __init__(
        self,
        diff_table_count: int = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        err_code: str = None,
        err_message: str = None,
        failed_table_count: int = None,
        finished_count: int = None,
        http_status_code: int = None,
        page_number: int = None,
        request_id: str = None,
        success: bool = None,
        table_details: List[main_models.DescribeDataCheckTableDetailsResponseBodyTableDetails] = None,
        total_count: int = None,
    ):
        # The number of tables that contain inconsistent data.
        self.diff_table_count = diff_table_count
        # The dynamic error code. This parameter will be discontinued in the future.
        self.dynamic_code = dynamic_code
        # The dynamic part in the error message. This parameter is used to replace the \\*\\*%s\\*\\* variable in the **ErrMessage** parameter.
        # 
        # > For example, if the returned value of the **ErrMessage** parameter is **The Value of Input Parameter %s is not valid** and the return value of the **DynamicMessage** parameter is **Type**, the specified **Type** parameter is invalid.
        self.dynamic_message = dynamic_message
        # The error code returned if the request failed.
        self.err_code = err_code
        # The error message returned if the request failed.
        self.err_message = err_message
        # The total number of data rows that were failed.
        self.failed_table_count = failed_table_count
        # The total number of data rows that were verified.
        self.finished_count = finished_count
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # The page number of the returned page.
        self.page_number = page_number
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success
        # The details of data verification results.
        self.table_details = table_details
        # The total number of tables on which data verification was performed.
        self.total_count = total_count

    def validate(self):
        if self.table_details:
            for v1 in self.table_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.diff_table_count is not None:
            result['DiffTableCount'] = self.diff_table_count

        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.failed_table_count is not None:
            result['FailedTableCount'] = self.failed_table_count

        if self.finished_count is not None:
            result['FinishedCount'] = self.finished_count

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        result['TableDetails'] = []
        if self.table_details is not None:
            for k1 in self.table_details:
                result['TableDetails'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiffTableCount') is not None:
            self.diff_table_count = m.get('DiffTableCount')

        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('FailedTableCount') is not None:
            self.failed_table_count = m.get('FailedTableCount')

        if m.get('FinishedCount') is not None:
            self.finished_count = m.get('FinishedCount')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        self.table_details = []
        if m.get('TableDetails') is not None:
            for k1 in m.get('TableDetails'):
                temp_model = main_models.DescribeDataCheckTableDetailsResponseBodyTableDetails()
                self.table_details.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDataCheckTableDetailsResponseBodyTableDetails(DaraModel):
    def __init__(
        self,
        boot_time: str = None,
        diff_count: int = None,
        error_code: int = None,
        finish_count: int = None,
        id: int = None,
        source_db_name: str = None,
        source_tb_name: str = None,
        status: str = None,
        target_db_name: str = None,
        target_tb_name: str = None,
        total_count: int = None,
    ):
        # The time when data verification was performed.
        self.boot_time = boot_time
        # The number of data rows that contain inconsistent data.
        self.diff_count = diff_count
        # The error code returned if the data verification task failed. Valid values:
        # 
        # *   **1**: The number of tables that do not contain primary keys exceeds the limit.
        # *   **2**: The number of data rows that contain inconsistent data exceeds 300.
        # *   **3**: One or more tables to be verified do not exist.
        # *   **4**: The SQL statements used for verifying data contain a syntax error.
        self.error_code = error_code
        # The number of data rows that were verified.
        self.finish_count = finish_count
        # The auto-increment primary key that is used to identify the data in a verification result.
        self.id = id
        # The name of the source database.
        self.source_db_name = source_db_name
        # The name of the source table.
        self.source_tb_name = source_tb_name
        # The status of data verification results. Valid values:
        # 
        # *   **0**: The data verification task was complete.
        # *   **2**: The data verification task was being initialized.
        # *   **3**: The data verification task was in progress.
        # *   **5**: The data verification task failed.
        self.status = status
        # The name of the destination database.
        self.target_db_name = target_db_name
        # The name of the destination table.
        self.target_tb_name = target_tb_name
        # The total number of data rows.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.boot_time is not None:
            result['BootTime'] = self.boot_time

        if self.diff_count is not None:
            result['DiffCount'] = self.diff_count

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.finish_count is not None:
            result['FinishCount'] = self.finish_count

        if self.id is not None:
            result['Id'] = self.id

        if self.source_db_name is not None:
            result['SourceDbName'] = self.source_db_name

        if self.source_tb_name is not None:
            result['SourceTbName'] = self.source_tb_name

        if self.status is not None:
            result['Status'] = self.status

        if self.target_db_name is not None:
            result['TargetDbName'] = self.target_db_name

        if self.target_tb_name is not None:
            result['TargetTbName'] = self.target_tb_name

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BootTime') is not None:
            self.boot_time = m.get('BootTime')

        if m.get('DiffCount') is not None:
            self.diff_count = m.get('DiffCount')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('FinishCount') is not None:
            self.finish_count = m.get('FinishCount')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('SourceDbName') is not None:
            self.source_db_name = m.get('SourceDbName')

        if m.get('SourceTbName') is not None:
            self.source_tb_name = m.get('SourceTbName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TargetDbName') is not None:
            self.target_db_name = m.get('TargetDbName')

        if m.get('TargetTbName') is not None:
            self.target_tb_name = m.get('TargetTbName')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

