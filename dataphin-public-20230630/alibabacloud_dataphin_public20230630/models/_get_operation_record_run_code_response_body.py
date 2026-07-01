# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetOperationRecordRunCodeResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        operation_log_code_response: main_models.GetOperationRecordRunCodeResponseBodyOperationLogCodeResponse = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The backend response code.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The backend exception details.
        self.message = message
        # The operation log code response.
        self.operation_log_code_response = operation_log_code_response
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.operation_log_code_response:
            self.operation_log_code_response.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.operation_log_code_response is not None:
            result['OperationLogCodeResponse'] = self.operation_log_code_response.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('OperationLogCodeResponse') is not None:
            temp_model = main_models.GetOperationRecordRunCodeResponseBodyOperationLogCodeResponse()
            self.operation_log_code_response = temp_model.from_map(m.get('OperationLogCodeResponse'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetOperationRecordRunCodeResponseBodyOperationLogCodeResponse(DaraModel):
    def __init__(
        self,
        code: str = None,
        operator_id: int = None,
        operator_name: str = None,
        sql_num: int = None,
    ):
        # The code content.
        self.code = code
        # The operator ID.
        self.operator_id = operator_id
        # The operator name.
        self.operator_name = operator_name
        # The number of SQL statements.
        self.sql_num = sql_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.operator_id is not None:
            result['OperatorId'] = self.operator_id

        if self.operator_name is not None:
            result['OperatorName'] = self.operator_name

        if self.sql_num is not None:
            result['SqlNum'] = self.sql_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('OperatorId') is not None:
            self.operator_id = m.get('OperatorId')

        if m.get('OperatorName') is not None:
            self.operator_name = m.get('OperatorName')

        if m.get('SqlNum') is not None:
            self.sql_num = m.get('SqlNum')

        return self

