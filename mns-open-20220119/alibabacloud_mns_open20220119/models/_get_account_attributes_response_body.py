# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_mns_open20220119 import models as main_models
from darabonba.model import DaraModel

class GetAccountAttributesResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetAccountAttributesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        # The response code.
        self.code = code
        # The response data.
        self.data = data
        # The response message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The response status.
        self.status = status
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetAccountAttributesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetAccountAttributesResponseBodyData(DaraModel):
    def __init__(
        self,
        log_enabled: bool = None,
        log_store_name: str = None,
        message_trace_enabled: bool = None,
        project_name: str = None,
    ):
        # Indicates whether the Log Management feature is enabled.
        self.log_enabled = log_enabled
        # The name of the Simple Log Service Logstore.
        self.log_store_name = log_store_name
        # Indicates whether the message trace feature is enabled.
        self.message_trace_enabled = message_trace_enabled
        # The name of the Simple Log Service project.
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.log_enabled is not None:
            result['LogEnabled'] = self.log_enabled

        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name

        if self.message_trace_enabled is not None:
            result['MessageTraceEnabled'] = self.message_trace_enabled

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogEnabled') is not None:
            self.log_enabled = m.get('LogEnabled')

        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')

        if m.get('MessageTraceEnabled') is not None:
            self.message_trace_enabled = m.get('MessageTraceEnabled')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        return self

