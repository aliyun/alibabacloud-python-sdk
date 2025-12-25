# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeCloudResourceAccessedPortsResponseBody(DaraModel):
    def __init__(
        self,
        http: List[int] = None,
        https: List[int] = None,
        request_id: str = None,
    ):
        # The HTTP ports.
        self.http = http
        # The HTTPS ports.
        self.https = https
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.http is not None:
            result['Http'] = self.http

        if self.https is not None:
            result['Https'] = self.https

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Http') is not None:
            self.http = m.get('Http')

        if m.get('Https') is not None:
            self.https = m.get('Https')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

