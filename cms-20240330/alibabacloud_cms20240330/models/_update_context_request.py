# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class UpdateContextRequest(DaraModel):
    def __init__(
        self,
        content: str = None,
        experience: Dict[str, Any] = None,
        metadata: Dict[str, Any] = None,
        payload: Dict[str, Any] = None,
        trigger_condition: str = None,
    ):
        # The updated text for the long-term memory.
        self.content = content
        # The experience object.
        self.experience = experience
        # A set of key-value pairs to attach to an object for storing custom information.
        self.metadata = metadata
        # The payload to update.
        self.payload = payload
        # The trigger condition.
        self.trigger_condition = trigger_condition

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.experience is not None:
            result['experience'] = self.experience

        if self.metadata is not None:
            result['metadata'] = self.metadata

        if self.payload is not None:
            result['payload'] = self.payload

        if self.trigger_condition is not None:
            result['triggerCondition'] = self.trigger_condition

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('experience') is not None:
            self.experience = m.get('experience')

        if m.get('metadata') is not None:
            self.metadata = m.get('metadata')

        if m.get('payload') is not None:
            self.payload = m.get('payload')

        if m.get('triggerCondition') is not None:
            self.trigger_condition = m.get('triggerCondition')

        return self

