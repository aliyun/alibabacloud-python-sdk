# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateServiceResponseBody(DaraModel):
    def __init__(
        self,
        pid: str = None,
        request_id: str = None,
        service_id: str = None,
    ):
        # Historical compatible ARMS application ID
        self.pid = pid
        # Request ID.
        self.request_id = request_id
        # Service ID
        self.service_id = service_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pid is not None:
            result['pid'] = self.pid

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.service_id is not None:
            result['serviceId'] = self.service_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pid') is not None:
            self.pid = m.get('pid')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')

        return self

