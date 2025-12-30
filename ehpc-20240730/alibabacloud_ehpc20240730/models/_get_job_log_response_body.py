# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetJobLogResponseBody(DaraModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
        stderr_log: str = None,
        stderr_log_size: str = None,
        stdout_log: str = None,
        stdout_log_size: str = None,
        success: str = None,
    ):
        # The job ID.
        self.job_id = job_id
        # The request ID.
        self.request_id = request_id
        # The error output log that is encoded in Base64.
        self.stderr_log = stderr_log
        # The size of the error output file.
        self.stderr_log_size = stderr_log_size
        # The standard output log that is encoded in Base64.
        self.stdout_log = stdout_log
        # The size of the standard output file.
        self.stdout_log_size = stdout_log_size
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.stderr_log is not None:
            result['StderrLog'] = self.stderr_log

        if self.stderr_log_size is not None:
            result['StderrLogSize'] = self.stderr_log_size

        if self.stdout_log is not None:
            result['StdoutLog'] = self.stdout_log

        if self.stdout_log_size is not None:
            result['StdoutLogSize'] = self.stdout_log_size

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StderrLog') is not None:
            self.stderr_log = m.get('StderrLog')

        if m.get('StderrLogSize') is not None:
            self.stderr_log_size = m.get('StderrLogSize')

        if m.get('StdoutLog') is not None:
            self.stdout_log = m.get('StdoutLog')

        if m.get('StdoutLogSize') is not None:
            self.stdout_log_size = m.get('StdoutLogSize')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

