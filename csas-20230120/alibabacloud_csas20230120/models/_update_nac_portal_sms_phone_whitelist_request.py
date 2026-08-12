# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateNacPortalSmsPhoneWhitelistRequest(DaraModel):
    def __init__(
        self,
        phones: List[str] = None,
    ):
        # The list of phone numbers.
        self.phones = phones

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.phones is not None:
            result['Phones'] = self.phones

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Phones') is not None:
            self.phones = m.get('Phones')

        return self

