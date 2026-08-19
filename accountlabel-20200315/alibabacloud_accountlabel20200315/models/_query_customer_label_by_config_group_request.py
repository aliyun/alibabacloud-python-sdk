# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryCustomerLabelByConfigGroupRequest(DaraModel):
    def __init__(
        self,
        group_type: str = None,
        pk: int = None,
        token: str = None,
    ):
        # This parameter is required.
        self.group_type = group_type
        # This parameter is required.
        self.pk = pk
        # This parameter is required.
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_type is not None:
            result['GroupType'] = self.group_type

        if self.pk is not None:
            result['PK'] = self.pk

        if self.token is not None:
            result['Token'] = self.token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')

        if m.get('PK') is not None:
            self.pk = m.get('PK')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        return self

