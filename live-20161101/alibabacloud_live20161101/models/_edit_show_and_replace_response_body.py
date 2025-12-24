# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EditShowAndReplaceResponseBody(DaraModel):
    def __init__(
        self,
        job_info: str = None,
        request_id: str = None,
    ):
        # The information about the editing task. The following fields are included:
        # 
        # *   **vodId**: the ID of the VOD file.
        # *   **mediaid**: the ID of the media file.
        # *   **jobId**: the ID of the editing task.
        self.job_info = job_info
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_info is not None:
            result['JobInfo'] = self.job_info

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobInfo') is not None:
            self.job_info = m.get('JobInfo')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

