# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTriggerInput(DaraModel):
    def __init__(
        self,
        description: str = None,
        invocation_role: str = None,
        qualifier: str = None,
        source_arn: str = None,
        trigger_config: str = None,
        trigger_name: str = None,
        trigger_type: str = None,
    ):
        self.description = description
        self.invocation_role = invocation_role
        self.qualifier = qualifier
        self.source_arn = source_arn
        # This parameter is required.
        self.trigger_config = trigger_config
        # This parameter is required.
        self.trigger_name = trigger_name
        # This parameter is required.
        self.trigger_type = trigger_type

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

        if self.source_arn is not None:
            result['sourceArn'] = self.source_arn

        if self.trigger_config is not None:
            result['triggerConfig'] = self.trigger_config

        if self.trigger_name is not None:
            result['triggerName'] = self.trigger_name

        if self.trigger_type is not None:
            result['triggerType'] = self.trigger_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('invocationRole') is not None:
            self.invocation_role = m.get('invocationRole')

        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')

        if m.get('sourceArn') is not None:
            self.source_arn = m.get('sourceArn')

        if m.get('triggerConfig') is not None:
            self.trigger_config = m.get('triggerConfig')

        if m.get('triggerName') is not None:
            self.trigger_name = m.get('triggerName')

        if m.get('triggerType') is not None:
            self.trigger_type = m.get('triggerType')

        return self

