# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListConsumeProcessorsRequest(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        offset: str = None,
        processor_name: str = None,
        size: str = None,
    ):
        # The display name of the consumption processor.
        self.display_name = display_name
        # The offset. Default value: 0.
        self.offset = offset
        # The identifier of the consumption processor.
        self.processor_name = processor_name
        # The number of entries. Default value: 200.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.offset is not None:
            result['offset'] = self.offset

        if self.processor_name is not None:
            result['processorName'] = self.processor_name

        if self.size is not None:
            result['size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('offset') is not None:
            self.offset = m.get('offset')

        if m.get('processorName') is not None:
            self.processor_name = m.get('processorName')

        if m.get('size') is not None:
            self.size = m.get('size')

        return self

