# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckTransitRouterServiceResponseBody(DaraModel):
    def __init__(
        self,
        enabled: str = None,
        request_id: str = None,
    ):
        # Indicates whether the transit router feature is activated.
        # 
        # *   **true**: activated
        # *   If this value is not returned, the system prompts that the current account does not have the transit router feature activated.
        self.enabled = enabled
        # The ID of the request.
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

