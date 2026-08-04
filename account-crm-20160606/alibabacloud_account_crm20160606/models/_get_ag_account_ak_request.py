# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAgAccountAkRequest(DaraModel):
    def __init__(
        self,
        ag_account_type: str = None,
        mpk: str = None,
        pk: str = None,
    ):
        self.ag_account_type = ag_account_type
        # This parameter is required.
        self.mpk = mpk
        # This parameter is required.
        self.pk = pk

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ag_account_type is not None:
            result['AgAccountType'] = self.ag_account_type

        if self.mpk is not None:
            result['Mpk'] = self.mpk

        if self.pk is not None:
            result['Pk'] = self.pk

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgAccountType') is not None:
            self.ag_account_type = m.get('AgAccountType')

        if m.get('Mpk') is not None:
            self.mpk = m.get('Mpk')

        if m.get('Pk') is not None:
            self.pk = m.get('Pk')

        return self

