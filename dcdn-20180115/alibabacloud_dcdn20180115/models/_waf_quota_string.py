# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class WafQuotaString(DaraModel):
    def __init__(
        self,
        regexp: str = None,
    ):
        self.regexp = regexp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.regexp is not None:
            result['Regexp'] = self.regexp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Regexp') is not None:
            self.regexp = m.get('Regexp')

        return self

