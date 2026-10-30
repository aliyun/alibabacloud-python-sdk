# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class GetCustomAgentImagePreparationResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetCustomAgentImagePreparationResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business status code.
        self.code = code
        # The preparation query result. Refer to the phase for the asynchronous execution status.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The response message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the API call is successful.
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
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetCustomAgentImagePreparationResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class GetCustomAgentImagePreparationResponseBodyData(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        error: main_models.GetCustomAgentImagePreparationResponseBodyDataError = None,
        failed_phase: str = None,
        phase: str = None,
        preparation_id: str = None,
    ):
        # The target agent ID.
        self.agent_id = agent_id
        # The error information. This field is returned only when the task fails. Otherwise, the value is null.
        self.error = error
        # The failed phase. This field is returned only when the status is FAILED. Otherwise, the value is null.
        self.failed_phase = failed_phase
        # The current phase. Only SUCCEEDED indicates that the deployment of the target version is successful.
        self.phase = phase
        # The console submission task ID.
        self.preparation_id = preparation_id

    def validate(self):
        if self.error:
            self.error.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['agentId'] = self.agent_id

        if self.error is not None:
            result['error'] = self.error.to_map()

        if self.failed_phase is not None:
            result['failedPhase'] = self.failed_phase

        if self.phase is not None:
            result['phase'] = self.phase

        if self.preparation_id is not None:
            result['preparationId'] = self.preparation_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')

        if m.get('error') is not None:
            temp_model = main_models.GetCustomAgentImagePreparationResponseBodyDataError()
            self.error = temp_model.from_map(m.get('error'))

        if m.get('failedPhase') is not None:
            self.failed_phase = m.get('failedPhase')

        if m.get('phase') is not None:
            self.phase = m.get('phase')

        if m.get('preparationId') is not None:
            self.preparation_id = m.get('preparationId')

        return self

class GetCustomAgentImagePreparationResponseBodyDataError(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # The business error code for image preparation. This code is used to identify the failure type. For the specific cause, refer to the message.
        self.code = code
        # The specific cause of the failure. This may include underlying errors such as image not found, authentication failure, network timeout, or certificate verification error. Passwords, tokens, or authentication headers are not returned. If the underlying system does not provide a cause, a general description is returned.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        return self

