# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetRerunWorkflowInstancesResultResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.GetRerunWorkflowInstancesResultResponseBodyResult = None,
    ):
        # The request ID, used for log tracing and troubleshooting.
        self.request_id = request_id
        # The result of the workflow instance rerun.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.GetRerunWorkflowInstancesResultResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class GetRerunWorkflowInstancesResultResponseBodyResult(DaraModel):
    def __init__(
        self,
        failure_message: str = None,
        status: str = None,
    ):
        # The failure message. Returned if the rerun fails.
        self.failure_message = failure_message
        # The status. NotRun Success Failure
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failure_message is not None:
            result['FailureMessage'] = self.failure_message

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailureMessage') is not None:
            self.failure_message = m.get('FailureMessage')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

