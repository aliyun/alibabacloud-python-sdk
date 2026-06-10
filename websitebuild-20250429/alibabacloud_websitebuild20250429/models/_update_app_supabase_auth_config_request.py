# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAppSupabaseAuthConfigRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        configs_json: str = None,
    ):
        # Business ID
        self.biz_id = biz_id
        # Configuration JSON
        self.configs_json = configs_json

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.configs_json is not None:
            result['ConfigsJson'] = self.configs_json

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('ConfigsJson') is not None:
            self.configs_json = m.get('ConfigsJson')

        return self

