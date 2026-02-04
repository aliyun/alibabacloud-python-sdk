# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dts20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeDtsServiceLogResponseBody(DaraModel):
    def __init__(
        self,
        dynamic_code: str = None,
        dynamic_message: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        service_log_contexts: List[main_models.DescribeDtsServiceLogResponseBodyServiceLogContexts] = None,
        success: bool = None,
        total_record_count: int = None,
    ):
        # The dynamic error code. This parameter will be removed soon.
        self.dynamic_code = dynamic_code
        # The dynamic part in the error message. This parameter is used to replace the \\*\\*%s\\*\\* variable in the **ErrMessage** parameter.
        self.dynamic_message = dynamic_message
        # The error code returned if the request fails.
        self.err_code = err_code
        # The error message returned if the request fails.
        self.err_message = err_message
        # The HTTP status code that is returned.
        self.http_status_code = http_status_code
        # The page number of the returned page.
        self.page_number = page_number
        # The number of log entries returned per page.
        self.page_record_count = page_record_count
        # The ID of the request.
        self.request_id = request_id
        # The details of the logs.
        self.service_log_contexts = service_log_contexts
        # Indicates whether the request is successful.
        self.success = success
        # The total number of logs that meet the query conditions.
        self.total_record_count = total_record_count

    def validate(self):
        if self.service_log_contexts:
            for v1 in self.service_log_contexts:
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

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ServiceLogContexts'] = []
        if self.service_log_contexts is not None:
            for k1 in self.service_log_contexts:
                result['ServiceLogContexts'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['Success'] = self.success

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

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

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.service_log_contexts = []
        if m.get('ServiceLogContexts') is not None:
            for k1 in m.get('ServiceLogContexts'):
                temp_model = main_models.DescribeDtsServiceLogResponseBodyServiceLogContexts()
                self.service_log_contexts.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeDtsServiceLogResponseBodyServiceLogContexts(DaraModel):
    def __init__(
        self,
        context: str = None,
        state: str = None,
        time: str = None,
    ):
        # The log content.
        self.context = context
        # The log level.
        self.state = state
        # The time when the logs were collected. The time follows the ISO 8601 standard in the yyyy-MM-ddThh:mm:ssZ format. The time is displayed in UTC.
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.context is not None:
            result['Context'] = self.context

        if self.state is not None:
            result['State'] = self.state

        if self.time is not None:
            result['Time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Context') is not None:
            self.context = m.get('Context')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        return self

