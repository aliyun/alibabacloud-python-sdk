# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetRequestLogRequest(DaraModel):
    def __init__(
        self,
        log_request_id: str = None,
    ):
        # The request ID of the log to query. The request ID is the unique identifier of an API request. The ID must be in the UUID format and in uppercase.
        # 
        # This parameter is required.
        self.log_request_id = log_request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.log_request_id is not None:
            result['logRequestId'] = self.log_request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logRequestId') is not None:
            self.log_request_id = m.get('logRequestId')

        return self

