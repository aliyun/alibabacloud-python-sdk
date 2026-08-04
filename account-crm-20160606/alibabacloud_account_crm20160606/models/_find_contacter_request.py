# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FindContacterRequest(DaraModel):
    def __init__(
        self,
        contacter_id: int = None,
        locale_string: str = None,
        type: str = None,
    ):
        # This parameter is required.
        self.contacter_id = contacter_id
        self.locale_string = locale_string
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contacter_id is not None:
            result['ContacterId'] = self.contacter_id

        if self.locale_string is not None:
            result['LocaleString'] = self.locale_string

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContacterId') is not None:
            self.contacter_id = m.get('ContacterId')

        if m.get('LocaleString') is not None:
            self.locale_string = m.get('LocaleString')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

