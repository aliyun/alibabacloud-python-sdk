# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImportCorpNumbersRequest(DaraModel):
    def __init__(
        self,
        city: str = None,
        corp_name: str = None,
        number_list: str = None,
        provider: str = None,
        province: str = None,
        tag_list: str = None,
    ):
        self.city = city
        self.corp_name = corp_name
        # This parameter is required.
        self.number_list = number_list
        # This parameter is required.
        self.provider = provider
        self.province = province
        self.tag_list = tag_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.city is not None:
            result['City'] = self.city

        if self.corp_name is not None:
            result['CorpName'] = self.corp_name

        if self.number_list is not None:
            result['NumberList'] = self.number_list

        if self.provider is not None:
            result['Provider'] = self.provider

        if self.province is not None:
            result['Province'] = self.province

        if self.tag_list is not None:
            result['TagList'] = self.tag_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('City') is not None:
            self.city = m.get('City')

        if m.get('CorpName') is not None:
            self.corp_name = m.get('CorpName')

        if m.get('NumberList') is not None:
            self.number_list = m.get('NumberList')

        if m.get('Provider') is not None:
            self.provider = m.get('Provider')

        if m.get('Province') is not None:
            self.province = m.get('Province')

        if m.get('TagList') is not None:
            self.tag_list = m.get('TagList')

        return self

