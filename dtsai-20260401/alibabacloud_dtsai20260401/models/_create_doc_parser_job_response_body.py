# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDocParserJobResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        http_status_code: int = None,
        job_id: str = None,
        request_id: str = None,
        result: str = None,
        result_type: str = None,
        result_url: str = None,
        status: str = None,
        success: bool = None,
    ):
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The document parsing task ID.
        self.job_id = job_id
        # The request ID.
        self.request_id = request_id
        self.result = result
        self.result_type = result_type
        self.result_url = result_url
        self.status = status
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result

        if self.result_type is not None:
            result['ResultType'] = self.result_type

        if self.result_url is not None:
            result['ResultUrl'] = self.result_url

        if self.status is not None:
            result['Status'] = self.status

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('ResultType') is not None:
            self.result_type = m.get('ResultType')

        if m.get('ResultUrl') is not None:
            self.result_url = m.get('ResultUrl')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

