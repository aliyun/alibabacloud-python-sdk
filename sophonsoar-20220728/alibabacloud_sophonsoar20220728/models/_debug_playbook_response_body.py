# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DebugPlaybookResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        request_uuid: str = None,
    ):
        # The ID of the request. Alibaba Cloud generates a unique ID for each request. Use this ID to troubleshoot and locate issues.
        self.request_id = request_id
        # The run UUID of the debugging task. Use this UUID to query information, such as the task result.
        self.request_uuid = request_uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.request_uuid is not None:
            result['RequestUuid'] = self.request_uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RequestUuid') is not None:
            self.request_uuid = m.get('RequestUuid')

        return self

