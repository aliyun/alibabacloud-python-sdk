# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BindInstance2VpcResponseBody(DaraModel):
    def __init__(
        self,
        domain: str = None,
        endpoint: str = None,
        request_id: str = None,
    ):
        self.domain = domain
        self.endpoint = endpoint
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

