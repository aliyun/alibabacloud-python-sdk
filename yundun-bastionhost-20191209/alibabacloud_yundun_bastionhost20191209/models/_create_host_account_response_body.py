# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateHostAccountResponseBody(DaraModel):
    def __init__(
        self,
        host_account_id: str = None,
        request_id: str = None,
    ):
        # The operation that you want to perform. Set the value to **CreateHostAccount**.
        self.host_account_id = host_account_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.host_account_id is not None:
            result['HostAccountId'] = self.host_account_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostAccountId') is not None:
            self.host_account_id = m.get('HostAccountId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

