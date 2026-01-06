# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExecutePolicyV2ResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        job_id: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Return code, 200 indicates success.
        self.code = code
        # Backup job ID.
        self.job_id = job_id
        # Description of the return message, usually returns \\"successful\\" on success, and corresponding error messages on failure.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        # 
        # - true: Success
        # - false: Failure
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.job_id is not None:
            result['JobId'] = self.job_id

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

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

