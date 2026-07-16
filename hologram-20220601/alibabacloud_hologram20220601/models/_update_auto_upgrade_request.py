# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAutoUpgradeRequest(DaraModel):
    def __init__(
        self,
        auto_upgrade: str = None,
    ):
        self.auto_upgrade = auto_upgrade

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_upgrade is not None:
            result['autoUpgrade'] = self.auto_upgrade

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoUpgrade') is not None:
            self.auto_upgrade = m.get('autoUpgrade')

        return self

