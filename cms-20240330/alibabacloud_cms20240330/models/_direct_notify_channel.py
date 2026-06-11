# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DirectNotifyChannel(DaraModel):
    def __init__(
        self,
        identifiers: List[str] = None,
        type: str = None,
    ):
        # An array of recipient identifiers. The format of each identifier depends on the `type`. For example, if `type` is `email`, the identifiers are email addresses.
        # 
        # This parameter is required.
        self.identifiers = identifiers
        # The notification channel type. For example, `sms` or `email`.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.identifiers is not None:
            result['identifiers'] = self.identifiers

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('identifiers') is not None:
            self.identifiers = m.get('identifiers')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

