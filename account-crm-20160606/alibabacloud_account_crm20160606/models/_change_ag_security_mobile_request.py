# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChangeAgSecurityMobileRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        mpk: str = None,
        pk: str = None,
        security_mobile: str = None,
    ):
        # This parameter is required.
        self.app_name = app_name
        # This parameter is required.
        self.mpk = mpk
        # This parameter is required.
        self.pk = pk
        # This parameter is required.
        self.security_mobile = security_mobile

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

        if self.pk is not None:
            result['Pk'] = self.pk

        if self.security_mobile is not None:
            result['SecurityMobile'] = self.security_mobile

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Mpk') is not None:
            self.mpk = m.get('Mpk')

        if m.get('Pk') is not None:
            self.pk = m.get('Pk')

        if m.get('SecurityMobile') is not None:
            self.security_mobile = m.get('SecurityMobile')

        return self

