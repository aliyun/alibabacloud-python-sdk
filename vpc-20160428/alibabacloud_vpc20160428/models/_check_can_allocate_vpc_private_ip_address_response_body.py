# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckCanAllocateVpcPrivateIpAddressResponseBody(DaraModel):
    def __init__(
        self,
        can_allocate: bool = None,
        request_id: str = None,
    ):
        # Indicates whether the private IP address is available. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.can_allocate = can_allocate
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.can_allocate is not None:
            result['CanAllocate'] = self.can_allocate

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanAllocate') is not None:
            self.can_allocate = m.get('CanAllocate')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

