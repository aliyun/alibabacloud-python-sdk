# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class SearchFromThirdPartyItem(DaraModel):
    def __init__(
        self,
        authentication_type: str = None,
        extra: str = None,
        identity: str = None,
        others: Dict[str, Any] = None,
    ):
        self.authentication_type = authentication_type
        self.extra = extra
        self.identity = identity
        self.others = others

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authentication_type is not None:
            result['authentication_type'] = self.authentication_type

        if self.extra is not None:
            result['extra'] = self.extra

        if self.identity is not None:
            result['identity'] = self.identity

        if self.others is not None:
            result['others'] = self.others

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authentication_type') is not None:
            self.authentication_type = m.get('authentication_type')

        if m.get('extra') is not None:
            self.extra = m.get('extra')

        if m.get('identity') is not None:
            self.identity = m.get('identity')

        if m.get('others') is not None:
            self.others = m.get('others')

        return self

