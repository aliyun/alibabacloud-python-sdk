# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetImageDefectDetectionTaskResultResponseBody(DaraModel):
    def __init__(
        self,
        abnormality_reason: str = None,
        abnormality_score: float = None,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        result: str = None,
        risk_code: str = None,
        status: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        # **The image abnormality reason.** This field is returned only when `Status` is `succeeded`.
        self.abnormality_reason = abnormality_reason
        # **The image abnormality score.** The value ranges from 0 to 1. A higher value indicates a more severe image abnormality. This field is returned only when `Status` is `succeeded`.
        self.abnormality_score = abnormality_score
        # **The business error code.** The value "OK" is returned for successful requests.
        self.code = code
        # **The HTTP status code.** The value 200 is returned for successful requests.
        self.http_status_code = http_status_code
        # The failure reason. This field is returned only when `Status` is `failed`.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The raw downstream detection result (JSON string). The `AbnormalityScore` and `AbnormalityReason` fields are parsed from this raw result. The raw result is retained for debugging and passing through newly added upstream fields.
        self.result = result
        # The risk code. **This field is deprecated and has no meaning.** Determine whether an abnormality exists based on the AbnormalityScore, AbnormalityReason, and Result fields.
        self.risk_code = risk_code
        # **The task status.** Valid values:
        # - `running`: The task is running.
        # - `succeeded`: The task is completed.
        # - `failed`: The task failed.
        self.status = status
        # Indicates whether the request was successful.
        self.success = success
        # **The task ID.**
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.abnormality_reason is not None:
            result['AbnormalityReason'] = self.abnormality_reason

        if self.abnormality_score is not None:
            result['AbnormalityScore'] = self.abnormality_score

        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result

        if self.risk_code is not None:
            result['RiskCode'] = self.risk_code

        if self.status is not None:
            result['Status'] = self.status

        if self.success is not None:
            result['Success'] = self.success

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbnormalityReason') is not None:
            self.abnormality_reason = m.get('AbnormalityReason')

        if m.get('AbnormalityScore') is not None:
            self.abnormality_score = m.get('AbnormalityScore')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('RiskCode') is not None:
            self.risk_code = m.get('RiskCode')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

