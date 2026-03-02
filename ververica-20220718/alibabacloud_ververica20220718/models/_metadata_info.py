# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MetadataInfo(DaraModel):
    def __init__(
        self,
        key: str = None,
        virtual: bool = None,
    ):
        # The metadata field.
        self.key = key
        # Specifies whether the metadata is read only.
        self.virtual = virtual

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['key'] = self.key

        if self.virtual is not None:
            result['virtual'] = self.virtual

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('virtual') is not None:
            self.virtual = m.get('virtual')

        return self

