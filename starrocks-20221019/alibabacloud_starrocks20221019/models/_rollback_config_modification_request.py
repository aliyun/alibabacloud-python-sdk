# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RollbackConfigModificationRequest(DaraModel):
    def __init__(
        self,
        config_history_id: int = None,
        instance_id: str = None,
        restart: bool = None,
    ):
        self.config_history_id = config_history_id
        self.instance_id = instance_id
        self.restart = restart

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_history_id is not None:
            result['ConfigHistoryId'] = self.config_history_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.restart is not None:
            result['Restart'] = self.restart

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigHistoryId') is not None:
            self.config_history_id = m.get('ConfigHistoryId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Restart') is not None:
            self.restart = m.get('Restart')

        return self

