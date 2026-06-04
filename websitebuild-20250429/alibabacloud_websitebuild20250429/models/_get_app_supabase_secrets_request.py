# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAppSupabaseSecretsRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        keyword: str = None,
    ):
        self.biz_id = biz_id
        self.keyword = keyword

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        return self

