# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InvalidateThirdPartyAppLoginStateShrinkRequest(DaraModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        third_party_app_id: str = None,
    ):
        # Device identification information
        # 
        # This parameter is required.
        self.device_info_shrink = device_info_shrink
        # Third-party application identity
        # 
        # This parameter is required.
        self.third_party_app_id = third_party_app_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink

        if self.third_party_app_id is not None:
            result['ThirdPartyAppId'] = self.third_party_app_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')

        if m.get('ThirdPartyAppId') is not None:
            self.third_party_app_id = m.get('ThirdPartyAppId')

        return self

