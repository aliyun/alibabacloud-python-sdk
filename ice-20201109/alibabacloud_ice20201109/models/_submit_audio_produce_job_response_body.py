# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitAudioProduceJobResponseBody(DaraModel):
    def __init__(
        self,
        job_id: str = None,
        media_id: str = None,
        request_id: str = None,
        state: str = None,
    ):
        # The job ID.
        self.job_id = job_id
        # The ID of the media asset.
        self.media_id = media_id
        # The request ID.
        self.request_id = request_id
        # The job state. Valid values:
        # 
        # *   Created
        # *   Executing
        # *   Finished
        # *   Failed
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

