# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSubscribedCalendarShrinkRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        managers_shrink: str = None,
        name: str = None,
        subscribe_scope_shrink: str = None,
    ):
        self.description = description
        self.managers_shrink = managers_shrink
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.subscribe_scope_shrink = subscribe_scope_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.managers_shrink is not None:
            result['Managers'] = self.managers_shrink

        if self.name is not None:
            result['Name'] = self.name

        if self.subscribe_scope_shrink is not None:
            result['SubscribeScope'] = self.subscribe_scope_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Managers') is not None:
            self.managers_shrink = m.get('Managers')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SubscribeScope') is not None:
            self.subscribe_scope_shrink = m.get('SubscribeScope')

        return self

