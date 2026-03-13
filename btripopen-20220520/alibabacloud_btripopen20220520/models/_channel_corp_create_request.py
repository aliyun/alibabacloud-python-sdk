# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChannelCorpCreateRequest(DaraModel):
    def __init__(
        self,
        administrator_name: str = None,
        administrator_phone: str = None,
        city: str = None,
        corp_name: str = None,
        province: str = None,
        scope: int = None,
        third_corp_id: str = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.administrator_name = administrator_name
        # This parameter is required.
        self.administrator_phone = administrator_phone
        self.city = city
        # This parameter is required.
        self.corp_name = corp_name
        self.province = province
        self.scope = scope
        # This parameter is required.
        self.third_corp_id = third_corp_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.administrator_name is not None:
            result['administrator_name'] = self.administrator_name

        if self.administrator_phone is not None:
            result['administrator_phone'] = self.administrator_phone

        if self.city is not None:
            result['city'] = self.city

        if self.corp_name is not None:
            result['corp_name'] = self.corp_name

        if self.province is not None:
            result['province'] = self.province

        if self.scope is not None:
            result['scope'] = self.scope

        if self.third_corp_id is not None:
            result['third_corp_id'] = self.third_corp_id

        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('administrator_name') is not None:
            self.administrator_name = m.get('administrator_name')

        if m.get('administrator_phone') is not None:
            self.administrator_phone = m.get('administrator_phone')

        if m.get('city') is not None:
            self.city = m.get('city')

        if m.get('corp_name') is not None:
            self.corp_name = m.get('corp_name')

        if m.get('province') is not None:
            self.province = m.get('province')

        if m.get('scope') is not None:
            self.scope = m.get('scope')

        if m.get('third_corp_id') is not None:
            self.third_corp_id = m.get('third_corp_id')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

