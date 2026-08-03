# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConfigDataAgentMemoryRequest(DaraModel):
    def __init__(
        self,
        dmsunit: str = None,
        enabled: bool = None,
        recall_enabled: bool = None,
    ):
        self.dmsunit = dmsunit
        self.enabled = enabled
        self.recall_enabled = recall_enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dmsunit is not None:
            result['DMSUnit'] = self.dmsunit

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.recall_enabled is not None:
            result['RecallEnabled'] = self.recall_enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DMSUnit') is not None:
            self.dmsunit = m.get('DMSUnit')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('RecallEnabled') is not None:
            self.recall_enabled = m.get('RecallEnabled')

        return self

