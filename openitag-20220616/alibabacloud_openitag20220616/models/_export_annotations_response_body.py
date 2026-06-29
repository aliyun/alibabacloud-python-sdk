# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_openitag20220616 import models as main_models
from darabonba.model import DaraModel

class ExportAnnotationsResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        details: str = None,
        error_code: str = None,
        flow_job: main_models.FlowJobInfo = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Return encoding. The default value is 0, indicating Normal execution.
        self.code = code
        # Details.
        self.details = details
        # Error code.
        # - When Success is false, returns a business error code.
        # - When Success is true, returns an empty value.
        self.error_code = error_code
        # Pipeline.
        self.flow_job = flow_job
        # The response message of the request.
        # 
        # This parameter is required.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Indicates whether the operation succeeded. Valid values:
        # - true: Succeeded.
        # - false: Failed.
        self.success = success

    def validate(self):
        if self.flow_job:
            self.flow_job.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.details is not None:
            result['Details'] = self.details

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.flow_job is not None:
            result['FlowJob'] = self.flow_job.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Details') is not None:
            self.details = m.get('Details')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('FlowJob') is not None:
            temp_model = main_models.FlowJobInfo()
            self.flow_job = temp_model.from_map(m.get('FlowJob'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

