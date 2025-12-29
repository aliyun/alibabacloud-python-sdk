# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ContainerResources(DaraModel):
    def __init__(
        self,
        cpu: int = None,
        memory: int = None,
    ):
        # This parameter is required.
        self.cpu = cpu
        # This parameter is required.
        self.memory = memory

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.memory is not None:
            result['Memory'] = self.memory

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        return self

