# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class GetMaterializedViewHeaders(DaraModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        content_type: str = None,
    ):
        self.common_headers = common_headers
        self.content_type = content_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers

        if self.content_type is not None:
            result['Content-Type'] = self.content_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')

        if m.get('Content-Type') is not None:
            self.content_type = m.get('Content-Type')

        return self

