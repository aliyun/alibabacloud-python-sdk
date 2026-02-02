# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Audit(DaraModel):
    def __init__(
        self,
        log_mode: str = None,
    ):
        self.log_mode = log_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.log_mode is not None:
            result['LogMode'] = self.log_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogMode') is not None:
            self.log_mode = m.get('LogMode')

        return self

