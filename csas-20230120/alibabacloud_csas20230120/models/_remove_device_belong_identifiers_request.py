# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RemoveDeviceBelongIdentifiersRequest(DaraModel):
    def __init__(
        self,
        identifier_ids: List[str] = None,
    ):
        # This parameter is required.
        self.identifier_ids = identifier_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.identifier_ids is not None:
            result['IdentifierIds'] = self.identifier_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdentifierIds') is not None:
            self.identifier_ids = m.get('IdentifierIds')

        return self

