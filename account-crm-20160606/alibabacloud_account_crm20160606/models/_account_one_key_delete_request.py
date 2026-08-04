# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AccountOneKeyDeleteRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        pk: str = None,
    ):
        # This parameter is required.
        self.app_name = app_name
        # This parameter is required.
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

        if self.pk is not None:
            result['Pk'] = self.pk

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Pk') is not None:
            self.pk = m.get('Pk')

        return self

