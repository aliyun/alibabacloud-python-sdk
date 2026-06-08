# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_ros20190910 import models as main_models
from darabonba.model import DaraModel

class GetDiagnosticResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        diagnostic_key: str = None,
        diagnostic_product: str = None,
        diagnostic_result: main_models.GetDiagnosticResponseBodyDiagnosticResult = None,
        diagnostic_time: str = None,
        http_code: str = None,
        http_status_code: int = None,
        message: str = None,
        recommends: Dict[str, Any] = None,
        report_id: str = None,
        request_id: str = None,
        status: str = None,
        status_reason: str = None,
        success: str = None,
    ):
        # The error code returned.
        self.code = code
        # The keyword in the diagnosis.
        self.diagnostic_key = diagnostic_key
        # The name of the diagnostic item.
        self.diagnostic_product = diagnostic_product
        # The diagnosis result.
        self.diagnostic_result = diagnostic_result
        # The time when the diagnosis was performed.
        self.diagnostic_time = diagnostic_time
        # The HTTP status code
        self.http_code = http_code
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # The error message returned.
        self.message = message
        # The suggestion for the diagnosis.
        self.recommends = recommends
        # The ID of the diagnostic report.
        self.report_id = report_id
        # The request ID.
        self.request_id = request_id
        # The diagnosis status. Valid values:
        # 
        # *   Running: The diagnosis is in progress.
        # *   Complete: The diagnosis is complete.
        # *   Failed: The diagnosis failed.
        self.status = status
        # The reason for the diagnosis status.
        self.status_reason = status_reason
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.diagnostic_result:
            self.diagnostic_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.diagnostic_key is not None:
            result['DiagnosticKey'] = self.diagnostic_key

        if self.diagnostic_product is not None:
            result['DiagnosticProduct'] = self.diagnostic_product

        if self.diagnostic_result is not None:
            result['DiagnosticResult'] = self.diagnostic_result.to_map()

        if self.diagnostic_time is not None:
            result['DiagnosticTime'] = self.diagnostic_time

        if self.http_code is not None:
            result['HttpCode'] = self.http_code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.recommends is not None:
            result['Recommends'] = self.recommends

        if self.report_id is not None:
            result['ReportId'] = self.report_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DiagnosticKey') is not None:
            self.diagnostic_key = m.get('DiagnosticKey')

        if m.get('DiagnosticProduct') is not None:
            self.diagnostic_product = m.get('DiagnosticProduct')

        if m.get('DiagnosticResult') is not None:
            temp_model = main_models.GetDiagnosticResponseBodyDiagnosticResult()
            self.diagnostic_result = temp_model.from_map(m.get('DiagnosticResult'))

        if m.get('DiagnosticTime') is not None:
            self.diagnostic_time = m.get('DiagnosticTime')

        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Recommends') is not None:
            self.recommends = m.get('Recommends')

        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetDiagnosticResponseBodyDiagnosticResult(DaraModel):
    def __init__(
        self,
        failed_resources: Dict[str, Any] = None,
        ros_action_messages: Dict[str, Any] = None,
        stack_messages: Dict[str, Any] = None,
    ):
        # The resources that failed to be diagnosed.
        self.failed_resources = failed_resources
        # The information about Resource Orchestration Service (ROS) calling.
        self.ros_action_messages = ros_action_messages
        # The stack information.
        self.stack_messages = stack_messages

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed_resources is not None:
            result['FailedResources'] = self.failed_resources

        if self.ros_action_messages is not None:
            result['RosActionMessages'] = self.ros_action_messages

        if self.stack_messages is not None:
            result['StackMessages'] = self.stack_messages

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailedResources') is not None:
            self.failed_resources = m.get('FailedResources')

        if m.get('RosActionMessages') is not None:
            self.ros_action_messages = m.get('RosActionMessages')

        if m.get('StackMessages') is not None:
            self.stack_messages = m.get('StackMessages')

        return self

