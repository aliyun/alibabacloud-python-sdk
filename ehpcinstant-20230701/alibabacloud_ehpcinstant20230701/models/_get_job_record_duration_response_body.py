# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetJobRecordDurationResponseBody(DaraModel):
    def __init__(
        self,
        job_record_duration: int = None,
        request_id: str = None,
    ):
        self.job_record_duration = job_record_duration
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_record_duration is not None:
            result['JobRecordDuration'] = self.job_record_duration

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobRecordDuration') is not None:
            self.job_record_duration = m.get('JobRecordDuration')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

