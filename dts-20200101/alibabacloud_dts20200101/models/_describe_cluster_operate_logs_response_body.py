# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dts20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeClusterOperateLogsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data_points: List[main_models.DescribeClusterOperateLogsResponseBodyDataPoints] = None,
        dynamic_message: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        success: bool = None,
        total_record_count: int = None,
    ):
        # The backend error code, which is incrementally numeric.
        self.code = code
        # The monitoring statistics information.
        self.data_points = data_points
        # The dynamic error message, which is used to replace the %s placeholder in the ErrMessage response parameter.
        self.dynamic_message = dynamic_message
        # The error code returned when the call fails.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The HTTP status code corresponding to the exception.
        self.http_status_code = http_status_code
        # The current page number.
        self.page_number = page_number
        # The number of entries displayed on the current page.
        self.page_record_count = page_record_count
        # The request ID.
        self.request_id = request_id
        # The call result.
        self.success = success
        # The total number of records.
        self.total_record_count = total_record_count

    def validate(self):
        if self.data_points:
            for v1 in self.data_points:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['DataPoints'] = []
        if self.data_points is not None:
            for k1 in self.data_points:
                result['DataPoints'].append(k1.to_map() if k1 else None)

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data_points = []
        if m.get('DataPoints') is not None:
            for k1 in m.get('DataPoints'):
                temp_model = main_models.DescribeClusterOperateLogsResponseBodyDataPoints()
                self.data_points.append(temp_model.from_map(k1))

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeClusterOperateLogsResponseBodyDataPoints(DaraModel):
    def __init__(
        self,
        content: str = None,
        id: str = None,
        log_datetime: int = None,
        new_value: str = None,
        old_value: str = None,
        operation_name: str = None,
        operation_user: str = None,
        success: int = None,
    ):
        # The additional remarks.
        self.content = content
        # The primary key of the log record table.
        self.id = id
        # The timestamp. Unit: milliseconds.
        self.log_datetime = log_datetime
        # The new parameter value when the operation type is update.
        self.new_value = new_value
        # The old parameter value when the operation type is update.
        self.old_value = old_value
        # The operation type.
        self.operation_name = operation_name
        # The operator.
        self.operation_user = operation_user
        # The call result. Indicates whether the call was successful. A value of **1** indicates success.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.id is not None:
            result['Id'] = self.id

        if self.log_datetime is not None:
            result['LogDatetime'] = self.log_datetime

        if self.new_value is not None:
            result['NewValue'] = self.new_value

        if self.old_value is not None:
            result['OldValue'] = self.old_value

        if self.operation_name is not None:
            result['OperationName'] = self.operation_name

        if self.operation_user is not None:
            result['OperationUser'] = self.operation_user

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LogDatetime') is not None:
            self.log_datetime = m.get('LogDatetime')

        if m.get('NewValue') is not None:
            self.new_value = m.get('NewValue')

        if m.get('OldValue') is not None:
            self.old_value = m.get('OldValue')

        if m.get('OperationName') is not None:
            self.operation_name = m.get('OperationName')

        if m.get('OperationUser') is not None:
            self.operation_user = m.get('OperationUser')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

