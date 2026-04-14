# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchSendMailResponseBody(DaraModel):
    def __init__(
        self,
        env_id: str = None,
        request_id: str = None,
    ):
        # Event ID
        self.env_id = env_id
        # Request ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.env_id is not None:
            result['EnvId'] = self.env_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

