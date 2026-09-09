# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListApiKeysRequest(DaraModel):
    def __init__(
        self,
        allowed_store: str = None,
        offset: int = None,
        size: int = None,
    ):
        # The Logstore that the API key is allowed to write to.
        self.allowed_store = allowed_store
        # The number of the page to return.
        self.offset = offset
        # The number of entries per page.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allowed_store is not None:
            result['allowedStore'] = self.allowed_store

        if self.offset is not None:
            result['offset'] = self.offset

        if self.size is not None:
            result['size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allowedStore') is not None:
            self.allowed_store = m.get('allowedStore')

        if m.get('offset') is not None:
            self.offset = m.get('offset')

        if m.get('size') is not None:
            self.size = m.get('size')

        return self

