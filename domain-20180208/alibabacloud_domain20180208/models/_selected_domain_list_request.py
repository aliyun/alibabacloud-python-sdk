# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SelectedDomainListRequest(DaraModel):
    def __init__(
        self,
        list_date: str = None,
    ):
        # This parameter is required.
        self.list_date = list_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.list_date is not None:
            result['ListDate'] = self.list_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListDate') is not None:
            self.list_date = m.get('ListDate')

        return self

