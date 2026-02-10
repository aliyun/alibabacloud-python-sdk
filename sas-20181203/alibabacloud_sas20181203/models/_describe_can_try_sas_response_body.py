# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCanTrySasResponseBody(DaraModel):
    def __init__(
        self,
        can_try: int = None,
        request_id: str = None,
    ):
        # Indicates whether you have the permissions on the trial use of Security Center. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.can_try = can_try
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.can_try is not None:
            result['CanTry'] = self.can_try

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanTry') is not None:
            self.can_try = m.get('CanTry')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

