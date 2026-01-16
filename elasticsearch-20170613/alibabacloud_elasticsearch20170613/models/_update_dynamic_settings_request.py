# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDynamicSettingsRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        region_id: str = None,
        body: str = None,
        mode: str = None,
    ):
        self.client_token = client_token
        self.region_id = region_id
        self.body = body
        self.mode = mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.body is not None:
            result['body'] = self.body

        if self.mode is not None:
            result['mode'] = self.mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('body') is not None:
            self.body = m.get('body')

        if m.get('mode') is not None:
            self.mode = m.get('mode')

        return self

