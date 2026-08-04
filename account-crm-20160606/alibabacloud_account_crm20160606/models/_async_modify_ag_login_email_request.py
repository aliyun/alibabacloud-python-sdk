# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AsyncModifyAgLoginEmailRequest(DaraModel):
    def __init__(
        self,
        mpk: str = None,
        new_login_email: str = None,
        pk: str = None,
    ):
        # This parameter is required.
        self.mpk = mpk
        # This parameter is required.
        self.new_login_email = new_login_email
        # This parameter is required.
        self.pk = pk

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mpk is not None:
            result['Mpk'] = self.mpk

        if self.new_login_email is not None:
            result['NewLoginEmail'] = self.new_login_email

        if self.pk is not None:
            result['Pk'] = self.pk

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mpk') is not None:
            self.mpk = m.get('Mpk')

        if m.get('NewLoginEmail') is not None:
            self.new_login_email = m.get('NewLoginEmail')

        if m.get('Pk') is not None:
            self.pk = m.get('Pk')

        return self

