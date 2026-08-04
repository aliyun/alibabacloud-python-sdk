# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAccountProfileInfoRequest(DaraModel):
    def __init__(
        self,
        account_json: str = None,
    ):
        self.account_json = account_json

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_json is not None:
            result['AccountJson'] = self.account_json

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountJson') is not None:
            self.account_json = m.get('AccountJson')

        return self

