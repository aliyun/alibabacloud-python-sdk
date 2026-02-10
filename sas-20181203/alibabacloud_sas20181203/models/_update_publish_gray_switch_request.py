# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdatePublishGraySwitchRequest(DaraModel):
    def __init__(
        self,
        gray_switch_status: int = None,
    ):
        # Specifies whether to enable the canary release feature. Valid values:
        # 
        # *   **1**: enabled.
        # *   **0**: disabled.
        # 
        # This parameter is required.
        self.gray_switch_status = gray_switch_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gray_switch_status is not None:
            result['GraySwitchStatus'] = self.gray_switch_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GraySwitchStatus') is not None:
            self.gray_switch_status = m.get('GraySwitchStatus')

        return self

