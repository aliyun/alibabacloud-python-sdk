# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DevelopServiceRequest(DaraModel):
    def __init__(
        self,
        exit: str = None,
    ):
        # Specifies whether to exit development mode. Valid values:
        # 
        # *   true: exits development mode.
        # *   false (default): enters development mode.
        self.exit = exit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exit is not None:
            result['Exit'] = self.exit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Exit') is not None:
            self.exit = m.get('Exit')

        return self

