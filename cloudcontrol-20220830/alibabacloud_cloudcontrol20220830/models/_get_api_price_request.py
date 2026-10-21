# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class GetApiPriceRequest(DaraModel):
    def __init__(
        self,
        body: Dict[str, Any] = None,
    ):
        # The pricing request body, including popCode, popVersion, apiName, and parameters. All calls return a unified pricing envelope. The language parameter specifies the server-side message language, such as en or zh. Target resource operations are not executed for cost-irrelevant or unsupported pricing queries.
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')

        return self

