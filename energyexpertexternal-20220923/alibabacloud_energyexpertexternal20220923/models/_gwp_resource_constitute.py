# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GwpResourceConstitute(DaraModel):
    def __init__(
        self,
        carbon_emission: float = None,
        name: str = None,
        percent: str = None,
        resource_type: int = None,
        unit: str = None,
    ):
        self.carbon_emission = carbon_emission
        self.name = name
        self.percent = percent
        self.resource_type = resource_type
        self.unit = unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.carbon_emission is not None:
            result['carbonEmission'] = self.carbon_emission

        if self.name is not None:
            result['name'] = self.name

        if self.percent is not None:
            result['percent'] = self.percent

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        if self.unit is not None:
            result['unit'] = self.unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('carbonEmission') is not None:
            self.carbon_emission = m.get('carbonEmission')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('percent') is not None:
            self.percent = m.get('percent')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        if m.get('unit') is not None:
            self.unit = m.get('unit')

        return self

