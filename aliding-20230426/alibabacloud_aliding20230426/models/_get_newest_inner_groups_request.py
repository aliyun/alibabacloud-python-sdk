# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class GetNewestInnerGroupsRequest(DaraModel):
    def __init__(
        self,
        request: Dict[str, Any] = None,
    ):
        self.request = request

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request is not None:
            result['Request'] = self.request

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Request') is not None:
            self.request = m.get('Request')

        return self

