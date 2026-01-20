# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class GetGroupHeaders(DaraModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        # The authentication information. The value is in the Bearer ${access_token} format. Example: Bearer ATxxxx.
        # 
        # This parameter is required.
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers

        if self.authorization is not None:
            result['Authorization'] = self.authorization

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')

        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')

        return self

