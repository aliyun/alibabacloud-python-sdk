# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class HttpApiMockContract(DaraModel):
    def __init__(
        self,
        enable: bool = None,
        response_code: int = None,
        response_content: str = None,
    ):
        self.enable = enable
        self.response_code = response_code
        self.response_content = response_content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['enable'] = self.enable

        if self.response_code is not None:
            result['responseCode'] = self.response_code

        if self.response_content is not None:
            result['responseContent'] = self.response_content

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('responseCode') is not None:
            self.response_code = m.get('responseCode')

        if m.get('responseContent') is not None:
            self.response_content = m.get('responseContent')

        return self

