# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DryRunConfigRuleRequest(DaraModel):
    def __init__(
        self,
        configuration_item: str = None,
        resource_type: str = None,
    ):
        self.configuration_item = configuration_item
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.configuration_item is not None:
            result['ConfigurationItem'] = self.configuration_item

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigurationItem') is not None:
            self.configuration_item = m.get('ConfigurationItem')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

