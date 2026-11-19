# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdatePersonalICodeRequest(DaraModel):
    def __init__(
        self,
        quick_biuser_id: str = None,
    ):
        # The user ID in Quick BI.
        self.quick_biuser_id = quick_biuser_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.quick_biuser_id is not None:
            result['QuickBIUserId'] = self.quick_biuser_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QuickBIUserId') is not None:
            self.quick_biuser_id = m.get('QuickBIUserId')

        return self

