# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAgAccountAddressInfoRequest(DaraModel):
    def __init__(
        self,
        address: str = None,
        address_2: str = None,
        app_name: str = None,
        city: str = None,
        mpk: str = None,
        pk: str = None,
        post_code: str = None,
        province: str = None,
    ):
        self.address = address
        self.address_2 = address_2
        self.app_name = app_name
        self.city = city
        self.mpk = mpk
        self.pk = pk
        self.post_code = post_code
        self.province = province

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address

        if self.address_2 is not None:
            result['Address2'] = self.address_2

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.city is not None:
            result['City'] = self.city

        if self.mpk is not None:
            result['Mpk'] = self.mpk

        if self.pk is not None:
            result['PK'] = self.pk

        if self.post_code is not None:
            result['PostCode'] = self.post_code

        if self.province is not None:
            result['Province'] = self.province

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('Address2') is not None:
            self.address_2 = m.get('Address2')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('City') is not None:
            self.city = m.get('City')

        if m.get('Mpk') is not None:
            self.mpk = m.get('Mpk')

        if m.get('PK') is not None:
            self.pk = m.get('PK')

        if m.get('PostCode') is not None:
            self.post_code = m.get('PostCode')

        if m.get('Province') is not None:
            self.province = m.get('Province')

        return self

