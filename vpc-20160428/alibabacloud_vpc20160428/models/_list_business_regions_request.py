# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListBusinessRegionsRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   **zh-CN** (default): Chinese
        # *   **en-US**: English.
        self.accept_language = accept_language

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        return self

