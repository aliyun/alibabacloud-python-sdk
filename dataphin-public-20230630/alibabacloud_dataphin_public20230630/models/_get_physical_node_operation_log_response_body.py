# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetPhysicalNodeOperationLogResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        operation_log_list: List[main_models.GetPhysicalNodeOperationLogResponseBodyOperationLogList] = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.operation_log_list = operation_log_list
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.operation_log_list:
            for v1 in self.operation_log_list:
                 if v1:
                    v1.validate()

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

        result['OperationLogList'] = []
        if self.operation_log_list is not None:
            for k1 in self.operation_log_list:
                result['OperationLogList'].append(k1.to_map() if k1 else None)

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

        self.operation_log_list = []
        if m.get('OperationLogList') is not None:
            for k1 in m.get('OperationLogList'):
                temp_model = main_models.GetPhysicalNodeOperationLogResponseBodyOperationLogList()
                self.operation_log_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetPhysicalNodeOperationLogResponseBodyOperationLogList(DaraModel):
    def __init__(
        self,
        context: str = None,
        operation_time: str = None,
        operation_type: str = None,
        operator: str = None,
        operator_name: str = None,
    ):
        self.context = context
        self.operation_time = operation_time
        self.operation_type = operation_type
        self.operator = operator
        self.operator_name = operator_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.context is not None:
            result['Context'] = self.context

        if self.operation_time is not None:
            result['OperationTime'] = self.operation_time

        if self.operation_type is not None:
            result['OperationType'] = self.operation_type

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.operator_name is not None:
            result['OperatorName'] = self.operator_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Context') is not None:
            self.context = m.get('Context')

        if m.get('OperationTime') is not None:
            self.operation_time = m.get('OperationTime')

        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('OperatorName') is not None:
            self.operator_name = m.get('OperatorName')

        return self

