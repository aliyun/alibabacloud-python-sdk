# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TrialOrderEligibilityVO(DaraModel):
    def __init__(
        self,
        message: str = None,
        valid: bool = None,
    ):
        self.message = message
        self.valid = valid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['Message'] = self.message

        if self.valid is not None:
            result['Valid'] = self.valid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Valid') is not None:
            self.valid = m.get('Valid')

        return self

