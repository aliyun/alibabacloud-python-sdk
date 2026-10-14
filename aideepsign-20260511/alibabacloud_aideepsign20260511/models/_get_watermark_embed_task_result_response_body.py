# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetWatermarkEmbedTaskResultResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
        task_id: str = None,
        url: str = None,
    ):
        # **The business error code.** The value OK is returned if the request is successful.
        self.code = code
        # **The HTTP status code.** The value 200 is returned if the request is successful.
        self.http_status_code = http_status_code
        # The failure reason when the task fails. This parameter is returned only when Status is failed.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The task status. The processing time is approximately equal to the media duration. Valid values:
        # - pending: The task is waiting.
        # - running: The task is running.
        # - succeeded: The task succeeded.
        # - failed: The task failed.
        self.status = status
        # Indicates whether the request was successful.
        self.success = success
        # The invisible watermark embedding task ID.
        self.task_id = task_id
        # The pre-signed URL for accessing the watermarked file. This parameter is returned only when Status is succeeded.
        self.url = url

    def validate(self):
        pass

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.success is not None:
            result['Success'] = self.success

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

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

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

