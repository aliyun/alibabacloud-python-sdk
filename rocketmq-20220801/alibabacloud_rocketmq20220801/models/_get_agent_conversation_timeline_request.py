# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAgentConversationTimelineRequest(DaraModel):
    def __init__(
        self,
        after: int = None,
        include_image_data: bool = None,
    ):
        self.after = after
        self.include_image_data = include_image_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.after is not None:
            result['after'] = self.after

        if self.include_image_data is not None:
            result['includeImageData'] = self.include_image_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('after') is not None:
            self.after = m.get('after')

        if m.get('includeImageData') is not None:
            self.include_image_data = m.get('includeImageData')

        return self

