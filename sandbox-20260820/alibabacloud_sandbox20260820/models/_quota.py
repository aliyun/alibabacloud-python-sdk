# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Quota(DaraModel):
    def __init__(
        self,
        cpu_cores: int = None,
        memory_gb: int = None,
        tag_value: str = None,
    ):
        self.cpu_cores = cpu_cores
        self.memory_gb = memory_gb
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu_cores is not None:
            result['cpuCores'] = self.cpu_cores

        if self.memory_gb is not None:
            result['memoryGB'] = self.memory_gb

        if self.tag_value is not None:
            result['tagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cpuCores') is not None:
            self.cpu_cores = m.get('cpuCores')

        if m.get('memoryGB') is not None:
            self.memory_gb = m.get('memoryGB')

        if m.get('tagValue') is not None:
            self.tag_value = m.get('tagValue')

        return self

