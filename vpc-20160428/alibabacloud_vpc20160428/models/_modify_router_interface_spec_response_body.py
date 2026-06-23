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
        # * **Mini.2**: 2 Mbps
        # 
        # * **Mini.5**: 5 Mbps
        # 
        # * **Small.1**: 10 Mbps
        # 
        # * **Small.2**: 20 Mbps
        # 
        # * **Small.5**: 50 Mbps
        # 
        # * **Middle.1**: 100 Mbps
        # 
        # * **Middle.2**: 200 Mbps
        # 
        # * **Middle.5**: 500 Mbps
        # 
        # * **Large.1**: 1000 Mbps
        # 
        # * **Large.2**: 2000 Mbps
        # 
        # * **Large.5**: 5000 Mbps
        # 
        # * **Xlarge.1**: 10000 Mbps.
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

