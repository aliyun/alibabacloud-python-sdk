# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListWhitePortalMenuRequest(DaraModel):
    def __init__(
        self,
        dataportal_id: str = None,
    ):
        # This parameter is required.
        self.dataportal_id = dataportal_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dataportal_id is not None:
            result['DataportalId'] = self.dataportal_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataportalId') is not None:
            self.dataportal_id = m.get('DataportalId')

        return self

