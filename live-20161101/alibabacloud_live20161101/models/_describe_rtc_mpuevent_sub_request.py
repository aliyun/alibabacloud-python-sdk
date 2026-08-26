# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRtcMPUEventSubRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        # The ID of the subscribed application. You can view your application IDs by navigating to **ApsaraVideo Live > Live+ > ApsaraVideo Real-time Communication > Application Management**.
        # 
        # > 
        # > - The application ID consists of uppercase and lowercase letters, digits, underscores, and hyphens (-), with a maximum of 64 characters.
        # > - You must first call CreateRtcMPUEventSub to create a stream mixing and forwarding event subscription for this application ID.
        # 
        # This parameter is required.
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        return self

