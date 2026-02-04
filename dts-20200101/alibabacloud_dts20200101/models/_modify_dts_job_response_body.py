# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDtsJobResponseBody(DaraModel):
    def __init__(
        self,
        dts_job_id: str = None,
        err_code: str = None,
        err_message: bool = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        # The ID of the DTS task.
        self.dts_job_id = dts_job_id
        # The error code returned if the request failed.
        self.err_code = err_code
        # The error message returned if the request failed.
        # 
        # >  The data type of this parameter is String. Sample value: **The actual sample value is The request processing has failed due to some unknown error.
        self.err_message = err_message
        # The ID of the request.
        self.request_id = request_id
        # The HTTP status code.
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
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id

        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')

        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

