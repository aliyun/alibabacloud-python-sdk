# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CancelPipelineRunResponseBody(DaraModel):
    def __init__(
        self,
        finish_time: str = None,
        request_id: str = None,
        run_id: str = None,
        status: str = None,
    ):
        # The time when the cancellation was completed, in ISO 8601 UTC format.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.finish_time = finish_time
        # The request ID, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The ID of the canceled run.
        self.run_id = run_id
        # The status of the run after cancellation. The value is fixed to Cancelled.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.finish_time is not None:
            result['finishTime'] = self.finish_time

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.run_id is not None:
            result['runId'] = self.run_id

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('finishTime') is not None:
            self.finish_time = m.get('finishTime')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('runId') is not None:
            self.run_id = m.get('runId')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

