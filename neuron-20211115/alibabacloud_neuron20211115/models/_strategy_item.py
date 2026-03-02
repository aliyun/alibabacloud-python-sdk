# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StrategyItem(DaraModel):
    def __init__(
        self,
        action: str = None,
        resource: str = None,
    ):
        self.action = action
        self.resource = resource

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['action'] = self.action

        if self.resource is not None:
            result['resource'] = self.resource

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')

        if m.get('resource') is not None:
            self.resource = m.get('resource')

        return self

