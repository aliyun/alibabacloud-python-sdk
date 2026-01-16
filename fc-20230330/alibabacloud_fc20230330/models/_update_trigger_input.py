# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateTriggerInput(DaraModel):
    def __init__(
        self,
        description: str = None,
        invocation_role: str = None,
        qualifier: str = None,
        trigger_config: str = None,
    ):
        self.description = description
        self.invocation_role = invocation_role
        self.qualifier = qualifier
        self.trigger_config = trigger_config

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.invocation_role is not None:
            result['invocationRole'] = self.invocation_role

        if self.qualifier is not None:
            result['qualifier'] = self.qualifier

        if self.trigger_config is not None:
            result['triggerConfig'] = self.trigger_config

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('invocationRole') is not None:
            self.invocation_role = m.get('invocationRole')

        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')

        if m.get('triggerConfig') is not None:
            self.trigger_config = m.get('triggerConfig')

        return self

