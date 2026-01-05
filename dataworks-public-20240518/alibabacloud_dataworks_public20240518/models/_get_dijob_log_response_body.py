# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDIJobLogResponseBody(DaraModel):
    def __init__(
        self,
        log: str = None,
        request_id: str = None,
    ):
        # The log.
        self.log = log
        # The request ID. You can use the ID to query logs and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.log is not None:
            result['Log'] = self.log

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Log') is not None:
            self.log = m.get('Log')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

