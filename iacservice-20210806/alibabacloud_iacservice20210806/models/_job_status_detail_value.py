# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class JobStatusDetailValue(DaraModel):
    def __init__(
        self,
        comment: str = None,
        job_result: str = None,
        time_stamps: str = None,
        error_message: str = None,
    ):
        self.comment = comment
        self.job_result = job_result
        self.time_stamps = time_stamps
        self.error_message = error_message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['comment'] = self.comment

        if self.job_result is not None:
            result['jobResult'] = self.job_result

        if self.time_stamps is not None:
            result['timeStamps'] = self.time_stamps

        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comment') is not None:
            self.comment = m.get('comment')

        if m.get('jobResult') is not None:
            self.job_result = m.get('jobResult')

        if m.get('timeStamps') is not None:
            self.time_stamps = m.get('timeStamps')

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        return self

