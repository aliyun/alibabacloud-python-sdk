# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAlertEnabledRequest(DaraModel):
    def __init__(
        self,
        x_debug_id: str = None,
        enabled: bool = None,
        id: int = None,
        x_sysom_invoke_source: str = None,
    ):
        self.x_debug_id = x_debug_id
        # Specifies whether the alert policy is enabled.
        self.enabled = enabled
        # The ID of the alert policy.
        self.id = id
        self.x_sysom_invoke_source = x_sysom_invoke_source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.x_debug_id is not None:
            result['X-Debug-Id'] = self.x_debug_id

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.id is not None:
            result['id'] = self.id

        if self.x_sysom_invoke_source is not None:
            result['x-sysom-invoke-source'] = self.x_sysom_invoke_source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Debug-Id') is not None:
            self.x_debug_id = m.get('X-Debug-Id')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('x-sysom-invoke-source') is not None:
            self.x_sysom_invoke_source = m.get('x-sysom-invoke-source')

        return self

