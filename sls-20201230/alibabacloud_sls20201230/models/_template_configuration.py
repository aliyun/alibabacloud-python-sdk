# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class TemplateConfiguration(DaraModel):
    def __init__(
        self,
        aonotations: Dict[str, Any] = None,
        id: str = None,
        lang: str = None,
        tokens: Dict[str, Any] = None,
        type: str = None,
        version: str = None,
    ):
        self.aonotations = aonotations
        # This parameter is required.
        self.id = id
        self.lang = lang
        self.tokens = tokens
        # This parameter is required.
        self.type = type
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aonotations is not None:
            result['aonotations'] = self.aonotations

        if self.id is not None:
            result['id'] = self.id

        if self.lang is not None:
            result['lang'] = self.lang

        if self.tokens is not None:
            result['tokens'] = self.tokens

        if self.type is not None:
            result['type'] = self.type

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aonotations') is not None:
            self.aonotations = m.get('aonotations')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('lang') is not None:
            self.lang = m.get('lang')

        if m.get('tokens') is not None:
            self.tokens = m.get('tokens')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

