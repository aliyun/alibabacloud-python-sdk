# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartApsJobResponseBody(DaraModel):
    def __init__(
        self,
        aps_job_id: str = None,
        code: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The job ID.
        self.aps_job_id = aps_job_id
        # The HTTP status code or the error code.
        self.code = code
        # The error code returned when the request fails.
        self.err_code = err_code
        # The error message returned if the request failed.
        self.err_message = err_message
        # The response code. The status code 200 indicates that the request was successful.
        self.http_status_code = http_status_code
        # The returned message. Valid values:
        # 
        # *   If the request was successful, a success message is returned.****
        # *   If the request failed, an error message is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aps_job_id is not None:
            result['ApsJobId'] = self.aps_job_id

        if self.code is not None:
            result['Code'] = self.code

        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApsJobId') is not None:
            self.aps_job_id = m.get('ApsJobId')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

