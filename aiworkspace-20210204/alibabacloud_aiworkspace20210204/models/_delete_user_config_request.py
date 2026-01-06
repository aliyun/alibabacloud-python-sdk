# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteUserConfigRequest(DaraModel):
    def __init__(
        self,
        config_key: str = None,
        scope: str = None,
    ):
        # The configuration item keys. Currently, only customizePAIAssumedRole.
        self.config_key = config_key
        # The scope. Valid values: subUser and owner.
        self.scope = scope

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_key is not None:
            result['ConfigKey'] = self.config_key

        if self.scope is not None:
            result['Scope'] = self.scope

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigKey') is not None:
            self.config_key = m.get('ConfigKey')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        return self

