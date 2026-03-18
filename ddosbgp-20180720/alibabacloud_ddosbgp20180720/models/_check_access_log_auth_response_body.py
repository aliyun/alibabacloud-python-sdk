# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckAccessLogAuthResponseBody(DaraModel):
    def __init__(
        self,
        access_log_auth: bool = None,
        request_id: str = None,
    ):
        # Indicates whether Anti-DDoS Origin was authorized to access Simple Log Service. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.access_log_auth = access_log_auth
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_log_auth is not None:
            result['AccessLogAuth'] = self.access_log_auth

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessLogAuth') is not None:
            self.access_log_auth = m.get('AccessLogAuth')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

