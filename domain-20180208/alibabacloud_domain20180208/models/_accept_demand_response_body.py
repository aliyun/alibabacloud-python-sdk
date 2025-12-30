# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AcceptDemandResponseBody(DaraModel):
    def __init__(
        self,
        bind_url: str = None,
        request_id: str = None,
    ):
        self.bind_url = bind_url
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bind_url is not None:
            result['BindUrl'] = self.bind_url

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindUrl') is not None:
            self.bind_url = m.get('BindUrl')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

