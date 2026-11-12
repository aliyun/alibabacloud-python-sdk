# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FindCustomAgentImagePreparationRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        # The idempotency token passed as a query parameter. Required when explicitly submitting customImage or container.type=custom. Optional for ACR image and code package submissions. The value must be 1 to 128 characters in length and can contain letters, digits, periods, underscores, colons, and hyphens. Reuse the same token for retries of the same submission. Using the same token for different parameters is rejected.
        # 
        # This parameter is required.
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['clientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        return self

