# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateThreadResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        thread_id: str = None,
        version: int = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.thread_id = thread_id
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.thread_id is not None:
            result['threadId'] = self.thread_id

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('threadId') is not None:
            self.thread_id = m.get('threadId')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

