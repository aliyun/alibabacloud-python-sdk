# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChangeAgAccountNationalityCodeRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        mpk: str = None,
        nationality_code: str = None,
        pk: str = None,
    ):
        self.app_name = app_name
        self.mpk = mpk
        self.nationality_code = nationality_code
        self.pk = pk

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.mpk is not None:
            result['Mpk'] = self.mpk

        if self.nationality_code is not None:
            result['NationalityCode'] = self.nationality_code

        if self.pk is not None:
            result['PK'] = self.pk

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Mpk') is not None:
            self.mpk = m.get('Mpk')

        if m.get('NationalityCode') is not None:
            self.nationality_code = m.get('NationalityCode')

        if m.get('PK') is not None:
            self.pk = m.get('PK')

        return self

