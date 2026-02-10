# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChangeUserLangRequest(DaraModel):
    def __init__(
        self,
        user_lang: str = None,
    ):
        # The new language. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.user_lang = user_lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_lang is not None:
            result['UserLang'] = self.user_lang

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserLang') is not None:
            self.user_lang = m.get('UserLang')

        return self

