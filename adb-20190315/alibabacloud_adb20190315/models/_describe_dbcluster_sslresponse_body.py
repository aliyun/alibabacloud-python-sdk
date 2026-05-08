# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDBClusterSSLResponseBody(DaraModel):
    def __init__(
        self,
        connection_string: str = None,
        expire_time: str = None,
        request_id: str = None,
        sslenabled: bool = None,
    ):
        # The endpoint that is protected by SSL encryption.
        self.connection_string = connection_string
        # The time when the SSL certificate expires. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.expire_time = expire_time
        # The request ID.
        self.request_id = request_id
        # Indicates whether SSL encryption is enabled. Valid values:
        # 
        # *   true
        # *   false
        self.sslenabled = sslenabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sslenabled is not None:
            result['SSLEnabled'] = self.sslenabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SSLEnabled') is not None:
            self.sslenabled = m.get('SSLEnabled')

        return self

