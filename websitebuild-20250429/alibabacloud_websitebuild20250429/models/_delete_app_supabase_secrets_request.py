# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAppSupabaseSecretsRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        keys_json: str = None,
    ):
        # Business ID
        self.biz_id = biz_id
        # JSON list of keys to be deleted
        self.keys_json = keys_json

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.keys_json is not None:
            result['KeysJson'] = self.keys_json

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('KeysJson') is not None:
            self.keys_json = m.get('KeysJson')

        return self

