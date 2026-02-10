# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCriteriaRequest(DaraModel):
    def __init__(
        self,
        machine_types: str = None,
        support_auto_tag: bool = None,
        value: str = None,
    ):
        # The type of the asset. Valid values:
        # 
        # *   Set the value to **ecs**, which specifies to query all Elastic Compute Service (ECS) instances.
        self.machine_types = machine_types
        # Specifies whether the keyword that you specify for fuzzy search can be automatically matched. Default value: **false**. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.support_auto_tag = support_auto_tag
        # The keyword that you specify for fuzzy search when you query the asset.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.machine_types is not None:
            result['MachineTypes'] = self.machine_types

        if self.support_auto_tag is not None:
            result['SupportAutoTag'] = self.support_auto_tag

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MachineTypes') is not None:
            self.machine_types = m.get('MachineTypes')

        if m.get('SupportAutoTag') is not None:
            self.support_auto_tag = m.get('SupportAutoTag')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

