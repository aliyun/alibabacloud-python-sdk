# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDomainOverviewResponseBody(DaraModel):
    def __init__(
        self,
        max_http: int = None,
        max_https: int = None,
        request_id: str = None,
    ):
        # The peak queries per second (QPS) during HTTP traffic scrubbing. Unit: QPS.
        self.max_http = max_http
        # The peak QPS during HTTPS traffic scrubbing. Unit: QPS.
        self.max_https = max_https
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_http is not None:
            result['MaxHttp'] = self.max_http

        if self.max_https is not None:
            result['MaxHttps'] = self.max_https

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxHttp') is not None:
            self.max_http = m.get('MaxHttp')

        if m.get('MaxHttps') is not None:
            self.max_https = m.get('MaxHttps')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

