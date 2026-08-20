# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SessionNetworkHeaderValueReplacement(DaraModel):
    def __init__(
        self,
        placeholder: str = None,
        value: str = None,
    ):
        # The fake value. A placeholder used by code in the sandbox. The gateway performs an exact substring match on this string within the header value.
        self.placeholder = placeholder
        # The real value. The actual value after the placeholder is replaced.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.placeholder is not None:
            result['placeholder'] = self.placeholder

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('placeholder') is not None:
            self.placeholder = m.get('placeholder')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

