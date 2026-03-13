# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSubCorpRequest(DaraModel):
    def __init__(
        self,
        outer_corp_id: str = None,
        outer_corp_name: str = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.outer_corp_id = outer_corp_id
        # This parameter is required.
        self.outer_corp_name = outer_corp_name
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.outer_corp_id is not None:
            result['outer_corp_id'] = self.outer_corp_id

        if self.outer_corp_name is not None:
            result['outer_corp_name'] = self.outer_corp_name

        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('outer_corp_id') is not None:
            self.outer_corp_id = m.get('outer_corp_id')

        if m.get('outer_corp_name') is not None:
            self.outer_corp_name = m.get('outer_corp_name')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

