# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateRiskNotificationRequest(DaraModel):
    def __init__(
        self,
        is_mute: bool = None,
        risk_code: str = None,
    ):
        self.is_mute = is_mute
        self.risk_code = risk_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_mute is not None:
            result['isMute'] = self.is_mute

        if self.risk_code is not None:
            result['riskCode'] = self.risk_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('isMute') is not None:
            self.is_mute = m.get('isMute')

        if m.get('riskCode') is not None:
            self.risk_code = m.get('riskCode')

        return self

