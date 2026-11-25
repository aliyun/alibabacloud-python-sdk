# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateProhibitedTagRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
    ):
        # The description of the prohibited software tag. The description can be up to 128 characters in length and can contain Chinese characters, uppercase and lowercase English letters, digits, spaces, periods (.), underscores (_), and hyphens (-). This parameter can be left empty.
        self.description = description
        # The name of the prohibited software tag. Fuzzy match is supported. The name can be up to 128 characters in length and can contain Chinese characters, uppercase and lowercase English letters, digits, periods (.), underscores (_), and hyphens (-). Spaces are not allowed.
        # 
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

