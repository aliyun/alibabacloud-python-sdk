# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SaveAppSupabaseSecretsRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        secrets_json: str = None,
    ):
        # Business ID
        self.biz_id = biz_id
        # Key list JSON
        self.secrets_json = secrets_json

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.secrets_json is not None:
            result['SecretsJson'] = self.secrets_json

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('SecretsJson') is not None:
            self.secrets_json = m.get('SecretsJson')

        return self

