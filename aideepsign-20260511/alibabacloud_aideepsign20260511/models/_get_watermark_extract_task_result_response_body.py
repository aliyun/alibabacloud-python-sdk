# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetWatermarkExtractTaskResultResponseBody(DaraModel):
    def __init__(
        self,
        avg_acc: float = None,
        code: str = None,
        detected: bool = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
        task_id: str = None,
        watermark_content: str = None,
    ):
        # The average extraction confidence, ranging from 0 to 1. This parameter is returned only when Status is succeeded.
        self.avg_acc = avg_acc
        # The business error code. OK is returned if the request is successful.
        self.code = code
        # Indicates whether a watermark is detected.
        self.detected = detected
        # The HTTP status code. 200 is returned if the request is successful.
        self.http_status_code = http_status_code
        # The failure reason when the task fails. This parameter is returned only when Status is failed.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # The task status. Valid values:
        # - running: In progress.
        # - succeeded: Completed.
        # - failed: Failed.
        self.status = status
        # Indicates whether the request is successful.
        self.success = success
        # The dark watermark extraction task ID.
        self.task_id = task_id
        # The extracted watermark content. This parameter is returned only when `Status` is `succeeded` and `Detected=true`.
        self.watermark_content = watermark_content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avg_acc is not None:
            result['AvgAcc'] = self.avg_acc

        if self.code is not None:
            result['Code'] = self.code

        if self.detected is not None:
            result['Detected'] = self.detected

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.success is not None:
            result['Success'] = self.success

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.watermark_content is not None:
            result['WatermarkContent'] = self.watermark_content

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvgAcc') is not None:
            self.avg_acc = m.get('AvgAcc')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Detected') is not None:
            self.detected = m.get('Detected')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('WatermarkContent') is not None:
            self.watermark_content = m.get('WatermarkContent')

        return self

