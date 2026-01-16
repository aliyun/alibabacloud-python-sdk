# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResultSpecInfoMapValue(DaraModel):
    def __init__(
        self,
        cpu_count: str = None,
        memory_size: str = None,
        enable: str = None,
        spec: str = None,
        spec_group_type: str = None,
        disk: str = None,
        disk_type: str = None,
    ):
        self.cpu_count = cpu_count
        self.memory_size = memory_size
        self.enable = enable
        self.spec = spec
        self.spec_group_type = spec_group_type
        self.disk = disk
        self.disk_type = disk_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu_count is not None:
            result['cpuCount'] = self.cpu_count

        if self.memory_size is not None:
            result['memorySize'] = self.memory_size

        if self.enable is not None:
            result['enable'] = self.enable

        if self.spec is not None:
            result['spec'] = self.spec

        if self.spec_group_type is not None:
            result['specGroupType'] = self.spec_group_type

        if self.disk is not None:
            result['disk'] = self.disk

        if self.disk_type is not None:
            result['diskType'] = self.disk_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cpuCount') is not None:
            self.cpu_count = m.get('cpuCount')

        if m.get('memorySize') is not None:
            self.memory_size = m.get('memorySize')

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('spec') is not None:
            self.spec = m.get('spec')

        if m.get('specGroupType') is not None:
            self.spec_group_type = m.get('specGroupType')

        if m.get('disk') is not None:
            self.disk = m.get('disk')

        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')

        return self

