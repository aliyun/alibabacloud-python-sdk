# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetMmsDataSourceRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        with_config: bool = None,
    ):
        self.lang = lang
        self.with_config = with_config

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['lang'] = self.lang

        if self.with_config is not None:
            result['withConfig'] = self.with_config

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('lang') is not None:
            self.lang = m.get('lang')

        if m.get('withConfig') is not None:
            self.with_config = m.get('withConfig')

        return self

