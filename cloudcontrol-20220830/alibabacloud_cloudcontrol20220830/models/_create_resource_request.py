# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class CreateResourceRequest(DaraModel):
    def __init__(
        self,
        body: Dict[str, Any] = None,
        client_token: str = None,
        region_id: str = None,
    ):
        # The request body. The property of the resource, which is specified in JSON format.
        self.body = body
        # The client token that is used to ensure the idempotence of the request. If a cloud service supports idempotence, the parameter takes effect.
        self.client_token = client_token
        # The region ID. This parameter is required if a cloud service is a regionalized.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        if self.region_id is not None:
            result['regionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        return self

