# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetClientSourceIpResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        client_ip: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.client_ip = client_ip
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

