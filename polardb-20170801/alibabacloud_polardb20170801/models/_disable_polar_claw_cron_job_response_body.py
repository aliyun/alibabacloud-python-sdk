# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DisablePolarClawCronJobResponseBody(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        code: int = None,
        job_id: str = None,
        message: str = None,
        ok: bool = None,
        request_id: str = None,
    ):
        # The ID of the application.
        self.application_id = application_id
        # The response status code.
        self.code = code
        # The ID of the disabled job.
        self.job_id = job_id
        # The response message.
        self.message = message
        # Indicates whether the operation was successful. A value of `true` indicates success.
        self.ok = ok
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.code is not None:
            result['Code'] = self.code

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.message is not None:
            result['Message'] = self.message

        if self.ok is not None:
            result['Ok'] = self.ok

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Ok') is not None:
            self.ok = m.get('Ok')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

