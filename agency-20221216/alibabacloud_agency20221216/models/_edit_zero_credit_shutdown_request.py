# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EditZeroCreditShutdownRequest(DaraModel):
    def __init__(
        self,
        shutdown_policy: str = None,
        uid: int = None,
    ):
        # UID
        self.shutdown_policy = shutdown_policy
        # No Change History
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.shutdown_policy is not None:
            result['ShutdownPolicy'] = self.shutdown_policy

        if self.uid is not None:
            result['Uid'] = self.uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ShutdownPolicy') is not None:
            self.shutdown_policy = m.get('ShutdownPolicy')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        return self

