# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class DeleteResourceRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        filter: Dict[str, Any] = None,
        region_id: str = None,
    ):
        # A client token to ensure idempotence. This parameter works only if the cloud product supports idempotence.
        self.client_token = client_token
        self.filter = filter
        # The region ID. This parameter is required if the cloud product is region-specific.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['clientToken'] = self.client_token

        if self.filter is not None:
            result['filter'] = self.filter

        if self.region_id is not None:
            result['regionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        if m.get('filter') is not None:
            self.filter = m.get('filter')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        return self

