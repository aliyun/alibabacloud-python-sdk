# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class DataToolSpecToolsMetaValue(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        templates: Dict[str, Any] = None,
    ):
        self.enabled = enabled
        self.templates = templates

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.templates is not None:
            result['Templates'] = self.templates

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('Templates') is not None:
            self.templates = m.get('Templates')

        return self

