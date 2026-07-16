# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateMemoryRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
    ):
        # The description of the long-term memory. The description must be 1 to 50 characters in length and can contain letters, digits, and characters in the Unicode letter category (including Chinese characters). The description can also contain colons (:), underscores (_), periods (.), and hyphens (-).
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        return self

