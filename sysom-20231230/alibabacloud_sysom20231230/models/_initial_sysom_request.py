# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InitialSysomRequest(DaraModel):
    def __init__(
        self,
        check_only: bool = None,
        source: str = None,
    ):
        self.check_only = check_only
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_only is not None:
            result['check_only'] = self.check_only

        if self.source is not None:
            result['source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('check_only') is not None:
            self.check_only = m.get('check_only')

        if m.get('source') is not None:
            self.source = m.get('source')

        return self

