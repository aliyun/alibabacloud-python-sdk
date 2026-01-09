# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class IngestProcessorConfiguration(DaraModel):
    def __init__(
        self,
        parse_fail: str = None,
        spl: str = None,
    ):
        self.parse_fail = parse_fail
        # This parameter is required.
        self.spl = spl

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.parse_fail is not None:
            result['parseFail'] = self.parse_fail

        if self.spl is not None:
            result['spl'] = self.spl

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('parseFail') is not None:
            self.parse_fail = m.get('parseFail')

        if m.get('spl') is not None:
            self.spl = m.get('spl')

        return self

