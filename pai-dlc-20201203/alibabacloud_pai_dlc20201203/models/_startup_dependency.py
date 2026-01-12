# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartupDependency(DaraModel):
    def __init__(
        self,
        min_replicas: str = None,
        on_phase: str = None,
        type: str = None,
    ):
        self.min_replicas = min_replicas
        self.on_phase = on_phase
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.min_replicas is not None:
            result['MinReplicas'] = self.min_replicas

        if self.on_phase is not None:
            result['OnPhase'] = self.on_phase

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MinReplicas') is not None:
            self.min_replicas = m.get('MinReplicas')

        if m.get('OnPhase') is not None:
            self.on_phase = m.get('OnPhase')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

