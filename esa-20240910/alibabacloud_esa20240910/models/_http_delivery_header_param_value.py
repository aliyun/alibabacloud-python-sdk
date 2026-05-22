# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class HttpDeliveryHeaderParamValue(DaraModel):
    def __init__(
        self,
        static_value: str = None,
    ):
        # The static variable.
        self.static_value = static_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.static_value is not None:
            result['StaticValue'] = self.static_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StaticValue') is not None:
            self.static_value = m.get('StaticValue')

        return self

