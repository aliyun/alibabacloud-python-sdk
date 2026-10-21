# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class ListProductsHeaders(DaraModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_accept_language: str = None,
    ):
        self.common_headers = common_headers
        # Select the language in which the response is returned.
        # 
        # zh_CH: Chinese (default).
        # 
        # en_US: English.
        self.x_acs_accept_language = x_acs_accept_language

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers

        if self.x_acs_accept_language is not None:
            result['x-acs-accept-language'] = self.x_acs_accept_language

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')

        if m.get('x-acs-accept-language') is not None:
            self.x_acs_accept_language = m.get('x-acs-accept-language')

        return self

