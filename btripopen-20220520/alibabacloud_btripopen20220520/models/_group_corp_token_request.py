# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GroupCorpTokenRequest(DaraModel):
    def __init__(
        self,
        app_secret: str = None,
        corp_id: str = None,
        sub_corp_id: str = None,
    ):
        # This parameter is required.
        self.app_secret = app_secret
        # This parameter is required.
        self.corp_id = corp_id
        # This parameter is required.
        self.sub_corp_id = sub_corp_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_secret is not None:
            result['app_secret'] = self.app_secret

        if self.corp_id is not None:
            result['corp_id'] = self.corp_id

        if self.sub_corp_id is not None:
            result['sub_corp_id'] = self.sub_corp_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('app_secret') is not None:
            self.app_secret = m.get('app_secret')

        if m.get('corp_id') is not None:
            self.corp_id = m.get('corp_id')

        if m.get('sub_corp_id') is not None:
            self.sub_corp_id = m.get('sub_corp_id')

        return self

