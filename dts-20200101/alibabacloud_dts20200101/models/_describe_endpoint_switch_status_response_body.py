# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeEndpointSwitchStatusResponseBody(DaraModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        error_message: str = None,
        request_id: str = None,
        status: str = None,
        success: str = None,
    ):
        # The error code returned if the call failed.
        self.err_code = err_code
        # The error message returned if the call failed.
        self.err_message = err_message
        # This parameter is no longer available.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # The status of the task. Valid values:
        # 
        # *   **NotStarted**: The task is not started.
        # *   **Initializing**: The task is being initialized.
        # *   **Switching**: The task is running.
        # *   **Failed**: The task failed.
        # *   **Finished**: The task is completed.
        self.status = status
        # Indicates whether the call was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

