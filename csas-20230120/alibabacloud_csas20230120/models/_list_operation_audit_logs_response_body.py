# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class ListOperationAuditLogsResponseBody(DaraModel):
    def __init__(
        self,
        logs: List[main_models.ListOperationAuditLogsResponseBodyLogs] = None,
        request_id: str = None,
        total_num: int = None,
    ):
        # The list of administrator operation audit logs, sorted by operation time in descending order.
        self.logs = logs
        # Id of the request
        self.request_id = request_id
        # The total number of logs that match the query conditions.
        self.total_num = total_num

    def validate(self):
        if self.logs:
            for v1 in self.logs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Logs'] = []
        if self.logs is not None:
            for k1 in self.logs:
                result['Logs'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.logs = []
        if m.get('Logs') is not None:
            for k1 in m.get('Logs'):
                temp_model = main_models.ListOperationAuditLogsResponseBodyLogs()
                self.logs.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        return self

class ListOperationAuditLogsResponseBodyLogs(DaraModel):
    def __init__(
        self,
        after_action: str = None,
        before_action: str = None,
        error_code: str = None,
        error_message: str = None,
        event_type: str = None,
        operation_func: str = None,
        operation_page: str = None,
        operation_time: str = None,
        operation_type: str = None,
        operator_id: str = None,
        success: bool = None,
    ):
        # The post-operation snapshot. This value is recorded as-is by the audit framework without localization. This field is empty for historical logs that are not integrated with the audit framework.
        self.after_action = after_action
        # The pre-operation snapshot. This value is recorded as-is by the audit framework without localization. This field is empty for historical logs that are not integrated with the audit framework.
        self.before_action = before_action
        # The error code when the operation failed. This field is empty when the operation succeeded.
        self.error_code = error_code
        # The error message when the operation failed. This field is empty when the operation succeeded.
        self.error_message = error_message
        # The event source type. Valid values:
        # - **console**: console call.
        # - **sdk**: SDK call.
        self.event_type = event_type
        # The operation function module. The return value is localized based on the request language.
        self.operation_func = operation_func
        # The operation page. The return value is localized based on the request language.
        self.operation_page = operation_page
        # The operation time.
        self.operation_time = operation_time
        # The operation type. The return value is localized based on the request language.
        self.operation_type = operation_type
        # The Alibaba Cloud account ID (AliUid) of the operator.
        self.operator_id = operator_id
        # Indicates whether the operation succeeded.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.after_action is not None:
            result['AfterAction'] = self.after_action

        if self.before_action is not None:
            result['BeforeAction'] = self.before_action

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.event_type is not None:
            result['EventType'] = self.event_type

        if self.operation_func is not None:
            result['OperationFunc'] = self.operation_func

        if self.operation_page is not None:
            result['OperationPage'] = self.operation_page

        if self.operation_time is not None:
            result['OperationTime'] = self.operation_time

        if self.operation_type is not None:
            result['OperationType'] = self.operation_type

        if self.operator_id is not None:
            result['OperatorId'] = self.operator_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AfterAction') is not None:
            self.after_action = m.get('AfterAction')

        if m.get('BeforeAction') is not None:
            self.before_action = m.get('BeforeAction')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        if m.get('OperationFunc') is not None:
            self.operation_func = m.get('OperationFunc')

        if m.get('OperationPage') is not None:
            self.operation_page = m.get('OperationPage')

        if m.get('OperationTime') is not None:
            self.operation_time = m.get('OperationTime')

        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')

        if m.get('OperatorId') is not None:
            self.operator_id = m.get('OperatorId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

