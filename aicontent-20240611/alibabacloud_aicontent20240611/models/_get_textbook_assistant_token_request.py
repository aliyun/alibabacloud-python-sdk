# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTextbookAssistantTokenRequest(DaraModel):
    def __init__(
        self,
        device_id: str = None,
        model: str = None,
    ):
        # This parameter is required.
        self.device_id = device_id
        # This parameter is required.
        self.model = model

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_id is not None:
            result['deviceId'] = self.device_id

        if self.model is not None:
            result['model'] = self.model

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deviceId') is not None:
            self.device_id = m.get('deviceId')

        if m.get('model') is not None:
            self.model = m.get('model')

        return self

