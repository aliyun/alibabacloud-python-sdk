# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class NeuronAppUnBindCmd(DaraModel):
    def __init__(
        self,
        app_id: int = None,
        reason: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['appId'] = self.app_id

        if self.reason is not None:
            result['reason'] = self.reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')

        if m.get('reason') is not None:
            self.reason = m.get('reason')

        return self

