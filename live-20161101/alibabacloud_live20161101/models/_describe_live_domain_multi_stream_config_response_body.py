# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLiveDomainMultiStreamConfigResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        switch: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # Indicates whether the dual-stream disaster recovery feature is enabled. Valid values:
        # 
        # *   **on**: enabled
        # *   **off**: disabled
        self.switch = switch

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.switch is not None:
            result['Switch'] = self.switch

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Switch') is not None:
            self.switch = m.get('Switch')

        return self

