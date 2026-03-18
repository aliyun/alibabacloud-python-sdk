# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ToggleAutoMinorVersionUpgradeRequest(DaraModel):
    def __init__(
        self,
        auto_upgrade: bool = None,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.auto_upgrade = auto_upgrade
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_upgrade is not None:
            result['AutoUpgrade'] = self.auto_upgrade

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoUpgrade') is not None:
            self.auto_upgrade = m.get('AutoUpgrade')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

