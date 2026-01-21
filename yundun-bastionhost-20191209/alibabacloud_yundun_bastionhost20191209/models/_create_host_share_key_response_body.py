# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateHostShareKeyResponseBody(DaraModel):
    def __init__(
        self,
        host_share_key_id: int = None,
        request_id: str = None,
    ):
        # The ID of the shared key.
        self.host_share_key_id = host_share_key_id
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.host_share_key_id is not None:
            result['HostShareKeyId'] = self.host_share_key_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostShareKeyId') is not None:
            self.host_share_key_id = m.get('HostShareKeyId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

