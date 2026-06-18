# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCustomHostnameResponseBody(DaraModel):
    def __init__(
        self,
        hostname: str = None,
        hostname_id: int = None,
        request_id: str = None,
    ):
        # The custom hostname.
        self.hostname = hostname
        # The ID of the custom hostname.
        self.hostname_id = hostname_id
        # The unique identifier for the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hostname is not None:
            result['Hostname'] = self.hostname

        if self.hostname_id is not None:
            result['HostnameId'] = self.hostname_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')

        if m.get('HostnameId') is not None:
            self.hostname_id = m.get('HostnameId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

