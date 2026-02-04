# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dts20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeEtlJobLogsResponseBody(DaraModel):
    def __init__(
        self,
        dynamic_code: str = None,
        dynamic_message: str = None,
        err_code: str = None,
        err_message: str = None,
        etl_running_logs: List[main_models.DescribeEtlJobLogsResponseBodyEtlRunningLogs] = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic part in the error message.
        self.dynamic_message = dynamic_message
        # The error code. This example indicates that the specified ETL task ID is invalid.
        self.err_code = err_code
        # The error message. This example indicates that the specified ETL task ID does not exist. In this case, the ETL task may be deleted.
        self.err_message = err_message
        # The logs of ETL tasks.
        self.etl_running_logs = etl_running_logs
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call was successful. If the call failed, false is returned.
        self.success = success

    def validate(self):
        if self.etl_running_logs:
            for v1 in self.etl_running_logs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        result['EtlRunningLogs'] = []
        if self.etl_running_logs is not None:
            for k1 in self.etl_running_logs:
                result['EtlRunningLogs'].append(k1.to_map() if k1 else None)

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        self.etl_running_logs = []
        if m.get('EtlRunningLogs') is not None:
            for k1 in m.get('EtlRunningLogs'):
                temp_model = main_models.DescribeEtlJobLogsResponseBodyEtlRunningLogs()
                self.etl_running_logs.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeEtlJobLogsResponseBodyEtlRunningLogs(DaraModel):
    def __init__(
        self,
        content: str = None,
        content_key: str = None,
        etl_id: str = None,
        log_datetime: str = None,
        status: str = None,
        user_id: str = None,
    ):
        # The state of the ETL task.
        self.content = content
        # The module for which the logs are generated, such as the conversion module of ETL tasks.
        self.content_key = content_key
        # The ID of the ETL task.
        self.etl_id = etl_id
        # The time when the log was generated. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.log_datetime = log_datetime
        # The log level. Valid values: ERROR, WARN, INFO, and DEBUG.
        self.status = status
        # The ID of the user.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.content_key is not None:
            result['ContentKey'] = self.content_key

        if self.etl_id is not None:
            result['EtlId'] = self.etl_id

        if self.log_datetime is not None:
            result['LogDatetime'] = self.log_datetime

        if self.status is not None:
            result['Status'] = self.status

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('ContentKey') is not None:
            self.content_key = m.get('ContentKey')

        if m.get('EtlId') is not None:
            self.etl_id = m.get('EtlId')

        if m.get('LogDatetime') is not None:
            self.log_datetime = m.get('LogDatetime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

