# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetMainDomainNameRequest(DaraModel):
    def __init__(
        self,
        input_string: str = None,
        lang: str = None,
    ):
        # The string. The string can be up to 128 characters in length.
        # 
        # This parameter is required.
        self.input_string = input_string
        # The language.
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_string is not None:
            result['InputString'] = self.input_string

        if self.lang is not None:
            result['Lang'] = self.lang

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputString') is not None:
            self.input_string = m.get('InputString')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        return self

