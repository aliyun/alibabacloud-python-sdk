# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateApplicationScaleConfigInput(DaraModel):
    def __init__(
        self,
        always_allocate_cpu: bool = None,
        maximum_instance_count: int = None,
        minimum_instance_count: int = None,
    ):
        self.always_allocate_cpu = always_allocate_cpu
        self.maximum_instance_count = maximum_instance_count
        self.minimum_instance_count = minimum_instance_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.always_allocate_cpu is not None:
            result['alwaysAllocateCPU'] = self.always_allocate_cpu

        if self.maximum_instance_count is not None:
            result['maximumInstanceCount'] = self.maximum_instance_count

        if self.minimum_instance_count is not None:
            result['minimumInstanceCount'] = self.minimum_instance_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alwaysAllocateCPU') is not None:
            self.always_allocate_cpu = m.get('alwaysAllocateCPU')

        if m.get('maximumInstanceCount') is not None:
            self.maximum_instance_count = m.get('maximumInstanceCount')

        if m.get('minimumInstanceCount') is not None:
            self.minimum_instance_count = m.get('minimumInstanceCount')

        return self

