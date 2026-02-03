# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeInstanceTDEStatusResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        tdestatus: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether TDE is enabled. Valid values:
        # 
        # *   **Enabled**: TDE is enabled.
        # *   **Disable**: TDE is disabled.
        self.tdestatus = tdestatus

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.tdestatus is not None:
            result['TDEStatus'] = self.tdestatus

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TDEStatus') is not None:
            self.tdestatus = m.get('TDEStatus')

        return self

