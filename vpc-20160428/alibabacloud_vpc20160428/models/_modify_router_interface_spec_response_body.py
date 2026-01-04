# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyRouterInterfaceSpecResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        spec: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The specification of the router interface. Valid values:
        # 
        # *   **Mini.2**: 2 Mbit/s
        # *   **Mini.5**: 5 Mbit/s
        # *   **Small.1**: 10 Mbit/s
        # *   **Small.2**: 20 Mbit/s
        # *   **Small.5**: 50 Mbit/s
        # *   **Middle.1**: 100 Mbit/s
        # *   **Middle.2**: 200 Mbit/s
        # *   **Middle.5**: 500 Mbit/s
        # *   **Large.1**: 1,000 Mbit/s
        # *   **Large.2**: 2,000 Mbit/s
        # *   **Large.5**: 5,000 Mbit/s
        # *   **Xlarge.1**: 10,000 Mbit/s
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.spec is not None:
            result['Spec'] = self.spec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        return self

