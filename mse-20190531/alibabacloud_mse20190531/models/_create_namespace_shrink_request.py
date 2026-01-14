# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateNamespaceShrinkRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        describe: str = None,
        name: str = None,
        tag_shrink: str = None,
    ):
        self.accept_language = accept_language
        self.describe = describe
        self.name = name
        self.tag_shrink = tag_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.describe is not None:
            result['Describe'] = self.describe

        if self.name is not None:
            result['Name'] = self.name

        if self.tag_shrink is not None:
            result['Tag'] = self.tag_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('Describe') is not None:
            self.describe = m.get('Describe')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Tag') is not None:
            self.tag_shrink = m.get('Tag')

        return self

