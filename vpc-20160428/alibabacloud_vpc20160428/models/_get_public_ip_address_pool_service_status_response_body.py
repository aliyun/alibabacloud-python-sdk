# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetPublicIpAddressPoolServiceStatusResponseBody(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        request_id: str = None,
    ):
        # Indicates whether the IP address pool feature is enabled. Valid values:
        # 
        # *   **true**
        # *   **false** You can call OpenPublicIpAddressPoolService to enable the IP address pool feature.
        self.enabled = enabled
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

