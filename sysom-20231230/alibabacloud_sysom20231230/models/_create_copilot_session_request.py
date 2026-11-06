# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCopilotSessionRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
    ):
        # The session name. The name must be 1 to 255 characters in length. Default value: New Session. Empty strings or null values are not supported. If no name is specified, the server uses content generation to create a session name based on the first user message when it is received.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        return self

