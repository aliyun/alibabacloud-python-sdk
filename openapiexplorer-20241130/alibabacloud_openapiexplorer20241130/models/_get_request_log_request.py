# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetRequestLogRequest(DaraModel):
    def __init__(
        self,
        log_request_id: str = None,
    ):
        # The request ID returned by the API for which you want to query the log. The value is the universally unique identifiers (UUID) of the API request and must be uppercase.
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

