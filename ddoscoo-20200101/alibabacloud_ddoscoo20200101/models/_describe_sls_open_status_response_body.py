# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSlsOpenStatusResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        sls_open_status: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether Log Service is activated. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.sls_open_status = sls_open_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sls_open_status is not None:
            result['SlsOpenStatus'] = self.sls_open_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SlsOpenStatus') is not None:
            self.sls_open_status = m.get('SlsOpenStatus')

        return self

