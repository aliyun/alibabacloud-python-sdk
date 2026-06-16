# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OpenTrialPackageRequest(DaraModel):
    def __init__(
        self,
        auto_close_switch: int = None,
        region_id: str = None,
    ):
        self.auto_close_switch = auto_close_switch
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_close_switch is not None:
            result['AutoCloseSwitch'] = self.auto_close_switch

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoCloseSwitch') is not None:
            self.auto_close_switch = m.get('AutoCloseSwitch')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

