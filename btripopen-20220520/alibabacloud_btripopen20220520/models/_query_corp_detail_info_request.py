# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryCorpDetailInfoRequest(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        target_corp_id: str = None,
        target_third_corp_id: str = None,
    ):
        self.account_id = account_id
        self.target_corp_id = target_corp_id
        self.target_third_corp_id = target_third_corp_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['account_id'] = self.account_id

        if self.target_corp_id is not None:
            result['target_corp_id'] = self.target_corp_id

        if self.target_third_corp_id is not None:
            result['target_third_corp_id'] = self.target_third_corp_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('account_id') is not None:
            self.account_id = m.get('account_id')

        if m.get('target_corp_id') is not None:
            self.target_corp_id = m.get('target_corp_id')

        if m.get('target_third_corp_id') is not None:
            self.target_third_corp_id = m.get('target_third_corp_id')

        return self

