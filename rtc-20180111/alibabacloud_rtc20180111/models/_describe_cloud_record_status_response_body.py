# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCloudRecordStatusResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        status: int = None,
    ):
        # Id of the request
        self.request_id = request_id
        # - 0: The task has started and is waiting for users to join.
        # - 100: The task has not started.
        # - 101: Recording is in progress.
        # - 102: The recording file is being uploaded.
        # - 200: Recording is completed (channel ended).
        # - 201: Recording is completed (stopped by user).
        # - 400: Recording failed (internal server error).
        # - 401: Recording failed (failed to write to user storage).
        # - 402: Recording failed (failed to start user storage).
        # - 403: Recording failed (recording duration too short).
        # - 404: Recording failed (incorrect user storage key).
        # - 405: Recording failed (bucket does not exist).
        # - 406: Recording failed (access to user storage denied).
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

