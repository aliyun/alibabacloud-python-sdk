# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitVideoRemakeJobResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        job_id: str = None,
        request_id: str = None,
    ):
        # The error code in the business response. This parameter is empty when the call is successful.
        self.error_code = error_code
        # The unified remake job ID. Use GetVideoRemakeJob to query the progress and outputs.
        self.job_id = job_id
        # The request tracking ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

