# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeMachineSpecRequest(DaraModel):
    def __init__(
        self,
        charge_type: str = None,
        instance_types: List[str] = None,
        resource_type: str = None,
    ):
        self.charge_type = charge_type
        # This parameter is deprecated.
        self.instance_types = instance_types
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.instance_types is not None:
            result['InstanceTypes'] = self.instance_types

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('InstanceTypes') is not None:
            self.instance_types = m.get('InstanceTypes')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

