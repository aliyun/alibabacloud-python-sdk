# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UploadDeviceRequest(DaraModel):
    def __init__(
        self,
        device_tokens: str = None,
    ):
        self.device_tokens = device_tokens

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_tokens is not None:
            result['DeviceTokens'] = self.device_tokens

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceTokens') is not None:
            self.device_tokens = m.get('DeviceTokens')

        return self

